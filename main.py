import google.generativeai as genai

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyBHA0ZZQu1Zy5u7xE1lAQW7-XYj-k1-asY")

# Zero-shot prompt for MythicMind character generation
prompt = """
You are a character generator for a creative writing app. 
Generate a detailed character profile for the following genre: fantasy.

Include:
- Name
- Personality traits
- Backstory
- Motivations
- Unique quirks

Do not use any examples. Only follow these instructions.
"""

# Use the latest available Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")
response = model.generate_content(prompt)

print(response.text)

# --- Video Explanation ---
# Zero-shot prompting means giving an AI a task using only instructions, without any examples.
# In this code, the prompt asks Gemini to generate a character profile for a fantasy genre.
# No sample profiles are provided, so the AI must understand and perform the task from the instructions alone.
# This demonstrates zero-shot prompting in action, where the AI applies its learned knowledge to a new task.