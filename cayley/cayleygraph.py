import math

import networkx as nx
import pylab

gen = 11
useGen = True
maxVal = 42
group = []

for n in range(maxVal):
    if math.gcd(maxVal, n) != 1:
        continue
    group.append(n)

G = nx.Graph()
for num in group:
    G.add_node(num, size='small', name=num)

if not useGen:
    for num in group:
        if (num != 1):
            for number in group:
                G.add_edge(number, (number * num % maxVal))

if useGen:
    for number in group:
        G.add_edge(number, (number * gen % maxVal))

labels = nx.get_node_attributes(G, 'name')
nx.draw(G, labels=labels, node_size=500, pos=nx.circular_layout(G))
pylab.show()
