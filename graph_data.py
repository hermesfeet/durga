from graph import Graph

g = { "a" : ["d", "e"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }


graph = Graph(g)

print("Vertices of graph:")
print(graph.vertices())

print("Edges of graph:")
print(graph.edges())


print('The path from vertex "a" to vertex "b":')
path = graph.find_path("a", "b")
print(path)

print('The path from vertex "a" to vertex "f":')
path = graph.find_path("a", "f")
print(path)

print('The path from vertex "c" to vertex "c":')
path = graph.find_path("c", "c")
print(path)

print('All paths from vertex "d" to vertex "b":')
path = graph.find_all_paths("d", "b")
print(path)

print("density of graph")
print(graph.density())

print("Is graph connected?")
print(graph.is_connected())
