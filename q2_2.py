from q1_1 import Parse_Docs 
from q2_1 import df
from q1_3 import remove_file, get_stop_words
import math


#TODO: this seems to be wrong.... come back and check again
def tfidf(doc, d_f, ndocs = 0):
    total_number_terms = len(doc.terms)
    weights = {}
    for term, num in doc.terms.items():
        tf = num / total_number_terms
        idf = math.log10(ndocs / d_f[term])
        
        weights[term] = tf * idf
        
        
    weights = dict(sorted(weights.items(), key=lambda item: item[1], reverse=True))
    return weights
