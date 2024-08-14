#!/usr/bin/env python3

"""
This module creates a Cache class,
if that was not obvious.
"""
import redis
from typing import Union, Callable, Any
import uuid
from functools import wraps


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

    def get(self, key: str,
            fn: Callable[[bytes], Union[str, int, float, bytes]] =
            None) -> Union[str, int, float, bytes]:
        """Value Getter Method"""
        theData = self._redis.get(key)
        if theData is None:
            return None
        if fn:
            return fn(theData)
        return theData

    def get_str(self, key: str) -> str:
        """String value getter method."""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Int value getter method."""
        return self.get(key, lambda x: int(x))


def count_calls(method: Callable) -> Callable:
    """
    This method counts how many times methods of the
    Cache class are called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Increment the call count."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Store the history of inputs and outputs
    for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputsKey = method.__qualname__ + ":inputs"
        outputsKey = method.__qualname__ + ":outputs"

        self._redis.rpush(inputsKey, str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(outputsKey, str(output))

        return output

    return wrapper
