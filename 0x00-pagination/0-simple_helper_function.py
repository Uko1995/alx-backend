#!/usr/bin/env python3
'''function takes two integers and returns start index and end index'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''index_range function'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
