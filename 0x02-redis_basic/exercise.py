#!/usr/bin/env python3

"""
This module creates a Cache class,
if that was not obvious.
"""
import redis
from typing import Union
import uuid


class Cache:
    """The Cache class."""

    def __init__(self):
        """Initialize."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method creates a random key and stores
        the input data in Redis.
        """
        theRandomKeyGeneratedKey = str(uuid.uuid4())
        self._redis.set(theRandomKeyGeneratedKey, data)
        return theRandomKeyGeneratedKey
