import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

"""#Florentine Families Graph"""

floren_families = nx.florentine_families_graph()

plt.figure(figsize=(5,5))
nx.draw(floren_families, node_size=40, font_size=10, with_labels=True)
plt.show()

deg_centrality = nx.degree_centrality(floren_families)
ev_centrality = nx.eigenvector_centrality(floren_families)
cn_centrality = nx.closeness_centrality(floren_families)
btwn_centrality = nx.betweenness_centrality(floren_families)

print('Degre Centrality: ', deg_centrality)
print('Eigenvector Centrality: ', ev_centrality)
print('Closeness Centrality: ', cn_centrality)
print('Betweenness Centrality: ', btwn_centrality)

graph_transitivity = nx.transitivity(floren_families)
graph_clustering = nx.average_clustering(floren_families)

print('Transitivity: ', graph_transitivity)
print('Clustering Coefficient: ', graph_clustering)

"""#Fast Gnp Random Graph
References: *https://networkx.org/documentation/stable/reference/generated/networkx.generators.random_graphs.fast_gnp_random_graph.html*
"""

N = 50
p = 0.2
G = nx.fast_gnp_random_graph(N, p, seed=42, directed=False)
plt.figure(figsize=(8,8))
nx.draw(G, node_size=40, font_size=10, edge_color='grey', with_labels=True)
plt.show()

deg_centrality = nx.degree_centrality(G)
ev_centrality = nx.eigenvector_centrality(G)
cn_centrality = nx.closeness_centrality(G)
btwn_centrality = nx.betweenness_centrality(G)

graph_transitivity = nx.transitivity(G)
graph_clustering = nx.average_clustering(G)

print('Degre Centrality: ', deg_centrality)
print('Eigenvector Centrality: ', ev_centrality)
print('Closeness Centrality: ', cn_centrality)
print('Betweenness Centrality: ', btwn_centrality)
print('Transitivity: ', graph_transitivity)
print('Clustering Coefficient: ', graph_clustering)

"""#Scale Free Graph"""

n = 50
graph = nx.scale_free_graph(n)
plt.figure(figsize=(6,5))
nx.draw(graph, node_size=40, font_size=10, edge_color='grey', with_labels=True)
plt.show()

in_deg_centrality = nx.in_degree_centrality(graph)
out_deg_centrality = nx.out_degree_centrality(graph)
cn_centrality = nx.closeness_centrality(graph)
btwn_centrality = nx.betweenness_centrality(graph)

print('In-Degre Centrality: ', in_deg_centrality)
print('Out-Degre Centrality: ', out_deg_centrality)
print('Closeness Centrality: ', cn_centrality)
print('Betweenness Centrality: ', btwn_centrality)

page_rank = nx.pagerank(graph)
print('Page Rank: ', page_rank)

# Convert the multigraph to a simple graph
simple_graph = nx.Graph(graph)

# Calculate clustering coefficient on the simple graph
graph_clustering = nx.average_clustering(simple_graph)
print('Clustering Coefficient: ', graph_clustering)
graph_transitivity = nx.transitivity(simple_graph)
print('Transitivity: ', graph_transitivity)

"""#Comments
1. Centrality Distributions:
- The Florentine Families graph shows a clear difference in centrality between nodes
- The Fast Gnp Random graph shows a more uniform distribution.
- The Scale-Free graph exhibits a highly skewed distribution in in-degree and PageRank, highlighting a few very central nodes and many nodes with low centrality.

2. Betweenness Centrality:
- The Florentime Families graph shows higher and more varied values, indicating that more node lies on the shortest paths and hence more access to information.
- The Fast Gnp Random graph show lower values and hence less flow of information among the nodes.
- In the Scale-Free graph, the high degree nodes dominate the shortest paths which leads to lower betweenness for other nodes.

3. Transitivity and Clustering Coefficient:
- The Florentine Families graph has a noticeably higher clustering coefficient (0.16) and transitivity (0.19) than the Fast Gnp Random graph (clustering ~0.19, transitivity ~0.20) and the Scale-Free graph (clustering ~0.16, transitivity ~0.08).
- It indicates that the Florentime Families graph has more number of triangles and denser local neighborhoods compared to the more random & scale-free networks.
"""
