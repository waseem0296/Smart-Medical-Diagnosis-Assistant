# emotion_model.py
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini 1.5 Flash
model = genai.GenerativeModel("gemini-1.5-flash")

def detect_emotion_from_audio(audio_file_path: str) -> str:
    """
    Detect emotion from a given audio file using Gemini 1.5 Flash.
    Input: path to audio file (wav/mp3/flac).
    Output: predicted emotion label (calm, anxious, distressed, angry, happy, neutral).
    """
    try:
        # Read audio bytes
        with open(audio_file_path, "rb") as f:
            audio_bytes = f.read()

        # Send audio + instruction to Gemini
        response = model.generate_content([
            {
                "role": "user",
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "audio/wav",  # change if mp3/flac
                            "data": audio_bytes
                        }
                    },
                    {
                        "text": (
                            "Classify the speaker's emotion as one of: "
                            "calm, anxious, distressed, angry, happy, neutral. "
                            "Respond with only the emotion word."
                        )
                    }
                ]
            }
        ])

        return response.text.strip()

    except Exception as e:
        return f"Error in emotion detection: {str(e)}"
