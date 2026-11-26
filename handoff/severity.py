def severity_rank(value: str) -> int:
    return {'info': 0, 'warning': 1, 'critical': 2}[value]
