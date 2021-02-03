import os
import rdflib
import requests
import json
from requests.exceptions import HTTPError
from abc import ABCMeta, abstractmethod


class DatabaseInterface:
    __metaclass__ = ABCMeta
    def __init__(self,record_storage =  None):
        if record_storage is None:
            record_storage = "records"
        self.record_storage = os.path.join(record_storage,"synbiohub")
        self.id_codes = []
        
    @abstractmethod
    def get(self,id):
        pass

    @abstractmethod
    def query(self,query_string):
        pass

    @abstractmethod
    def count(self,query_string):
        pass

    @abstractmethod
    def related(self,id):
        pass

    @abstractmethod
    def generalise_get_results(self,result):
        pass

    @abstractmethod
    def generalise_query_results(self,result):
        pass
    
    def _load_graph(self,fn):
        record_graph = rdflib.Graph()
        record_graph.load(fn)
        return record_graph
        
    def _store_record(self,target,record):
        try:
            os.makedirs(self.record_storage)
        except FileExistsError:
            pass
        
        if os.path.isfile(target):
            return target

        f = open(target,"a")
        f.write(record)
        f.close()
        return target



