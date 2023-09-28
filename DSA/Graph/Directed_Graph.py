from pprint import *
from queue import LifoQueue, SimpleQueue
from graph import directed_graph


class acyclic_graph(directed_graph):
    def __init__(self, edges, start_node):
        super().__init__(edges)
        self.graph = super().create_graph()
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

    def has_path_dfs(self, src, dest):
        if src == dest:
            return True
        for neighbor in self.graph.get(src):
            if self.has_path_dfs(neighbor, dest):
                return True
        return False

    def has_path_bfs(self, src, dest):
        queue = SimpleQueue()
        queue.put(src)

        while not queue.empty():
            curr_node = queue.get()
            if curr_node == dest:
                return True
            for next_node in self.graph.get(curr_node):
                queue.put(next_node)
        return False


edges = [
    ["a", "b"],
    ["a", "c"],
    ["b", "d"],
    ["c", "e"],
    ["d", "f"],
]

acgraph = acyclic_graph(edges, "a")

print("Graph: ")
PrettyPrinter(width=20).pprint(acgraph.create_graph())

print("\nDFS:")
acgraph.dfs_iterative()
print("\n", acgraph.dfs_recursive("a"))

print("\nBFS:")
acgraph.bfs_iterative()

src = input("\n\nSource node : ")
dest = input("Destination node : ")
print(f"\nHas path or not from {src} -> {dest}:", acgraph.has_path_dfs(src, dest))
print(f"Has path or not from {src} -> {dest}:", acgraph.has_path_bfs(src, dest))
