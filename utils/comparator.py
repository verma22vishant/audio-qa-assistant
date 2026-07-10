from difflib import ndiff
from jiwer import wer


def compare_transcripts(text1, text2):
    words1 = text1.split()
    words2 = text2.split()

    differences = list(ndiff(words1, words2))

    missing_words = []
    extra_words = []

    for item in differences:
        if item.startswith("- "):
            missing_words.append(item[2:])

        elif item.startswith("+ "):
            extra_words.append(item[2:])

    error_rate = wer(text1, text2)

    similarity = round((1 - error_rate) * 100, 2)

    return {
        "similarity": similarity,
        "missing_words": missing_words,
        "extra_words": extra_words
    }