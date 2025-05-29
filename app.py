import streamlit as st
from utils.agents_factory import AgentsFactory

# Set page config (MUST be the first Streamlit command)
st.set_page_config(
    page_title="🤖 Multi Agent Swarm Chatbot",
    layout="centered"
)

st.markdown("Choose an agent and start chatting!")

agent_type = st.selectbox(
    "Choose an AI Agent", 
    ["Assistant", "Developer", "Therapist", "Teacher"]
)
user_input = st.text_area("Your message: ", height=150)

if user_input:
    agent = AgentsFactory.get_agent(agent_type)
    if agent:
        response = agent.respond(user_input)
        st.markdown(f"**{agent_type}**: {response}")

    