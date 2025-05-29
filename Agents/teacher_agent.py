from Agents.base_agent import BaseAgent

class TeacherAgent(BaseAgent):
    def generate_prompt(self, user_input):
        return f"you are an experienced teacher. Explain : {user_input}"