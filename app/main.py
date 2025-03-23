from fastapi import FastAPI, Request
from pydantic import BaseModel
import logging 
import time
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from prometheus_fastapi_instrumentator import Instrumentator
from app.model  import predict_entities

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

app = FastAPI()

logging.basicConfig(
    filename="logs/api.log", 
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

instrumentator = Instrumentator().instrument(app)
instrumentator.expose(app)

sentry_sdk.init(
    dsn="https://your_sentry_dsn@sentry.io/your_project_id",
    integrations=[FastApiIntegration()],
    traces_sample_rate=1.0,  # 100% sampling for full monitoring
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Logs each API request with response time."""
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    logging.info(
        f"{request.method} {request.url} - {response.status_code} - {duration:.4f}s"
    )
    return response

@app.get("/")
def root():
    logging.info("Root endpoint was accessed.")
    return {"message": "NER API is running"}


class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input_text: TextInput):
    """
    API endpoint for Named Entity Recognition.
    Accepts a text input and returns detected entities.
    """
    response = predict_entities(input_text.text)
    return response
                                        