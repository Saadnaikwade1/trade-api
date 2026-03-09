from fastapi import APIRouter, Request, HTTPException
from app.rate_limiter import limiter
from app.services.search_service import search_market_data
from app.services.ai_service import analyze_market
from app.services.report_service import generate_markdown
import logging

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(request: Request, sector: str):

    logging.info(f"Analyzing sector: {sector}")   # ✅ correct place

    if len(sector) < 3:
        raise HTTPException(status_code=400, detail="Invalid sector")

    # Step 1: collect data
    market_data = search_market_data(sector)

    # Step 2: AI analysis
    analysis = analyze_market(sector, market_data)

    # Step 3: generate report
    report = generate_markdown(sector, analysis)

    return {
        "sector": sector,
        "report": report
    }