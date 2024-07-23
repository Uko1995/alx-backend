#!/usr/bin/env python3
'''module implements a method in a class'''
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get_page method'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        size = len(data)
        start, end = index_range(page, page_size)
        if (start or end) > size:
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        '''returns a dictionary with the following:
        page_size, page, data, next_page, prev_page and total_pages
        '''
        data = self.get_page(page, page_size)
        num_pages = len(self.dataset()) // page_size
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': page + 1 if page < num_pages else None,
            'prev_page': page - 1 if page > 0 else None,
            'total_pages': num_pages
        }
