# import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# print(os.getenv("GOOGLE_API_KEY")is not None)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="tell me something about goa"
)

print(response.text)