# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import logging
# from voice_of_patient import voice_recorder, transcription_from_voice_text, file_path
# from ai_brain import ask_text_model
# from voice_of_doctor import text_to_speech_with_gtts
# from emotion_model import detect_emotion_from_audio
# # ======================
# # Setup
# # ======================
# app = Flask(__name__)
# CORS(app)   # allow frontend
# logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


# # ======================
# # Routes
# # ======================
# @app.route("/ask", methods=["POST"])
# def ask():
#     """
#     Handles text-based questions from frontend
#     """
#     data = request.json
#     question = data.get("question", "")

#     if not question:
#         return jsonify({"answer": "No question provided"}), 400

#     # ---Logic of LLM call---
#     # answer = f"You asked: '{question}'. This is a dummy response."
#     answer = ask_text_model(question)
#     text_to_speech_with_gtts(answer,"doctor_voice.mp3")

#     return jsonify({"answer": answer})


# @app.route("/voice", methods=["POST"])
# def record_voice():
#     """
#     Records user voice and transcribes it
#     """
#     # success = voice_recorder(file_path)
#     # if not success:
#     #     return jsonify({"error": "Failed to record voice"}), 500

#     # try:
#     #     text = transcription_from_voice_text(file_path)
#     #     print("doctor responce:",text)
#     #     answer = ask_text_model(text)
#     #     text_to_speech_with_gtts(answer,"doctor_voice.mp3")
        
        
#     #     # return jsonify({"answer": answer})
#     #     return jsonify({"transcription": answer})
    
        
#     #     # return jsonify({"transcription": text})
#     # except Exception as e:
#     #     logging.error(f"Error in transcription: {e}")
#     #     return jsonify({"error": str(e)}), 500
    
    
#     # ///////////////////
#     try:
#         voice_recorder(file_path)  # just record, no return needed
#         text = transcription_from_voice_text(file_path)
#         emotion=detect_emotion_from_audio(file_path)
#         print("Emotions are:",emotion)
#         # answer = ask_text_model(text)
#     #   text_to_speech_with_gtts(answer,"doctor_voice.mp3")
        
#         # return jsonify({"transcription": text,"Emotions":emotion})
#         return jsonify({"transcription": text})
#     except Exception as e:
#         logging.error(f"Error in transcription: {e}")
#         return jsonify({"error": str(e)}), 500
#     # /////////////////////


# # ======================
# # Main
# # ======================
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from voice_of_patient import voice_recorder, transcription_from_voice_text, file_path
from ai_brain import ask_text_model
from voice_of_doctor import text_to_speech_with_gtts
from emotion_model import detect_emotion_from_audio

# ======================
# Setup
# ======================
app = Flask(__name__)
CORS(app)   # allow frontend
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


# ======================
# Routes
# ======================
@app.route("/ask", methods=["POST"])
def ask():
    """
    Handles text-based questions from frontend (no emotion)
    """
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"answer": "No question provided"}), 400

    # --- Plain text query ---
    answer = ask_text_model(question)
    text_to_speech_with_gtts(answer, "doctor_voice.mp3")

    return jsonify({"answer": answer})


@app.route("/voice", methods=["POST"])
def record_voice():
    """
    Records user voice, extracts transcription + emotion,
    then sends both to reasoning model.
    """
    try:
        # 1. Record patient’s voice
        voice_recorder(file_path)

        # 2. Transcribe audio -> text
        text = transcription_from_voice_text(file_path)

        # 3. Extract emotion from audio
        emotion = detect_emotion_from_audio(file_path)
        logging.info(f"Transcription: {text}")
        logging.info(f"Emotions are: {emotion}")

        # 4. Build enriched query (VERY IMPORTANT: no system role, only user)
        enriched_query = (
            f"Patient query: {text}\n"
            f"Detected emotion: {emotion}\n"
            "Please provide a helpful and empathetic medical response, "
            "considering both the medical question and the patient’s emotional state.But the answer should not tool long, it should be not too short and not too long answer but effective."
        )

        # 5. Ask reasoning LLM with enriched query
        answer = ask_text_model(enriched_query)

        # 6. Convert doctor’s answer to speech
        text_to_speech_with_gtts(answer, "doctor_voice.mp3")

        # 7. Return everything back to frontend
        return jsonify({
            "transcription": text,
            "emotion": emotion,
            "answer": answer
        })

    except Exception as e:
        logging.error(f"Error in voice pipeline: {e}")
        return jsonify({"error": str(e)}), 500


# ======================
# Main
# ======================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
