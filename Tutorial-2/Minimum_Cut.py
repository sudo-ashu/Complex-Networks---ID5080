#Tutorial 2

#Perform the following operations
#- Draw the network
#- Plot the adjacency matrix
#- Compute the Laplacian matrix and plot
#- Partition the graph using the spectral bisection algorithm
#- Compute the cut size of the graph

import numpy as np
import networkx as nx
import seaborn as sns
import matplotlib.pyplot as plt
import random
import math
import pandas as pd

adj_mat = np.loadtxt('/content/graph_partition_dataset_2')
adj_mat

plt.imshow(adj_mat, cmap='viridis')
plt.axis('off')
plt.show()

Graph = nx.from_numpy_array(adj_mat)

plt.figure(figsize=(4,4))
nx.draw(Graph, with_labels=True, node_color="skyblue", node_size=40, font_size=10)
plt.show()

d = [Graph.degree(n) for n in Graph.nodes()] #calculates degree of each node
L_mat = np.diag(d) - adj_mat #laplacian matrix
L_mat

from numpy.linalg import eigh
eigenvalues, eigenvectors = eigh(L_mat)
print('Eigen values', eigenvalues)
print('Eigen vectors', eigenvectors)

# getting Fiedler vectors
v = eigenvectors[:,1] #vector corresponding to 2nd smallest eigenvalue
print(v)

partitionA = [node for i, node in enumerate(Graph.nodes()) if v[i] > 0]
partitionB = [node for i, node in enumerate(Graph.nodes()) if v[i] <= 0]
print(f"Partition A: {partitionA}")
print(f"Partition B: {partitionB}")

cut_size = 0
for a, b in Graph.edges():
  if (a in partitionA and b in partitionB) or (a in partitionB and b in partitionA):
    cut_size += 1
print(f'Cut size: {cut_size}')

node_colors = []
for node in Graph.nodes():
  if node in partitionA:
    node_colors.append('red')
  else:
    node_colors.append('blue')

plt.figure(figsize=(4,4))
nx.draw(Graph, with_labels=True, node_color=node_colors, edge_color="gray", node_size=40, font_size=10)
plt.show()
