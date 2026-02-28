"""Path utilities - path join, normalize, relative. Daily task 2026-03-01."""
import os
from pathlib import Path

def safe_join(base: str, *parts: str) -> str:
    """Join path parts, normalize and resolve relative to base."""
    return str(Path(base).joinpath(*parts).resolve())