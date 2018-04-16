# Jules - a Chit-Chatbot (Project Name Durga)

PURPOSE
Jules is a chatbot that talks to older people and asks them questions about their life, to record their stories, wisdom, and thoughts for younger generations

Jules.py is the main file to run in Python.
Knowledge.py has her brain and database.

DEPENDENCIES
See the Requirements.txt file.
Mostly NLTK and Numpy.

STUFF TO DO NEXT - DEV TIMELINE

-More state management: don't repeat volleys (keep track of them) \n
-Small talk module \n
    -(questions people commonly ask bots) - short rsponse or tell a story from the bank \n
-Update memory module - \n
    -ST Memory - what was recently said, context, name, volley count, PPT count to dig in, what sentences or volleys to not repeat \n
    -LT Memory - User profile, Bot profile of itself, PPT triples of what was discussed \n
-KB1: Record user answers in a KB as a set of triples (Name, verb, adjective/descriptor) \n
-KB3: Bot personality \n
-Jokes function module - weighted low, based on what someone says, takes a diff versus a jokes database and returns one \n
-Function after some time to go to LT memory and dig into user profile or PPT triples \n
-Emotional state (analyze sentiment of last 5-15 user statements, map to 7 main emotions and store in memory, and create fillers and language to mirror \n
    -Use textblob for sentiment analysis on laste 20 statements in memory, also for last statment to pick the filler \n
    -https://pypi.python.org/pypi/textblob \n
    -Empathic statements \n
-Movie lines and famous quotes - take a user string, do a diff and match it to a movie quote or pithy quote \n
-Upgrade topics with common things said in chats \n
-Current news - ask them if there's something current (sports, politics, etc) that has been on their mind, then do a Google News scraper search and ask them 1-2 follow up qs \n

Go over Chatscript documents - how does it work, what to learn?

CORPORA TO CHECK OUT:
http://www.linguistics.ucsb.edu/research/santa-barbara-corpus#SBC008 \n
http://courses.washington.edu/englhtml/engl560/corplingresources.htm \n
https://www.microsoft.com/en-us/download/details.aspx?id=52375&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F6096d3da-0c3b-42fa-a480-646929aa06f1%2F \n
https://people.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html \n
https://chenhaot.com/pages/changemyview.html \n
http://faculty.nps.edu/cmartell/NPSChat.htm \n
http://corpus.byu.edu/overview.asp \n
