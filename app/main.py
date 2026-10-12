
"""FastAPI application for the Week 4 Compose lab."""

import os

import psycopg
from fastapi import FastAPI, HTTPException

APP_NAME = os.getenv("APP_NAME", "sdp-starter")
APP_VERSION = "0.1.0"
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI(title=APP_NAME, version=APP_VERSION)

ITEMS = [
    {"id": 1, "name": "Write a Dockerfile", "done": False},
    {"id": 2, "name": "Run it with Compose", "done": False},
    {"id": 3, "name": "Deploy it to Render", "done": False},
]


@app.get("/")
def root():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "message": "Hello from the starter app",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/health/db")
def health_db():
    if not DATABASE_URL:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured",
        )

    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=5) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM notes")
                count = cur.fetchone()[0]

        return {"db": "ok", "notes": count}

    except psycopg.Error:
        raise HTTPException(
            status_code=503,
            detail="Database connection or query failed",
        )


@app.get("/items")
def list_items():
    return ITEMS


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in ITEMS:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
