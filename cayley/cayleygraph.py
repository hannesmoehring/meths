import math

import networkx as nx
import matplotlib.pylab as pylab

gen = int(input("generator, if only use one gen   "))
if input("use only one gen? y/n   " ) == "y":
    useGen = True
else: useGen = False
maxVal = int(input("natural number: maxVal:  "))
group = []
chooseDisplay = input("for graph, input g, for text, input t  ").lower()

for n in range(maxVal):
    if math.gcd(maxVal, n) != 1:
        continue
    group.append(n)

if chooseDisplay == "g":
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

else:
    print("generator : " + str(gen))
    print("max : " + str(maxVal))
    for number in group:
        print("orgin: " + str(number) + " -> " + str(number * gen % maxVal))

    if (input("Do you want full graph? y/n      ") == "y"):
        for num in group:
            print()
            print("Generator now is : " + str(num))
            print()
            if (num != 1):
                for number in group:
                    print("orgin: " + str(number) + " -> " + str(number * num % maxVal))
