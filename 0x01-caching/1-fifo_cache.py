#!/usr/bin/env python3
'''module that creates FIFOCache class from BaseCaching'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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
                first_item = next(iter(self.cache_data))
                del self.cache_data[first_item]
                print(f"DISCARD: {first_item}")

    def get(self, key):
        '''
        returns the value in self.cache_data linked to key
        '''
        if key is not None:
            return self.cache_data.get(key, None)
