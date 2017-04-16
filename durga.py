import re
import random
 
# Replaces 1st person user input with bot's response, in the 2nd person
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

# Take the user's 1st person input and process as a Regex, return the bot's response as 2nd person
topics = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"]],
 
    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],
 
    [r'Why can\'?t I ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]],
 
    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],
 
    [r'I am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"]],
 
    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you tell me you're {0}?",
      "Why do you think you're {0}?"]],
 
    [r'Are you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "Would you prefer it if I were not {0}?",
      "Perhaps you believe I am {0}.",
      "I may be {0} -- what do you think?"]],
 
    [r'What (.*)',
     ["Why do you ask?",
      "How would an answer to that help you?",
      "What do you think?"]],
 
    [r'How (.*)',
     ["How do you suppose?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?"]],
 
    [r'Because (.*)',
     ["Is that the real reason?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"]],
 
    [r'(.*) sorry (.*)',
     ["There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
 
    [r'Hello(.*)',
     ["Hello... I'm glad you could drop by today.",
      "Hi there... how are you today?",
      "Hello, how are you feeling today?"]],
 
    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}?"]],
 
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
 
    [r'Yes',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?",
      "Glad to hear you say yes, but I need more.  Tell me more."]],
 
    [r'(.*) computer(.*)',
     ["Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel threatened by computers?"]],
 
    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "It could well be that {0}."]],
 
    [r'It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],
 
    [r'Can you ([^\?]*)\??',
     ["What makes you think I can't {0}?",
      "If I could {0}, then what?",
      "Why do you ask if I can {0}?"]],
 
    [r'Can I ([^\?]*)\??',
     ["Perhaps you don't want to {0}.",
      "Do you want to be able to {0}?",
      "If you could {0}, would you?"]],
 
    [r'You are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"]],
 
    [r'You\'?re (.*)',
     ["Why do you say I am {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],
 
    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?"]],
 
    [r'I feel (.*)',
     ["Good, tell me more about these feelings.",
      "Do you often feel {0}?",
      "When do you usually feel {0}?",
      "When you feel {0}, what do you do?"]],
 
    [r'I have (.*)',
     ["Why do you tell me that you've {0}?",
      "Have you really {0}?",
      "Now that you have {0}, what will you do next?"]],
 
    [r'I would (.*)',
     ["Could you explain why you would {0}?",
      "Why would you {0}?",
      "Who else knows that you would {0}?"]],
 
    [r'Is there (.*)',
     ["Do you think there is {0}?",
      "It's likely that there is {0}.",
      "Would you like there to be {0}?"]],
 
    [r'My (.*)',
     ["I see, your {0}.",
      "Why do you say that your {0}?",
      "When your {0}, how do you feel?"]],
 
    [r'You (.*)',
     ["We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I {0}?"]],
 
    [r'Why (.*)',
     ["Why don't you tell me the reason why {0}?",
      "Why do you think {0}?"]],
 
    [r'I want (.*)',
     ["What would it mean to you if you got {0}?",
      "Why do you want {0}?",
      "What would you do if you got {0}?",
      "If you got {0}, then what would you do?"]],

    [r'(.*)God(.*)',
     ["Tell me more about God.  How do you see God?",
      "What was your relationship with God like?",
      "How deeply do you believe in God?",
      "How does this relate to your feelings on Nature and God?",
      "God is hard to see and seems to be everywhere and nowhere.  What do you think?"]],

    [r'(.*) lover(.*)',
     ["Tell me more about your lover.",
      "What was your relationship with your lover like in bed?",
      "How do you feel about your lover cheating on you?",
      "How does this relate to your feelings today?",
      "Good conjugal and amorous relations are important."]],

    [r'(.*) mother(.*)',
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are important."]],
 
    [r'(.*) father(.*)',
     ["Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?"]],
 
    [r'(.*) child(.*)',
     ["Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],
 
    [r'(.*)\?',
     ["Why do you ask that?",
      "Can you answer your own question - what would you say?",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?",
      "I don't really know, what's your best guess?",
      "I'm having trouble telling you this, can you tell me your opinion?",
      "Some questions are tough.  Can we talk about your favorite animal instead?"]],
 
    [r'quit',
     ["Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!"]],
 
    [r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"]]
]
 
# This function exists only to take a 1st person statement, parse it into tokens, and then return 2nd person language.
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 

# The main statement:  Takes the user's input statement and analyzes it for a pattern or response in
# the topics list above - if there is a match, it gives the matching statement as a random pick and reflects it
#If there is no match, it defaults to the last regex statement, the r'(.*)' above default
def analyze(statement):
    for pattern, responses in topics:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])




hellos = ["Hi!", "Hey!", "Yo!","Hey lovely!", "Bonjour", "Salutations!", "Good day!", "Howdy stranger!", "Friend."]
byes = ["Bye.", 'Later gator', 'Ciao mouse.', 'Seeya friend.', 'Till next time then.', "May we meet again in heaven or hell."]

intros = [
"How are you feeling today?",
    "What's going on?",
    "What're you tiddly diddly doing?",
    "How goes your path this holy day?",
    "So what's up?"
]

def main():
    name = raw_input(random.choice(hellos)+" What's your name? \n> ")
    print ("Durga:  Ok, " + name + "! " + random.choice(intros))
 
    while True:
        statement = raw_input(name + ":  ")
        print "Durga:  " + analyze(statement)
 
        if statement in ["quit", "exit", "bye", "au revoir"]:
            print (name + ", you said "+statement+", so I am saying bye. \n" + random.choice(byes)+"\n")
            break
 
 
if __name__ == "__main__":
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
-More state management: other user variables, use name, most recent topic
---Stats: identify as a person, place, or thing, keep a record as a list
-Small talk module
-Logging
-Upgrade topics with common things said in chats
-Old person questions about life or childhood

CORPORA TO CHECK OUT:
http://www.linguistics.ucsb.edu/research/santa-barbara-corpus#SBC008
http://courses.washington.edu/englhtml/engl560/corplingresources.htm
https://www.microsoft.com/en-us/download/details.aspx?id=52375&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F6096d3da-0c3b-42fa-a480-646929aa06f1%2F
https://people.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html
https://chenhaot.com/pages/changemyview.html
http://faculty.nps.edu/cmartell/NPSChat.htm

'''