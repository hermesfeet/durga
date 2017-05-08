import re, random

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

#Filler words are discourse markers
fillers = ["", "Like, ", "Well, ", "Ok. ", "Gotcha. ", "Makes sense. ", "Yup, got it.  ", "Allrighty, ", "Anyway, ", "like, ", "Right. ", "So you know, ", "Fine - ", "Now ", "So... ", "Good! ", "Oh!  Ok. ", "Well... ", "It makes me think... ", "Great - ", "Okay - "]
filler_weights = [0.6, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02 ]



#Transitions for volleys
change_topics = [
    "OK, changing the topic to your ",
    "I want to talk about your ",
    "Let's switch over to your ",
    "Something I was wondering about: your ",
    "So, I was thinking, can we discuss your "

]

#example of a native Python graph
graph_example = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : [],
          "g" : []
        }

#Main volley topics, called life questions.  Need at least 10 per topic, each question should link to 4 others min
#How this works: first letter is key for graph, then the first value item is question, then the second item
#is a list of other graph points/keys that the question could connect to
life_questions = {
    "family":
        {"a":["Who in your family do you now care the most about?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
        "b":["What is the most vivid memory you have of your parents?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "c":["What did your family do for fun when you were a child?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "d":["Who was the most important adult in your life growing up?", [ "b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "e":["What are your mom's pet peeves, or your dad's?", [ "b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "f":["Whom do you love most in your family?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "g":["Did you have a family pet you loved, and what was their story?", [ "b", "c", "d", "e", "f", "g","h", "j", "k"]],
        "h":["Who in your family did you have the hardest time with?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "i":["What got you out of bed as a kid?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "j":["Who protected you as a child?", [ "d", "e", "f", "g","h", "i", "j", "k"]],
        "k":["Could you tell me a story or any memory of your brothers and sisters?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
         },

    "religion":
        {"a":["What religion were your parents?", ["b","c", "d", "e", "f", "h", "i", "j", "k"]],
        "b":["What religion did most of your neighbors or community practice?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "c":["Did you grow up believing in God?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "d":["Were ethics or morals built into your childhood", [ "b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "e":["Do you think God runs the world - why or why not?", [ "b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "f":["Are you an atheist?", ["e", "f", "g","h", "i", "j", "k"]],
        "g":["What do you think or religious people who do bad things?", [ "b", "c", "d", "e", "f", "g","h", "j", "k"]],
        "h":["What do you think or religious people who do really kind and generous things?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "i":["What scared you about angels or demons as a child?", ["f", "g","h", "i", "j", "k"]],
        "j":["Who gave you your faith?", ["d", "e", "f", "g","h", "i", "j", "k"]],
        "k":["Do you have any spiritual or religious beliefs you want to pass on?", ["c", "d", "e", "f", "g","h", "i", "j", "k"]]
         },
    "school":
        {"a":["How did you like school?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
        "b":["Where was school and what did you do there?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "c":["What were your schools like?", ["b", "c", "d", "e", "f", "g","h", "i", "j", "k"]],
        "d":["What was your favorite subject in school and why?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "e":["What subject in school was the easiest for you?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "f":["What was your least favorite subject in school and why?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "g":["Who was your favorite teacher and why was he/she special?", ["b", "c", "d", "e", "f", "h", "i", "j", "h"]],
        "h":["How do your fellow classmates from school remember you best?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "i":["What school activities and sports did you participate in?", ["b", "c", "d", "e", "h", "i", "j", "k"]],
        "j":["Did you and your friends have a special hangout where you liked to spend time?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "k":["Were you ever given any special awards for your studies or school activities?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
        "l":["How many years of education have you completed?", ["b", "c", "d", "e", "f", "p"]],
        "m":["Describe yourself as a young adult.", [ "f", "h", "i", "j", "k"]],
        "n":["Did you attend any school or training after high school - what did you study?", ["d", "e", "f", "h", "i", "j", "k"]],
        "o":["Do you have a college degree(s)?", ["g", "h", "l", "m"]],
        "p":["Did you get good grades?", ["f", "h", "i", "j", "k"]]
    },
    "home":
        {"a":["Where was your first home?", ["c", "d", "e", "f", "h", "i", "k"]],
        "b":["What were your earliest memories of your home?", ["c", "d", "e", "f", "h", "i", "k"]],
        "c":["Were there any fads during your childhood that you remember vividly?", ["b", "c", "d", "e", "f", "g","h", "i", "k"]],
        "d":["Was there a chore you really hated doing as a child?", [ "b", "c", "d", "e", "f", "g","h", "i",  "k"]],
        "e":["What books did you grow up with and love?", [ "c", "d", "e", "f", "g","h", "i", "k"]],
        "f":["Do you remember having a favorite song, cartoon, or TV show growing up?", ["d", "e", "f", "g","h", "i", "k"]],
        "g":["What games did you play the most growing up?", [ "c", "d", "e", "f", "g","h", "k"]],
        "h":["Were there any hard times, like when you didn't have enough food, money, or clothes?", ["e", "f", "g","h", "i", "j", "k"]],
        "i":["What was the most difficult memory growing up?", [ "f", "g","h", "i", "j", "k"]],
        "j":["Did anyone take advantage of you when you were a child?", [ "d", "e", "f", "g","h", "i", "j", "k"]],
        "k":["If there was one thing you could change about your home life growing up, what would it be?", [ "e", "f", "g","h", "i", "j", "k"]]
         },
    "job":
        {"a": ["As a child, what did you want to be when you grew up?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
         "b": ["What were your jobs as a kid, if you had any?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
         "c": ["Tell me about all the jobs you've had!",
               [ "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "d": ["What was your first real job?", ["c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "e": ["Did you ever have a really difficult or challening job - what was it like?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "f": ["What have you learned about a work ethic and reliability along the way?", ["d", "e", "f", "g", "h", "i", "j", "k"]],
         "g": ["What job do you wish everyone should experience?", ["d", "e", "f", "g", "h", "j", "k"]],
         "h": ["Was there a career you ever got on?", [ "e", "f", "g", "h", "i", "j", "k"]],
         "i": ["What job advice would you give young people today?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "j": ["Did you ever see someone badly hurt at work?", [ "h", "i", "e", "k"]],
         "k": ["Who do you know that has the best job in the world, and what is it?", [ "e", "f", "g", "h", "i", "j", "k"]],
        "l": ["Did you ever make enough money to live comfortably?", [ "g", "h", "i", "j", "k"]]
         },

    "partners":
        {"a": ["How old were you when you started dating?", ["c", "d", "e", ]],
         "b": ["Do you remember the first person you ever loved - who was it and describe them?", ["b", "c", "d", "e"]],
         "c": ["Can you tell me who your last 2 lovers were?",
               ["f", "g", "h", "i", "j", "k"]],
         "d": ["Did you ever want to get married in your life?", [ "e", "f", "g", "h", "i", "j", "k"]],
         "e": ["Do you have a spouse now?  If you do, can you tell me about your wedding proposal or first date?", ["e", "f", "g", "h", "i", "j", "k"]],
         "f": ["What did your learn from your parents about dating or marriage?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "g": ["From your own experience or watching others, what advice would you give about long term relationships or marriage?", ["b", "c", "d", "e", "f", "g", "h", "j", "k"]],
         "h": ["Who are the happiest married people you know, and why?", [ "g", "h", "i", "j", "k"]],
         "i": ["Why do you think people get divorced?", [ "f", "g", "h", "i", "j", "k"]],
         "j": ["If you were single now and had to marry a close friend, who would it be?", [ "g", "h", "i", "j", "k"]],
         "k": ["Is marriage even worth it?", ["e", "f", "g", "h", "i", "j", "k"]]
         },


    "health":
        {"a": ["What do you do regularly for exercise?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
         "b": ["Did you have any of the childhood diseases or major problems?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
         "c": ["Did your parents have any major health issues?",
               ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "d": ["Do you have any bad habits now or in the past?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "e": ["Have you ever been in a serious accident?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "f": ["Have you ever been nearly dead - tell me about it?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "g": ["Has anyone ever saved your life?", [ "g", "h", "j", "k"]],
         "h": ["What have you learned about staying healthy or getting sick?", ["c", "d", "g", "h", "i", "j", "k"]],
         "i": ["Do you have any health or eating or exercise advice for others?", ["h", "i", "j", "k"]],
         "j": ["Any major health issues you'd like to share?", ["d", "e", "f", "g", "h", "i", "j", "k"]],
         "k": ["Who is the healthiest person you know, and why?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]]
         },

    "history":
        {"a": ["What do you think was the most important historical event in your life?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
         "b": ["Do you remember your family discussing world events and politics?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
         "c": ["How is the world different from what it was like when you were a child?",
               ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "d": ["What would you consider the most important inventions during your lifetime?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "e": ["How would you describe yourself politically? Are you conservative or liberal, and why?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "f": ["How did hard times like depressions and recessions affect you and your family?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "g": ["What wars have happened in your life - and did you take part in any?", ["b", "c", "d", "e", "f", "g", "h", "j", "k"]],
         "h": ["Who was the most important historical figure you followed in your life, and why?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "i": ["Have you ever been the victim of a serious crime?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "j": ["What event in the past has left you with the most sad or bitter memories?", ["d", "e", "f", "g", "h", "i", "j", "k"]],
         "k": ["What do you think about the future, having lived so many years?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]]
         },

    "friends":
        {"a": ["Name a good friend you have known the longest. How many years have you been friends?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
         "b": ["Who was your best friend growing up?  Tell me about them.", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
         "c": ["What person really changed the course of your life by something he/she did?",
               ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "d": ["Has there ever been anyone in your life you would consider a kindred spirit or soul mate? Who was this and why did you feel a special bond?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "e": ["Have you ever had to let go of a friend?", [ "f", "g", "h", "i", "j", "k"]],
         "f": ["Have you ever had a pet or animal as a close friend, and what was the story?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "g": ["Has a good friend ever betrayed you?", ["g", "h", "j", "k"]],
         "h": ["Have you ever done something dumb to lose a good friend?", [ "f", "g", "h", "i", "j", "k"]],
         "i": ["What's the worst thing a friend ever did to you?", [ "f", "g", "h", "i", "j", "k"]],
         "j": ["What advice would you give to others about friendship?", ["f", "g", "h", "i", "j", "k"]],
         "k": ["Which group of friends have been the most important to you?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]]
         },


    "moments":
        {"a": ["What are your hobbies?", ["c", "d", "e", "f",  "j", "k","l"]],
         "b": ["What do you do the most when not working?", ["b", "c", "d", "e", "f",  "j", "k"]],
         "c": ["What is the most amazing thing that has ever happened to you?",
               ["b", "c", "d", "e", "f", "g",  "j", "k"]],
         "d": ["Would you consider yourself creative?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l"]],
         "e": ["Did you ever play musical instruments or make art?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "f": ["If you could change something about yourself, what would it be?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
         "g": ["What is the most stressful experience you ever lived through?", ["b", "c", "d", "e", "f", "g", "h", "j", "k", "l"]],
         "h": ["What is the scariest thing that ever happened to you?", [ "g", "h", "i", "j", "k"]],
         "i": ["What things have you made that others have enjoyed?", [ "f", "g", "h", "i", "j", "k","l"]],
         "j": ["Have you ever met any famous people?", ["d", "e", "f", "g", "h", "i", "j", "k"]],
        "k": ["How would you describe your sense of humor?", ["d", "e", "f", "g", "h", "i", "j", "k"]],
         "l": ["Do you remember any advice or comments that had a big impact on how you lived your life?", ["b", "c", "d", "e", "f", "g", "j", "k"]]
         },

    "choices":
{"a": ["How do you feel about the choices you made in school, career, spouse?", ["c", "d", "e", "f", "h", "i", "j", "k"]],
 "b": ["What is the longest trip that you have ever gone on? Where did you go?", ["b", "c", "d", "e", "f", "h", "i", "j", "k"]],
 "c": ["What is the single most memorable moment of your life?",
       ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
 "d": ["What organizations or groups have you belonged to?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
 "e": ["Have you ever won any special awards or prizes as an adult? What were they for?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
 "f": ["Describe a time and a place you remember feeling truly at peace and happy to be alive. Where were you and what were you doing?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
 "g": ["Is there anything you have always wanted to do but haven't?", ["b", "c", "d", "e", "f", "g", "h", "j", "k"]],
 "h": ["What was the favorite place you ever visited and what was it like?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
 "i": ["What is the most beautiful place you have ever visited and what was it like?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]],
 "j": ["What has been your favorite vacation? Where did you go and why was it special?", ["d", "e", "f", "g", "h", "i", "j", "k"]],
 "k": ["What is the best decision rule you have for making choices that you want to share?", ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]]
 }
}

#Need to find a way to re-insert question about kids ONLY IF the kids module activates?
"""
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
    "What advice would you give/did you give to your child or grandchild on his/her wedding day?"
"""

# Take the user's 1st person input and process as a Regex, return the bot's response as 2nd person

def test_analyze(statement):
    for pattern, responses in topics:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response

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

if __name__ == '__main__':
    input = raw_input("Tell me something:")
    response = test_analyze(input)
    print response