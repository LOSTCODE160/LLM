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
