#!/usr/bin/env python3
"""dfv f f"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Cordr.
    Args: fce
    Returns: df
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wracf
        Args:
            self: Thfc
            *args: Thcf
            **kwargs: Tf
        Returns: rf
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Cfc
    Args: rf
    Returns: fcfr
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wfcf
        Args:
            self: Tfce
            *args: Then
            **kwargs: Then
        Returns:
            Tion
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """
    Rection
    Args:
        method: Thrc
    Returns:
        N
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """Decr fc r"""
    def __init__(self) -> None:
        """
        Inv
        Attributes:
            self._redis (redis.Redis): r
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        St
        Args:
            data (dict): d
        Returns:
            str: k
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float, None]:
        """S dv vf"""
        data = self._redis.get(key)
        if data is not None and fn is not None and callable(fn):
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Ge
        Args:
            key (str): k
        Returns:
            str: d
        """
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data

    def get_int(self, key: str) -> int:
        """
        Gache
        Args:
            key (str): k
        Returns:
            int: d
        """
        data = self
