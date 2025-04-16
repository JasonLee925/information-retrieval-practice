from q1_1 import Parse_Docs 
from q2_1 import df
from q1_3 import remove_file, get_stop_words
import math


#TODO: this seems to be wrong.... come back and check again
def tfidf(doc, d_f, ndocs = 0):
    
    weights = {}
    denom = 0.0

    for term, freq in doc.terms.items():
            if term in d_f and d_f[term] > 0:

                tf = math.log(freq) + 1
                idf = math.log(ndocs / d_f[term])

                weight = tf * idf
                weights[term] = weight

                denom += weight ** 2
    norm = math.sqrt(denom)

    if norm == 0:
        return {term: 0.0 for term in weights}  
    normalized_weights = {term: weight / norm for term, weight in weights.items()}
    normalized_weights = dict(sorted(normalized_weights.items(), key=lambda item: item[1], reverse=True)) # sort
    return normalized_weights
