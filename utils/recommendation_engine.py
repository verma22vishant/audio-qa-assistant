def generate_recommendations(
    similarity,
    wpm_1,
    wpm_2,
    pause_count_1,
    pause_count_2
):

    recommendations = []

    if similarity < 90:

        recommendations.append(
            "Transcript similarity is low. Review the audio."
        )

    if wpm_1 > 180:

        recommendations.append(
            "Audio 1 speech is too fast."
        )

    if wpm_2 > 180:

        recommendations.append(
            "Audio 2 speech is too fast."
        )

    if wpm_1 < 100:

        recommendations.append(
            "Audio 1 speech is too slow."
        )

    if wpm_2 < 100:

        recommendations.append(
            "Audio 2 speech is too slow."
        )

    if pause_count_1 > 10:

        recommendations.append(
            "Audio 1 contains too many pauses."
        )

    if pause_count_2 > 10:

        recommendations.append(
            "Audio 2 contains too many pauses."
        )

    if not recommendations:

        recommendations.append(
            "Audio quality looks good."
        )

    return recommendations