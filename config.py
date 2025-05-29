# config.py - Properly formatted configuration file

class Config:
    # API Configuration
    OPENROUTER_API_KEY = "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"  # Must be in quotes
    BASE_URL = "https://openrouter.ai/api/v1"
    
    # Required Headers
    HEADERS = {
        "HTTP-Referer": "http://localhost:8501",  # For local development
        "X-Title": "AI Agent App"                # Your application name
    }

    # Model Configuration
    MODELS = {
        "assistant": "openai/gpt-4o",  # Note: Added :free
        "developer": "openai/gpt-3.5-turbo",
        "therapist": "openai/gpt-3.5-turbo",
        "teacher": "openai/gpt-4"
    }