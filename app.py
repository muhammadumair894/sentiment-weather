import os
import nest_asyncio
import uvicorn
from pyngrok import ngrok
from fastapi import FastAPI, File, UploadFile, Form
import requests
from transformers import pipeline

classifier = pipeline('sentiment-analysis')


app = FastAPI()

@app.get("/")
def home():
    return "Welcome to Our FastAPI Endpoints  bla bla bla "

@app.get("/1")
def home():
    return "We are learning FastAPI "

@app.get("/sentiment/{text}")
def sentiment(text):
    return str(classifier([text])[0]['label'])

@app.get("/weather/{text}")
def weather(text):
  url = "https://weather-api167.p.rapidapi.com/api/weather/overview"

  querystring = {"place":text}

  headers = {
    "x-rapidapi-key": "5cf8fcaf61msh613f010a34f3576p1953e5jsn110a1e6c667d",
    "x-rapidapi-host": "weather-api167.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)

  #print(response.json())

  return response.json()
