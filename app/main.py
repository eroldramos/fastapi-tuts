from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind=engine)



app = FastAPI()
origins=[
    '*'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello-World !!!!!!!!!!!!!"}

















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


# select title, content, email from posts LEFT JOIN users ON posts.user_id = users.id;
# select title, content, email, posts.id, users.id from posts LEFT JOIN users ON posts.user_id = users.id;

# select posts.* email from posts LEFT JOIN users ON posts.user_id = users.id;

# select users.id, COUNT(*) from posts LEFT JOIN users ON posts.user_id = users.id GROUP BY users.id;

# select users.id, COUNT(*) from posts RIGHT JOIN users ON posts.user_id = users.id GROUP BY users.id;


# select users.id, COUNT(posts.id) from posts RIGHT JOIN users ON posts.user_id = users.id GROUP BY users.id;

# select users.id, users.email, COUNT(posts.id) as user_post_count from posts RIGHT JOIN users ON posts.user_id = users.id GROUP BY users.id;

# select * from posts LEFT JOIN votes ON posts.id = votes.post_id

# select posts.*, count(votes.post_id)as votes from posts LEFT JOIN votes ON posts.id = votes.post_id group by posts.id


