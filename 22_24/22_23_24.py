import networkx as nx
import matplotlib.pyplot as plt
import random
import powerlaw

G = nx.read_edgelist("soc-Epinions1.txt",nodetype=int,create_using=nx.DiGraph)


#2.1 --> Compute the in-degree and out-degree distributions
res =[]

for  node in list(G.nodes()):
    res.append(G.in_degree(node))
plt.plot(res,list( G.nodes()))
plt.title("in-degree Distribution")
plt.xlabel("in degree")
plt.ylabel("nods")
plt.show() 


# #. out degree distributions
res =[]

for  node in list(G.nodes()):
    res.append(G.out_degree(node))
plt.plot(res,list( G.nodes()))
plt.title("out-degree Distribution")
plt.xlabel("out degree")
plt.ylabel("nods")
plt.show() 

# fit = powerlaw.Fit([1,4,5,7,8],xmin=1,discrete=True)
# fit.power_law.plot_pdf( color= 'b',linestyle='--',label='fit ccdf')
# fit.plot_pdf( color= 'b')

# print( powerlaw.Fit(res))



## 23 Choose 100 nodes at random from the network and do one forward and one
#backward BFS traversal for each node. Plot the cumulative distributions of the nodes

j =0
nodes =[]
number_of_reached =[]

while j<10:
     
     start  = random.randint(0, G.number_of_nodes())
     nodes.append(start)
     backward = sorted(list(nx.bfs_tree(G, source=start,reverse=True)))
     forward = sorted(list(nx.bfs_tree(G, source=start)))
     number_of_reached.append(len(backward)+len(forward))
     print(dict(backward))
     j =j+1

plt.plot(nodes,number_of_reached)
plt.title("BFS")
plt.xlabel("nodes")
plt.ylabel("number_of_reached")
plt.show() 






