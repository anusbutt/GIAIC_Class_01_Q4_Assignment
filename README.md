# 🤖 AI Agent Chatbot – GIAIC Q4 Assignment

This is a basic multi-agent AI chatbot built using Python and [LiteLLM](https://docs.litellm.ai/) with models served via [OpenRouter](https://openrouter.ai). It lets users choose from multiple personas like a therapist, teacher, assistant, or developer, and start chatting with them!

---

## 🧠 Agents Included

| Agent     | Model                         | Hosted on     |
|-----------|-------------------------------|---------------|
| 🧑‍💼 Assistant | `openai/gpt-4o`               | OpenRouter    |
| 👨‍💻 Developer| `openai/gpt-3.5-turbo`         | OpenRouter    |
| 🧠 Therapist| `mistralai/mistral-7b-instruct`| OpenRouter    |
| 👩‍🏫 Teacher  | `openai/gpt-4`                 | OpenRouter    |

---

## 🔧 Tech Stack

- **Python 3.10+**
- **LiteLLM** – Unified API wrapper for calling LLMs
- **OpenRouter API** – Provides free and paid access to many LLMs
- **Streamlit** (optional) – For the user interface
- **Git + GitHub** – Version control and hosting

---

## 📁 Folder Structure

.
├── app.py # Main interface (Streamlit or CLI)
├── llm_client.py # Core logic to communicate with OpenRouter via LiteLLM
├── config.py # API keys and model configs
├── requirements.txt # Dependency list
└── README.md # This file

🌐 Free Deployment Options

| Platform                                   | Best For                 | Notes                                 |
| ------------------------------------------ | ------------------------ | ------------------------------------- |
| [Streamlit.io](https://streamlit.io/cloud) | LLM chat apps            | ✅ Highly recommended for this project |
| [Render](https://render.com)               | Flask/Backend APIs       | Free, but may sleep after inactivity  |
| [Replit](https://replit.com)               | Quick full-stack hosting | Slower but easy for beginners         |
