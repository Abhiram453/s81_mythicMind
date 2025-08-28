import google.generativeai as genai

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyBHA0ZZQu1Zy5u7xE1lAQW7-XYj-k1-asY")

def generate_character_prompt(genre, traits=None, quirks=None):
    # Dynamic prompting: build the prompt based on user input
    prompt = f"You are a character generator for a creative writing app. Generate a detailed character profile for the following genre: {genre}.\n\n"
    prompt += "Include:\n- Name\n- Personality traits\n- Backstory\n- Motivations\n- Unique quirks\n"
    if traits:
        prompt += f"\nFocus on these traits: {', '.join(traits)}.\n"
    if quirks:
        prompt += f"\nAdd these quirks: {', '.join(quirks)}.\n"
    prompt += "\nRespond with a complete character profile."
    return prompt

# Example usage: user selects genre and custom traits/quirks
genre = "sci-fi"
traits = ["curious", "resourceful"]
quirks = ["always hums a tune", "collects alien artifacts"]

prompt = generate_character_prompt(genre, traits, quirks)

model = genai.GenerativeModel("gemini-1.5-pro-latest")
response = model.generate_content(prompt)
print(response.text)

# --- Video Explanation ---
# Dynamic prompting means building AI prompts on-the-fly based on user choices or context.
# In this code, the prompt is constructed using the genre, traits, and quirks chosen by the user.
# This lets the AI generate more personalized and relevant character profiles, adapting to each user's needs.
# The code demonstrates dynamic prompting by assembling the prompt dynamically before sending it to Gemini.