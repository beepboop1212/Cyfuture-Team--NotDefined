📚 EduGenie AI – Your Personal Learning Companion

EduGenie AI is an intelligent and user-friendly Streamlit web app that leverages the power of Google Gemini (Generative AI) to make learning interactive, accessible, and personalized for students from grades 6 to 12. Whether you’re a visual learner, prefer in-depth textual explanations, or thrive with interactive Socratic dialogue, EduGenie AI adapts to your preferred learning style.

⸻

🚀 Features
	•	✅ Ask Anything: Type any subject-related question and get AI-generated answers instantly.
	•	🧠 Multiple Learning Styles:
	•	Textual: Textbook-style detailed explanations.
	•	Visual: Visual analogies and intuitive comparisons.
	•	Interactive: Socratic step-by-step reasoning. (more styles to be added in the future)
	•	📄 Doc Support: Upload class notes or books in PDF format and extract text for question generation or explanation. Doubts in image format are also allowed
	•	📈 Track Progress: View your learning history and question count.
	•	📝 Learning History: See your past queries and explanations to reinforce understanding.

⸻

📷 Demo

https://drive.google.com/file/d/1UyLxoTGy6zxXNzdzhDqv3M7dcB5V3Txl/view?usp=share_link

⸻

🔧 Tech Stack
	•	Frontend: Streamlit
	•	AI Backend: Gemini 1.5 Flash (Google Generative AI)
	•	PDF Processing: PyMuPDF (fitz)

⸻

📁 Project Structure

├── app.py              # Streamlit UI and main logic
├── utils.py            # AI interaction, logging, and PDF processing
├── requirements.txt    # Python dependencies
└── README.md           # Project overview


⸻

✅ Getting Started

🔧 Installation

git clone https://github.com/yourusername/edugenie-ai.git
cd edugenie-ai
pip install -r requirements.txt

🔑 Setup

Replace "API_KEY" in utils.py with your Google Generative AI API key.

genai.configure(api_key="YOUR_ACTUAL_API_KEY")

▶️ Run the App

streamlit run app.py


⸻

🌟 Potential Use Cases
	•	Students: Get instant help on tough concepts.
	•	Teachers: Generate concept explanations for lesson plans.
	•	Parents: Support children in homework and revision.
	•	Self-learners: Study independently using AI as a tutor.

⸻

📬 Contributing

Have ideas to improve EduGenie AI? PRs and issues are welcome!

⸻

🛡️ Disclaimer

EduGenie AI is an educational support tool. Answers may not always be perfect — always verify with a teacher or trusted source.

⸻

📃 License

This project is open for educational and personal use. No license applied.

