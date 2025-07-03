##🧭 Smart GIKI Navigator – Vision & Voice Guided Campus Mapping  
##🎯 A Location-Aware Navigation Demo Without GPS – Built with MobileNetV2, Speech Recognition & Google Maps API  
## License: MIT • Python • Streamlit • TorchVision • gTTS • Google Maps API  

##🎥 Your camera becomes your compass.  
##🧠 This AI-powered app locates you using a photo, takes your voice as destination input, and gives real-time walking directions — all without relying on GPS.  

---

## 💡 Project Overview & Motivation  

How do you navigate when GPS isn’t available, like deep inside campuses or buildings?  
**Smart GIKI Navigator** tackles that — an AI-based demo designed to visually recognize where you are and guide you to where you need to go.

Built as a final project for our CV/NLP course, this system uses:
- **Image-based classification** to detect your location from a photo  
- **Voice commands** to understand your destination  
- **Google Maps API** to provide step-by-step walking directions  
- **Text-to-speech** to speak each navigation step aloud

It's a smart, voice-guided assistant — optimized for GIKI, but adaptable anywhere.

---

## ✨ Key Features  

🔍 **Visual Location Detection**  
Upload an image → model predicts which building you're at using MobileNetV2.

🎙️ **Voice Navigation**  
Say “take me to the library” → model extracts your intended destination.

🗺️ **Google Maps Step-by-Step Directions**  
Gets real walking directions using coordinates + Google Maps API.

🔊 **Audio Instructions**  
Each step is spoken aloud using gTTS for intuitive guidance.

🖥️ **Streamlit Web App**  
Everything is wrapped in a clean, interactive UI — no coding needed.

---

## 🚀 How It Works

1. Upload an image → model predicts location & coordinates  
2. Speak or type your destination → voice model extracts the location  
3. System queries Google Maps API → returns walking instructions  
4. Directions are printed + spoken using generated audio  
5. You’re guided — visually and aurally!

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

yaml
Copy
Edit

---

## 🔒 API Keys & Model Notes  

- **Google Maps API**  
  Add your API key to a `.env` file like this:  
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE

yaml
Copy
Edit
Never commit your `.env` file to GitHub.

- **Image Classifier Model**  
The model (`building_classifier.pth`) classifies photos into one of GIKI’s key buildings (e.g., FCSE, FME, Library).  
You can retrain using your own dataset via `train_classifier.py`.

---

## 🛠️ Setup and Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/Smart-GIKI-Navigator.git
cd Smart-GIKI-Navigator
2. Create Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your Google Maps API Key
Create a file .env in the root folder with this line:

ini
Copy
Edit
GOOGLE_MAPS_API_KEY=YOUR_API_KEY_HERE
5. Run the App
bash
Copy
Edit
streamlit run app-base.py
🧪 Train Your Own Model
To retrain the location classifier:

Organize building photos into class-labeled folders under a dataset directory

Update the DATA_DIR path in train_classifier.py accordingly

Run:

bash
Copy
Edit
python train_classifier.py
Your new weights will be saved to models/building_classifier.pth

🙋‍♂️ Contributing
Contributions welcome!
Fork the repo → make a branch → submit a PR!

📜 License
This project is licensed under the MIT License.
Feel free to reuse or adapt — just give credit where due.

👥 Credits
Developed by Aaiz Mohsin (BS AI, GIKI) as part of the CV & NLP course project (Semester 6)
Grateful to our instructors and GIKI for their guidance.

🤝 Let’s Connect
💬 Feedback, improvements, or collaboration ideas?
📫 Aaiz-Am17 on GitHub
🌐 Drop a ⭐ if you found this helpful!
