#!/usr/bin/env python3
'''module that creates LRUCache class from BaseCaching'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    basic caching class
    '''
    def __init__(self):
        '''
        constructor method
        '''
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        '''
        assigns item value to key in self.cache_data
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.used_keys:
                self.used_keys.remove(key)
            self.used_keys.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            least = self.used_keys.pop(0)
            del self.cache_data[least]
            print(f"DISCARD: {least}")

    def get(self, key):
        '''
        returns the value in self.cache_data linked to key
        '''
        if key is not None and key in self.cache_data.keys():
            if key in self.used_keys:
                self.used_keys.remove(key)
            self.used_keys.append(key)
            return self.cache_data.get(key, None)
