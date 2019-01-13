from nltk.corpus import wordnet as wn

yare = wn.synset('good.n.01')
hyper = lambda s: s.hypernyms()

print(list(yare.closure(hyper)))

for ss in wn.synsets('good'):
    print(ss.name(), ss.lemma_names())