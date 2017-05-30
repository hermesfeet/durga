import random
import knowledge as kb
import nltk, re, pprint, urllib
from nltk.tokenize import *
import time, datetime, uuid
import collections
import boto3

st = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# Install requirement:  Make sure to download:  nltk.download('punkt'), nltk.download('averaged_perceptron_tagger')

# Volley are topics the conversation can cover
volleys = ["school", "religion", "family", "home", "job", "partners", "health", "history", "friends", "moments",
           "choices"]

volley = random.choice(["family", "home"])  # start with this is a volley seed
volley_count = 0
volley_completed = ["home"]  # keep a list of volleys done
question_follow = 1  # if 0, asks a new question, otherwise if another number, could do a followup
last_volley = volley_completed[-1]
sentiment = 0.5

# question_history is the session_attributes of the last 20 questions asked, older than 20 are popped out
question_history = collections.deque(maxlen=20)

session_attributes = {
    "age": 23,
    "last questions": question_history,
    "name": name,
    "q_follow": question_follow,
    "volley": volley,
    "volley_count": volley_count,
    "volley_question": volley_question,
}


# Reflections replace 1st person user input with bot's response, in the 2nd person


def reflect(fragment):
    """    
    :param fragment: 
    :return:
    # Return statement, with 1st person languaged  
    replaced with 2nd person language. 
    """
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
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)


tell_me_more = [
    "What more can you tell me?",
    "Can you explain some more?",
    "I'm curious, can you tell me more?"
]


def analyze(statement, session_attributes):
    """
    :param statement: 
    :param session_attributes: 
    :return: 
    The main function to analyze a statement:  Takes the user's input statement and analyzes it for a pattern or response
    in the topics list above. If there is a match, it gives the matching statement as a random pick and reflects it
    If there is no match, it defaults to the last regex statement, the r'(.*)' above default
    This takes you to the life questions dictionary, where you are put inside a volley and asked questions from that list
    """
    session_attributes["q_follow"] = random.choice([1, 2])
    try:
        # first try to reflect their topic based on the topics list
        for pattern, responses in kb.topics:
            match = re.match(pattern, statement.rstrip(".!"))
            if match:
                response = random.choice(responses)
                return response.format(*[reflect(g) for g in match.groups()])
    except:
        # goes to life questions structure for next q in volley
        response = kb.life_questions[session_attributes["volley"]][session_attributes["volley_question"]][0]
        session_attributes["volley_question"] = random.choice(
            kb.life_questions[session_attributes["volley"]][session_attributes["volley_question"]][1])
        return response


def ask_deeper_question(statement, session_attributes):
    """
    :param statement: 
    :return:
    Dig into a person, place, or thing (PPT) mentioned in a user response, via a part of speech (pos)
    """
    response = nltk.word_tokenize(statement)
    pos = nltk.pos_tag(response)
    # print pos #use this to debug the pos
    # define a noun phrase
    for tuples in pos:
        if tuples[1] == 'NN':  # using a noun
            focus_word = random.choice(
                ["Can you tell me more about your ", "Give me some insight into your ", "I want to know about your "]) + \
                         tuples[0] + "?"
        elif tuples[1] == 'NNP':  # using a proper noun
            focus_word = random.choice(["", "Who was ", "Give me details about ", "I want to know more about "]) + \
                         tuples[0] + "?"
        elif tuples[1] == 'JJ':  # using an adjective
            focus_word = "When you say " + tuples[0] + ", can you explain more?"
        else:
            focus_word = random.choice(tell_me_more)
    return focus_word


def analyze_or_dig(statement):
    """
    Calls analyze, or calls ask_deeper_question.
    """
    if random.uniform(0, 1) > .7:
        return analyze(statement)
    else:
        return ask_deeper_question(statement)


def log(ts, speaker, said):
    """
    :param ts: What time is it.  
    :param user_said: What user said.
    :param durga_said: What Durga said.
    :return:
    Write what was said to a file. 
    """
    with open('chat_logs.txt', 'a') as logs:
        string = ts + ', ' + user_said + ', ' + durga_said
        logs.write(string)
        string = ts + ', ' + user_said + ', ' + durga_said
        logs.write(string)


def process_volley(user_said, session_attributes, action, username):
    """
    :param user_said: 
    :param session_attributes: 
    :param action: 
    :return:
    Logs, 
    """
    # TODO: add id, timestmp
    log(user_ts=datetime.datetime.utcnow(), speaker=session_attributes.get('name'), said=user_said)
    res = get_durga_response(user_said=user_said, session_attributes=session_attributes, action=action)
    log(user_ts=datetime.datetime.utcnow(), speaker="Durga", said=user_said)
    return res


def get_durga_response(user_said, session_attributes, action=None):
    """
    :param user_said: 
    :param session_attributes: 
    :param action: 
    :return: 
     Logic for everything Durga says.
    """

    # Start logic
    if action and action == 'Start':
        session_attributes['expecting'] = 'name'
        session_attributes['volley_count'] = 0
        return "I'm Jules and I'm here to learn about your life story. What's your name?"

    # End logic
    # TODO: Replace "Actions == finish" with the actual Alexa logic.
    if action == 'Finish' or user_said in ["quit", "exit", "bye", "good bye", "I'm done", "au revoir"]:
        res = "Okay " + session_attributes['name'] + ", you said " + user_said + ", so I am saying bye. \n" + \
              random.choice(kb.byes) + "\n"
        return res

    # Logic for first volley, when I expect 'name'
    if session_attributes['expecting'] == 'name':
        session_attributes["name"] = user_said.upper()  # Replace this with Lex.
        res = "Ok, " + session_attributes['name'], + "! " + random.choice(kb.intros)
        return res

    try:  # first try, if you haven't done follow ups, q follow will be greater than one and it needs to decrement
        if session_attributes["q_follow"] == 0:
            response = analyze_or_dig(user_said)  # weighted choice - need to do without Numpy random choice
        else:
            decrement = session_attributes["q_follow"]
            session_attributes["q_follow"] = decrement - 1
            response = ask_deeper_question(user_said)
    except:
        try:
            decrement = session_attributes["q_follow"]
            session_attributes["q_follow"] = decrement - 1
            response = ask_deeper_question(user_said)
        except:
            response = random.choice(kb.damnit)
            # TODO: Add random joke or epigram

    while response in session_attributes['last questions']:  # This makes sure you don't repeat items in a volley
        response = analyze(statement=user_said)

    if session_attributes['volley_count'] < 6:  # This makes you change volleys after 7 questions
        session_attributes['volley_count'] += 1
    else:
        session_attributes['volley_count'] = 0
        new_volley = random.choice(volleys)
        session_attributes["volley"] = new_volley
        alternate = random.choice(kb.change_topics) + new_volley + ". " + random.choice(kb.last_thoughts)
        with open('chat_logs.txt', 'a') as logs:
            logs.write(alternate + "\n")
        print (alternate)

    combined_response = random.choice(kb.fillers) + response
    question_history.append(response)
    return combined_response


if __name__ == '__main__':
    """
    The "Main" module is for simulating the Alexa / Google Actions functionality using a Python command line.
    """
    main_session_attributes = dict()
    main_session_attributes['user_id'] = str(uuid.uuid4())

    durga_res = process_volley(user_said=None, session_attributes=main_session_attributes, actions='Start')
    keep_going = True
    user_said = raw_input(durga_res)

    while keep_going:
        durga_res = process_volley(user_said=user_said, session_attributes=main_session_attributes, action=None)
        raw_input(durga_res)
