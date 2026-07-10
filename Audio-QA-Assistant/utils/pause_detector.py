import librosa
import numpy as np


def detect_pauses(audio_path):

    y, sr = librosa.load(audio_path)

    intervals = librosa.effects.split(
        y,
        top_db=30
    )

    pauses = []

    previous_end = 0

    for start, end in intervals:

        pause_duration = (
            start - previous_end
        ) / sr

        if pause_duration > 0.5:

            pauses.append(
                round(
                    pause_duration,
                    2
                )
            )

        previous_end = end

    return pauses