from pydantic import BaseModel, Field

class Book:
    id: int
    title: str
    author: str
    ranking: float
    
    def __init__(self, id, title, author, ranking) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.ranking = ranking

class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=10)
    ranking: float = Field(gt=0)