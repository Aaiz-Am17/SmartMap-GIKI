# 🗺️ SmartMap-GIK 
### 🎯 Vision + Voice Navigation for Campus Buildings using AI & Google Maps  

[![GitHub stars](https://img.shields.io/github/stars/Aaiz-Am17/SmartMap-GIKI?style=social)](https://github.com/Aaiz-Am17/SmartMap-GIKI/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![MobileNetV2](https://img.shields.io/badge/MobileNetV2-Image%20Classification-success?logo=pytorch)
![GoogleMaps](https://img.shields.io/badge/API-Google%20Maps-blue?logo=googlemaps)

---

🎯 **Navigate GIKI’s campus visually and vocally — without GPS.**  
📍 Upload a photo to detect your location and speak your destination — the app handles the rest using AI and Google Maps.

---

## 💡 Project Overview & Motivation
  
How do you navigate when GPS isn’t available, like deep inside campuses or buildings?  
**Smart GIKI Navigator** is a vision-driven campus navigation assistant that tackles just that — an AI-based demo designed to visually recognize where you are and guide you to where you need to go.

Built as a final project for our CV/NLP course, this system uses:
- **Image-based classification** to detect your location from a photo  
- **Voice commands** to understand your destination  
- **Google Maps API** to provide step-by-step walking directions  
- **Text-to-speech** to speak each navigation step aloud

It's a smart, voice-guided assistant — optimized for GIKI, but adaptable anywhere.

---

## ✨ Key Features

📸 **Visual Place Detection**  
Upload a photo and let the MobileNetV2-based classifier identify your current building.

🎙️ **Voice Command Support**  
Speak your destination — no typing needed.

🗺️ **Live Directions from Google Maps API**  
Generates walking instructions based on detected coordinates.

🔊 **Audio Navigation**  
Each direction is narrated using text-to-speech — ideal for on-the-go users.

🖥️ **Streamlit GUI**  
Simple, clean interface that anyone can use.

🧠 **Modular AI Utilities**  
Clean code structure for CV, NLP, and navigation logic.

---

## 🚀 How It Works

1. Upload a photo of where you are
2. App uses MobileNetV2 to classify the building
3. Speak or type your desired destination
4. App fetches walking directions via Google Maps API
5. Directions are read aloud, step-by-step

---

## 📁 Project Structure

Smart-GIKI-Navigator/
├── app-base.py # Streamlit app (main interface)
├── train_classifier.py # Trains MobileNetV2 location classifier
├── .env # Stores your Google Maps API key (not public)
├── static/
│ └── audio/ # Stores generated voice files
├── utils/
│ ├── CV_utils.py # Image classification (MobileNetV2 + GIKI landmarks)
│ ├── voice_utils.py # Voice input & gTTS text-to-speech
│ └── map_utils.py # Google Maps API integration
├── models/
│ └── building_classifier.pth # Saved PyTorch model weights
├── requirements.txt # Project dependencies
├── LICENSE # MIT License
└── README.md # You're reading it


---


## 🔒 API Keys & Model Notes  

- **Google Maps API**  
  Add your API key to a `.env` file like this:  
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE


- **Image Classifier Model**  
The model (`building_classifier.pth`) classifies photos into one of GIKI’s key buildings (e.g., FCSE, FME, Library).  
You can retrain using your own dataset via `train_classifier.py`.

---

## 🛠️ Setup and Installation  

### 1. Clone the Repository  
```
git clone https://github.com/yourusername/Smart-GIKI-Navigator.git
cd Smart-GIKI-Navigator
```
### 2. Create Virtual Environment (Recommended)
```
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
'''
pip install -r requirements.txt
'''
### 4. Add Your Google Maps API Key
Create a file .env in the root folder with this line:
```
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
```
### 5. Run the App
```
streamlit run app-base.py
```
### 🧪 Train Your Own Model
To retrain the location classifier:

Organize building photos into class-labeled folders under a dataset directory

Update the DATA_DIR path in train_classifier.py accordingly

Run:
```
python train_classifier.py
```
Your new weights will be saved to models/building_classifier.pth

## 🙋‍♂️ Contributing
Contributions are welcome!
Fork the repo → make a branch → submit a PR!

## 📜 License
This project is licensed under the MIT License.
Feel free to reuse or adapt — just give credit where due.

## 👥 Credits
Developed by Aaiz Mohsin (BS AI, GIKI) as part of the CV & NLP course project (Semester 6)
Grateful to our instructors and GIKI for their guidance.

## 🤝 Let’s Connect
## 💬 Feedback, improvements, or collaboration ideas?
##📫[LinkedIn](https://www.linkedin.com/in/aaizmohsin)
## 🌐 Drop a ⭐ if you found this helpful!


