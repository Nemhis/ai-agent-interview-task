import requests

from .config import API_KEY, API_URL, MODEL


def call_llm(messages: list[dict], tools: list[dict]) -> dict:
    """Один вызов модели. Возвращает assistant-сообщение целиком."""
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": MODEL,
            "messages": messages,
            "tools": tools,
            "temperature": 0,
            # фиксируем провайдера: иначе один и тот же model-id
            # может уехать к разным бэкендам с разным поведением
            "provider": {"order": ["openai"], "allow_fallbacks": False},
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]
