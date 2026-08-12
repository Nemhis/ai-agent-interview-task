import json

from .llm import call_llm
from .tools import get_metric, get_norms, today
from .tools.schema import TOOLS

SYSTEM_PROMPT = "You are a health assistant."


def run(question: str) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    while True:
        message = call_llm(messages, TOOLS)
        print(json.dumps(message, ensure_ascii=False, indent=2))

    return ""
