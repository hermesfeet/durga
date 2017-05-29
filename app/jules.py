import random
from knowledge import *
import nltk, re, pprint, urllib
from nltk.tokenize import *
from nltk import word_tokenize
import time, datetime, uuid
import collections
from numpy.random import choice
import boto3

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
id = str(uuid.uuid4())

client = boto3.client('dynamodb')

# Install requirement:  Make sure to download:  nltk.download('punkt'), nltk.download('averaged_perceptron_tagger')

#Volley are topics the conversation can cover
volleys = ["school", "religion", "family", "home", "job", "partners", "health", "history", "friends", "moments", "choices"]
volley = random.choice(["family", "home"])  #start with this is a volley seed
volley_count = 0
volley_completed = ["home"]  #keep a list of volleys done
question_follow = 1  #if 0, asks a new question, otherwise if another number, could do a followup
last_volley = volley_completed[-1]
volley_question = "a"
sentiment = 0.5

#Memory as a dictionary of lists - simple state management
name = "friend"
question_history = collections.deque(maxlen=20) # this is the memory of the last 20 questions asked, older than 20 are popped out
memory = {"name":name, "age":23, "volley":volley, "volley_count":volley_count, "last questions":question_history, "volley_question":volley_question, "q_follow":question_follow}

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
tell_me_more = [
    "What more can you tell me?",
    "Can you explain some more?",
    "I'm curious, can you tell me more?"
]

def analyze(statement):
    memory["q_follow"] = random.choice([1,2])
    try:
        #first try to reflect their topic based on the topics list
        for pattern, responses in topics:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response.format(*[reflect(g) for g in match.groups()])
    except:
        #goes to life questions structure for next q in volley
        response = life_questions[memory["volley"]][memory["volley_question"]][0]
        memory["volley_question"] = random.choice(life_questions[memory["volley"]][memory["volley_question"]][1])
        return response

def ask_deeper_question(statement):
    #Dig into a person, place, or thing (PPT) mentioned in a user response, via a part of speech (pos)
    response = word_tokenize(statement)
    pos = nltk.pos_tag(response)
    #print pos #use this to debug the pos
    #define a noun phrase
    for tuples in pos:
        if tuples[1] == 'NN':  #using a noun
            focus_word = random.choice(["Can you tell me more about your ", "Give me some insight into your ", "I want to know about your "])+ tuples[0] +"?"
        elif tuples[1] == 'NNP':  #using a proper noun
            focus_word = random.choice(["", "Who was ", "Give me details about ", "I want to know more about "])+ tuples[0] +"?"
        elif tuples[1] == 'JJ': #using an adjective
            focus_word = "When you say " + tuples[0] + ", can you explain more?"
        else:
            focus_word = random.choice(tell_me_more)
    return focus_word

# This allows the main string to either analyze the statement
#and give the Rogerian response or the life questions in the analyze function, or to dig into a person
#place or thing mentioned, a PPT, and ask a question about that.
func_list = [analyze, ask_deeper_question]
weights = [0.70, 0.30]

# The core function that is running - starts with intros and then runs analyze over and over
# Volley count is some state management to know which volley you are in
# Note the print statement for memory - it allows you to debug and follow the memory as needed


def printer(print_this):
    # Prints conversation to a simple text log
    with open('chat_logs.txt', 'a') as logs:
        logs.write(print_this)

def main():
    name = raw_input("JULES: "+ random.choice(hellos)+" I'm Jules and I'm here to learn about your life story. What's your name? \n> ")
    memory["name"] = name.upper() #updates name
    salutations = "JULES:  Ok, " + name + "! " + random.choice(intros)
    printer("\n\nConversation ID:  " + id + "\nTimestamp:  " + st + "\n")  #prints conversation information
    with open('chat_logs.txt', 'a') as logs:
        logs.write(salutations + "\n")
    print (salutations)
    volley_count = 0  #starts a counter for each new volley, so that you don't stay too long

    while True:
        statement = raw_input(name.upper() + ":  ")
        printer(" "+ name.upper()+":  "+ statement + "\n")
        try:  #first try, if you haven't done follow ups, q follow will be greater than one and it needs to decrement
            if memory["q_follow"] == 0:
                response = random.choice(func_list)(statement) #weighted choice - need to do without Numpy random coice
            else:
                decrement = memory["q_follow"]
                memory["q_follow"] = decrement - 1
                response = ask_deeper_question(statement)
        except:
            try:
                decrement = memory["q_follow"]
                memory["q_follow"] = decrement - 1
                response = ask_deeper_question(statement)
            except:
                response = random.choice("Boo wha wha!", "Having one of those day, are we!", "May the Lord guide us quietly through the valley of death!")  #put random joke or epigram
        while response in memory['last questions']:  #This makes sure you don't repeat items in a volley
            response = analyze(statement)
        if volley_count < 6:  #This makes you change volleys after 7 questions - can make this random from 5 to 8  later
            volley_count += 1
        else:
            volley_count = 0
            new_volley = random.choice(volleys)
            memory["volley"] = new_volley
            alternate = "JULES:  " + random.choice(change_topics) + new_volley + ". " + random.choice(["But one last thing...", "One final question though.", "One thing I want to ask before moving on."])
            with open('chat_logs.txt', 'a') as logs:
                logs.write(alternate + "\n")
            print (alternate)
        combined_response = "JULES:  " + random.choice(fillers) + response
        with open('chat_logs.txt', 'a') as logs:
            logs.write(combined_response + "\n")
        print(combined_response)
        memory["volley_count"] = volley_count
        question_history.append(response)
        print( "        ", memory)  # use this to look at memory
 
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
