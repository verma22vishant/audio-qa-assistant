import pandas as pd


def export_to_excel(
    comparison,
    wpm_1,
    wpm_2,
    pauses_1,
    pauses_2
):

    data = {

        "Metric": [

            "Similarity",

            "Audio 1 WPM",

            "Audio 2 WPM",

            "Audio 1 Pause Count",

            "Audio 2 Pause Count"
        ],

        "Value": [

            comparison["similarity"],

            wpm_1,

            wpm_2,

            len(pauses_1),

            len(pauses_2)
        ]
    }

    df = pd.DataFrame(data)

    path = "reports/report.xlsx"

    df.to_excel(
        path,
        index=False
    )

    return path