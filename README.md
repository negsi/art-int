# Artint - An intelligent argentic system for AI.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Artint enables the simple and convenient creation of intelligent AI agents that can take over any conceivable task on your computer for you.

## 🚀 Requirements

- Python 3.10 or newer
- pip (Python Package Installer)
- Optional: a virtual environment (recommended)

## 📦 Installation

### 1. Clone or download repository

```bash
git clone https://github.com/negsi/art-int.git
cd art-int
```

### 2. Create a virtual environment (optional, but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API Token

For testing purposes we currently support only OpenAI language models.
Please make sure to provide a valid _OPENAI_API_KEY_ in your _.env_ file to run the app. 

```bash
cp .env.template .env
```
Then edit _.env_ and insert your _OPENAI_API_KEY_.

## ▶️ Running the application

```bash
flask --app app run --debug # Use this...
python app.py # ...or this
```

You can now access the application at:

```bash
http://127.0.0.1:5000
```