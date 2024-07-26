#!/usr/bin/env python3
'''module that creates BasicCache class from BaseCaching'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    basic caching class
    '''
    def __init__(self):
        '''
        constructor method
        '''
        super().__init__()

    def put(self, key, item):
        '''
        assigns item value to key in self.cache_data
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        returns the value in self.cache_data linked to key
        '''
        if key is not None:
            return self.cache_data.get(key, None)
