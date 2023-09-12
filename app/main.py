from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor
import psycopg2
import time


class Post(BaseModel):
        title: str
        content: str

app = FastAPI()
while True:
        try:
                conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
                                        password='badr', cursor_factory=RealDictCursor)
                cursor = conn.cursor()
                print("Database connection was succesfull!")
                break
        except Exception as error:
                print("Connecting to database failed")
                print("Error: ", error)
                time.sleep(3)

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    return posts


@app.get("/posts/{post_id}")
def get_post(post_id: int):
        cursor.execute("SELECT * FROM posts WHERE id=%s", (post_id,))
        post = cursor.fetchone()
        if post:
                return post
        else:
                raise HTTPException(status_code=404, detail="Post not found")
        

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
        cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (post.title, post.content))
        conn.commit()
        return {"message": "Post created successfully"}

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: Post):
        cursor.execute("UPDATE posts SET title=%s, content=%s WHERE id=%s", (post.title, post.content, post_id))
        conn.commit()
        return {"message": "Post updated successfully"}


