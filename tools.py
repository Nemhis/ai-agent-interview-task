import datetime

TODAY = datetime.date(2026, 3, 15)

# последние 30 дней, от старых к новым
_DATA = {
    "steps": [
        7204, 9812, 6033, 11240, 8455, 4120, 5390,
        10233, 8901, 7766, 12405, 6688, 3902, 6150,
        9034, 8712, 7455, 10890, 9321, 5044, 6803,
        8421, 9950, 7188, 11002, 8377, 4566, 7290,
        9633, 8104,
    ],
    "sleep_hours": [
        6.5, 7.2, 8.0, 5.9, 7.4, 9.1, 8.3,
        6.8, 7.0, 7.7, 6.2, 8.5, 9.0, 7.9,
        6.4, 7.1, 7.6, 5.5, 6.9, 8.8, 8.2,
        7.3, 6.6, 7.8, 6.1, 7.5, 9.2, 8.4,
        7.0, 6.7,
    ],
    "resting_hr": [
        62, 64, 61, 68, 65, 59, 60,
        63, 66, 64, 70, 62, 58, 61,
        65, 67, 63, 69, 64, 60, 59,
        62, 66, 65, 71, 63, 58, 60,
        64, 62,
    ],
}

_NORMS = {
    "steps": {"min": 7000, "max": None, "unit": "шагов/день"},
    "sleep_hours": {"min": 7.0, "max": 9.0, "unit": "часов/ночь"},
    "resting_hr": {"min": 50, "max": 80, "unit": "уд/мин"},
}


def get_metric(name: str, days: int) -> list[dict]:
    """Значения метрики за последние `days` дней."""
    if name not in _DATA:
        raise ValueError(
            f"unknown metric '{name}'. available: {', '.join(_DATA)}"
        )

    values = _DATA[name][-days:]
    start = TODAY - datetime.timedelta(days=len(values) - 1)
    return [
        {"date": str(start + datetime.timedelta(days=i)), "value": v}
        for i, v in enumerate(values)
    ]


def get_norms(name: str) -> dict:
    """Референсный диапазон для метрики."""
    if name not in _NORMS:
        raise ValueError(
            f"unknown metric '{name}'. available: {', '.join(_NORMS)}"
        )
    return _NORMS[name]


def today() -> str:
    """Сегодняшняя дата в формате YYYY-MM-DD."""
    return str(TODAY)
