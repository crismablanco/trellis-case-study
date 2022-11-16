def str2bool(value: str or bool) -> bool:
    if not value:
        return False
    if isinstance(value, bool):
        return value

    return value.lower() in ("yes", "true", "t", "1")
