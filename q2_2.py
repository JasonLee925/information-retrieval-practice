from q1_1 import Parse_Docs 
from q2_1 import df
from q1_3 import remove_file, get_stop_words
import math


#TODO: this seems to be wrong.... rethink
def tfidf(doc, d_f, ndocs = 0):
    total_number_terms = len(doc.terms)
    weights = {}
    for term, num in doc.terms.items():
        tf = num / total_number_terms
        idf = math.log10(ndocs / d_f[term])
        
        weights[term] = tf * idf
        
        
    weights = dict(sorted(weights.items(), key=lambda item: item[1], reverse=True))
    return weights


def main():

    stop_words = get_stop_words()


    directory = "RCV1v3/"  # Change this to your target directory

    with open("shenglee_Q2.txt", "a") as file:  

        docV3s = Parse_Docs(stop_words, directory)
        dfs = df(docV3s)


        for _, doc in docV3s.items():
            print(f'Document: {doc.newsID} contains {len(doc.terms)} terms', file=file)
            x = tfidf(doc, dfs, len(docV3s))
            print(x, file=file)
        
    
    

if __name__ == "__main__":
    remove_file('shenglee_Q2.txt')
    main()
