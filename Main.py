from .matrix import *

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

graph = Graph.create_from_nodes([a, b, c, d, e, f])
graph.print()
print()
graph.connect(a, b, 5)
graph.connect(a, c, 10)
graph.connect(a, e, 2)
graph.connect(b, c, 2)
graph.connect(b, d, 4)
graph.connect(c, d, 7)
graph.connect(c, f, 10)
graph.connect(d, e, 3)
graph.print()

graph.dijkstra(a)
graph.print_dijkstra()
