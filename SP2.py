import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def floyd_warshall(graph):
    nodes = list(graph.keys())
    distance = np.full((len(nodes), len(nodes)), float('inf'))
    
    for i, u in enumerate(nodes):
        distance[i][i] = 0
        for v, weight in graph[u]:
            j = nodes.index(v)
            distance[i][j] = weight
            
    for k in range(len(nodes)):
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    
    return distance, nodes

graph = {
    'A': [('B', 3), ('C', 8), ('D', 5)],
    'B': [('C', 2), ('D', 1)],
    'C': [('D', 7)],
    'D': []
}

distance_matrix, nodes = floyd_warshall(graph)
print("Shortest distance matrix:")
print(distance_matrix)

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