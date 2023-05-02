import graphviz
import networkx as nx
import matplotlib.pyplot as mat

graph_data = graphviz.Graph()
graph = nx.Graph()
gr=[]
with open("list.txt", 'r') as file:
    const = 0
    for tops in file:
        top = tops.strip().split()
        if len(top) == 2:
            graph.add_edge(int(top[0]), int(top[1]))
            graph_data.edge(top[0],top[1])
            gr.append(top)
        elif len(top) == 1:
            graph.add_node(int(top[0]))
            graph_data.edge(top[0])
            gr.append(top)
    print(gr)

n=len(graph.nodes())
e=len(graph.edges())

if (e > (n-1)*(n-2)/2):
    print("Your graph is connected")
else:
    print("Your graph isn't connected")

graph_data.view()