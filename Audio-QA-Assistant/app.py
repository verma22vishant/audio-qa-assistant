import os

import pandas as pd
import streamlit as st

from utils.recommendation_engine import generate_recommendations
from utils.excel_export import export_to_excel
from utils.pause_detector import detect_pauses
from utils.comparator import compare_transcripts
from utils.pdf_generator import generate_pdf_report
from utils.speed_checker import calculate_wpm
from utils.transcriber import generate_transcript, save_transcript

# =========================
# Folders
# =========================

os.makedirs("uploads", exist_ok=True)
os.makedirs("transcripts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="AI Audio QA Assistant",
    page_icon="🎧",
    layout="wide"
)

# =========================
# Sidebar
# =========================

st.sidebar.title("🎧 Audio QA Assistant")

st.sidebar.info(
    """
    ### Features

    ✅ Audio comparison

    ✅ Transcript comparison

    ✅ WPM analysis

    ✅ Pause detection

    ✅ AI recommendations

    ✅ PDF export

    ✅ Excel export
    """
)

# =========================
# Header
# =========================

st.title("🎧 AI Audio QA Assistant")

st.write(
    "Compare two audio files or upload transcripts to analyze quality."
)

# =========================
# Transcript Upload
# =========================

st.subheader("📄 Upload Transcripts (Optional)")

col1, col2 = st.columns(2)

with col1:

    txt_1 = st.file_uploader(
        "Transcript 1 (.txt)",
        type=["txt"],
        key="txt1"
    )

with col2:

    txt_2 = st.file_uploader(
        "Transcript 2 (.txt)",
        type=["txt"],
        key="txt2"
    )

# =========================
# Audio Upload
# =========================

st.subheader("🎵 Upload Audio Files")

col1, col2 = st.columns(2)

with col1:

    audio_1 = st.file_uploader(
        "Upload Audio File 1",
        type=["mp3", "wav", "m4a"],
        key="audio1"
    )

with col2:

    audio_2 = st.file_uploader(
        "Upload Audio File 2",
        type=["mp3", "wav", "m4a"],
        key="audio2"
    )

# =========================
# Main Button
# =========================

