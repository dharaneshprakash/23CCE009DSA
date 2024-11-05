import networkx as nx
import matplotlib.pyplot as plt

# Function to create an undirected graph with weighted edges based on user input
def create_graph():
    graph = nx.Graph()
    num_edges = int(input("Enter the number of edges: "))
    print("Enter each edge with the format 'node1 node2 weight' (e.g., 'A B 3'):")
    for _ in range(num_edges):
        u, v, w = input().split()
        w = int(w)
        graph.add_edge(u, v, weight=w)
    return graph

# Prim's Algorithm for MST
def prim_mst(graph, start_node):
    mst_edges = []
    visited = set([start_node])
    edges = [(data['weight'], start_node, neighbor) for neighbor, data in graph[start_node].items()]
    edges = sorted(edges)  # Initialize edges sorted by weight

    while edges:
        weight, u, v = edges.pop(0)
        if v not in visited:
            visited.add(v)
            mst_edges.append((u, v, weight))
            for neighbor, data in graph[v].items():
                if neighbor not in visited:
                    edges.append((data['weight'], v, neighbor))
            edges.sort()  # Re-sort edges after adding new ones

    return mst_edges

# Kruskal's Algorithm for MST
def kruskal_mst(graph):
    mst_edges = []
    edges = sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])
    parent = {node: node for node in graph.nodes}

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(u, v):
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v

    for u, v, data in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, data['weight']))

    return mst_edges

# Visualizing the MST
def visualize_mst(graph, mst_edges, title):
    pos = nx.spring_layout(graph)
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10)
    nx.draw_networkx_edges(graph, pos, edgelist=[(u, v) for u, v, _ in mst_edges], edge_color="blue", width=2)
    edge_labels = {(u, v): w for u, v, w in mst_edges}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

# Main function to execute MST algorithms
def main():
    graph = create_graph()
    start_node = input("Enter the starting node for Prim's Algorithm: ")

    # Run Prim's and Kruskal's algorithms
    prim_edges = prim_mst(graph, start_node)
    kruskal_edges = kruskal_mst(graph)

    print("\nPrim's MST edges:", prim_edges)
    print("\nKruskal's MST edges:", kruskal_edges)

    # Visualize the results
    print("\nVisualizing Prim's MST:")
    visualize_mst(graph, prim_edges, "Prim's MST")

    print("\nVisualizing Kruskal's MST:")
    visualize_mst(graph, kruskal_edges, "Kruskal's MST")

main()