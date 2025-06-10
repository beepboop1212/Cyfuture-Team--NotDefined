# utils.py

import os
import google.generativeai as genai


genai.configure(api_key="API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_explanation(question_or_text, style):
    style_prompts = {
        "Textual": "Explain this concept in a detailed but simple textbook-like way.",
        "Visual": "Use visual analogies to explain this concept.",
        "Interactive": "Use the Socratic method to explain this concept step by step."
    }

    prompt = f"{style_prompts.get(style, '')}\n\nQuestion: {question_or_text}"

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {e}"

def log_question(question, style):
    pass

def load_progress():
    return {"total_questions": 0, "mastery": "Getting Started"}