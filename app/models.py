from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    ...

class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    rating: Mapped[float]
    director: Mapped[str]
    category: Mapped[str]
    duration: Mapped[int]
    description: Mapped[str]
    release_year: Mapped[int]
