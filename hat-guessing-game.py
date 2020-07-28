# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:52:57 2020
Each color is marked as a number.
@author: GeighZ
"""
import networkx as nx
from random import randint


g = nx.Graph()

numOfNodes = 10

for node in range(0,numOfNodes):
    g.add_node(node, color=randint(0,numOfNodes))
    
for nodeIn in range(0,numOfNodes):
    for nodeOut in range(nodeIn+1,numOfNodes):
        g.add_edge(nodeIn,nodeOut);


#nx.draw(G)
print(g.number_of_edges())
nx.draw(g);


