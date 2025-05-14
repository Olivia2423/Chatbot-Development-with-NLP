# Chatbot Web Application

A simple Django-based chatbot web application integrated with the Gemini AI model to handle user queries and provide intelligent responses. Users can register, log in, and interact with the AI through a chat interface. This project demonstrates the integration of Django with external APIs to create a functional AI-powered chatbot.

## Features

- **User Authentication**: Allows users to register, log in, and log out.
- **Chat Interface**: Users can send messages to the AI chatbot and receive responses.
- **Integration with Gemini AI**: The chatbot leverages Gemini for generating responses based on user input.
- **Real-time Communication**: As users type messages, responses are provided in real-time.

## Technologies Used

- **Backend**: Django (Python)
- **AI Model**: Gemini (Generative AI)
- **Frontend**: HTML, CSS, JavaScript (for interactivity)
- **Database**: SQLite (default database for Django)
- **Environment Variables**: Used to store sensitive API keys securely using a `.env` file.
- **Authentication**: Django’s built-in authentication system.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python (version 3.8 or higher)
- Django
- Google Generative AI SDK (for model integration)
- `python-dotenv` (for environment variable management)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Olivia2423/Chatbot-Development-with-NLP.git
   cd chatbot-django
2. **Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
3. **Install the dependencies
   pip install -r requirements.txt
4. **Set up environment variables
   Create a .env file in the root of your project with your API keys. For example:
    ```bash
    GEMINI_API_KEY=your_api_key_here
Make sure the .env file is listed in .gitignore to prevent it from being pushed to GitHub.

5. **Apply migrations:
   python manage.py migrate
6. **Run the development server
   python manage.py runserver

You should now be able to access the chatbot at http://127.0.0.1:8000/.

### uSAGE
1. Login/Register: If you don't have an account, register. Otherwise, log in using your credentials.
2.nteract with the Chatbot: Type your messages in the input box, and the chatbot will generate responses using Gemini.
