from abc import ABC, abstractmethod
from models.llm_client import LLMClient

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name
        self.client = LLMClient(name)

    @abstractmethod
    def generate_prompt(self, user_input):
        pass

    def respond(self, user_input):
        prompt = self.generate_prompt(user_input)
        return self.client.query(prompt)

        
