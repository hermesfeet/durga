
#Hello and Goodby
hellos = ["Hi!", "Hey!", "Yo!","Hey lovely!", "Bonjour", "Salutations!", "Good day!", "Howdy stranger!", "Friend."]
byes = ["Bye.", 'Later gator', 'Ciao mouse.', 'Seeya friend.', 'Till next time then.', "May we meet again in heaven or hell."]

#Introductory statements
intros = [
"How are you feeling today?",
    "What's going on?",
    "What're you tiddly diddly doing?",
    "How goes your path this holy day?",
    "So what's up?",
    "Tell me what is on your mind!"
]

#Transitions for volleys
change_topics = [
    "OK, changing the topic to your ",
    "I want to talk about your ",
    "Let's switch over to your ",
    "Something I was wondering about: your ",
    "An area of interest to me, let's discuss your "

]

#Main volley topics, called life questions.  Need at least 5 per topic.
life_questions = {
    "family": [
        "Could you tell me a story or any memory of your brothers and sisters?",
        "What are the full names of your brothers and sisters?",
        "What did your family do for fun when you were a child?",
        "Who was your grandfather?",
        "What are your aunt's pet peeves?"
    ],
    "church": [
        "When and where were you born?",
        "When were you baptized, and what was your religion?",
        "What was the religion of your parents and your grandparents?",
        "What church, if any, do you attend now?",
        "What church do your parents and your grandparents attend?"],
    "school": [
        "Where did you attend grade school?",
        "Where did you attend high school?",
        "What were your schools like?",
        "How did you like school?",
        "What was your favorite subject in school and why?",
        "What subject in school was the easiest for you?",
        "What was your least favorite subject in school and why?",
        "Who was your favorite teacher and why was he/she special?",
        "How do your fellow classmates from school remember you best?",
        "Did you get good grades?"],
    "home": [
        "Where was your first home?",
        "In what other homes/places have you lived?",
        "What were your earliest memories of your home?",
        "Was there a chore you really hated doing as a child?",
        "What kinds of books did you like to read?",
        "Do you remember having a favorite nursery rhyme or bedtime story? What was it?",
        "Do you remember not having enough food to eat because times were hard for your family?",
        "What were your favorite toys and what were they like?",
        "What were your favorite childhood games?",
        "Were there any fads during your youth that you remember vividly?"]
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

    [r'(.*) ignore (.*)',
     ["I give you my full attention, but some things I can't do.  I want to move on.",
      "I will always respect you and never ignore you - some things are too hard for me.  I want to move on."]],

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
     life_questions]
]



'''
     ["Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?",
      ]]
'''