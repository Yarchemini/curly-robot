def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список словарей с операциями, у которых ключ state равен переданному значению."""
    return [operation for operation in operations if operation.get("state") == state]
