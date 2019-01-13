from nltk import sent_tokenize, word_tokenize
from gensim.models import Word2Vec

# See Tutorial here:  https://machinelearningmastery.com/develop-word-embeddings-python-gensim/

# define training data, tokenize document into sentences
with open("shaks.txt") as shaks:
    shaks_all = shaks.read()

sentences = [word_tokenize(t) for t in sent_tokenize(shaks_all)]

# train model
model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)

# summarize the loaded model
print(model)

# summarize vocabulary
words = list(model.wv.vocab)

# access vector for one word
test_word = 'love'
print("Embedding for: ", test_word)
print(model.wv[test_word])

another_word = 'hate'
print("Embedding for: ", another_word)
print(model.wv[another_word])

#test similarity'
print("Similarity for: ", test_word, another_word)
print(model.wv.similarity(test_word, another_word))

stop = input("stop")

# save model
model.save('model.bin')

# load model
new_model = Word2Vec.load('model.bin')
print(new_model)