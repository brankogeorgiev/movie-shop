FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi || cat /app/poetry.lock

COPY ./app /app/app

EXPOSE 80