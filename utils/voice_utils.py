# utils/voice_utils.py
import speech_recognition as sr
from gtts import gTTS
import os
import uuid

LOCATION_ALIASES = {
    "fes": "FES",
    "Fcse": "FCSE",
    "Mosque": "Mosque",
    "Fme": "Faculty of Mechanical Engineering",
    "Matirials": "Faculty of Materials and Chemical Engineering",
    "Acb": "Academic Block",
    "Auditorium": "Agha Hassan Abedi Auditorium",
    "Audi": "Agha Hassan Abedi Auditorium",
    "Hbl": "Habib Bank Ltd",
    "Logic": "LOGIK",
    "Guest house": "GIKI Guest House",
    "Tuc": "Tuc",
    "Library": "Library",
}

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print("✅ You said:", text)
        return text
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def extract_destination(text):
    text = text.lower()
    skip_phrases = ["take me to", "navigate to", "go to", "i want to go to", "lead me to", "take me to the", "go to the"]
    for phrase in skip_phrases:
        if phrase in text:
            text = text.replace(phrase, "")
            break
    text = text.strip()
    return LOCATION_ALIASES.get(text, text).title()

def speak_text(text):
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(PROJECT_ROOT, "..", "static", "audio")
    os.makedirs(output_dir, exist_ok=True)

    filename = f"voice_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(output_dir, filename)

    tts = gTTS(text)
    tts.save(filepath)
    return filepath

def speak_directions_with_pause(steps):
    return [speak_text(f"Step {i}. {step}") for i, step in enumerate(steps, 3)]
