#!/usr/bin/env python3
'''module that creates MRUCache class from BaseCaching'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    basic caching class
    '''
    def __init__(self):
        '''
        constructor method
        '''
        super().__init__()
        self.used_keys = []

