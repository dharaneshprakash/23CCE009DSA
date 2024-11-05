import matplotlib.pyplot as plt
import networkx as nx

def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph}
    distance[source] = 0
    
    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
    
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")
    
    return distance

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}

source_node = 'A'
try:
    distances = bellman_ford(graph, source_node)
    print("Shortest distances from source node:", distances)
except ValueError as e:
    print(e)

G = nx.DiGraph()
for u in graph:
    for v, weight in graph[u]:
        G.add_edge(u, v, weight=weight)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))

nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
nx.draw_networkx_edges(G, pos, edgelist=G.edges, arrowstyle='->', arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")

edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graph Visualization with Weights")
plt.show()