from Agents.base_agent import BaseAgent

class AssistantAgent(BaseAgent):
    def generate_prompt(self, user_input):
        return f"you are a helpful assistant. User asked: {user_input}"
     