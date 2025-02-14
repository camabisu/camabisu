import nltk

lemmatizer = WordNetLemmatizer()
s = "A apple and two bananas,three pens please." #s=semtence
morph = nltk.word_tokenize(s)
pos = nltk.pos_tag(morph)
# chunk.ne_chunkに品詞情報を渡す
entities = nltk.chunk.ne_chunk(pos)
print(entities)

n=[]

for w, d in pos:
  if d in['DT','CD','NN','NNS']:
    #「please」を消す
    if w  == "please":
      pass
    else:
      n.append(w)
print(n)
#コンマを消す
print(' '.join(n))

#(S
  A/DT
  apple/NN
  and/CC
  two/CD
  bananas/NNS
  ,/,
  three/CD
  pens/NNS
  please/NN
  ./.)
['A', 'apple', 'two', 'bananas', 'three', 'pens']
A apple two bananas three pens
