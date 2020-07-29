# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:52:57 2020
Each color is marked as a number.
This program will guarantee that there will always be a correct guess in a group,
all other guesses will be incorrect.
@author: GeighZ
"""
import networkx as nx
from random import randint
import collections

g = nx.Graph()
#Number of Tests wished to make, Number of nodes to be tested.
numOfNodes = 1000
tests = 5
for test in range(0,tests):
    for node in range(0,numOfNodes):
        g.add_node(node, color=randint(0,numOfNodes-1))
        
    for nodeIn in range(0,numOfNodes):
        for nodeOut in range(nodeIn+1,numOfNodes):
            g.add_edge(nodeIn,nodeOut);
            
    #Where each node guesses:
    correct = 0;
    incorrect = 0;
    for node in g.nodes():
        allColorModTotals = 0;
        colorModTotals = 0;
        colorCnt = {};
        for edge in g.edges(node):
            check = str(g.nodes[edge[1]]['color']);
            if check not in colorCnt.keys():
                colorCnt[check] = 0;
            colorCnt[check]+=1;
        #ADD up all keys.
        for color in colorCnt.keys():
            allColorModTotals += (colorCnt[str(color)] * int(color))%numOfNodes;
        guess = node-(allColorModTotals%numOfNodes);
        if guess<0:
            guess = numOfNodes + guess;
        if guess == g.nodes[node]['color']:
            correct+=1
        else:
            incorrect+=1
            #print("Guess is ",guess," Correct is ",g.nodes[node]['color']);
    print("Correct = ",correct," Incorrect = ",incorrect);    
    if correct == 1:
        print("Test ",test," passed.")
    else:
        print("Test ",test," Failed.")
        
#nx.draw(G)
print("Number of edges = ",g.number_of_edges())



