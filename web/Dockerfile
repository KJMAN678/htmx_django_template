FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.9.15 /uv /bin/uv

WORKDIR /app/web
COPY . /app/web

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
        python3-dev \
    && uv sync --frozen --no-dev \
    && rm -rf /var/lib/apt/lists/*
