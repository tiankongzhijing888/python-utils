"""
file_hasher.py - Compute and verify file checksums (MD5, SHA1, SHA256).

Usage:
    from file_hasher import FileHasher
    
    hasher = FileHasher('sha256')
    digest = hasher.hash_file('document.pdf')
    hasher.verify_file('document.pdf', digest)  # True
"""

import hashlib
from pathlib import Path
from typing import Optional


class FileHasher:
    """Compute and verify file hashes with streaming support for large files."""
    
    SUPPORTED = ('md5', 'sha1', 'sha256', 'sha512')
    CHUNK_SIZE = 8192
    
    def __init__(self, algorithm: str = 'sha256'):
        if algorithm not in self.SUPPORTED:
            raise ValueError(f"Unsupported algorithm: {algorithm}. Use one of {self.SUPPORTED}")
        self.algorithm = algorithm
    
    def hash_file(self, filepath: str, chunk_size: Optional[int] = None) -> str:
        """Stream-hash a file and return hex digest."""
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        h = hashlib.new(self.algorithm)
        cs = chunk_size or self.CHUNK_SIZE
        
        with open(path, 'rb') as f:
            while True:
                chunk = f.read(cs)
                if not chunk:
                    break
                h.update(chunk)
        
        return h.hexdigest()
    
    def verify_file(self, filepath: str, expected_hash: str) -> bool:
        """Verify a file matches the expected hash."""
        actual = self.hash_file(filepath)
        return actual.lower() == expected_hash.lower()
    
    def hash_string(self, text: str, encoding: str = 'utf-8') -> str:
        """Hash a string value."""
        h = hashlib.new(self.algorithm)
        h.update(text.encode(encoding))
        return h.hexdigest()
    
    @staticmethod
    def generate_checksum_file(directory: str, algorithm: str = 'sha256') -> dict:
        """Generate checksums for all files in a directory."""
        hasher = FileHasher(algorithm)
        results = {}
        for path in Path(directory).rglob('*'):
            if path.is_file():
                results[str(path)] = hasher.hash_file(str(path))
        return results


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python file_hasher.py <file> [algorithm]")
        sys.exit(1)
    
    algo = sys.argv[2] if len(sys.argv) > 2 else 'sha256'
    hasher = FileHasher(algo)
    digest = hasher.hash_file(sys.argv[1])
    print(f"{algo.upper()}: {digest}")