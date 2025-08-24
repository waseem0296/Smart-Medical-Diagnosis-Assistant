
import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("Chatbot")

FLASK_BACKEND_URL = "http://localhost:5000/ask"


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# user_input = st.chat_input("Ask a question based on the website...")
col1, col2 = st.columns([8,1])

with col1:
    user_input = st.chat_input("Ask a question...", key="text_input")

with col2:
    if st.button("🎤"):
        try:
            response = requests.post("http://localhost:5000/voice")
            result = response.json()
            user_input = result.get("transcription", "")

           
        except Exception as e:
            st.error(f"Voice recording failed: {str(e)}")



if user_input:
   
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
       
        response = requests.post(FLASK_BACKEND_URL, json={"question": user_input})
        response.raise_for_status()
        result = response.json()

       
        answer = result.get("answer", "Sorry, no answer received.")

    except Exception as e:
        answer = f" Error: {str(e)}"


    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})




# import streamlit as st
# import time
# import random

# st.set_page_config(page_title="Voice + Text Chat", layout="wide")

# # --- Session State ---
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "recording" not in st.session_state:
#     st.session_state.recording = False

# if "record_start_time" not in st.session_state:
#     st.session_state.record_start_time = None


# # --- Helper Functions ---
# def add_message(role, text, emotion=None, audio_path=None):
#     st.session_state.chat_history.append({
#         "role": role,
#         "text": text,
#         "emotion": emotion,
#         "audio": audio_path
#     })

# def get_timer():
#     if st.session_state.recording and st.session_state.record_start_time:
#         return int(time.time() - st.session_state.record_start_time)
#     return 0


# # --- Chat History (Top Area) ---
# st.markdown("### 🗨️ Conversation History")
# chat_container = st.container()

# with chat_container:
#     for msg in st.session_state.chat_history:
#         with st.chat_message(msg["role"]):
#             # Chat bubble text
#             st.markdown(msg["text"])

#             # If emotion is available, show in styled card
#             if msg["emotion"]:
#                 st.info(f"🎭 Emotion: **{msg['emotion']}**")

#             # If audio is attached, allow replay
#             if msg["audio"]:
#                 st.audio(msg["audio"], format="audio/wav")


# # --- Chat Input (Bottom, Static) ---
# st.markdown("---")
# col1, col2, col3 = st.columns([1, 5, 1])

# with col1:
#     # 🎤 Mic button with timer
#     if not st.session_state.recording:
#         if st.button("🎤 Start Recording"):
#             st.session_state.recording = True
#             st.session_state.record_start_time = time.time()
#     else:
#         if st.button("⏹ Stop"):
#             st.session_state.recording = False
#             duration = get_timer()
#             add_message("user", f"[Voice Message] ⏺ {duration}s", 
#                         emotion=random.choice(["Happy", "Sad", "Neutral"]), 
#                         audio_path="dummy_audio.wav")
#     if st.session_state.recording:
#         st.markdown(f"⏺ **Recording... {get_timer()}s**")

# with col2:
#     # 💬 Text input
#     user_text = st.text_input("Type your message...", key="user_input", label_visibility="collapsed")
#     if user_text:
#         add_message("user", user_text, emotion=random.choice(["Happy", "Sad", "Angry"]))
#         st.session_state.user_input = ""

# with col3:
#     # 📂 File uploader for audio
#     uploaded_file = st.file_uploader(" ", type=["wav", "mp3"], label_visibility="collapsed")
#     if uploaded_file:
#         add_message("user", "[Uploaded Audio]", 
#                     emotion=random.choice(["Excited", "Calm", "Tired"]), 
#                     audio_path=uploaded_file)



# import streamlit as st
# import requests
# import time

# st.set_page_config(page_title="AI Chatbot", layout="wide")

# FLASK_BACKEND_TEXT = "http://localhost:5000/ask"
# FLASK_BACKEND_VOICE = "http://localhost:5000/voice"

# # --- Session State ---
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# if "recording" not in st.session_state:
#     st.session_state.recording = False
# if "record_start_time" not in st.session_state:
#     st.session_state.record_start_time = None


# # --- Helper ---
# def get_timer():
#     if st.session_state.recording and st.session_state.record_start_time:
#         return int(time.time() - st.session_state.record_start_time)
#     return 0


# # --- Chat History (Top) ---
# st.markdown("## 🗨️ Conversation History")
# chat_container = st.container()

# with chat_container:
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])
#             if "emotion" in msg and msg["emotion"]:
#                 st.info(f"🎭 Emotion: **{msg['emotion']}**")
#             if "audio" in msg and msg["audio"]:
#                 st.audio(msg["audio"], format="audio/mp3")


# # --- Input Area (Bottom, Fixed) ---
# st.markdown("---")
# col1, col2, col3 = st.columns([1, 6, 1])

# with col1:
#     if not st.session_state.recording:
#         if st.button("🎤 Start"):
#             st.session_state.recording = True
#             st.session_state.record_start_time = time.time()
#             try:
#                 response = requests.post(FLASK_BACKEND_VOICE)
#                 result = response.json()
#                 transcription = result.get("transcription", "")
#                 emotion = result.get("emotion", "")
#                 answer = result.get("answer", "")

#                 st.session_state.messages.append({
#                     "role": "user", 
#                     "content": transcription, 
#                     "emotion": emotion
#                 })
#                 st.session_state.messages.append({
#                     "role": "assistant", 
#                     "content": answer
#                 })
#             except Exception as e:
#                 st.error(f"Voice request failed: {str(e)}")
#             st.session_state.recording = False
#     else:
#         st.markdown(f"⏺ Recording... {get_timer()}s")

# with col2:
#     user_text = st.text_input("Type your message...", key="text_input", label_visibility="collapsed")
#     if user_text:
#         st.session_state.messages.append({"role": "user", "content": user_text})

#         try:
#             response = requests.post(FLASK_BACKEND_TEXT, json={"question": user_text})
#             response.raise_for_status()
#             result = response.json()
#             answer = result.get("answer", "Sorry, no answer received.")
#         except Exception as e:
#             answer = f"❌ Error: {str(e)}"

#         st.session_state.messages.append({"role": "assistant", "content": answer})

#         # clear text input safely
#         st.session_state["text_input"] = ""

# with col3:
#     uploaded_audio = st.file_uploader(" ", type=["wav", "mp3"], label_visibility="collapsed")
#     if uploaded_audio:
#         st.session_state.messages.append({
#             "role": "user", 
#             "content": "[Uploaded Voice Message]", 
#             "audio": uploaded_audio
#         })
