import pytest
from utils import validate_email, generate_uuid, truncate_string, chunk_list

def test_validate_email():
    assert validate_email("test@example.com") is True
    assert validate_email("invalid") is False

def test_generate_uuid():
    uid = generate_uuid()
    assert len(uid) == 36
    assert "-" in uid

def test_truncate_string():
    assert truncate_string("hello", 10) == "hello"
    assert truncate_string("hello world", 8) == "hello..."

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]