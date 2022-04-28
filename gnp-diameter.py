import networkx as nx
from networkx.generators import *
import math
import matplotlib.pyplot as plt


for r in range(10):
    ## GENERATE NETWORK
    G=binomial_graph(50,0.5)

    ## CONNECTED COMPONENTS
    print("The network's diameter is  ",nx.diameter(G))
