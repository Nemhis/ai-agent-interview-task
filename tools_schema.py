TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_metric",
            "description": "Returns metric data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": ""},
                    "days": {"type": "string", "description": "period"},
                },
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_norms",
            "description": "Returns norms.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "today",
            "description": "Date.",
            "parameters": {"type": "object", "properties": {}},
        },
    },
]
