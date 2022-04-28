import networkx as nx
from networkx.generators import *
import matplotlib.pyplot as plt

## GENERATE NETWORK
n=20       ## number of nodes
p=0.5      ## link probability
G=binomial_graph(n,p)

## DEGREE DISTRIBUTION
deg = [0 for i in range(n)]
for i in range(n):
    deg[G.degree[i]] = deg[G.degree[i]]+1

print("Degree counts: ",end=" ")
for i in range(n):
    print(deg[i],end=" ")
print("\nDegree distribution: ",end=" ")
for i in range(n):
    print(deg[i]/n,end=" ")
    

## PLOTTING
pos = nx.random_layout(G)
nx.draw(G,pos,node_size=10,node_color='red',edge_color='grey')
plt.show()