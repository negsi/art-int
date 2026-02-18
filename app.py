"""
MIT License
Copyright (c) 2026 Christian Siewert

Art-Int - An intelligent argent system for AI.

|======================================================|
| FOR TESTING PURPOSES WE ONLY SUPPORT OPENAI LLMs ATM |
|      AND FOR NOW YOU >>>MUST<<< PROVIDE A VALID      |
|   OPENAI_API_KEY IN YOUR .env FILE TO RUN THE APP.   |
|======================================================|
"""

# --- Standard library imports ---
import os

# --- Third‑party imports ---
import requests
from openai import OpenAI
from dotenv import load_dotenv 
from flask import Flask, request, jsonify, render_template

# --- Load environment variables ---
load_dotenv()

# --- Validate required variables ---
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError("OPENAI_API_KEY is not set. Please configure your .env file.")

# --- Initialize clients ---
client = OpenAI()

# --- Initialize Flask ---
app = Flask(__name__)

# --- Load system prompt ---
def load_system_prompt():
    with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
        return f.read().strip()

SYSTEM_PROMPT = load_system_prompt()
OPENAI_MODEL  = os.getenv("OPENAI_MODEL", "gpt-5-nano") 

@app.route("/")
def index():
    """
    Render the main application interface for our application.

    Purpose:
        Serve the root page that displays the application base view.

    Behavior:
        - Delivers the frontend HTML for the application UI
        - Acts as the entry point for all client-side interactions

    Returns:
        Rendered HTML template for the main overview page.
    """
    return render_template("app.html")


def call_ai(text):
    """
    Calls an AI.

    Parameters:
        text (str): The user prompt

    Returns:
        str: An AI answer

    Notes:
        - This function acts as an abstraction layer so the backend
          remains independent of the specific AI provider.
        - The actual model request should be implemented here.
    """

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content


# Development entry point
if __name__ == "__main__":
    app.run(debug=True)
