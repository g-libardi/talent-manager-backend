FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY . .

RUN uv sync

EXPOSE 8000

run uv run manage.py migrate
run uv run manage.py loaddata fixtures/start.json

CMD ["uv", "run", "gunicorn", "talent_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
