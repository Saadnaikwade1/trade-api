import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_market(sector, market_data):

    prompt = f"""
    Analyze the {sector} sector in India.

    Market information:
    {market_data}

    Provide analysis in sections:

    1. Market Trends
    2. Trade Opportunities
    3. Risks
    4. Future Outlook
    """

    response = model.generate_content(prompt)

    return response.text