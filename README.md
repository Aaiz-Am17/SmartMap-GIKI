# 🧭 Smart GIKI Navigator – Vision & Voice Guided Campus Mapping  
## 🎯 A Location-Aware Navigation Demo Without GPS  
**Built with:** MobileNetV2 • Speech Recognition • Google Maps API  
**License:** MIT | Python | Streamlit | TorchVision | gTTS  

---

🎥 **Your camera becomes your compass.**  
🧠 This AI-powered app locates you using a photo, takes your voice as destination input, and gives real-time walking directions — all without relying on GPS.

---

## 💡 Project Overview & Motivation  

How do you navigate when GPS isn’t available — like deep inside campuses or academic blocks?

**Smart GIKI Navigator** tackles that by combining computer vision, natural language processing, and real-world map APIs. This demo application was developed for the CV & NLP course and is capable of:

- Detecting your location visually via a **MobileNetV2 image classifier**
- Taking **voice input** to extract your destination
- Generating **step-by-step walking directions** using Google Maps
- Speaking those steps aloud using **gTTS (text-to-speech)**

Whether you’re a student, visitor, or just exploring campus, this tool acts like your personal AR navigation assistant.

---

## ✨ Key Features  

- 🔍 **Visual Location Detection**  
  Upload a building photo → AI classifies your current location.

- 🎙️ **Voice Navigation**  
  Speak your destination → system extracts & understands the command.

- 🗺️ **Google Maps Step-by-Step Directions**  
  Uses coordinates + Maps API to calculate walking route.

- 🔊 **Audio Directions**  
  Each direction is spoken aloud using gTTS.

- 🖥️ **Streamlit Web Interface**  
  Fully interactive — no code or CLI required.

---

## 🚀 How It Works  

1. **Upload an Image**  
   → Model classifies which GIKI building you're in.

2. **Speak or Type Your Destination**  
   → Voice command is parsed using speech recognition + keyword mapping.

3. **Generate Directions**  
   → API fetches walking instructions from your current location to the destination.

4. **Listen & Follow**  
   → Steps are displayed *and* spoken in real-time.

---

## 📁 Project Structure  

Smart-GIKI-Navigator/
├── app-base.py # Streamlit main app
├── train_classifier.py # Training script for MobileNetV2
├── .env # Google Maps API key (DO NOT COMMIT)
├── static/
│ └── audio/ # Voice instruction files
├── utils/
│ ├── CV_utils.py # Visual location classifier
│ ├── voice_utils.py # Voice input and TTS
│ └── map_utils.py # Google Maps API interface
├── models/
│ └── building_classifier.pth # Saved PyTorch model
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── README.md # This file

yaml
Copy
Edit

---

## 🔒 API Keys & Model Notes  

- **Google Maps API**  
  Store your API key in a `.env` file:
  ```env
  GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
⚠️ Make sure to add .env to .gitignore before pushing to GitHub!

Model Checkpoint
The file building_classifier.pth stores the trained MobileNetV2 model that detects 12 different GIKI buildings.

🛠️ Setup & Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/Smart-GIKI-Navigator.git
cd Smart-GIKI-Navigator
2. Create Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
# Activate:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your API Key
Create a file named .env in the root directory:

env
Copy
Edit
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
5. Run the App
bash
Copy
Edit
streamlit run app-base.py
🧪 Train Your Own Model
To retrain the MobileNetV2 image classifier:

Organize images into class-labeled folders like:
data/Library/, data/FCSE/, etc.

Update the DATA_DIR path inside train_classifier.py

Run:

bash
Copy
Edit
python train_classifier.py
New model will be saved at models/building_classifier.pth

🙋‍♂️ Contributing
Pull requests are welcome!
To contribute:

Fork this repository

Create a feature branch

Make your changes

Submit a pull request with a clear explanation

📜 License
This project is released under the MIT License.
Feel free to reuse, remix, and share — just credit the authors.

👥 Credits
Developed by Aaiz Mohsin
🎓 BS Artificial Intelligence – GIKI (2022–2026)
🧠 Final Project for CV & NLP (6th Semester)

Huge thanks to faculty, teammates, and every friend whose photo made this demo possible!

🌐 Let’s Connect
💻 GitHub – Aaiz-Am17

💬 Suggestions? Feedback? Drop a ⭐ if you liked it!
