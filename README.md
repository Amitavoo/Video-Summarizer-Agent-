# 🎙️ Video-Agent: AI Meeting Intelligence Assistant

<div align="center">

### **Production-Ready AI Meeting Assistant powered by Whisper, Mistral AI, LangChain & ChromaDB**

Automatically transcribe meetings and YouTube videos, generate summaries, extract action items, and chat with your meetings using Retrieval-Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge\&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/Vector-Database-orange?style=for-the-badge)

</div>

---

# 📌 Overview

**Video-Agent** is a production-ready AI application that converts long-form videos, meeting recordings, and YouTube content into an intelligent knowledge base.

Instead of manually watching hours of recordings, Video-Agent automatically:

* Downloads YouTube videos
* Extracts audio
* Transcribes speech (including Hinglish)
* Generates AI summaries
* Extracts action items
* Creates meeting titles
* Stores transcript embeddings inside ChromaDB
* Lets you chat with your meetings using Retrieval-Augmented Generation (RAG)

The project demonstrates an end-to-end LLM pipeline built with modern AI engineering practices.

---

# ✨ Features

## 🎥 Video Processing

* YouTube URL support
* Automatic audio extraction
* FFmpeg audio conversion
* Local audio file support

---

## 🎙️ Speech Recognition

* OpenAI Whisper transcription
* Hinglish support
* Automatic transcript generation
* 30-second intelligent chunking

---

## 🧠 AI Meeting Intelligence

* AI-generated summaries
* Meeting title generation
* Action item extraction
* Context-aware question answering
* Long transcript understanding

---

## 🔍 Retrieval-Augmented Generation (RAG)

* Semantic search
* Context retrieval
* ChromaDB vector storage
* HuggingFace embeddings
* LangChain LCEL pipelines

---

## 📄 Export

* Transcript export
* Summary export
* PDF generation

---

# 🏗️ System Architecture

```text
                    YouTube URL / Audio File
                              │
                              ▼
                         yt-dlp + FFmpeg
                              │
                              ▼
                    Audio Preprocessing
                              │
                              ▼
                     OpenAI Whisper STT
                              │
                       Full Transcript
                              │
                30 Second Intelligent Chunking
                              │
                              ▼
               HuggingFace Sentence Embeddings
                              │
                              ▼
                    ChromaDB Vector Database
                              │
                              ▼
                  LangChain LCEL RAG Pipeline
                              │
         ┌────────────────────┴───────────────────┐
         │                                        │
         ▼                                        ▼
   Mistral AI Summary                  Conversational Chat
   Action Items                        Semantic Search
   Meeting Title                       Context Retrieval
                              │
                              ▼
                      Streamlit Web UI
```

---

# 🛠️ Tech Stack

| Category         | Technologies                      |
| ---------------- | --------------------------------- |
| Programming      | Python                            |
| Frontend         | Streamlit                         |
| Speech-to-Text   | OpenAI Whisper                    |
| LLM              | Mistral AI                        |
| Embeddings       | HuggingFace Sentence Transformers |
| Framework        | LangChain LCEL                    |
| Vector Database  | ChromaDB                          |
| Audio Processing | FFmpeg                            |
| Video Download   | yt-dlp                            |
| PDF Reports      | FPDF2                             |

---

# 📂 Project Structure

```text
Video-Agent/
│
├── core/
│   ├── rag_engine.py          # Conversational RAG pipeline
│   ├── summarize.py           # Summary, titles & action items
│   ├── transcriber.py         # Whisper transcription
│   └── vector_store.py        # ChromaDB integration
│
├── downloads/                 # Downloaded media & processed audio
│
├── utils/
│   └── audio_processor.py     # yt-dlp + FFmpeg processing
│
├── .env
├── .gitignore
├── app.py                     # Streamlit application
├── main.py                    # Main workflow
├── test.py                    # Testing script
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/video-agent.git

cd video-agent
```

---

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install FFmpeg

Download FFmpeg and ensure both `ffmpeg` and `ffprobe` are available in your system PATH.

Verify installation:

```bash
ffmpeg -version
ffprobe -version
```

---

## 5. Configure Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_api_key
```

---

# 🚀 Running the Application

Launch the Streamlit UI:

```bash
streamlit run app.py
```

Or run the project directly:

```bash
python main.py
```

---

# 🔄 Workflow

```text
Input Video
      │
      ▼
Download Audio
      │
      ▼
Audio Processing
      │
      ▼
Whisper Transcription
      │
      ▼
Transcript Chunking
      │
      ▼
Embedding Generation
      │
      ▼
ChromaDB Storage
      │
      ▼
Mistral AI
 ├── Summary
 ├── Title
 └── Action Items
      │
      ▼
Chat with Transcript (RAG)
```

---

# 💬 Example Questions

Users can ask:

* What was discussed in the meeting?
* Give me the key takeaways.
* What action items were assigned?
* Who is responsible for each task?
* Summarize the last 10 minutes.
* Explain the discussion about AI.
* What decisions were made?
* Generate meeting notes.

---

# 🎯 Use Cases

* Business Meetings
* Team Stand-ups
* Client Calls
* Podcasts
* Online Lectures
* Research Discussions
* Interview Analysis
* YouTube Video Summaries
* Technical Workshops
* Educational Content

---

# 🔮 Future Enhancements

* Speaker Diarization
* Live Meeting Transcription
* Multi-language Translation
* Cloud Deployment
* User Authentication
* Calendar Integration
* Email Automation
* Meeting Analytics Dashboard
* Multi-LLM Support
* Docker Deployment

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📜 License

Licensed under the **MIT License**.

---

# 👨‍💻 Author

**Amitava Mondal**

B.Tech CSE (AI) | AI & Machine Learning Enthusiast | Full Stack Developer

Building production-ready AI systems powered by LLMs, RAG, and Generative AI.

---

⭐ **If you found this project useful, consider giving it a Star on GitHub!**

