# Jules - A Chit-Chatbot for Seniors (Project Name Durga)

![Alt text](conversation.png?raw=true "Conversation")

## What It Does
Jules is a chatbot that talks to seniors and asks them questions about their life, to record their stories, wisdom, and thoughts for younger generations.

I loosely based on her an older Eliza module, updated to ask life questions and dig even deeper into a user's statements.  Here is the [Original Eliza paper](http://web.stanford.edu/class/cs124/p36-weizenabaum.pdf) and some [recent research on chatbots (Jurafsky).](http://web.stanford.edu/~jurafsky/slp3/29.pdf)

## Running the App
Jules.py is the main file to run in Python.  So in bash, cd over to the folder and run:
> python jules.py

Knowledge.py has her brain and database.

## Built With / Dependencies
Built in Python 3.6. See the Requirements.txt file.
Mostly regex, NLTK, time, and collections.  

## Built With / Dependencies
Version 1.6 - moved to Python3 and integrated question follow-on.

## Dev Timeline - Next To Do
- More state management: don't repeat volleys (keep track of them)
- Small talk module (questions people commonly ask bots) - short rsponse or tell a story from the bank
- Update memory module with ST Memory (what was recently said, context, name, volley count, PPT count to dig in, what sentences or volleys to not repeat) and LT Memory (User profile, Bot profile of itself, PPT triples of what was discussed) 
- KB1: Record user answers in a KB as a set of triples (Name, verb, adjective/descriptor) 
- KB3: Bot personality 
- Jokes function module - weighted low, based on what someone says, takes a diff versus a jokes database and returns one 
- Function after some time to go to LT memory and dig into user profile or PPT triples 
- Emotional state (analyze sentiment of last 5-15 user statements, map to 7 main emotions and store in memory, and create fillers and language to mirror. Use textblob for sentiment analysis on laste 20 statements in memory, also for last statment to pick the filler.  https://pypi.python.org/pypi/textblob.  Empathic statements 
- Movie lines and famous quotes - take a user string, do a diff and match it to a movie quote or pithy quote 
- Upgrade topics with common things said in chats
- Current news - ask them if there's something current (sports, politics, etc) that has been on their mind, then do a Google News scraper search and ask them 1-2 follow up qs
- Go over Chatscript documents - how does it work, what to learn?

## License
This project is licensed under the MIT License.

Copyright 2019 - HermesFeet

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Appendix - Corpora to Check Out
- [A Survey of Available Corpora for Building Data-Driven Dialogue Systems - UM Paper] (https://arxiv.org/pdf/1512.05742.pdf)
- [Dialogue Datasets] (https://breakend.github.io/DialogDatasets/)
- [SEMAINE Sensitive Virtual Agent database] (https://semaine-db.eu/)
- [Switchboard Telephone Corpus] (http://groups.inf.ed.ac.uk/switchboard/overview.html)
- [CallHome Corpus of family conversation] (https://talkbank.org/access/CABank/CallHome/eng.html)
- [Soap opera dialogue corpus] (https://corpus.byu.edu/soap/)
- [Pair conversation corpus] (Conversation Dialog Corpus)
- [UCSB Corpus](http://www.linguistics.ucsb.edu/research/santa-barbara-corpus#SBC008)
- [UW Corpus](http://courses.washington.edu/englhtml/engl560/corplingresources.htm)
- [Microsoft Research](https://www.microsoft.com/en-us/download/details.aspx?id=52375&from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fdownloads%2F6096d3da-0c3b-42fa-a480-646929aa06f1%2F  "MSFT Research")
- [Cornell Movie Corpus](https://people.mpi-sws.org/~cristian/Cornell_Movie-Dialogs_Corpus.html  "Cornell Movie Corpus")
- [Change my view dataset](https://chenhaot.com/pages/changemyview.html  "Change my View persuasion dataset")
- [NPS online posts](http://faculty.nps.edu/cmartell/NPSChat.htm  "NPS online post chat corpus")
- [BYU Corpus](http://corpus.byu.edu/overview.asp "BYU Corpus")
- [COCA Spoken Corpus] (https://corpus.byu.edu/coca/)
- [NUS Corpus] (https://github.com/kite1988/nus-sms-corpus)
- [Other spoken corpora] (http://martinweisser.org/corpora_site/spoken_corpora.html)
- [Intimate Discourse book] (https://www.amazon.com/Investigating-Intimate-Discourse-Exploring-interaction)

