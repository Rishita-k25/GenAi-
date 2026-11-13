
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Send prompt to AI
# Send prompt to AI
print("Connecting to Gemini...")

try:
    response = client.models.generate_content(
       model="gemini-3.5-flash-lite",
       contents="Explain Machine Learning with a real-life example."
    )

    print("\nLLM Response:")
    print(response.text)

except Exception as e:
    print("\nError:", e)
# Display response

