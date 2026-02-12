"""
Python Utils - A collection of utility functions
"""
import re
import hashlib
import uuid
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any


def validate_email(email: str) -> bool:
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def generate_uuid() -> str:
    """Generate a unique UUID4 string."""
    return str(uuid.uuid4())


def hash_password(password: str, salt: str = "default") -> str:
    """Hash password with SHA-256."""
    return hashlib.sha256(f"{password}{salt}".encode()).hexdigest()


def truncate_string(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate string to max length with suffix."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def parse_date(date_str: str, fmt: str = "%Y-%m-%d") -> Optional[datetime]:
    """Safely parse date string."""
    try:
        return datetime.strptime(date_str, fmt)
    except ValueError:
        return None


def flatten_list(nested: List[List[Any]]) -> List[Any]:
    """Flatten a nested list."""
    return [item for sublist in nested for item in sublist]


def chunk_list(lst: List[Any], size: int) -> List[List[Any]]:
    """Split list into chunks of given size."""
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def dict_deep_merge(base: Dict, override: Dict) -> Dict:
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = dict_deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator for retrying failed function calls."""
    import time
    import functools

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(delay * (attempt + 1))
            raise last_exception
        return wrapper
    return decorator