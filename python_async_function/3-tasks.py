#!/usr/bin/env python3
"""Function that wraps wait_random in an asyncio Task"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an asyncio Task running wait_random"""

    return asyncio.create_task(wait_random(max_delay))
