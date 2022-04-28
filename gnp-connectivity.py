import networkx as nx
from networkx.generators import *
import math
import matplotlib.pyplot as plt

## GENERATE NETWORK
n=20       ## number of nodes
p=.7/n    ## link probability (no giant)
## p=3/n    ## link probability (giant)
## p=3*math.log(n)/n    ## link probability (connected)

G=binomial_graph(n,p)

## CONNECTED COMPONENTS
print("Network on ",n," nodes, edge probability ",p)
print("The network has ",nx.number_connected_components(G)," components")

## PLOTTING (no layout given, it will use spring layout by default)
nx.draw(G,node_size=10,node_color='red',edge_color='grey')
plt.show()