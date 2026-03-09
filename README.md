# Trade Opportunities API

**Trade Opportunities API** is a FastAPI-based backend service that analyzes market data for Indian sectors and generates trade opportunity insights. It integrates web search, AI analysis using **Google Gemini**, and returns a structured markdown report.

---

## ✅ Features

- FastAPI backend with clean architecture
- Single endpoint `/analyze/{sector}` for sector analysis
- Market data collection via DuckDuckGo search
- AI-powered analysis using Google Gemini (`gemini-1.5-flash`)
- Markdown report generation
- Rate limiting (5 requests/minute)
- Logging for debugging
- Swagger API documentation

---

## 🏗️ Project Structure


trade_api/
│
├── app/
│ ├── main.py # FastAPI app entry point
│ ├── routes.py # API endpoints
│ ├── rate_limiter.py # SlowAPI rate limiter
│ └── services/
│ ├── search_service.py # Market data collection
│ ├── ai_service.py # Gemini AI analysis
│ └── report_service.py # Markdown report generation
│
├── .env # Environment variables (Gemini API key)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚡ Prerequisites

- Python 3.10+
- Virtual environment (`venv` recommended)
- Gemini AI API key ([Google AI Studio](https://aistudio.google.com/app/apikey))

---

## 💻 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd trade_api

Create virtual environment:

python -m venv venv

Activate virtual environment:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create .env file in the root:

GEMINI_API_KEY=your_gemini_api_key_here
🚀 Running the API

Start the FastAPI server:

uvicorn app.main:app --reload

Open Swagger documentation:

http://127.0.0.1:8000/docs
📦 API Endpoint
GET /analyze/{sector}

Analyze a sector in India and return a market analysis report.

Request:

GET /analyze/pharmaceuticals
Headers:
  x-token: <optional if authentication implemented>
```
##### Response Example:

{
  "sector": "pharmaceuticals",
  "report": "# Market Analysis Report\n\n## Sector\nPharmaceuticals\n\n## Analysis\nThe Indian pharmaceuticals sector is a global powerhouse..."
}



sector: The name of the sector analyzed

report: AI-generated markdown analysis including:

Market Trends

Trade Opportunities

Risks

Future Outlook

---

#### 🔒 Security & Rate Limiting

Rate limiting: 5 requests per minute per user

Optional authentication: JWT or token-based authentication can be added

Input validation: Ensures valid sector names

#### 🛠️ Logging

- Logging is implemented using Python logging module

- Logs API calls and errors

- Example log:

  - INFO:root:Analyzing sector: pharmaceuticals
#### ⚙️ How it Works

- User sends GET request with a sector name

- API collects current market data from web search (DuckDuckGo)

- Collected data is sent to Google Gemini AI (gemini-2.5-flash) for analysis

- AI generates structured markdown analysis

- API returns report in JSON response