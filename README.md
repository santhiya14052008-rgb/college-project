# LegalEase

LegalEase is an AI-powered legal document assistance project designed to help users understand and work with legal documents.

## Features

- Legal document processing
- Document format conversion
- Legal text assistance
- AI-based document support
- PDF, DOCX and HTML document handling

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- FastAPI
- Python-dotenv

## Project Structure

- `api_core/` - API and backend logic
- `backend/` - Backend services
- `frontend/` - Streamlit application
- `services/` - Document processing services
- `utils/` - Utility functions

## Setup

1. Clone the repository.
2. Create a Python virtual environment.
3. Install the required packages.

```bash
pip install -r requirements.txt
LegalEase/
│
├── api_core/
│   ├── __init__.py
│   └── ...
│
├── backend/
│   ├── __init__.py
│   └── ...
│
├── frontend/
│   ├── app.py
│   └── ...
│
├── services/
│   ├── __init__.py
│   └── ...
│
├── utils/
│   ├── __init__.py
│   └── ...
│
├── check_models.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
