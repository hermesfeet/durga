import re
import random
from knowledge import *
import nltk, re, pprint, urllib
from nltk.tokenize import *
from nltk import word_tokenize
from numpy.random import choice



# Install requirement:  Make sure to download:  nltk.download('punkt'), nltk.download('averaged_perceptron_tagger')

#Volley are topics the conversation can cover
volleys = ["school", "religion", "family", "home", "job", "partners", "health", "history", "friends", "moments", "choices"]
volley = "family" #random.choice(volleys)  #start with this is a volley seed
volley_count = 0
volley_completed = ["home"]  #keep a list of volleys done
last_volley = volley_completed[-1]
volley_question = "a"

#Memory as a dictionary of lists - simple state management
name = "friend"
question_history = []
memory = {"name":name, "age":23, "last questions":question_history, "volley":volley, "volley_count":volley_count, "volley_question":volley_question}

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
                response = life_questions[memory["volley"]][memory["volley_question"]][0]
                memory["volley_question"] = random.choice(life_questions[memory["volley"]][memory["volley_question"]][1])
                return response.format(*[reflect(g) for g in match.groups()])

def dig_into_PPT(statement):
    #Dig into a person, place, or thing (PPT) mentioned in a user response, via a part of speech (pos)
    response = word_tokenize(statement)
    pos = nltk.pos_tag(response)
    #print pos #use this to debug the pos
    for tuples in pos:
        if tuples[1] == 'NN':  #using a noun
            focus_word = "Can you tell me more about "+ tuples[0] +"?"
        elif tuples[1] == 'PRON': #using an adjective
            focus_word = "What did " + tuples[0] + " do?"
        elif tuples[1] == 'JJ': #using an adjective
            focus_word = "When you say " + tuples[0] + ", can you explain more?"
        else:
            focus_word = "What more can you tell me?"
    return focus_word

# This allows the main string to either analyze the statement
#and give the Rogerian response or the life questions in the analyze function, or to dig into a person
#place or thing mentioned, a PPT, and ask a question about that.
func_list = [analyze, dig_into_PPT]
weights = [0.7, 0.3]

# The core function that is running - starts with intros and then runs analyze over and over
# Volley count is some state management to know which volley you are in
# Note the print statement for memory - it allows you to debug and follow the memory as needed

def main():
    name = raw_input("Durga:  "+ random.choice(hellos)+" What's your name? \n> ")
    memory["name"] = name #updates name
    print ("Durga:  Ok, " + name + "! " + random.choice(intros))
    volley_count = 0

    while True:
        statement = raw_input(name + ":  ")
        response = choice(func_list, p=weights)(statement) #weighted choice
        while response in memory['last questions']:  #This makes sure you don't repeat items in a volley
            response = analyze(statement)
        if volley_count < 6:  #This makes you change volleys after 7 questions
            volley_count += 1
        else:
            volley_count = 0
            new_volley = random.choice(volleys)
            memory["volley"] = new_volley
            print "Durga:  " + random.choice(change_topics) + new_volley + ". " + random.choice(["But one last thing...", "One final question though.", "One thing I want to ask before moving on."])
        print "Durga:  " + response
        memory["volley_count"] = volley_count
        question_history.append(response)
        print "        ", memory  # use this to look at memory
 
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
-More state management: don't repeat volleys (keep track of them) ***
-Small talk module (questions people commonly ask) - "You" function to deflect questions about self
-Personal reflection function - tell a story from the bank
-Update PPT to ask questions about a proper noun using NLTK
-Maybe a counter when we get to PPTs, 2-5 follow ups?
-Update memory module -
    -ST Memory - what was recently said, context, name, volley count, PPT count to dig in, what sentences or volleys to not repeat
    -LT Memory - User profile, Bot profile of itself, PPT triples of what was discussed
-Empathic statements
-Jokes function module - weighted low, based on what someone says, takes a diff versus a jokes database and returns one
-Epigrams function module, works like jokes, smaller weight
-Function after some time to go to LT memory and dig into user profile or PPT triples
-Emotional state (analyze sentiment of last 5-15 user statements, map to 7 main emotions and store in memory, and create fillers and language to mirror
-Movie lines and famous quotes - take a user string, do a diff and match it to a movie quote or pithy quote
-Kind of transitional filler words before doing new questions, but only 30-60% of the time
-Logging of the entire transcript
-Upgrade topics with common things said in chats
-Record answers in a KB as a certain format
-Current news - ask them if there's something current (sports, politics, etc) that has been on their mind, then do a Google News scraper search and ask them 1-2 follow up qs

Go over Chatscript documents - how does it work, what to learn?

CORPORA TO CHECK OUT:
http://www.linguistics.ucsb.edu/research/santa-barbara-corpus#SBC008
http://courses.washington.edu/englhtml/engl560/corplingresources.htm
https://www.microsoft.com/en-us/download/details.aspx?id=52375&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F6096d3da-0c3b-42fa-a480-646929aa06f1%2F
https://people.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html
https://chenhaot.com/pages/changemyview.html
http://faculty.nps.edu/cmartell/NPSChat.htm

'''