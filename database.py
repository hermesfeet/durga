from py2neo.ogm import RelatedFrom, Property, GraphObject, RelatedTo
from py2neo import Graph, Relationship

# from py2neo.packages.httpstream import http
# http.socket_timeout = 1000 * 60 * 5


# g = Graph(
#     bolt_port=7687,
#     https_port=7474,
#     bolt=True,
#     secure=True,
#     host='54.201.4.121',
#     user='neo4j',
#     password='julesrules')
#
environment = 'production'

def get_graph_object():
    if environment == 'production':
        g = Graph(
                bolt_port=7687,
                https_port=7474,
                bolt=True,
                secure=True,
                host='54.201.4.121',
                user='neo4j',
                password='julesrules')
    elif environment == 'local':
        g = Graph(
                bolt_port=7687,
                https_port=7473,
                bolt=True,
                secure=False,
                host='localhost',
                user='neo4j',
                password='passwordhere')
    return g


class Utterance(GraphObject):
    __primarykey__ = "id"

    name = Property()

    evokes = RelatedTo("Utterance", "EVOKES")  #related to means this node has a relation going outward
    evoked_by = RelatedFrom("Utterance", "EVOKES")
    said_by = RelatedFrom("Speaker", "SAID")
    regards = RelatedTo("Volley", "REGARDS")


class Speaker(GraphObject):
    __primarykey__ = "name"

    name = Property()

    said = RelatedTo("Utterance", "SAID")

class Volley(GraphObject):
    __primarykey__ = "name"

    name = Property()

    concerns = RelatedFrom("Utterance", "REGARDS")



class Evokes(Relationship):
    pass

class Said(Relationship):
    pass

class Regards(Relationship):
    pass

if __name__ == '__main__':
    import code
    import readline
    from py2neo import watch

    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    shell.interact()