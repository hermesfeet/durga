import re
import random
from knowledge import *
import nltk, re, pprint, urllib
from nltk.tokenize import *
from nltk import word_tokenize
from numpy.random import choice



# Install requirement:  Make sure to download:  nltk.download('punkt'), nltk.download('averaged_perceptron_tagger')

#Volley are topics the conversation can cover
volleys = ["school", "church", "family", "home"]
volley = "home"  #start with this is a volley seed
volley_count = 0
volley_completed = ["home"]  #keep a list of volleys done
last_volley = volley_completed[-1]

#Memory as a dictionary of lists - simple state management
name = "friend"
question_history = []
memory = {"name":name, "age":23, "last questions":question_history, "volley":volley, "volley_count":volley_count}

# Reflections replace 1st person user input with bot's response, in the 2nd person
reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

# This function exists only to take a 1st person statement, parse it into tokens, and then return 2nd person language.
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 

# The main function to analyze a statement:  Takes the user's input statement and analyzes it for a pattern or response in
# the topics list above - if there is a match, it gives the matching statement as a random pick and reflects it
#If there is no match, it defaults to the last regex statement, the r'(.*)' above default
#This takes you to the life questions dictionary, where you are put inside a volley and asked questions from that list

def analyze(statement):
    for pattern, responses in topics:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            if type(responses) == list:
                response = random.choice(responses)
                return response.format(*[reflect(g) for g in match.groups()])
            else:
                response = random.choice(life_questions[memory["volley"]])
                return response.format(*[reflect(g) for g in match.groups()])

def dig_into_PPT(statement):
    #Dig into a person, place, or thing (PPT) mentioned in a user response, via a part of speech (pos)
    response = word_tokenize(statement)
    pos = nltk.pos_tag(response)
    #print pos #use this to debug the pos
    for tuples in pos:
        if tuples[1] == 'NN':  #using a noun
            focus_word = "Can you tell me more about the "+ tuples[0] +"?"
        elif tuples[1] == 'PRON': #using an adjective
            focus_word = "What did " + tuples[0] + " do?"
        elif tuples[1] == 'JJ': #using an adjective
            focus_word = "When you say " + tuples[0] + ", can you explain more?"
        else:
            focus_word = "What more can you tell me?"
    return focus_word

func_list = [analyze, dig_into_PPT] # This allows the main string to either analyze the statement
#and give the Rogerian response or the life questions in the analyze function, or to dig into a person
#place or thing mentioned, a PPT, and ask a question about that.
weights = [0.4, 0.6]

# The core function that is running - starts with intros and then runs analyze over and over
# Volley count is some state management to know which volley you are in
# Note the print statement for memory - it allows you to debug and follow the memory as needed

def main():
    name = raw_input(random.choice(hellos)+" What's your name? \n> ")
    memory["name"] = name #updates name
    print ("Durga:  Ok, " + name + "! " + random.choice(intros))
    volley_count = 0

    while True:
        statement = raw_input(name + ":  ")
        response = choice(func_list, p=weights)(statement) #weighted choice
        while response in memory['last questions']:  #This makes sure you don't repeat items in a volley
            response = analyze(statement)
        if volley_count < 7:  #This makes you change volleys after 7 questions
            volley_count += 1
        else:
            volley_count = 0
            new_volley = random.choice(volleys)
            memory["volley"] = new_volley
            print "Durga:  " + random.choice(change_topics) + new_volley + ".  "
        print "Durga:  " + response
        memory["volley_count"] = volley_count
        question_history.append(response)
        #print "        ", memory  # use this to look at memory
 
        if statement in ["quit", "exit", "bye", "au revoir"]:
            print (name + ", you said "+statement+", so I am saying bye. \n" + random.choice(byes)+"\n")
            break
 
 
if __name__ == "__main__":
    volley_count = 0
    main()



#  Regex Statements Review
# . any character
# * 0 to n repetition
# ( ) group
#  (.*) - this is any characters repeated as a group, so a random word - it captures all
# ^\?  not any optional character
# [ab] only what is in this group, so here a and/or b
#  ([^\?]*)\? - these are many characters, so a group of words, a phrase


'''
STUFF TO DO NEXT:
-More state management: don't repeat volleys (keep track of them)
---Generic follow up to a statement that has a person, place, thing (PPT): parse response to identify as a PPT, keep a record as a list
-Small talk module (questions people commonly ask)
-Update memory module - what to persist and refer back to
-Logging
-Upgrade topics with common things said in chats
-Update all volleys with old person questions about life or childhood
-Record answers in a KB as a certain format

CORPORA TO CHECK OUT:
http://www.linguistics.ucsb.edu/research/santa-barbara-corpus#SBC008
http://courses.washington.edu/englhtml/engl560/corplingresources.htm
https://www.microsoft.com/en-us/download/details.aspx?id=52375&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F6096d3da-0c3b-42fa-a480-646929aa06f1%2F
https://people.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html
https://chenhaot.com/pages/changemyview.html
http://faculty.nps.edu/cmartell/NPSChat.htm

'''