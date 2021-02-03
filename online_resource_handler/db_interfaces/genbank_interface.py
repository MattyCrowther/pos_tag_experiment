import os
import rdflib
from .db_interface import DatabaseInterface
from Bio import Entrez
from Bio import GenBank

Entrez.email = "m.crowther1@ncl.ac.uk"
target_dbs = ['protein','nuccore']
predicate_blacklist = ["sequence","locus","date","contig","dblinks"]
object_blacklist = [[],"",None,{},()]
qualifier_object_whitelist = ["/product=","/type_material=","/mol_type=","/organism="]

class GenBankInterface(DatabaseInterface):
    def __init__(self,record_storage =  None):
        DatabaseInterface.__init__(self, record_storage=record_storage)
        if record_storage is None:
            record_storage = "records"
        self.record_storage = os.path.join(record_storage,"genbank")
        self.id_codes = [".-"]
        
    def get(self,id, sub_database_name = "nucleotide"):
        expected_fn = os.path.join(self.record_storage,str(id) + ".gbk")
        if not os.path.isfile(expected_fn):
            if _is_valid_db_name(sub_database_name):
                net_handle = Entrez.efetch(
                    db=sub_database_name, id=id, rettype="gb", retmode="text"
                )
                self._store_record(expected_fn,net_handle.read())
                net_handle.close()
            else:
                raise ValueError(f'{sub_database_name} is not a valid sub-db.')
        records = _read_file(expected_fn)
        return records

    def query(self,query, sub_database_name = "nucleotide", search_limit = 5):
        print(query)
        if _is_valid_db_name(sub_database_name):
            def query_inner(query_i):
                handle = Entrez.esearch(db=sub_database_name, term=query, retmax=search_limit)
                results = Entrez.read(handle)
                return results
            results = query_inner(query)
            if results["Count"] == "0":
                spelling = spelling_suggest(query,sub_database_name)
                if spelling is not None and spelling["CorrectedQuery"] != "":
                    results = query_inner(spelling["CorrectedQuery"])
            return [results]
        raise ValueError(f'{sub_database_name} is not a valid sub-db.')
    
    def count(self,query):
        count = 0
        query = f'"{query}"'
        handle = Entrez.egquery(term=query)
        record = Entrez.read(handle)
        handle.close()
        for row in record["eGQueryResult"]:
            if row["DbName"] in target_dbs:
                try:
                    count = count + int(row["Count"])
                except ValueError:
                    continue
        return count

    def related(self,id,sub_database_name = "nucleotide"):
        related_records = []
        if _is_valid_db_name(sub_database_name):
            related_records_raw = Entrez.read(Entrez.elink(dbfrom=sub_database_name, id=id))
            for record in related_records_raw:
                for db in record["LinkSetDb"]:
                    for record_id in db["Link"]:
                        if db["DbTo"] in target_dbs:
                            related_records.append(record_id["Id"])
            return related_records
        raise ValueError(f'{sub_database_name} is not a valid sub-db.')

    def generalise_query_results(self,query_results):
        generalised_results = []
        if isinstance(query_results,list):
            for result in query_results:
                if "IdList" in result.keys():
                    for id in result["IdList"]:
                        generalised_results.append(id)

        elif isinstance(query_results,dict):
            if "IdList" in query_results.keys():
                for id in query_results["IdList"]:
                    generalised_results.append(id)
        return generalised_results

    def generalise_get_results(self,get_results):
        general_graph = rdflib.Graph()
        if not isinstance(get_results,(list,tuple,set)):
            get_results = [get_results]
        
        for result in get_results:
            namespace = rdflib.Namespace("http://genbank2graph/")
            subject = namespace + rdflib.URIRef(result.locus)
            for attr, value in result.__dict__.items():
                if attr[0] == "_" or attr in predicate_blacklist or value in object_blacklist:
                    continue
                predicate = namespace + rdflib.URIRef(str(attr.replace(" ","")))
                if isinstance(value,(dict,list,set,tuple)): 
                    value = _handle_entry(value,namespace,subject,predicate,general_graph)
                else:
                    object = rdflib.Literal(value)
                    general_graph.add((subject,predicate,object)) 
        return general_graph

def _handle_entry(entry,namespace,subject,predicate,graph):
    if isinstance(entry,dict):
        for k,v in entry.items():
            tmp_predicate = rdflib.URIRef(predicate + "/" + str(k.replace(" ","")))  
            graph = _handle_entry(v,namespace,subject,tmp_predicate,graph)
    elif isinstance(entry,(list,set,tuple)):
        for e in entry:
            graph = _handle_entry(e,namespace,subject,predicate,graph)
    elif isinstance(entry,GenBank.Record.Feature):
        for qualifier in entry.qualifiers:
            if qualifier.key in qualifier_object_whitelist:
                graph = _handle_entry(qualifier.value,namespace,subject,predicate,graph)
    elif isinstance(entry,GenBank.Record.Reference):
        graph = _handle_entry(entry.title,namespace,subject,predicate,graph)
    else:
        object = rdflib.Literal(entry.replace(" ","_"))
        graph.add((subject,predicate,object))
    return graph

def _is_valid_db_name(db_name):
    handle = Entrez.einfo()
    databases = Entrez.read(handle)
    handle.close()
    if db_name in databases["DbList"]:
        return True
    else:
        return False

def _read_file(fn):
    records = []
    with open(fn) as handle:
        for record in GenBank.parse(handle):
            records.append(record)
    return records

def spelling_suggest(search_term,db_name = "nucleotide"):
    try:
        handle = Entrez.espell(term=search_term,db=db_name)
        record = Entrez.read(handle)
        return record
    except RuntimeError:
        return None








