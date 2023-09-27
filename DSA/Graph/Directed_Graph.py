# from pprint import *
# PrettyPrinter(width=20).pprint(self.graph)
from queue import LifoQueue, SimpleQueue


class acyclic_graph:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.node = start_node

    def dfs_iterative(self):
        stack = LifoQueue()
        stack.put(self.node)

        while not stack.empty():
            curr_node = stack.get()
            print(curr_node, end=", ")
            if curr_node not in self.graph:
                continue
            for node in self.graph.get(curr_node):
                stack.put(node)

    def dfs_recursive(self, node, path=[]):
        if node not in path:
            path.append(node)

            if node not in self.graph:
                # leaf node, backtrack
                return path

            for neighbour in self.graph.get(node):
                path = self.dfs_recursive(neighbour, path)

        return path

    def bfs_iterative(self):
        queue = SimpleQueue()
        queue.put(self.node)

        while not queue.empty():
            curr_node = queue.get()
            print(curr_node, end=", ")
            if curr_node not in self.graph:
                continue
            for next_node in self.graph.get(curr_node):
                queue.put(next_node)

    def bfs_recursive(self):
        pass


graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
}

acgraph_obj = acyclic_graph(graph, "a")

print("DFS:")
acgraph_obj.dfs_iterative()
print("\n", acgraph_obj.dfs_recursive("a"))


print("\nBFS:")
acgraph_obj.bfs_iterative()
# print("\n", acgraph_obj.bfs_recursive("a"))
