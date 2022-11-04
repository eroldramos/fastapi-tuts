import enum
from typing import Optional
from fastapi import FastAPI, requests, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
app = FastAPI()
# scram-sha-256

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(
            host='localhost', 
            database='fastapi', 
            user='postgres', 
            password='admin', 
            cursor_factory=RealDictCursor
            )
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as e:
        print("Connecting to database failed!")
        print('Error was', e)
        time.sleep(2)

        
my_posts = [{
    "title": "title of post 1",
    "content" : "content of post 1",
    "id" : 1
},
{
    "title": "title of post 2",
    "content" : "content of post 2",
    "id" : 2
}
]


# business logics

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i

@app.get("/")
def root():

    return {"message": "dsds"}

@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""
        INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *
    """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data" : new_post}

# @app.get('/posts/latest')
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

@app.get('/posts/{id}')
def get_post(id: int, response:Response):
    cursor.execute("""
        SELECT * FROM posts WHERE id = %s 
    """,(str(id),))
    post = cursor.fetchone()
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message':f'post with id: {id} was not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} was not found')
    return {"post_detail": post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    cursor.execute("""
        DELETE FROM posts WHERE id = %s returning *
    """, (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists!")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id:int, post:Post):
    cursor.execute("""
        UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *
    """, (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exists!")
 
    return {
        'data' : updated_post
    }
    
# SELECT * FROM products WHERE name LIKE '%BLU%' ;
# SELECT * FROM products ORDER BY price ASC;
# SELECT * FROM products ORDER BY price DESC;
# SELECT * FROM products ORDER BY inventory DESC, price;
# SELECT * FROM products ORDER BY  created_at DESC;
# SELECT * FROM products WHERE price ORDER BY  created_at DESC;
# SELECT * FROM products WHERE price > 10 LIMIT 2;
# SELECT * FROM products ORDER BY id  LIMIT 10 OFFSET 1;

# INSERT INTO products (price, name, inventory) VALUES (24, 'burger', 300);
# INSERT INTO products (price, name, inventory) VALUES (24, 'burger', 300) returning *;
# DELETE FROM products  WHERE id = 10;
# DELETE FROM products  WHERE id = 11 RETURNING *;
# DELETE FROM products  WHERE inventory = 0 RETURNING *;
# UPDATE products SET name = 'flourtortilla', price = 40 WHERE id = 50 ;
# UPDATE products SET name = 'flourtortilla', price = 40 WHERE id > 4 RETURNING * ; 
