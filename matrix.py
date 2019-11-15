class Node:

    def __init__(self, name, indexloc=None):
        self.name = name
        self.index = indexloc


class Graph:

    @classmethod
    def create_from_nodes(cls, nodes):
        return Graph(len(nodes), len(nodes), nodes)

    def __init__(self, row, col, nodes=None):
        self.dijkstra_distance = None
        self.adj_mat = []
        for i in range(row):
            self.adj_mat += [[0] * col]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

    def connect(self, n1, n2, weight=1):
        self.write_connection(n1, n2, weight)
        self.write_connection(n2, n1, weight)

    def write_connection(self, node1, node2, weight):
        self.adj_mat[node1.index][node2.index] = weight

    def print(self):
        for row in self.adj_mat:
            print(row)

    def connections_from(self, node):
        # result = [None]
        # for col in range(len(self.adj_mat[node.index])):
        #     if self.adj_mat[node.index][col] != 0:
        #         result += [(self.nodes[node.index], self.adj_mat[node.index][col])]
        # return result
        return [(self.nodes[col_num], self.adj_mat[node.index][col_num]) for col_num in range(len(self.adj_mat[node.index])) if
                self.adj_mat[node.index][col_num] != 0]

    def print_dijkstra(self):
        for path in self.dijkstra_distance:
            print(path)

    def dijkstra(self, start_node):
        distance = [None] * len(self.nodes)
        print(distance)
        for i in range(len(distance)):
            distance[i] = [float("inf")]
            distance[i].append([self.nodes[start_node.index].name])
        print(distance)
        distance[start_node.index][0] = 0
        print(distance)
        # Hier ligt das problem es gibt nur eine Reference
        queue = [i for i in self.nodes]
        seen = set()
        while len(queue) > 0:
            smalest_dist = float("inf")
            smalest_dist_node = None
            for n in queue:
                if distance[n.index][0] < smalest_dist and n not in seen:
                    smalest_dist = distance[n.index][0]
                    smalest_dist_node = n
            queue.remove(smalest_dist_node)
            seen.add(smalest_dist_node)

            connections = self.connections_from(smalest_dist_node)
            print(connections)
            for (node, weight) in connections:
                tot_dist = weight + smalest_dist
                if tot_dist < distance[node.index][0]:
                    distance[node.index][0] = tot_dist
                    distance[node.index][1] = list(distance[smalest_dist_node.index][1])
                    distance[node.index][1].append(node.name)
        self.dijkstra_distance = distance
        return distance
