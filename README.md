# 🎧 AI Audio QA Assistant

An AI-powered tool that compares audio files and transcripts to help QA engineers, content testers, and e-learning teams detect mismatches, missing words, speech speed issues, and pauses.

---

## 🚀 Features

- 🎵 Compare two audio files
- 📝 Upload transcripts manually
- 🤖 Generate transcripts automatically using Whisper
- 🔍 Detect missing and extra words
- ⚡ Analyze speech speed (Words Per Minute)
- ⏸️ Detect pauses in audio
- 💡 AI-powered recommendations
- 📄 Export comparison reports as PDF
- 📊 Export analysis reports as Excel

---

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI Whisper
- Pandas
- Librosa
- PyDub
- FFmpeg
- ReportLab
- OpenPyXL

---

## 📂 Project Structure

```text
Audio-QA-Assistant/
├── assets/
├── models/
├── reports/
├── tests/
├── transcripts/
├── uploads/
├── utils/
├── app.py
├── config.py
├── Dockerfile
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/verma22vishant/audio-qa-assistant.git
```

Move into the project directory:

```bash
cd audio-qa-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser at:

```text
http://localhost:8501
```

---

## 📋 How It Works

1. Upload two audio files.
2. Optionally upload transcripts.
3. Generate transcripts automatically.
4. Compare transcripts and audio.
5. Analyze speech speed and pauses.
6. Download PDF and Excel reports.

---

## 📸 Screenshots

Add screenshots of your application here.

---

## 👨‍💻 Author

**Vishant Kumar**

- GitHub: https://github.com/verma22vishant
- LinkedIn: https://www.linkedin.com/in/vishantv/

---

## 📄 License

This project is licensed under the MIT License.