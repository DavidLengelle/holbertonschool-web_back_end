#!/usr/bin/env python3
"""Module defining an asynchronous generator of random numbers"""


import asyncio
import random

from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine yielding ten random floats between 0 and 10 every second"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
