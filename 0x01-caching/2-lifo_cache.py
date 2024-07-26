#!/usr/bin/env python3
'''module that creates LIFOCache class from BaseCaching'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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

        if len(self.cache_data) > self.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-2]
            del self.cache_data[last_item]
            print(f"DISCARD: {last_item}")

    def get(self, key):
        '''
        returns the value in self.cache_data linked to key
        '''
        if key is not None:
            return self.cache_data.get(key, None)
