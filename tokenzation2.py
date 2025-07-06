import re
class simpletokenizerv1:
    def __init__(self,vocab):
        self.str_to_int=vocab
        self. int_to_str={ i:s for s,i in vocab.items()} # create a mapping from integer token to token
    def encode(self,text):
        preprosseded=re.split(r'([,.:;?_!"()\']|--|\s)',text)
        preprosseded=[t for t in preprosseded if t.strip()]
        ids=[self.str_to_int[t] for t in preprosseded]
        return ids
    def decode(self,ids):
        
    
        
    