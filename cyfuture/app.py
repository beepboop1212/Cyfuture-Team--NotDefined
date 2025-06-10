# app.py

import streamlit as st
from utils import get_explanation, log_question, load_progress
import fitz  # PyMuPDF

st.set_page_config(page_title="EduGenie AI", page_icon="🧠", layout="wide")
st.title("📚 EduGenie AI – Your Personal Learning Companion")

# Session state
if "questions" not in st.session_state:
    st.session_state.questions = []

# Sidebar Onboarding
with st.sidebar:
    st.header("🎓 Onboarding")
    grade = st.selectbox("Select Grade", ["6", "7", "8", "9", "10", "11", "12"])
    subject = st.selectbox("Select Subject", ["Math", "Science"])
    style = st.radio("Preferred Learning Style", ["Textual", "Visual", "Interactive"])

# Main Input Section
st.markdown("### 🙋 Ask a Question")
q_input = st.text_area("Type your question here")

uploaded_file = st.file_uploader("Or upload a PDF file", type=["pdf"])

def extract_text_from_pdf(file) -> str:
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"❌ Error reading PDF: {e}"

# Handle PDF Upload
if uploaded_file:
    extracted_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Extracted Text from PDF", value=extracted_text, height=200)
    if not q_input:
        q_input = extracted_text

# Handle Submission
if st.button("🔍 Solve My Doubt"):
    if q_input.strip():
        response = get_explanation(q_input.strip(), style)
        st.session_state.questions.append({
            "question": q_input.strip(),
            "answer": response,
            "style": style
        })
        log_question(q_input, style)
        st.success("✅ Here's your explanation:")
        st.write(response)
    else:
        st.warning("Please type a question or upload a valid PDF.")

# Progress Display
st.markdown("---")
st.markdown("### 📈 Your Learning Progress")
progress = load_progress()

st.write(f"Total Questions Asked: {len(st.session_state.questions)}")
st.write("Preferred Learning Style:", style)
st.progress(len(st.session_state.questions) % 10)

# Show History
st.markdown("### 📝 Previous Questions")
for q in st.session_state.questions[-5:][::-1]:
    st.markdown(f"**Q:** {q['question']}")
    st.markdown(f"**Style:** {q['style']}")
    st.markdown(f"**A:** {q['answer']}")
    st.markdown("---")