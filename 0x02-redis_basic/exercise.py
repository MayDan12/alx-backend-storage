#!/usr/bin/env python3
import redis
import uuid
from typing import Union

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
