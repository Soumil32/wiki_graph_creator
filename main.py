from graph_tool.all import *

g = Graph()

v1 = g.add_vertex()
v2 = g.add_vertex()
e = g.add_edge(v1, v2)

print("Vertices:", g.num_vertices())