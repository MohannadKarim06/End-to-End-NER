FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m spacy download en_core_web_sm

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /app/logs
VOLUME /app/logs

EXPOSE 8000

CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]





