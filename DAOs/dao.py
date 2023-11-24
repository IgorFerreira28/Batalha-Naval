import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        with open(self.__datasource, 'wb') as file:
            pickle.dump(self.__cache, file)

    def __load(self):
        with open(self.__datasource, 'rb') as file:
            data = pickle.load(file)
            self.__cache = data

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def update(self, key, obj):        
        if(self.__cache[key] != None):
            self.__cache[key] = obj
            self.__dump()

    def get(self, key):
        return self.__cache[key]

    def remove(self, key):        
        self.__cache.pop(key)
        self.__dump()

    def get_all(self):
        return self.__cache.values()
