import json

from py2neo import Node, Relationship, Graph
from database import Utterance, Speaker, Volley, get_graph_object
import hashlib

g = get_graph_object()

# turn is computer asks, human responds
# utterance is a half turn, the message from just one side

def log_utterance(input, speaker, volley, ts, last_id):
    #Log the new utterance as a node
    tx = g.begin(autocommit=False)

    new_utterance = Node("Utterance", id=last_id)
    new_utterance['ts'] = ts
    new_utterance['input'] = input
    tx.create(new_utterance)
    get_cl()
    tx.commit()
    print('Added: Utterance: {0}'.format(new_utterance))
    return id

    #Creates a relationship from the current utterance to the last utterance
    last_utterance = g.find_one(label='Utterance', property_key='id', property_value=last_id)
    new_relationship = Evokes(last_utterance, new_utterance)
    tx = g.begin(autocommit=False)
    tx.create(new_relationship)
    tx.commit()

    #Create a relationship from the utterance to a speaker
    speaker = find_or_create_speaker(speaker)
    new_speakership = Said(speaker, new_utterance)
    tx = g.begin(autocommit=False)
    tx.create(new_speakership)
    tx.commit()

    # Create a relationship from the utterance to the volley
    volley = find_or_create_speaker(speaker)
    new_volleyship = Regards(new_utterance, volley)
    tx = g.begin(autocommit=False)
    tx.create(new_volleyship)
    tx.commit()

def find_or_create_speaker(speaker_name):
    #Returns the node of the speaker, or creates and saves one if it doesn't exist
    speaker = g.find_one(label='speaker', property_key='name', property_value=speaker_name)
    if not speaker:
        speaker = Node("Speaker", name=speaker_name)
        tx = g.begin(autocommit=False)
        tx.create(speaker)
        tx.commit()
    return speaker

def find_or_create_volley(volley):
    #Returns the node of the volley, or creates and saves one if it doesn't exist
    volley = g.find_one(label='volley', property_key='name', property_value=volley)
    if not volley:
        volley = Node("Volley", name=volley)
        tx = g.begin(autocommit=False)
        tx.create(volley)
        tx.commit()
    return volley


def get_cl():
    """
    Gets a command line, for debugging
    :return:
    """
    import code
    import readline

    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    shell.interact()


if __name__ == '__main__':
    """
    Move data from the JSON file to the graph db.
    """
    log_utterance("I said test this", "Moroni", "Death", "Monday eves", "1214")


