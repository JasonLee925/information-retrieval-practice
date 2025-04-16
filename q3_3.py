from q1_3 import get_stop_words, remove_file
from q1_1 import Parse_Docs 
from q3_1 import avg_length
from q3_2 import my_bm25
from q2_1 import df


def main():
    stop_words = get_stop_words()
    docV3s = Parse_Docs(stop_words, "RCV1v3/")
    dfs = df(docV3s)
    
    with open("shenglee_Q3.txt", "a") as file:     
        
        avg_len = int(avg_length(docV3s))
        print("Average document length for this collection is: " + str(avg_len), file=file)
        
        # my_bm25:
        query_text = "US EPA ranks Geo Metro car most fuel-efficient 1997 car." 
        print("The query is: " + query_text, file=file)
        print("", file=file)
        scores = my_bm25(coll=docV3s, q=query_text, df=dfs)
        for filename, doc in docV3s.items():
            id = doc.newsID
            score = scores.get(id, None)
            
            if score == None: 
                continue
            
            print(f'Document ID: {id}, Doc Length: {doc.doc_size} -- BM25 Score: {score}', file=file)
            
        print("", file=file)
            
        # ranking score:
        queries = [
            'The British-Fashion Awards',
            'Rocket attacks',
            'Broadcast Fashion Awards',
            'US EPA ranks Geo Metro car most fuel-efficient 1997 car.',
        ]
        
        for q in queries:
            print(f'For query "{q}", the top-5 relevant documents are: ', file=file)
            scores = my_bm25(docV3s, q,  dfs)
            result= sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
            print(result, file=file)
                
        
    

if __name__ == "__main__":
    remove_file('shenglee_Q3.txt')
    main()
