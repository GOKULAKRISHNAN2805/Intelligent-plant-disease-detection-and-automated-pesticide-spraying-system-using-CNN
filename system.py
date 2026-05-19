import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np
import requests
import time
from torchvision import models

print("🚀 STARTING PROGRAM...")

# =========================
# TELEGRAM SETTINGS
# =========================
BOT_TOKEN = "token"
CHAT_ID = "chat id"

# =========================
# ESP32 SETTINGS (Add this section)
# =========================
ESP32_IP = "ip"   # ← CHANGE THIS to your ESP32 IP from Serial Monitor
ESP32_URL = f"http://{ESP32_IP}/trigger"

# =========================
# LOAD CLASSESq
# =========================
try:
    classes = torch.load("classes.pth")
    print("✅ Classes Loaded:")
    for i, c in enumerate(classes):
        print(f"{i} → {c}")
except:
    print("❌ classes.pth missing")
    exit()

# =========================
# LOAD MODEL (RESNET18)
# =========================
try:
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(classes))
    model.load_state_dict(torch.load("tomato_model.pth", map_location='cpu'))
    model.eval()
    print("✅ Model Loaded")
except:
    print("❌ Model loading failed")
    exit()

# =========================
# CAMERA
# =========================
# =========================
# EXTERNAL ZEBRONICS USB WEBCAM
# =========================
print("📷 Opening External Zebronics USB Webcam...")

cap = cv2.VideoCapture(1)                    # 1 = External USB Webcam (Zebronics)
if not cap.isOpened():
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) # Try with DirectShow backend

if not cap.isOpened():
    print("❌ Could not open Zebronics external webcam.")
    print("   → Make sure it is plugged in.")
    print("   → Try changing 1 to 2 or 0 and run again.")
    exit()

# Good resolution for leaf detection
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("✅ Zebronics External Webcam Started!")
print("   Point the Zebronics camera directly at the tomato leaf (good lighting helps)")
# =========================
# PREPROCESS
# =========================
def preprocess(frame):

    # FILTER
    blurred = cv2.GaussianBlur(frame, (5,5), 0)

    # SEGMENTATION
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    lower_green = np.array([25,40,40])
    upper_green = np.array([90,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    segmented = cv2.bitwise_and(frame, frame, mask=mask)

    # DISEASE SPOTS
    disease_mask = cv2.bitwise_not(mask)
    kernel = np.ones((5,5), np.uint8)
    disease_mask = cv2.morphologyEx(disease_mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(disease_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = frame.copy()

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            cv2.drawContours(output, [cnt], -1, (0,0,255), 2)

    # MODEL INPUT
    img = cv2.resize(segmented, (224,224))
    img = img / 255.0
    img = np.transpose(img, (2,0,1))

    return torch.tensor(img, dtype=torch.float32).unsqueeze(0), blurred, segmented, output

# =========================
# PREDICT
# =========================
def predict(frame):
    img, blurred, segmented, output = preprocess(frame)

    with torch.no_grad():
        out = model(img)
        prob = F.softmax(out, dim=1)
        conf, pred = torch.max(prob, 1)

    return classes[pred.item()], conf.item()*100, blurred, segmented, output

# =========================
# TELEGRAM
# =========================
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": text}, timeout=5)
    except:
        print("⚠️ Telegram message failed")

def send_photo(path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    try:
        with open(path, 'rb') as img:
            requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": img}, timeout=5)
    except:
        print("⚠️ Telegram photo failed")

# =========================
# NEW: SEND TRIGGER TO ESP32
# =========================
def send_to_esp32(disease, confidence):
    try:
        trigger_data = {
            "disease": disease,
            "confidence": round(confidence, 2)
        }
        response = requests.post(ESP32_URL, json=trigger_data, timeout=5)
        if response.status_code == 200:
            print(f"✅ Sent to ESP32: {disease} ({confidence:.1f}%)")
        else:
            print(f"⚠️ ESP32 error: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Failed to reach ESP32 at {ESP32_IP}: {e}")

# =========================
# MAIN LOOP
# =========================
INTERVAL = 60
last_time = 0
last_label = None

print("🚀 System Running... Press 'q' to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Camera error")
        break

    label, conf, blurred, segmented, output = predict(frame)

    # =========================
    # DRAW LABEL ON IMAGE
    # =========================
    cv2.rectangle(output, (5,5), (500,40), (0,0,0), -1)
    cv2.putText(output,
                f"{label} ({round(conf,2)}%)",
                (10,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0,255,0),
                2)

    # =========================
    # DISPLAY
    # =========================
    cv2.imshow("Original", frame)
    cv2.imshow("Filtered Image", blurred)
    cv2.imshow("Segmented Leaf", segmented)
    cv2.imshow("Disease Detection", output)

    # =========================
    # SAVE FINAL IMAGE
    # =========================
    filename = "result.jpg"
    cv2.imwrite(filename, output)

    current_time = time.time()

    # =========================
    # TELEGRAM + ESP32 TRIGGER
    # =========================
    if conf > 80:
        if (current_time - last_time > INTERVAL) or (label != last_label):

            message = f"""
🌿 Tomato Disease Detection

🦠 Disease: {label}
📊 Confidence: {round(conf,2)} %
"""

            print(message)

            send_message(message)
            send_photo(filename)

            # Send to ESP32 for OLED update + spraying
            send_to_esp32(label, conf)

            last_time = current_time
            last_label = label

    # EXIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Exiting...")
        break

    time.sleep(1)

cap.release()
cv2.destroyAllWindows()