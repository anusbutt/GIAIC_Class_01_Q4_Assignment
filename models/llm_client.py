import litellm
import os
from config import Config

class LLMClient:
    def __init__(self, model_name):
        try:
            self.model = Config.MODELS[model_name.lower()]
            # Direct configuration (more reliable than environment variables)
            self.api_key = Config.OPENROUTER_API_KEY
            self.api_base = Config.BASE_URL
            self.timeout = 30
        except KeyError:
            raise ValueError(f"Unknown model for agent type: {model_name}")

    def query(self, prompt):
        """Send query to LLM with proper OpenRouter authentication"""
        try:
            response = litellm.completion(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                api_key=self.api_key,  # Explicitly pass key
                api_base=self.api_base,
                timeout=self.timeout,
                max_tokens=512,
                litellm_provider="openrouter"
            )
            # Proper response access (litellm returns object, not dict)
            return response.choices[0].message.content
        except litellm.AuthenticationError as e:
            return f"🔑 Authentication Failed: {str(e)}\nPlease verify your OpenRouter API key"
        except Exception as e:
            return f"⚡ Error: {str(e)}"