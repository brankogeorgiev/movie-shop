from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def create_movie(db: Session, schema: schemas.MovieSchema):
    movie = models.Movie(**schema.dict())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def read_movie(db: Session, movie_id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found!")
    return movie

def update_movie(db: Session, movie_id: int, schema: schemas.MovieSchema):
    movie = read_movie(db, movie_id)

    if movie:
        for key, value in schema.dict().items():
            setattr(movie, key, value)

        db.commit()
        db.refresh(movie)
    return movie


def delete_movie(db: Session, movie_id: int):
    movie = read_movie(db, movie_id)

    db.delete(movie)
    db.commit()

    return movie

def list_all_movies(db: Session):
    return db.query(models.Movie).all()