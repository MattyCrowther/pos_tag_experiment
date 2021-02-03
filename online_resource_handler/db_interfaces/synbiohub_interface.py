import os
import rdflib
import requests
import json
from requests.exceptions import HTTPError
from .db_interface import DatabaseInterface
from .sbol_rdflib_identifiers import identifiers

synbiohub_url_base = "https://synbiohub.org/"
predicate_whitelist = [identifiers.predicates.display_id,
                       identifiers.predicates.title,
                       identifiers.predicates.description,
                       identifiers.predicates.role,
                       identifiers.predicates.type,
                       identifiers.predicates.mutable_description,
                       identifiers.predicates.mutable_notes,
                       identifiers.predicates.mutable_provenance
                       ]



class SynBioHubInterface(DatabaseInterface):
    def __init__(self,record_storage =  None):
        DatabaseInterface.__init__(self, record_storage=record_storage)
        if record_storage is None:
            record_storage = "records"
        self.record_storage = os.path.join(record_storage,"synbiohub")
        self.id_codes = ["bba_"]

    def get(self,synbio_id, collection = None):
        expected_fn = os.path.join(self.record_storage,synbio_id + ".xml")
        if not os.path.isfile(expected_fn):
            if collection == None:
                collections = self.get_root_collections()
            else:
                collections = [collection]
            for collection in collections:
                collection = "public/" + collection
                synbiohub_url = synbiohub_url_base + collection + "/" + synbio_id + "/1/sbol"
                r = requests.get(synbiohub_url)
                # If the response was successful, no Exception will be raised
                r.raise_for_status()
                # Another quirk of the SBOL synbio stack, sends a 200 return code even if the record has not been found.
                if "Error: https://synbiohub.org/public" in r.text :
                    continue
                else:
                    break

            if "Error: https://synbiohub.org/public" in r.text :
                raise ValueError(f"{synbio_id} Not Found.")

            self._store_record(expected_fn,r.text)

        return self._load_graph(expected_fn)

    def query(self,query_string = None, query_pairs = None, collection = None, search_limit = 5):
        synbiohub_url = synbiohub_url_base + "search/"

        if isinstance(query_pairs,dict):
            for index,k in enumerate(list(query_pairs.keys())):
                synbiohub_url = f'{synbiohub_url}{k}={query_pairs[k]}'
                if index != len(list(query_pairs.keys())) - 1:
                    synbiohub_url = synbiohub_url + "&"
            if query_string is not None:
                synbiohub_url = synbiohub_url + "&"

        if query_string is not None:
            synbiohub_url = f'{synbiohub_url}{query_string}'
        synbiohub_url = synbiohub_url +  "/?limit=" + str(search_limit)
        r = requests.get(synbiohub_url,headers={'Accept': 'text/plain'})

        r.raise_for_status()    
        return json.loads(r.text)

    def count(self,query_string = None, query_pairs = None, collection = None):
        synbiohub_url = synbiohub_url_base + "searchCount/"
        if isinstance(query_pairs,dict):
            for index,k in enumerate(list(query_pairs.keys())):
                synbiohub_url = f'{synbiohub_url}{k}={query_pairs[k]}'
                if index != len(list(query_pairs.keys())) - 1:
                    synbiohub_url = synbiohub_url + "&"
            if query_string is not None:
                synbiohub_url = synbiohub_url + "&"
        if query_string is not None:
            synbiohub_url = f'{synbiohub_url}{query_string}'
        r = requests.get(synbiohub_url,headers={'Accept': 'text/plain'})
        r.raise_for_status()    
        return json.loads(r.text)


    def related(self,synbio_id,collection = None):
        pass

    def generalise_query_results(self,query_results):
        generalised_results = []

        for result in query_results:
            generalised_results.append(result["name"])
        return generalised_results

    def generalise_get_results(self,graph):
        for s,p,o in graph:
            if p not in predicate_whitelist:
                graph.remove((None,p,None))    
        return graph
        
    def get_root_collections(self):
        response = requests.get(
        'https://synbiohub.org/rootCollections',
        params={'X-authorization': 'token'},
        headers={'Accept': 'text/plain'},)

        roots = json.loads(response.text)
        roots = [k['uri'].split("/")[4] for k in roots]
        return roots



