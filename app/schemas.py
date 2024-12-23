from pydantic import BaseModel

class MovieSchema(BaseModel):
    title: str
    rating: float
    director: str
    category: str
    duration: int
    description: str
    release_year: int
