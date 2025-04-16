#3-2
import math
from q1_2 import Parse_Q
from q2_1 import df
from q1_3 import get_stop_words
from q3_1 import avg_length
from q1_1 import Parse_Docs 


def my_bm25(coll: dict, q, df):
     stop_words = get_stop_words()

     # constant variables
     k1 = 1.2
     k2 = 100
     b = 0.75
     N = len(coll)

     # compute avg doc length
     avg_len = avg_length(coll)

     # Tokenize query
     query_terms = Parse_Q(q, stop_words)

     scores = {}
     for _, doc in coll.items():
          doc_len = doc.doc_size
          doc_tf = doc.terms
          score = 0

          for term in query_terms:
               if term not in df or df[term] == 0:
                    continue  # Skip terms not found in DF dictionary

               f_i = doc_tf[term] if term in doc_tf else 0 
               n_i = df[term]
               qf_i = query_terms[term]

               idf = math.log((N - n_i + 0.5) / (n_i + 0.5) + 1)  

               K = k1 * ((1 - b) + b * (doc_len / avg_len))
               tf_component = ((k1 + 1) * f_i) / (K + f_i) if f_i > 0 else 0
               qf_component = ((k2 + 1) * qf_i) / (k2 + qf_i)          

               score += idf * tf_component  * qf_component #multiply

          scores[doc.newsID] = score

     return scores


def main():
     query_text = "US EPA ranks Geo Metro car most fuel-efficient 1997 car." # update here if you want to test
     stop_words = get_stop_words()
     docV3s = Parse_Docs(stop_words, "RCV1v3/")
     dfs = df(docV3s)
     x = my_bm25(docV3s, query_text,  dfs)
     print("The query is: " + query_text)
     print(x)
    

if __name__ == "__main__":
    main()
