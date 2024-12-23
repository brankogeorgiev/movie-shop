from fastapi import FastAPI, Depends, HTTPException
import time
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from app.db import SessionLocal, engine
from app.models import Base
from app import schemas, crud

app = FastAPI()

for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/movies/", response_model=schemas.MovieSchema)
def create_movie(movie: schemas.MovieSchema, db: Session = Depends(get_db)):
    return crud.create_movie(db=db, schema=movie)


@app.get("/movies/{movie_id}", response_model=schemas.MovieSchema)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_item = crud.read_movie(db=db, movie_id=movie_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Movie not found!")
    return db_item


@app.put("/movies/{movie_id}", response_model=schemas.MovieSchema)
def update_movie(movie_id: int, movie: schemas.MovieSchema, db: Session = Depends(get_db)):
    db_item = crud.update_movie(db=db, movie_id=movie_id, schema=movie)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Movie not found!")
    return db_item


@app.delete("/movies/{movie_id}", response_model=schemas.MovieSchema)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_movie(db=db, movie_id=movie_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Movie not found!")
    return db_item


@app.get("/movies/", response_model=list[schemas.MovieSchema])
def list_all_movies(db: Session = Depends(get_db)):
    return crud.list_all_movies(db=db)
