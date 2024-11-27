# AI-Powered Chatbot (Small-Scale)

This project is a simple chatbot API powered by OpenAI's GPT model. Users can ask questions and receive intelligent responses. Optionally, chat history is saved to a database.

## Features
- Intelligent chatbot powered by OpenAI GPT
- Optional chat history storage
- File-based knowledge integration (e.g., via llama_index)

## Tech Stack
- **Backend**: FastAPI
- **Chatbot**: OpenAI GPT
- **Database**: SQLite (optional)

## Installation

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-chatbot.git
   cd ai-chatbot
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
6. Access the API documentation:
   Swagger UI: http://127.0.0.1:8000/docs
7. Example Request:
   ```bash
   {
     "message": "What is the capital of France?"
   }
8. Example Response:
   ```bash
   {
     "response": "The capital of France is Paris."
   }
