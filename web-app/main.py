from fastapi import FastAPI
from pydantic import BaseModel
import requests
import psycopg2

app = FastAPI()

class Item(BaseModel):
    questions_num: int

@app.post("/questions/")
async def create_item(item: Item):
    conn = psycopg2.connect(
        host="db",
        database="testdb",
        user="testuser",
        password="testpassword")
    cur = conn.cursor()

    for _ in range(item.questions_num):
        response = requests.get("https://jservice.io/api/random?count=1")
        question = response.json()[0]
        cur.execute("INSERT INTO questions (id, question, answer, created_at) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                    (question['id'], question['question'], question['answer'], question['created_at']))
        conn.commit()

    cur.execute("SELECT * FROM questions ORDER BY created_at DESC LIMIT 1")
    last_question = cur.fetchone()

    cur.close()
    conn.close()

    return last_question