if st.button("🚀 Analyze Files"):

    if audio_1 and audio_2:

        audio_1_path = os.path.join(
            "uploads",
            audio_1.name
        )

        audio_2_path = os.path.join(
            "uploads",
            audio_2.name
        )

        with open(audio_1_path, "wb") as file:

            file.write(
                audio_1.getbuffer()
            )

        with open(audio_2_path, "wb") as file:

            file.write(
                audio_2.getbuffer()
            )

        with st.spinner("Generating transcripts..."):

            # Transcript 1

            if txt_1:

                transcript_1 = txt_1.read().decode(
                    "utf-8"
                )

            else:

                transcript_1 = generate_transcript(
                    audio_1_path
                )

            # Transcript 2

            if txt_2:

                transcript_2 = txt_2.read().decode(
                    "utf-8"
                )

            else:

                transcript_2 = generate_transcript(
                    audio_2_path
                )

            save_transcript(
                transcript_1,
                "transcripts/transcript_1.txt"
            )

            save_transcript(
                transcript_2,
                "transcripts/transcript_2.txt"
            )

        st.success(
            "Analysis completed successfully!"
        )

        # =========================
        # Show Transcripts
        # =========================

        st.subheader("📄 Generated Transcripts")

        col1, col2 = st.columns(2)

        with col1:

            st.text_area(
                "Transcript 1",
                transcript_1,
                height=250
            )

        with col2:

            st.text_area(
                "Transcript 2",
                transcript_2,
                height=250
            )

        # =========================
        # Comparison
        # =========================

        comparison = compare_transcripts(
            transcript_1,
            transcript_2
        )

        wpm_1 = calculate_wpm(
            audio_1_path,
            transcript_1
        )

        wpm_2 = calculate_wpm(
            audio_2_path,
            transcript_2
        )

        pauses_1 = detect_pauses(
            audio_1_path
        )

        pauses_2 = detect_pauses(
            audio_2_path
        )

        # =========================
        # Metrics
        # =========================

        st.subheader("📊 Overview")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "Similarity",
                f"{comparison['similarity']}%"
            )

        with c2:

            st.metric(
                "Audio 1 WPM",
                f"{wpm_1}"
            )

        with c3:

            st.metric(
                "Audio 2 WPM",
                f"{wpm_2}"
            )

        # =========================
        # Speech Warnings
        # =========================

        st.subheader("⚠️ Speech Quality")

        if wpm_1 > 180:

            st.warning(
                "Audio 1 is too fast."
            )

        elif wpm_1 < 100:

            st.warning(
                "Audio 1 is too slow."
            )

        else:

            st.success(
                "Audio 1 speed is normal."
            )

        if wpm_2 > 180:

            st.warning(
                "Audio 2 is too fast."
            )

        elif wpm_2 < 100:

            st.warning(
                "Audio 2 is too slow."
            )

        else:

            st.success(
                "Audio 2 speed is normal."
            )

        # =========================
        # Missing Words
        # =========================

        st.subheader("🔍 Comparison Report")

        st.write("### Missing Words")

        if comparison["missing_words"]:

            st.write(
                comparison["missing_words"]
            )

        else:

            st.success(
                "No missing words found."
            )

        st.write("### Extra Words")

        if comparison["extra_words"]:

            st.write(
                comparison["extra_words"]
            )

        else:

            st.success(
                "No extra words found."
            )

        # =========================
        # Pause Analysis
        # =========================

        st.subheader("⏸️ Pause Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"Audio 1 pauses: {len(pauses_1)}"
            )

            st.write(pauses_1)

        with col2:

            st.write(
                f"Audio 2 pauses: {len(pauses_2)}"
            )

            st.write(pauses_2)

        # =========================
        # AI Recommendations
        # =========================

        recommendations = generate_recommendations(
            comparison["similarity"],
            wpm_1,
            wpm_2,
            len(pauses_1),
            len(pauses_2)
        )

        st.subheader("🤖 AI Recommendations")

        for item in recommendations:

            st.info(item)

        # =========================
        # Analytics Chart
        # =========================

        chart_data = {

            "Metric": [

                "Similarity",

                "Audio 1 WPM",

                "Audio 2 WPM",

                "Pause Count 1",

                "Pause Count 2"
            ],

            "Value": [

                comparison["similarity"],

                wpm_1,

                wpm_2,

                len(pauses_1),

                len(pauses_2)
            ]
        }

        chart_df = pd.DataFrame(
            chart_data
        )

        st.subheader(
            "📈 Analytics Dashboard"
        )

        st.bar_chart(
            chart_df.set_index(
                "Metric"
            )
        )

        # =========================
        # Transcript Table
        # =========================

        st.subheader(
            "📝 Transcript Comparison"
        )

        words_1 = transcript_1.split()

        words_2 = transcript_2.split()

        max_len = max(
            len(words_1),
            len(words_2)
        )

        words_1.extend(
            [""] * (
                max_len - len(words_1)
            )
        )

        words_2.extend(
            [""] * (
                max_len - len(words_2)
            )
        )

        comparison_df = pd.DataFrame(
            {
                "Transcript 1": words_1,
                "Transcript 2": words_2
            }
        )

        st.dataframe(
            comparison_df,
            use_container_width=True
        )

        # =========================
        # PDF Export
        # =========================

        pdf_path = (
            "reports/comparison_report.pdf"
        )

        generate_pdf_report(
            transcript_1,
            transcript_2,
            comparison,
            pdf_path
        )

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="comparison_report.pdf",
                mime="application/pdf"
            )

        # =========================
        # Excel Export
        # =========================

        excel_path = export_to_excel(
            comparison,
            wpm_1,
            wpm_2,
            pauses_1,
            pauses_2
        )

        with open(
            excel_path,
            "rb"
        ) as excel_file:

            st.download_button(
                label="📥 Download Excel Report",
                data=excel_file,
                file_name="report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    else:

        st.warning(
            "Please upload both audio files."
        )