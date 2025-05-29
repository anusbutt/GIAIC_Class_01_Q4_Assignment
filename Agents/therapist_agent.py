from Agents.base_agent import BaseAgent

class TherapistAgent(BaseAgent):
    def generate_prompt(self, user_input):
        return f"you are compassionate therapist. help user with : {user_input}"
            
