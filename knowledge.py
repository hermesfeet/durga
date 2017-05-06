
#Hello and Goodby
hellos = ["Hi!", "Hey!", "Yo!","Hey lovely!", "Bonjour.", "Salutations!", "Good day!", "Howdy stranger!", "Hey Friend."]
byes = ["Bye.", 'Later gator', 'Ciao mouse.', 'Seeya friend.', 'Till next time then.', "May we meet again in heaven or hell."]

#Introductory statements
intros = [
"How are you feeling today - I want to go deep?",
    "What's going on - let's be real?",
    "I go deep.  What're you tiddly diddly doing?",
    "Life is a blessing.  How goes your path this holy day?",
    "Beyond the superficial... what's up?",
    "Tell me what is on your mind!  Let's get personal."
]

#Transitions for volleys
change_topics = [
    "OK, changing the topic to your ",
    "I want to talk about your ",
    "Let's switch over to your ",
    "Something I was wondering about: your ",
    "So, I was thinking, can we discuss your "

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
        "What school activities and sports did you participate in?",
        "Did you and your friends have a special hangout where you liked to spend time?",
        "Where was it and what did you do there?",
        "Were you ever given any special awards for your studies or school activities?",
        "How many years of education have you completed?",
        "Describe yourself as a young adult.",
        "Did you attend any school or training after high school? If so, what was your field of study?",
        "Do you have a college degree(s)?",
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
        "Were there any fads during your youth that you remember vividly?"],

    "job": [
    "As a child, what did you want to be when you grew up?",
    "What was your first job?",
    "How did you decide on a career?",
    "What jobs have you had?",
    "Did you make enough money to live comfortably?",
    "How long did you have to work each day at your job?",
    "How old were you when you retired? Or when do you want to retire or will be able to retire?"],

    "partners": [
    "How old were you when you started dating?",
    "Do you remember your first date? Could you tell me something about it?",
    "When, where and how did you first meet your present spouse?",
    "Do you remember where you went on the first date with your spouse?",
    "How long did you know him/her before you got married?",
    "Describe your wedding proposal.",
    "Where and when did you get married? (Include date, place, church, etc.)",
    "Describe your wedding ceremony.",
    "Who was there? Were there a best man, a bridesmaid, other wedding party members and who were they?",
    "Did you have a honeymoon? Where did you go?",
    "Were you married more than once? If so, answer the previous questions about each spouse.",
    "How would you describe your spouse(s)?",
    "What do (did) you admire most about your dates and spouses?",
    "How long have you been or were you married?",
    "What advice would you give/did you give to your child or grandchild on his/her wedding day?"],

    "kids":[
    "How did you find out you were going to be a parent for the first time?",
    "How many children did you have all together?",
    "What were their names, birth dates and birthplaces?",
    "Why did you give them the names that you did?",
    "Do you remember anything your children did when they were small that really amazed you?",
    "What is one of the most unusual things one of your children did regularly when they were small?",
    "What was the funniest thing you can remember that one of your children said or did?",
    "If you had to do it all over again, would you change the way you raised your family?",
    "What did you find most difficult about raising children?",
    "What did you find most rewarding about being a parent?",
    "Did you spoil any of your children?",
    "Were you strict or lenient as a parent?",
    "Did you find you had to treat each of your children differently? If so, why?",
    "How did you feel when the first of your children went to school for the first time?",
    "How did you first hear that you were a grandparent and how did you feel about it?",
    "What advice do you have for your children and grandchildren about being a parent?",
    "Where did your spouse's parents live?",
    "When and where did your parents die? What do you remember about it?",
    "How did they die? Where were they hospitalized and buried?",
    "What do you remember about the death of your spouse's parents?",
    "Do you remember hearing your grandparents describe their lives? What did they say?",
    "Do you remember your great-grandparents?",
    "Who were your parents? Please give full names.",
    "Who were your grandparents? Please give full names."],

    "health":[
    "Who was the oldest person you remember as a child?",
    "Did you have any of the childhood diseases?",
    "Do you have any health problems that are considered hereditary?",
    "What do you do regularly for exercise?",
    "Do you have any bad habits now or in the past?",
    "Have you ever been the victim of a crime?",
    "Have you ever been in a serious accident?",
    "Has anyone ever saved your life?",
    "Have you ever been hospitalized? If so, what for?",
    "Have you ever had surgery?"],

    "history":[
    "What would you consider the most important inventions during your lifetime?",
    "Do you remember the first time you saw a television; a car; a refrigerator?",
    "How is the world different from what it was like when you were a child?",
    "Do you remember your family discussing world events and politics?",
    "How would you describe yourself politically? Are you conservative or liberal, and why?",
    "Do you remember what you or your parents thought about income tax when it began in 1913?",
    "Do you remember anything about the days of Prohibition?",
    "How did the Depression affect you?",
    "What U.S. president have you admired the most and why?",
    "What did you think of President Franklin D. Roosevelt? How did you react to his death?",
    "How did you react to the assassination of President John F. Kennedy?",
    "What wars have been fought during your lifetime?",
    "What were you doing when you heard the news of the Pearl Harbor bombing?",
    "How did World War II affect you?",
    "How did the Korean War affect you?",
    "How did the Vietnam War affect you?"],

    "friends":[
    "Name a good friend you have known the longest. How many years have you been friends?",
    "Has a good friend ever betrayed you?",
    "Who was your best friend when you were a teenager?",
    "Has there ever been anyone in your life you would consider a kindred spirit or soul mate? Who was he/she and why did you feel a special bond with him/her?",
    "What were the hardest choices you ever had to make?",
    "What person really changed the course of your life by something he/she did?"],

    "moments":[
    "Do you remember any advice or comments that had a big impact on how you lived your life?",
    "If you could change something about yourself, what would it be?",
    "What is the most stressful experience you ever lived through?",
    "What is the scariest thing that ever happened to you?",
    "What kinds of musical instruments have you learned to play?",
    "Would you consider yourself creative?",
    "What things have you made that others have enjoyed?",
    "How would you describe your sense of humor?",
    "What is the funniest practical joke you ever played on someone?",
    "What activities have you especially enjoyed as an adult?",
    "What are your hobbies?",
    "What did you like to do when you were not working?",
    "What is the most amazing thing that has ever happened to you?",
    "Have you ever met any famous people?"],

    "choices":[
    "How do you feel about the choices you made in school, career, spouse?",
    "What organizations or groups have you belonged to?",
    "Have you ever won any special awards or prizes as an adult? What were they for?",
    "Describe a time and a place you remember feeling truly at peace and happy to be alive. Where were you and what were you doing?",
    "What is the most beautiful place you have ever visited and what was it like",
    "What is the longest trip that you have ever gone on? Where did you go",
    "What has been your favorite vacation? Where did you go and why was it special?",
    "What was the favorite place you ever visited and what was it like?",
    "What pets have you had? Do you have a favorite story about a pet?",
    "Is there anything you have always wanted to do but haven't?",
    "Have you ever been to a world's fair?",
    "What is the single most memorable moment of your life?"],
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

    [r'(.*) (computer|bot|robot)(.*)',
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

    [r'(.*) God (.*)',
     ["Tell me more about God.  How do you see God?",
      "What was your relationship with God like?",
      "How deeply do you believe in God?",
      "How does this relate to your feelings on Nature and God?",
      "God is hard to see and seems to be everywhere and nowhere.  What do you think?"]],

    [r'(.*) (lover|girlfriend|boyfriend) (.*)',
     ["Tell me more about your lover.",
      "What was your relationship with your lover like in bed?",
      "How do you feel about your lover cheating on you?",
      "How does this relate to your feelings today?",
      "Good conjugal and amorous relations are important."]],

    [r'(.*) (mother|mom) (.*)',
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does your mom relate to your feelings today?",
      "Good family relations are important - moms set the tone."]],

    [r'(.*) father(.*)',
     ["Tell me more about your father.",
      "How did your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family, or your father?"]],

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