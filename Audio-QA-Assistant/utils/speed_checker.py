import librosa


def calculate_wpm(audio_path, transcript):
    audio, sample_rate = librosa.load(
        audio_path,
        sr=None
    )

    duration_seconds = librosa.get_duration(
        y=audio,
        sr=sample_rate
    )

    words = transcript.split()

    total_words = len(words)

    duration_minutes = duration_seconds / 60

    if duration_minutes == 0:
        return 0

    wpm = round(
        total_words / duration_minutes,
        2
    )

    return wpm