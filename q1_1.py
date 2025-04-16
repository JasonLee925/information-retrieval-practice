import re, os
import string
from stemming.porter2 import stem

"""

Definition of words and terms
- Words are fundamental constructs in many natural languages. A term is a label for one specific concept, which can contain a
single word (simple term) or many words (e.g., n-grams). A term can also be a symbol (©, ®) or a formula (H2O).

"""
class DocV3:
    def __init__(self, parsed_doc):
        self.parsed_doc = self.__validate_parsed_doc(parsed_doc) # "parsed_doc" must pass this validation func so the object can read the data
        self.newsID = list(self.parsed_doc[1])[0]
        self.terms = list(dict(self.parsed_doc[1]).values())[0]
        self.doc_size = self.parsed_doc[0]
    
    # internal use only: validate the parsed_doc object
    def __validate_parsed_doc(self, parsed_doc: tuple): 
        if parsed_doc == None:
            print("Error: the DocV3 is not created due to invalid 'parsed_doc'")
            return
        return parsed_doc
    
    def getNewsID(self): 
        return self.newsID
    
    def get_sorted_termList(self) -> dict:
        return dict(sorted(self.terms.items(), key=lambda item: item[1], reverse=True))
    
    # for Q1-3: print pretty
    def get_printable_termList(self):
        ret = ""
        for doc in self.parsed_doc[1].items():
            ret += 'Document '+ doc[0]+ ' contains ' + str(len(doc[1])) + ' indexing terms and have total ' + str(self.parsed_doc[0]) + ' words'
            ret += '\r\n'
            sorted_dict_desc = self.get_sorted_termList()
            ret += str(sorted_dict_desc) + '\r\n'
        return ret
     
     
    # add new term & count the number of term occurance 
    @staticmethod 
    def add_term(curr_doc, term, stop_ws):
        if len(term) > 2 and term not in stop_ws: 
            curr_doc[term] = curr_doc.get(term, 0) + 1
            
        return curr_doc
        
    # main logic for parsing a document ..
    @staticmethod
    def parse_doc(filepath, stop_ws):
        myfile=open(filepath)
    
        curr_doc = {}
        start_end = False
        
        file_=myfile.readlines()
        word_count = 0 
        for line in file_:
            line = line.strip()
            #print(line) # testing
            if(start_end == False):
                if line.startswith("<newsitem "):
                    for part in line.split():
                        if part.startswith("itemid="):
                            docid = part.split("=")[1].split("\"")[1]
                            break  
                if line.startswith("<text>"):
                    start_end = True  
            elif line.startswith("</text>"):
                break
            else:
                line = line.replace("<p>", "").replace("</p>", "").replace("&quot;", "") # "&quot;" is xml language so it should be removed
                line = line.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
                line = re.sub(r"\s+", " ", line) # remove extra space
                # print(line) # testing
                for term in line.split():
                    word_count += 1 
                    term = stem(term.lower() )
                    curr_doc = DocV3.add_term(curr_doc, term, stop_ws)

                
        myfile.close()
        return(word_count, {docid:curr_doc})
    
    
    

def Parse_Docs(stop_words, inputfolder):
    docV3_collection = {}
    for filename in os.listdir(inputfolder):
        file_path = os.path.join(inputfolder, filename)
        if os.path.isfile(file_path):  
            x = DocV3.parse_doc(file_path, stop_words)
            doc = DocV3(x)
            docV3_collection[file_path] = doc
    return docV3_collection