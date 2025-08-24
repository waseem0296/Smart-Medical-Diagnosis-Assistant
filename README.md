# 🧠 Smart Medical Diagnosis Assistant

The **Smart Medical Diagnosis Assistant** is an AI-powered system that allows patients to interact with a **virtual doctor** through **text** and **voice**. It combines advanced **Large Language Models (LLMs)**, **speech recognition**, **emotion detection**, and **text-to-speech** to deliver **empathetic and medically relevant responses**.

This project is modular, consisting of different components for AI reasoning, frontend UI, voice processing, and emotion detection. It is built with **Flask (backend)**, **Streamlit (frontend)**, and **Groq + Gemini APIs** for AI capabilities.

---

## ✨ Features

- 💬 **Chatbot (Text)** → Ask questions and get AI-powered responses.
- 🎤 **Voice Input** → Speak your question, which is transcribed automatically.
- 🎭 **Emotion Detection** → The assistant detects your emotional tone (e.g., calm, anxious, distressed).
- 🗣 **Voice Output** → The doctor responds with natural-sounding speech.
- 🧩 **Modular Design** → Each function (AI, voice, emotion) is separated for easy development.
- 🔒 **Secure API Management** via `.env`.

---

## 📂 Project Structure

Smart-Medical-Diagnosis-Assistant/

│── ai_brain.py # AI reasoning logic with Groq LLaMA model

│── frontend.py # Streamlit-based chatbot UI

│── voice_of_doctor.py # Doctor's voice synthesis (Text-to-Speech)

│── voice_of_patient.py # Patient's voice recording + transcription

│── emotion_model.py # Detects emotion from patient audio

│── app.py # Flask backend connecting all modules

│── .env # Environment variables (ignored by Git)

│── requirements.txt # Dependencies


---

## ⚙️ Components Overview

### 1. **AI Brain (`ai_brain.py`)**
- Uses Groq’s **LLaMA 3.1 8B-Instant** for reasoning.
- Provides `ask_text_model(user_input)` function.
- Future-ready for **image analysis** (commented prototype inside code).

### 2. **Voice of Patient (`voice_of_patient.py`)**
- Records voice input using `speech_recognition`.
- Converts audio to `.mp3` using `pydub`.
- Transcribes audio → text using Groq’s **Whisper-Large-v3** ASR.

### 3. **Emotion Model (`emotion_model.py`)**
- Uses **Google Gemini 1.5 Flash** to classify audio emotions.
- Supports labels: `calm, anxious, distressed, angry, happy, neutral`.
- Returns most likely emotion as plain text.

### 4. **Voice of Doctor (`voice_of_doctor.py`)**
- Converts doctor’s AI-generated answers into voice using **gTTS**.
- Saves response as `.mp3`.
- Plays audio automatically (uses `ffplay` on Windows).

### 5. **Backend (`app.py`)**
- Built with Flask.
- Endpoints:
  - `/ask` → Handles text queries.
  - `/voice` → Handles full voice pipeline:
    - Record patient’s voice
    - Transcribe → text
    - Detect emotion
    - Build enriched query: *text + emotion*
    - Generate empathetic answer with Groq LLM
    - Convert to speech & return JSON: `{transcription, emotion, answer}`

### 6. **Frontend (`frontend.py`)**
- Built with Streamlit.
- Provides a **chat-style UI** for patients.
- Two input modes:
  - Text input box
  - 🎤 Voice button (records and sends to `/voice`)
- Maintains conversation history (`st.session_state`).

---

## 🛠 Installation

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/Smart-Medical-Diagnosis-Assistant.git
cd Smart-Medical-Diagnosis-Assistant
```

## Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac

## Install Dependencies
pip install -r requirements.txt

## Configure Environment Variables

Create a .env file in the root folder:

GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here




## ▶️ Running the Project

Start Flask backend:

python app.py


Start Streamlit frontend:

streamlit run frontend.py


Open browser → http://localhost:8501

You can now:

Type questions into the chat.

Use 🎤 button to ask by voice.

Receive doctor’s answers in text + voice.

📦 Requirements

Example requirements.txt:

flask
flask-cors
streamlit
requests
python-dotenv
groq
gtts
pydub
SpeechRecognition
google-generativeai


## System Dependencies:

FFmpeg (for audio playback in voice_of_doctor.py)

PortAudio (needed for speech_recognition)

## 📌 Future Enhancements

🖼 Medical image analysis (X-rays, MRIs).

🌍 Multi-language support.

☁️ Deployment to cloud (Heroku / AWS / Streamlit Cloud).

📖 Patient medical history tracking.

👨‍⚕️ Integration with real doctors for telemedicine.

🔒 Security Notes

.env is added to .gitignore.

Never commit real API keys.

Use a dummy .env.example file for collaboration:

GROQ_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here

🧑‍🤝‍🧑 Authors & Contributors

Waseem Abbas (Project Lead & Developer)

Open for collaboration: Contributions, issues, and feature requests are welcome!

