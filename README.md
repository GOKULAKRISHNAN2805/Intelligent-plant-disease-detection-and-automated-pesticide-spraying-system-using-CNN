# Intelligent-plant-disease-detection-and-automated-pesticide-spraying-system-using-CNN
🌱 Intelligent Plant Disease Detection and Automated Pesticide Spraying System using CNN

An AI-powered smart agriculture system developed using Deep Learning, Computer Vision, IoT, and Embedded Systems for real-time plant disease detection and automated pesticide spraying.

📌 Project Overview

Agriculture plays a vital role in global food production, but plant diseases significantly reduce crop yield and quality. Traditional disease detection methods rely on manual inspection, which is time-consuming, labor-intensive, and often inaccurate.

This project presents an intelligent smart agriculture solution that combines Artificial Intelligence (AI), Convolutional Neural Networks (CNN), Computer Vision, and IoT technologies to automatically detect plant diseases and perform pesticide spraying in real time.

The system captures plant leaf images using a webcam, processes the images using OpenCV preprocessing techniques, and classifies diseases using a ResNet-18 deep learning model. Once a disease is detected, the system communicates with an ESP32 microcontroller to automate pesticide spraying using a relay-controlled DC pump.

This project demonstrates the integration of:

Deep Learning
Computer Vision
Embedded Systems
IoT Automation
Smart Farming Technologies
🚀 Key Features

✅ Real-time plant disease detection
✅ CNN-based deep learning classification
✅ OpenCV image preprocessing
✅ ResNet-18 model implementation
✅ ESP32-based hardware automation
✅ Automated pesticide spraying system
✅ Telegram bot alert integration
✅ Real-time monitoring system
✅ Smart agriculture application
✅ Reduced pesticide wastage
✅ IoT-enabled automation system

🧠 Technologies Used
Software Technologies
Python
OpenCV
PyTorch
NumPy
CNN (Convolutional Neural Network)
ResNet-18
VS Code
Google Colab
Hardware Components
ESP32 Microcontroller
Webcam / Camera
Relay Module
DC Pump
Power Supply Unit
Connecting Wires
Communication Technologies
Wi-Fi Communication
HTTP Requests
Telegram Bot API
Serial Communication
🌿 Plant Diseases Detected

The model is trained to classify plant leaves into the following categories:

Class	Description
Healthy	Healthy leaf condition
Spider Mite	Pest infestation detection
Septoria Leaf Spot	Fungal disease
Bacterial Spot	Bacterial infection
Yellow Leaf Curl Virus	Viral disease
⚙️ System Architecture

The overall workflow of the system is:

Camera
   ↓
Image Acquisition
   ↓
Image Preprocessing (Resize + Gaussian Blur)
   ↓
Deep Learning Model (ResNet-18)
   ↓
Disease Classification
   ↓
ESP32 Microcontroller
   ↓
Relay Module
   ↓
DC Pump
   ↓
Automated Pesticide Spraying
🖼️ Working Principle
Step 1 — Image Capture

A webcam continuously captures images of plant leaves in real time.

Step 2 — Image Preprocessing

Captured images are processed using:

Image resizing
Normalization
Gaussian Blur filtering

This improves image quality and removes unwanted noise.

Step 3 — Disease Classification

The preprocessed image is passed to the ResNet-18 CNN model for classification.

The model predicts:

Healthy leaf
Spider Mite
Septoria Leaf Spot
Bacterial Spot
Yellow Leaf Curl Virus
Step 4 — ESP32 Communication

The prediction result is transmitted to the ESP32 microcontroller using Wi-Fi communication.

Step 5 — Automated Pesticide Spraying

If Spider Mite infestation is detected:

ESP32 activates relay module
Relay switches ON the DC pump
Pump sprays pesticide automatically

If the plant is healthy:

Pump remains OFF
🔥 Deep Learning Model
CNN Architecture

The project uses a Convolutional Neural Network (CNN) for feature extraction and classification.

ResNet-18 Model

ResNet-18 is selected because:

High accuracy
Better feature extraction
Efficient training
Reduced vanishing gradient problem
📊 Model Performance
Metric	Performance
Model Used	ResNet-18
Accuracy	90% – 95%
Detection Type	Real-Time
Framework	PyTorch

The model performs efficiently under proper lighting conditions and accurately identifies disease symptoms from plant leaves.

🛠 Hardware Components
Component	Function
Webcam	Captures leaf images
ESP32	Controls automation system
Relay Module	Switches DC pump
DC Pump	Sprays pesticide
Power Supply	Provides electrical power
💻 Software Modules
1. Image Acquisition Module

Captures real-time leaf images using webcam.

2. Image Preprocessing Module

Performs:

Resizing
Normalization
Gaussian Blur filtering
3. CNN Classification Module

Uses ResNet-18 for disease classification.

4. ESP32 Control Module

Receives classification results and controls relay module.

5. Pump Automation Module

Activates pesticide spraying mechanism.

📡 Telegram Bot Integration

The system sends:

Disease detection alerts
Confidence scores
Captured leaf images

through Telegram Bot API for remote monitoring.

📁 Project Structure
AI-Plant-Disease-Detection/
│
├── README.md
├── plant_detection.py
├── esp32_code.ino
├── model.pth
├── classes.pth
├── requirements.txt
├── dataset/
├── outputs/
├── images/
├── screenshots/
└── Project_Report.pdf
📦 Installation
Clone Repository
git clone https://github.com/yourusername/AI-Plant-Disease-Detection.git
Navigate to Project Folder
cd AI-Plant-Disease-Detection
Install Required Libraries
pip install -r requirements.txt
▶️ Run the Project
python plant_detection.py
📜 Requirements

Create a requirements.txt file:

torch
torchvision
opencv-python
numpy
requests
pyserial
🧪 Experimental Results

The system successfully:

Detects plant diseases in real time
Achieves high classification accuracy
Sends Telegram alerts
Automates pesticide spraying
Reduces manual effort
📷 Output Screenshots
Healthy Leaf Detection

(Add image here)

Spider Mite Detection

(Add image here)

Telegram Alert Output

(Add image here)

ESP32 + Pump Integration

(Add image here)

📈 Advantages of the System

✅ High detection accuracy
✅ Real-time disease monitoring
✅ Automated pesticide spraying
✅ Reduced human effort
✅ Efficient pesticide usage
✅ Smart agriculture application
✅ IoT-enabled automation
✅ Scalable architecture

⚠️ Limitations
Requires proper lighting conditions
Depends on dataset quality
Limited disease categories
Requires hardware setup
Environmental variations may affect prediction accuracy
🔮 Future Scope

The project can be improved further by adding:

Mobile application support
Cloud-based monitoring
Multi-disease automated spraying
Drone-based monitoring system
Solar-powered operation
Additional sensors (temperature, humidity, soil moisture)
Raspberry Pi / Edge AI deployment
Smart irrigation integration
📚 Research References
Deep Residual Learning for Image Recognition — Kaiming He et al.
Using Deep Learning for Image-Based Plant Disease Detection — Mohanty et al.
MobileNets for Embedded Vision Applications
Digital Image Processing — Gonzalez & Woods
IoT-Based Smart Agriculture Systems


⭐ GitHub Repository

If you like this project, give it a ⭐ on GitHub

🌾 Conclusion

This project demonstrates the successful integration of Artificial Intelligence, Computer Vision, IoT, and Embedded Systems in smart agriculture applications. The proposed system provides real-time plant disease detection and automated pesticide spraying, improving agricultural efficiency while reducing manual effort and pesticide wastage.

The project highlights how modern technologies can contribute to sustainable and intelligent farming solutions for the future.
