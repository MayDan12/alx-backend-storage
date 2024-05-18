#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable, Optional

"""
    a cache class
"""


class Cache:

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None) -> Optional[Union[str,bytes,int,float]]:
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data
    
    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda d: d.decode('utf-8'))
    
    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, lambda d: int(d))
