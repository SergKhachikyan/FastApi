from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

books = [
    {
        "id":1,
        "title":"Async in Python",
        "author":"Matthew",
    },
    {
        "id":2,
        "title":"Backend in Python",
        "author":"John"
    }
]

class BookSchema(BaseModel):
    
    title:str
    author:str
    
@app.get("/books",
        tags=["Books"],
        summary="Get book list",
        description="<h1>Gives all book lists</h1>",
)
def get_books():
    return books

@app.post("/books",tags=["Books"])
def add_book(book:BookSchema):
    new_book_id = len(books) + 1
    books.append({
        "id":new_book_id,
        "title":book.title,
        "author":book.author,
    })
    return {"success":True,"message":"Book was added"}

if __name__ == "__main__":
    uvicorn.run("books:app")