FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requrements.txt

COPY . .

CMD [ "python", "ai_model.py"]

