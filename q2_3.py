from q1_3 import get_stop_words, remove_file
from q1_1 import Parse_Docs 
from q2_1 import df
from q2_2 import tfidf
from q1_2 import Parse_Q

# compose the tf-idf metrix
def tfidf_matrix_index(stop_words, directory = "RCV1v3/"):
    docV3s = Parse_Docs(stop_words, directory)
    dfs = df(docV3s)
    R= {}
    for _, doc in docV3s.items():
        vals = tfidf(doc, dfs, len(docV3s))
        R[doc.newsID] = vals
    return R

def doc_at_a_time(I, Q): 
    R = {}
    for i_doc, i_term_vals in I.items():
        R[i_doc] = 0
        for q_term, q_freq in Q.items():
            if q_term in i_term_vals.keys(): 
                # if a query's term is present in a document
                f = i_term_vals[q_term] 
                q = q_freq
                R[i_doc] = R[i_doc] + f * q # the god damn equation
    return R

def main():
    stop_words = get_stop_words()
    
    docV3s = Parse_Docs(stop_words, "RCV1v3/")

    # total terms:
    dfs = df(docV3s)
    with open("shenglee_Q2.txt", "a") as file:          
        print('There are ' +  str(len(docV3s)) + ' documents in this data set and contains ' + str(len(dfs)) + ' terms', file=file)
        print('The following are the terms’ document-frequency:', file=file)
        print(dfs, file=file)
    
        print("\r\n ===========BOARDER LINE===========", file=file) 
    
    # tf-idf: 
    with open("shenglee_Q2.txt", "a") as file:          
        for _, doc in docV3s.items():
            print(f'Document: {doc.newsID} contains {len(doc.terms)} terms', file=file)
            x = tfidf(doc, dfs, len(docV3s))
            x = dict(list(x.items())[:20]) # print top 20
            print(x, file=file)
            
        print("\r\n ===========BOARDER LINE===========", file=file) 
    
    
    # ranking score:
    I = tfidf_matrix_index(stop_words)
    queries_title = ["US EPA ranks Geo Metro car most fuel-efficient 1997 car.", # 86961
               "BELGIUM: MOTOR RACING-LEHTO AND SOPER HOLD ON FOR GT VICTORY.", #ß741299 
               "ISRAEL: Israel threatens tough response to rocket attacks." #809495
               ]
    
    for query in queries_title:
        Q = Parse_Q(query, stop_words)
        R = doc_at_a_time(I, Q)
        ret = dict(sorted(R.items(), key=lambda item: item[1], reverse=True))

        with open("shenglee_Q2.txt", "a") as file:  
            print('',file=file) 
            print(f'The Ranking Result for query: {query}',file=file)
            print(ret,file=file)
    
    

if __name__ == "__main__":
    remove_file('shenglee_Q2.txt')
    main()
