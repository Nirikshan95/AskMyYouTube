# AskMyYouTube

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-DeepSeek--V3-yellow)](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 🎯 Overview

AskMyYouTube is an intelligent Q&A application that allows users to ask questions about YouTube videos and get accurate answers based on the video's transcript. The application leverages advanced AI models to process video transcripts, create searchable knowledge bases, and provide contextually relevant answers to user queries.

## ✨ Key Features

- **🎬 YouTube Video Processing**: Automatically extracts and processes YouTube video transcripts
- **🧠 AI-Powered Q&A**: Uses DeepSeek-V3 model for intelligent question answering
- **🔍 Smart Retrieval**: Implements vector-based semantic search for finding relevant content
- **💬 Interactive Chat Interface**: User-friendly Streamlit web application with chat history
- **⚡ Efficient Indexing**: Creates and reuses vector stores for faster subsequent queries
- **🎯 Context-Aware Responses**: Provides answers strictly based on video content

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Models**: 
  - DeepSeek-V3-0324 (Chat/Q&A)
  - sentence-transformers/all-MiniLM-L6-v2 (Embeddings)
- **Vector Database**: FAISS
- **Text Processing**: LangChain
- **YouTube Integration**: youtube-transcript-api

## 📋 Prerequisites

- Python 3.8 or higher
- Hugging Face API token
- Internet connection for YouTube transcript fetching

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AskMyYouTube.git
cd AskMyYouTube
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the root directory:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
HF_TOKEN=your_huggingface_token_here
```

**Getting your Hugging Face token:**
1. Visit [Hugging Face](https://huggingface.co/)
2. Sign up/Login to your account
3. Go to Settings → Access Tokens
4. Create a new token with "Read" permissions

## 🎮 Usage

### Starting the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### How to Use

1. **Enter YouTube URL**: Paste any YouTube video URL in the input field
2. **Submit URL**: Click "Submit" to process the video transcript
3. **Ask Questions**: Use the chat input to ask questions about the video content
4. **View Answers**: Get AI-powered answers based on the video transcript
5. **Chat History**: Review previous questions and answers in the conversation history

### Example Workflow

```
1. URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
2. Question: "What is the main topic discussed in this video?"
3. AI Response: [Contextual answer based on video transcript]
```

## 📁 Project Structure

```
AskMyYouTube/
├── configs/
│   └── config.py              # Configuration settings
├── prompts/
│   └── template.txt           # Prompt template for AI model
├── src/
│   ├── indexing/
│   │   ├── chunking.py        # Text chunking utilities
│   │   ├── vector_store.py    # Vector database operations
│   │   └── youtube_transcript.py # YouTube transcript extraction
│   ├── ans_generation.py      # Answer generation pipeline
│   ├── models.py              # AI model loading functions
│   └── pipeline.py            # Main processing pipeline
├── vector_store/              # Cached vector databases
├── app.py                     # Streamlit application
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## ⚙️ Configuration

Customize the application behavior by modifying `configs/config.py`:

```python
# AI Models
EMBEDDING_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
CHAT_MODEL_ID = "deepseek-ai/DeepSeek-V3-0324"

# Text Processing
CHUNK_SIZE = 1000              # Characters per chunk
CHUNK_OVERLAP = 100            # Overlap between chunks

# AI Parameters
MAX_TOKENS = 200               # Maximum response length
TEMPERATURE = 0.3              # Response creativity (0-1)

# Retrieval
RETRIEVAL_K = 5                # Number of relevant chunks to retrieve
```

## 🔧 How It Works

### 1. **Video Processing**
- Extracts video ID from YouTube URL
- Fetches transcript using YouTube Transcript API
- Handles various URL formats (`youtu.be/`, `youtube.com/watch?v=`)

### 2. **Text Indexing**
- Splits transcript into manageable chunks
- Creates vector embeddings using sentence transformers
- Stores in FAISS vector database for fast retrieval
- Caches vector stores for repeated queries

### 3. **Question Answering**
- Processes user queries through semantic search
- Retrieves most relevant transcript segments
- Generates contextual answers using DeepSeek-V3
- Maintains conversation history

### 4. **Smart Caching**
- Reuses existing vector stores for the same video
- Significantly faster response times for repeated queries
- Automatic cache management

## 📊 Supported Video Types

- ✅ Videos with auto-generated captions
- ✅ Videos with manual captions
- ✅ Videos with multiple language captions
- ❌ Videos without any captions
- ❌ Private or restricted videos

## 🚨 Troubleshooting

### Common Issues

**"An error occurred: Try again"**
- Video might not have captions available
- Check if the video is public and has captions
- Try a different YouTube video

**"Failed to load model"**
- Verify your Hugging Face API token
- Check internet connectivity
- Ensure token has proper permissions

**Slow initial responses**
- First query processes the entire transcript
- Subsequent queries use cached data and are faster
- Processing time depends on video length

### Getting Help

1. Check the video has captions enabled
2. Verify your `.env` file configuration
3. Ensure all dependencies are installed
4. Try with a different YouTube video

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
5. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run the application in development mode
streamlit run app.py --server.runOnSave true
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the AI models
- [Streamlit](https://streamlit.io/) for the web application framework
- [LangChain](https://langchain.com/) for the AI pipeline tools
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction

## 📬 Contact

**MAHESH KETAM** - [GitHub Profile](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/AskMyYouTube](https://github.com/yourusername/AskMyYouTube)

---

⭐ **Star this repository if you find it helpful!**