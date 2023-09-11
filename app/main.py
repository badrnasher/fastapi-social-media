from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
import psycopg2


app = FastAPI()

try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                password='badr', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
