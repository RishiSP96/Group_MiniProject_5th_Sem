# ai_module.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ====== Get API key from environment variable ======
# Set your API key as an environment variable: export GEMINI_API_KEY="your-key-here"
# Or create a .env file with: GEMINI_API_KEY=your-key-here
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini with your API key
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    print("Warning: GEMINI_API_KEY environment variable not set. AI features will not work.")

def ask_gemini(question, context=""):
    """
    Ask Gemini AI for market insights.
    :param question: User question string
    :param context: Optional chart/signal context
    :return: AI response text
    """
    if not API_KEY:
        raise ValueError("Missing API_KEY in ai_module.py. Please set your Gemini API key.")

    # Initialize the Gemini model (you can change to 'gemini-1.5-pro' or 'gemini-1.5-flash')
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Construct the full prompt
    prompt = f"""
    You are a professional AI analyst specialized in real-time technical analysis and crypto market insights.

    Context: {context}

    Question: {question}
    """

    # Generate the response
    response = model.generate_content(prompt)

    # Return the text output
    return response.text
