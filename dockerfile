FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
COPY src/ ./src

RUN pip install --upgrade pip \
    && pip install uv

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "--host", "0.0.0.0", "src/main.py"]
