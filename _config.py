"""Конфигурация доступа к модели. Значения читаются из окружения."""

import os

from dotenv import load_dotenv

load_dotenv()

API_URL = os.environ.get(
    "LLM_API_URL", "https://openrouter.ai/api/v1/chat/completions"
)
API_KEY = os.environ.get("LLM_API_KEY")
MODEL = os.environ.get("LLM_MODEL", "openai/gpt-4o-mini")

if not API_KEY:
    raise RuntimeError(
        "LLM_API_KEY не задан. Скопируйте .env.example в .env "
        "и впишите ключ, либо экспортируйте переменную окружения."
    )
