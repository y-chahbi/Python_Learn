
import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyCG64hH7wkecx8EqQHM5a03WY7jCKGmods"

# Configure the genai client
genai.configure(api_key=API_KEY)

# Example request using the genai generate_text method
response = genai.generate_text(
    model="text-bison-001",  # Choose a model, e.g., text-bison-001, gemini-1.5, etc.
    prompt="Explain how artificial intelligence works.",
    temperature=0.7,         # Adjust creativity level (0.0 for deterministic, 1.0 for high randomness)
    max_output_tokens=200,   # Limit output length
)

# Print the generated response
print(response.result)
