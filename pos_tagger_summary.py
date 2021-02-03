from online_resource_handler.database_handler import DatabaseHandler
from online_resource_handler.db_interfaces.sbol_rdflib_identifiers import identifiers
import os
from Bio import GenBank
import rdflib
import nltk
import nltk
import string
import re
from fuzzywuzzy import fuzz,process

records = os.path.join("online_resource_handler","db_interfaces","records")
shb_records = os.path.join(records,"synbiohub")
gbk_records = os.path.join(records,"genbank")

predicate_whitelist = [identifiers.predicates.title,
                       identifiers.predicates.description,
                       identifiers.predicates.mutable_description,
                       identifiers.predicates.mutable_notes,
                       identifiers.predicates.mutable_provenance
                       ]

def download():
    t_descriptors = ["g","l","s"]
    db_handler = DatabaseHandler()
    graphs = db_handler.get_record_from_descriptors(t_descriptors)

def mine_sentences(sentences):
    mine_words = []
    sentences = tokenize_sentences(sentences)
    for sentence in sentences:
        mine_words = mine_words + mine_sentence(sentence)
    return mine_words

def tokenize_sentences(sentences):
    sentences = nltk.sent_tokenize(sentences)
    return sentences

# ------------------------ Sentence Level ------------------------
def mine_sentence(sentence):
    words = tokenize_sentence(sentence)
    pos_tagged_words = pos_tag_sentence(words)
    mined_words = []
    for word,tag in pos_tagged_words:
        mined_words = mined_words + mine_word(word,tag)
    return mined_words

def tokenize_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    return words

def pos_tag_sentence(sentence):
    sentences = nltk.pos_tag(sentence)
    return sentences


# ------------------------ Word Level ------------------------
def mine_word(word,pos_tag=None):
    words = []
    tokens = tokenize_word(word)
    for token in tokens:
        if is_valid_token(token,pos_tag):
            words.append((token.lower(),pos_tag))
    return words
    
def tokenize_word(word):
    return re.split("[" + string.punctuation + "]+", word)

# ------------------------ Token Level ------------------------
def is_valid_token(token,pos_tag=None):
    blacklist_confidence = 90
    if len(token) <= 2:
        return False
    if not token.isalpha():
        return False
    return True


def main():
    sorted_pos_tagged = {}
    db_handler = DatabaseHandler()
    for entry in os.scandir(shb_records):
        graph = rdflib.Graph()
        graph.load(entry.path)
        for s,p,o in graph:
            if p in predicate_whitelist and isinstance(o,rdflib.Literal):
                pos_tagged = mine_sentences(o)
                for p in pos_tagged:
                    if p[1] in sorted_pos_tagged.keys():
                        sorted_pos_tagged[p[1]].append(p[0])
                    else:
                        sorted_pos_tagged[p[1]] = [p[0]]
                        

    for entry in os.scandir(gbk_records):
        with open(entry) as handle:
            for record in GenBank.parse(handle):
                graph = db_handler._db_util.db_mapping_calls["genbank"].generalise_get_results(record)
                for s,p,o in graph:
                    if isinstance(o,rdflib.Literal):
                        pos_tagged = mine_sentences(o)
                        for p in pos_tagged:
                            if p[1] in sorted_pos_tagged.keys():
                                sorted_pos_tagged[p[1]].append(p[0])
                            else:
                                sorted_pos_tagged[p[1]] = [p[0]]
    
    f = open("summary.txt","a+")
    for k,v in sorted_pos_tagged.items():
        v = list(set(v))
        print(k,v)
        print("\n")
        f.write(f'{k} - {"-".join(v)}\n')


if __name__ == "__main__":
    main()