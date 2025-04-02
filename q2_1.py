from q1_1 import Parse_Docs 


def df(col):
    df_ = {}
    for _, doc in col.items():
        terms = doc.terms
        for term in terms.keys():
            try:
                df_[term] += 1
            except KeyError:
                df_[term] = 1
                
    df_ =  dict(sorted(df_.items(), key=lambda item: item[1], reverse=True))
    return df_

       
    
if __name__ == "__main__":
    stopwords_f = open('common-english-words.txt', 'r') 
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    
    directory = "RCV1v3/"  # Change this to your target directory
    
    docV3s = Parse_Docs(stop_words, directory)
    dfs = df(docV3s)
    
    print('There are ' +  str(len(docV3s)) + ' documents in this data set and contains ' + str(len(dfs)) + ' terms')
    print('The following are the terms’ document-frequency:')
    print(dfs)