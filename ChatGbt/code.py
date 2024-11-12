import google.generativeai as genai

API_KEY = "AIzaSyCG64hH7wkecx8EqQHM5a03WY7jCKGmods"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)