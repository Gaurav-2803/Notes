from pprint import *
from graph import undirected_graph


class unweighted_graph(undirected_graph):
    def __init__(self, edges):
        super().__init__(edges)
        self.graph = super().create_graph()

    def has_path_dfs(self, src, dest, visited=set()):
        if src == dest:
            return True

        if src in visited:
            return False

        visited.add(src)
        for neighbor in self.graph.get(src):
            if self.has_path_dfs(neighbor, dest, visited):
                return True
        return False

    def dfs_recursive(self, node, path=set()):
        if node in path:
            return False
        path.add(node)

        for neighbour in self.graph.get(node):
            self.dfs_recursive(neighbour, path)

        return True

    def connected_components_count(self):
        count = 0
        for node in self.graph:
            if self.dfs_recursive(node):
                count += 1
        return count


# edges = [
#     ["i", "j"],
#     ["k", "i"],
#     ["m", "k"],
#     ["k", "l"],
#     ["o", "n"],
# ]
edges = [
    [3, ""],
    [1, 2],
    [4, 6],
    [5, 6],
    [7, 6],
    [8, 6],
]
unw_graph = unweighted_graph(edges)

graph = unw_graph.create_graph()
PrettyPrinter(width=30).pprint(graph)

# src = input("\nSource node : ")
# dest = input("Destination node : ")
# print(f"\nHas path or not from {src} -> {dest}:", unw_graph.has_path_dfs(src, dest))
print("\nConnected Compound Count = ", unw_graph.connected_components_count())
