from textblob import TextBlob
import random

text = '''
I hate god.
'''

# blob = TextBlob(text)
# blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
#                     #  ('threat', 'NN'), ('of', 'IN'), ...]
#
# blob.noun_phrases   # WordList(['titular threat', 'blob',
#                     #            'ultimate movie monster',
#                     #            'amoeba-like mass', ...])
#
# for sentence in blob.sentences:
#     print(sentence.sentiment.polarity)


def weight_choice(choices, weights):
    total = sum(weights)
    treshold = random.uniform(0, total)
    for k, weight in enumerate(weights):
        total -= weight
        if total < treshold:
            return choices[k]

func_list = ["analyze", "ask_deeper_question"]
weights = [0.20, 0.80]

print (weight_choice(func_list, weights),"  ") *5