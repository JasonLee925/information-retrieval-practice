import re, string
from stemming.porter2 import stem

def Parse_Q(query, stop_ws):
    curr_doc = {}
    
    query = query.strip()
    
    #Important: the transformation technique must be the same as add_term() in Q1-1
    query = query.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
    query = re.sub(r"\s+", " ", query) # remove extra space
    
    for term in query.split():
        term = stem(term.lower() )
        if len(term) > 2 and term not in stop_ws: 
            curr_doc[term] = curr_doc.get(term, 0) + 1
        
        
    return(curr_doc)

