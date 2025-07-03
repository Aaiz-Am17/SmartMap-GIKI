import streamlit as st
import time
import base64
from utils.map_utils import get_directions_and_steps
from utils.voice_utils import listen_to_user, extract_destination, speak_text
from utils.CV_utils import predict_and_locate

st.set_page_config(page_title="Smart GIKI Map", layout="wide")
st.title("📍 GIKI Smart Map Navigator")

# -----------------------A
# 🖼️ Upload Image for Location Detection
# -----------------------
st.header("📸 Upload Image of Location")
uploaded_file = st.file_uploader("Upload a photo to identify your current location")

if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image("temp.jpg", caption="Uploaded Image", use_column_width=True)

    label, coords = predict_and_locate("temp.jpg")
    if label == "Unknown":
        st.error("❌ Could not identify location. Using default coordinates.")
    else:
        st.success(f"📍 Detected Location: {label}")
    st.info(f"📌 Coordinates in use: {coords[0]}, {coords[1]}")
else:
    coords = (34.068283, 72.644278)  # Default coords if no image
    st.warning(f"📍 Using default location: {coords}")

# -----------------------
# 🎙️ VOICE COMMAND INPUT
# -----------------------
st.header("🎙️ Voice Command")
destination_input = st.text_input("Destination", value="")

# -----------------------
# 🧠 SESSION STATE INIT
# -----------------------
if "steps" not in st.session_state:
    st.session_state.steps = []
if "audio_paths" not in st.session_state:
    st.session_state.audio_paths = []

# -----------------------
# 🎤 SPEAK DESTINATION or TYPED INPUT
# -----------------------
if st.button("🎤 Speak Destination") or destination_input:
    if destination_input == "":
        user_text = listen_to_user()
        destination = extract_destination(user_text)
    else:
        destination = extract_destination(destination_input)

    if destination:
        st.success(f"🎯 Destination: {destination}")
        steps, maps_url = get_directions_and_steps(f"{coords[0]},{coords[1]}", destination)

        if steps:
            st.session_state.steps = steps
            st.subheader("🧭 Directions")

            for i, step in enumerate(steps, 1):
                st.markdown(f"{i}. {step}", unsafe_allow_html=True)

            # Generate audio files
            audio_paths = []
            for i, step in enumerate(steps, 1):
                audio_path = speak_text(f"Step {i}. {step}")
                audio_paths.append(audio_path)
            st.session_state.audio_paths = audio_paths

            st.markdown(f"[🗺️ Open in Google Maps]({maps_url})", unsafe_allow_html=True)
        else:
            st.error("❌ Could not fetch directions. Try again later.")
    else:
        st.error("❌ Could not recognize voice. Try again.")

# -----------------------
# 🔊 VOICE NAVIGATION AUTOPLAY
# -----------------------
if st.button("🔊 Voice Navigation"):
    if st.session_state.audio_paths:
        for audio in st.session_state.audio_paths:
            with open(audio, "rb") as f:
                audio_bytes = f.read()
                b64_audio = base64.b64encode(audio_bytes).decode()
                audio_html = f"""
                    <audio autoplay>
                        <source src="data:audio/mp3;base64,{b64_audio}" type="audio/mp3">
                    </audio>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
            time.sleep(10)  # Optional pause between steps
    else:
        st.warning("⚠️ No directions to speak. Use voice command first.")
