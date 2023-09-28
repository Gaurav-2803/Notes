class Graph:
    def __init__(self, edges):
        self.edges = edges


class directed_graph(Graph):
    def __init__(self, edges):
        super().__init__(edges)

    def create_graph(self):
        graph = {}
        for node, neighbor in self.edges:
            if node not in graph:
                graph[node] = [neighbor]
            else:
                graph[node].append(neighbor)

            if neighbor not in graph:
                graph[neighbor] = []
        return graph


class undirected_graph(Graph):
    def __init__(self, edges):
        super().__init__(edges)

    def create_graph(self):
        graph = {}
        for node, neighbor in self.edges:
            if neighbor == "":
                graph[node] = []
                continue

            if node not in graph:
                graph[node] = [neighbor]
            else:
                graph[node].append(neighbor)

            # if any(map(lambda x: isinstance(neighbor, x), {list, set, tuple})):
            #     for neighbor in graph:
            #         if neighbor not in graph:
            #             graph[neighbor] = [node]
            #         else:
            #             graph[neighbor].append(node)
            # else:
            if neighbor not in graph:
                graph[neighbor] = [node]
            else:
                graph[neighbor].append(node)

        return graph
