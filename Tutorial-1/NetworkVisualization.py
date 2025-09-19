
#NETWORK-1

import numpy as np
import networkx as nx
from networkx.algorithms import bipartite
import seaborn as sns
import matplotlib.pyplot as plt
import random
import math
import pandas as pd

graph = nx.read_gml('INSERT A GML FILE HERE')

plt.figure(figsize = (10, 8))
pos = nx.kamada_kawai_layout(graph)
nx.draw(graph, pos, node_size = 15, width = 0.5, edge_color = 'gray')

plt.figure(figsize=(10,8))
pos = nx.circular_layout(graph)
nx.draw(graph, pos, node_size=15, width=0.5, edge_color='gray')

degrees = [graph.degree(n) for n in graph.nodes()]
plt.figure(figsize=(10, 6))
plt.hist(degrees, alpha=0.7, rwidth=0.8)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

A = nx.adjacency_matrix(graph)
A
print(A)

#NETWORK-2

excel_file = pd.ExcelFile('/content/lake_of_the_woods.xls') ## you can get this on the internet

df = excel_file.parse(excel_file.sheet_names[0])
data_df = df.iloc[2:].copy()
data_df.columns = ['Host species', 'Sample size'] + df.columns[2:].tolist()
set1_nodes = data_df['Host species'].dropna().unique().tolist()
set2_nodes = data_df.columns[2:].tolist()

edgelist = []
for i, row in data_df.iterrows():
    node1 = row['Host species']
    if pd.notna(node1):
        for node2 in set2_nodes:
            weight = row[node2]
            if pd.notna(weight) and weight != 0:
                edgelist.append((node1, node2, {'weight': weight}))

bipartite_graph = nx.Graph()
bipartite_graph.add_nodes_from(set1_nodes, bipartite=0)
bipartite_graph.add_nodes_from(set2_nodes, bipartite=1)
bipartite_graph.add_edges_from(edgelist)


print(f"nodes: {bipartite_graph.number_of_nodes()}")
print(f"edges: {bipartite_graph.number_of_edges()}")
set_1, set_2 = bipartite.sets(bipartite_graph)
print(f"set 1: {len(set_1)}")
print(f"set 2: {len(set_2)}")

pos = nx.drawing.layout.bipartite_layout(bipartite_graph, set1_nodes)
plt.figure(figsize = (10, 8))
nx.draw(bipartite_graph, pos, node_size = 5, width = 0.1, edge_color = 'gray')
plt.show()

A_bipartite = nx.adjacency_matrix(bipartite_graph)
print(A_bipartite)

A_bipartite_tranpose = A_bipartite.T
print(A_bipartite_tranpose)
