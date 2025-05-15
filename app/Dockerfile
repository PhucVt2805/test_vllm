FROM python:3.11.9-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml .
COPY requirements.txt .
RUN uv add -r requirements.txt
COPY . .
CMD ["uv", "run", "main.py"]