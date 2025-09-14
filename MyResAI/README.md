# MyResAI

A voice-enabled restaurant assistant app for South Indian cuisine, built with Python, FastAPI, Gemini, Sarvam AI, and SQLite.

## Features
- Telugu speech input and speech-to-text (STT) using Sarvam AI
- Gemini-2.5-flash integration for AI-powered responses
- FastAPI MCP server for menu and queries
- SQLite database for customers, menu, orders, and reservations
- Unit tests with pytest
- Easy extensibility for TTS, RAG, and vector database

## Project Structure
```
MyResAI/
├── app.py                  # Main application logic
├── database_setup.py       # Creates and populates the SQLite database
├── mcp_server.py           # FastAPI MCP server
├── gemini_integration.py   # Gemini API integration
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── unittesting/            # Unit tests
└── README.md               # Project documentation
```

## Getting Started
1. **Clone the repository:**
   ```
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>/MyResAI
   ```
2. **Set up the environment:**
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in your API keys.

4. **Set up the database:**
   ```
   python database_setup.py
   ```

5. **Run the MCP server:**
   ```
   uvicorn mcp_server:app --reload
   ```

6. **Run the main app:**
   ```
   python app.py
   ```

## Testing
Run unit tests with:
```
pytest
```

## Extending
- Add TTS, RAG, or vector DB features by creating new modules and updating `app.py`.
- Update the database schema in `database_setup.py` as needed.

## License
MIT

## Author
- Srinivas (srinidevops1)

---
For questions or contributions, open an issue or pull request on GitHub.
