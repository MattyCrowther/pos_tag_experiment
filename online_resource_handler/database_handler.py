from .db_interfaces.db_util import DatabaseUtility
from concurrent.futures import ThreadPoolExecutor as PoolExecutor,as_completed

class DatabaseHandler:
    def __init__(self,offline=False):
        self.is_offline = offline
        if not offline:
            self._db_util = DatabaseUtility()

        for k,v in self._db_util.db_mapping_calls.items():
            setattr(DatabaseHandler, k, k)
    
    def get(self,identity,db_name):
        if self.is_offline : return None
        record = self._db_util.get(identity,db_name)
        return record

    def query(self,query,db_name):
        if self.is_offline : return []
        records = self._db_util.query(query,db_name=db_name)
        return records
    
    def get_db_names(self):
        if self.is_offline : return False
        return self._db_util.db_mapping_calls.keys()

    def get_potential_db_names(self,identity):
        if self.is_offline : return []
        potential_codes = self._db_util.get_potential_db_names(identity)
        if len(potential_codes) == 0:
            return self.get_db_names()
        return potential_codes
        
    def get_record(self,identity):
        if self.is_offline : return False
        for db in  self.get_potential_db_names(identity):
            record = self.get(identity,db)
            if record is not None:
                return record
        return None
            
    def get_record_from_descriptors(self,actual_descriptors):
        if self.is_offline : return False

        def query_inner(desc,db_name):
            return (self.query(desc,db_name),db_name)

        def get_inner(identity,db_name):
            return self.get(identity,db_name)
        records = []
        # Two threading operations, one for queries to different dbs then another on the get.
        with PoolExecutor(max_workers=4) as query_executor:
            query_results = [query_executor.submit(query_inner,actual_descriptors,db) for db in self.get_db_names()]
            for q_results in as_completed(query_results):
                q_results,db = q_results.result()
                with PoolExecutor(max_workers=4) as get_executor:
                    get_results = [get_executor.submit(get_inner,q_result,db) for q_result in q_results]
                    for get_result in as_completed(get_results):
                        records.append(get_result.result())
        return records


    def count_by_descriptors(self,actual_descriptors,expected_descriptors):
        actual_descriptor_str = " ".join(actual_descriptors)
        for descriptor in expected_descriptors:
            query_str = actual_descriptor_str + " " + descriptor
            for db in self.get_db_names():
                count = self._db_util.count(query_str,db)
                yield count

        
