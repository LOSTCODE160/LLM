import re
with open("the-verdict.txt","r",encoding="utf-8") as f:
    raw_text=f.read()
print("total number of char:",len(raw_text))
print(raw_text[:99])
preprocessed=re.split(r'([, .:;?_!"\')]|--|\s)', raw_text)

preprocessed=[t for t in preprocessed if t.strip()]
print(preprocessed[:30])
print(len(preprocessed))

vocab=sorted(set(preprocessed))
print("vocab len:", len(vocab))

int_vocab={t:i for i,t in enumerate(vocab)} # create a mapping from token to integer token:is used for dictionary then i for i is used  for loop through the vocab t in enumate is used to assign the number to the token

print(int_vocab)

class simpletokenizerv1:
    def __init__(self,int_vocab):
        self.str_to_int=int_vocab
        self. int_to_str={ i:s for s,i in int_vocab.items()} # create a mapping from integer token to token
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
    
tokenizer = simpletokenizerv1(int_vocab)

text = "The cat sat on the mat."
ids=tokenizer.encode(text)
print("encode",ids)
tokenizer.decode(ids)
        
    
        
    
