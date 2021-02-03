import os
import shutil
import atexit

from rdflib import Graph
from .synbiohub_interface import SynBioHubInterface
from .genbank_interface import GenBankInterface
from urllib.error import HTTPError
import time

record_storage = os.path.join(os.path.dirname(__file__),"records")
class DatabaseUtility:
    def __init__(self):
        self.db_mapping_calls = {"synbiohub" : SynBioHubInterface(record_storage),
                                 "genbank"   : GenBankInterface(record_storage)}
        atexit.register(self._remove_records)

    def _remove_records(self):
        print("WARN:: Stopped deleting records on db util for testing.")
        return None
        if os.path.isdir(record_storage):
            shutil.rmtree(record_storage) 

    def get(self, id, db_name = None):
        try:
            record = self.db_mapping_calls[db_name].get(id)
            record = self.db_mapping_calls[db_name].generalise_get_results(record)
            return record
        except (HTTPError,ValueError,KeyError):
            return None

    def query(self,queries,db_name=None,search_limit = 100):
        if not isinstance(queries,(list,set,tuple)):
            queries = [queries]
        
        results = []
        for query in queries:
            returned = False
            attempts = 0
            while not returned and attempts < 5:
                try:
                    results = (results + 
                        self.db_mapping_calls[db_name].query(query,search_limit=search_limit))
                    returned = True
                except HTTPError:
                    print(f'WARN:: Err querying with {query} for db: {db_name}. Attempt: {attempts}')
                    attempts = attempts + 1
                    time.sleep(5)
        results = self.db_mapping_calls[db_name].generalise_query_results(results)
        return results

    def count(self,queries,db_name):
        if not isinstance(queries,(list,set,tuple)):
            queries = [queries]
        count = 0
        for query in queries:
            count = count + self.db_mapping_calls[db_name].count(query)
        return count
         
    def related(self,id,db_name = None):
        results = self.db_mapping_calls[db_name].related(id)
        return results

    def get_potential_db_names(self,identity):
        potential_dbs = []
        for name,db in self.db_mapping_calls.items():
            id_codes = db.id_codes
            if any(code.lower() in identity.lower() for code in id_codes):
                potential_dbs.append(name)
        return potential_dbs



        




