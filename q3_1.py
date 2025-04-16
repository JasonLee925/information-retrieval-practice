from q1_3 import get_stop_words
from q1_1 import Parse_Docs 



def avg_length(coll: dict):
     sum_of_length = sum(doc.doc_size for _,doc in coll.items())
     return sum_of_length / len(coll)




def main():
    stop_words = get_stop_words()
    docV3s = Parse_Docs(stop_words, "RCV1v3/")
    print("Average document length for this collection is: " + str(int(avg_length(docV3s))))
    

if __name__ == "__main__":
    main()
