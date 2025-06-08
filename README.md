# GPT-4.1 Nano CLI Chatbot with Tool Integration

Welcome to my project illustrating a simple command-line chatbot using OpenAI's GPT-4.1 Nano model that can delegate math operations (add, subtract, multiply, divide) to Python functions as tools.

---

## Features

- Interacts with the GPT-4.1 Nano model
- Routes mathematical queries to specific Python functions
- Modular code structure with tools and main chatbot logic separated
- Uses `.env` file for secure API key management

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create and activate a virtual environment

```bash
python -m venv <environment name>
source <environment name>/bin/activate      # Linux/macOS
.\<environment name>\Scripts\activate       # Windows
```

### 3. Install dependancies

```bash
pip install -r requirements.txt
```

### 4. Configure your OpenAI or Other LLM API key
Create a .env file in the project root with the following content:
```bash
OPENAI_API_KEY = <your_openai_api_key_here>
```

### 5. Running the chatbot

```bash
python main.py
```

## Notes
Make sure you have an active OpenAI API or other platform subscription and enough quota.
The chatbot currently supports simple math operations and can be extended with more tools.