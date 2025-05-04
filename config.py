import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    REDIS_URL = os.environ.get("REDIS_URL") or "redis://localhost:6379/0"
