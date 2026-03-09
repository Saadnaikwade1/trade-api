from fastapi import FastAPI
from app.routes import router
from app.rate_limiter import limiter
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Trade Opportunities API",
    description="Market analysis API for Indian sectors",
    version="1.0",
    contact={
        "name": "Saad Naikwade",
        "email": "naikwadesaad@gmail.com"
    }
)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logging.info("Trade Opportunities API started successfully")

@app.get("/")
def home():
    return {"message": "Trade Opportunities API Running"}