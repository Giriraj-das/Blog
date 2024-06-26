from fastapi import FastAPI

from routers import posts, categories, tags, authors

app = FastAPI(
    title='Blog',
    description='This is the blog documentation',
    version='0.0.001'
)

app.include_router(posts.router)
app.include_router(categories.router)
app.include_router(tags.router)
app.include_router(authors.router)
