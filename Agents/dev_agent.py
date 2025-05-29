from Agents.base_agent import BaseAgent

class DevAgent(BaseAgent):
    def generate_prompt(self, user_input):
        return f"you are a senior software engineer. Help with : {user_input}"
        
