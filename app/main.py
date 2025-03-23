from fastapi import FastAPI
from pydantic import BaseModel
from app.model  import predict_entities

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

app = FastAPI()

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
                                        