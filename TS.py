import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (e.g., A B for an edge from A to B):")
    for _ in range(num_edges):
        u, v = input().split()
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    return graph
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()
def visualize_graph(graph):
    G = nx.DiGraph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)
    plt.figure(figsize=(10, 6))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    plt.title("Directed Graph Visualization")
    plt.show()
def main():
    graph = create_graph()
    print("\nGraph created successfully.")
    start_node = input("Enter the starting node for traversal: ")
    print("\nDFS Traversal:")
    dfs(graph, start_node)
    print("\n\nBFS Traversal:")
    bfs(graph, start_node)
    print("\nVisualizing the Graph:")
    visualize_graph(graph)
main()