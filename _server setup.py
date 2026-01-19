import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException, UploadFile

load_dotenv() # This loads the variables from the .env file

app = FastAPI()
EXPECTED_TOKEN = os.getenv("NVDA_SYNC_TOKEN")
