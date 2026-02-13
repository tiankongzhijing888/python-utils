# Date Utilities - Added 2026-02-14
from datetime import datetime, timedelta
from typing import Optional

def days_between(start: str, end: str, fmt: str = '%Y-%m-%d') -> int:
    d1 = datetime.strptime(start, fmt)
    d2 = datetime.strptime(end, fmt)
    return abs((d2 - d1).days)

def add_business_days(start_date: datetime, days: int) -> datetime:
    current = start_date
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current

def format_relative(dt: datetime) -> str:
    diff = datetime.now() - dt
    if diff.days > 365:
        return f'{diff.days // 365}y ago'
    elif diff.days > 30:
        return f'{diff.days // 30}mo ago'
    elif diff.days > 0:
        return f'{diff.days}d ago'
    elif diff.seconds > 3600:
        return f'{diff.seconds // 3600}h ago'
    else:
        return f'{diff.seconds // 60}m ago'