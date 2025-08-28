import google.generativeai as genai

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyBHA0ZZQu1Zy5u7xE1lAQW7-XYj-k1-asY")

def generate_character_prompt(genre, traits=None, quirks=None):
    # Dynamic prompting: build the prompt based on user input
    prompt = f"You are a character generator for a creative writing app. Generate a detailed character profile for the following genre: {genre}.\n\n"
    prompt += "Respond ONLY in valid JSON format with the following keys: name, personality_traits, backstory, motivations, unique_quirks.\n"
    prompt += "Include:\n- name\n- personality_traits\n- backstory\n- motivations\n- unique_quirks\n"
    if traits:
        prompt += f"\nFocus on these traits: {', '.join(traits)}.\n"
    if quirks:
        prompt += f"\nAdd these quirks: {', '.join(quirks)}.\n"
    prompt += "\nRespond with a complete character profile in JSON."
    return prompt

# Example usage: user selects genre and custom traits/quirks
genre = "sci-fi"
traits = ["curious", "resourceful"]
quirks = ["always hums a tune", "collects alien artifacts"]

prompt = generate_character_prompt(genre, traits, quirks)

model = genai.GenerativeModel("gemini-1.5-pro-latest")
response = model.generate_content(
    prompt,
    generation_config={"top_p": 0.8, "temperature": 1.2, "top_k": 50}
)
print(response.text)

# Log the number of tokens used
if hasattr(response, "usage_metadata") and "total_tokens" in response.usage_metadata:
    print(f"Tokens used: {response.usage_metadata['total_tokens']}")
else:
    print("Token usage information not available.")

# --- Video Explanation ---
# Structured output means the AI returns data in a specific format, like JSON, making it easier to parse and use in applications.
# In this code, the prompt instructs Gemini to respond with a character profile in JSON format.
# This allows developers to reliably extract and use each field, improving integration and automation.