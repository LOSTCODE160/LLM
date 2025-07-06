import re
class simpletokenizerv1:
    def __init__(self,vocab):
        self.str_to_int=vocab
        self. int_to_str={ i:s for s,i in vocab.items()} # create a mapping from integer token to token
    def encode(self,text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
                                
        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids=[self.str_to_int[s] for s in preprocessed]
        return ids
    def decode(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
    
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
        
    
        
    