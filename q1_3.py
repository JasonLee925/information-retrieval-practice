from q1_1 import Parse_Docs 
from q1_2 import Parse_Q 
import os

def main():
    stop_words = get_stop_words()

    directory = "RCV1v3/" 

    with open("shenglee_Q1.txt", "a") as file:  
        # Parse_Docs() print out
        docs = Parse_Docs(stop_words, directory)
        for doc in docs.items():       
            print(doc[1].get_printable_termList(), file=file)  


        print('===========BOARDER LINE===========', file=file)

        # Parse_Q() print out
        queries = [
            'US EPA ranks Geo Metro car most fuel-efficient 1997 car.',
            'For instance, a study published in Cognition & Emotion in 1954 found that positive emotions like contentment and amusement can accelerate cardiovascular recovery following negative emotional experiences.',
            'Research indicates that positive emotions can undo the cardiovascular effects of negative emotions, helping the body return to a resting state more quickly'
        ]
        for qy in queries:
            print('Query: ' + qy, file=file)
            print('The parsed query:', file=file)
            print(Parse_Q(qy, stop_words), file=file)
            print('\r\n', file=file)

# create this to avoid repeated codes
def get_stop_words():
    stopwords_f = open('./common-english-words.txt', 'r') 
    stop_words = stopwords_f.read().split(',')
    stopwords_f.close()
    return stop_words

# remove file: this is for convinience only
def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")

if __name__ == "__main__":
    remove_file('shenglee_Q1.txt')
    main()
