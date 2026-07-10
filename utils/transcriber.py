import whisper
import os

# Load Whisper model once
model = whisper.load_model("base")


def generate_transcript(audio_path):
    """
    Generate transcript from an audio file.
    """

    result = model.transcribe(audio_path)

    return result["text"]


def save_transcript(text, output_file):
    """
    Save transcript to a text file.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)