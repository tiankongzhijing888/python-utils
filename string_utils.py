# String Utilities - Updated 2026-02-13

def slugify(text: str) -> str:
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text)

def truncate(text: str, length: int = 100, suffix: str = '...') -> str:
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + suffix