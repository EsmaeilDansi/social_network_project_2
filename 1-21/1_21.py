import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.read_edgelist("email-Eu-core.txt",nodetype=int,create_using=nx.DiGraph)

#1: number of nodes
print("number of nodes")
print(G.number_of_nodes())

print("numer of edgs")
#2: numer of edgs
print(G.number_of_edges())

#3 :  In-degree, out-degree and degree of the first five nodes
print("In-degree, out-degree and degree of the first five nodes")
for  node in list(G.nodes())[:5]:
    print(G.in_degree(node))
    print(G.out_degree(node))
    print(G.degree(node))


#4: Number of source nodes
print("#4: Number of source nodes")
number_of_sorce_node = 0
for  node in list(G.nodes()):
    if(G.in_degree(node)==0):
       number_of_sorce_node  = number_of_sorce_node+1
print(number_of_sorce_node)   


#5: Number of sink nodes
print("#5: Number of sink nodes")
number_of_sink_node = 0
for  node in list(G.nodes()):
    if(G.out_degree(node)==0):
       number_of_sink_node  = number_of_sink_node+1
print(number_of_sink_node)   


#6: Number of isolated nodes
print("#6: Number of isolated nodes")
number_of_isolated_node = 0
for  node in list(G.nodes()):
    if(G.degree(node)==0):
       number_of_isolated_node  = number_of_isolated_node+1
print(number_of_isolated_node) 


# #7:  In-degree distribution
degrees = [G.in_degree(n) for n in G.nodes()]
plt.hist(degrees)
plt.show()

#8: out-degree distribution
degrees = [G.out_degree(n) for n in G.nodes()]
plt.hist(degrees)
plt.show()

#9:  Average degree, average in-degree and average out-degree

print("#9:  Average degree, average in-degree and average out-degree")

average_degree = sum([val for (node, val) in G.degree()])/G.number_of_nodes()
print(average_degree)

average_in_degree = sum([val for (node, val) in G.in_degree()])/G.number_of_nodes()
print(average_in_degree)


average_out_degree = sum([val for (node, val) in G.out_degree()])/G.number_of_nodes()
print(average_out_degree)


# 10 : Distance between five pairs of random nodes

print("# 10 : Distance between five pairs of random nodes")

i = 0
while i<5:
  print("random pair"+str(i))
  start  = random.randint(0, G.number_of_nodes())
  end = random.randint(0, G.number_of_nodes())
  distance = 0
  try:
   distance = nx.shortest_path_length(G,source=start,target=end)
  except:
     distance = 0
  print("distance "+ str(start)+ " and   "+ str(end) + "equal to " +str(distance)) 
  i= i+1; 


# 11 : Shortest path length distribution

lengths = dict(nx.all_pairs_shortest_path_length(G))
node_distance = []
for star in lengths:
    for end in lengths[start]:
        node_distance.append(lengths[start][end])


plt.hist(node_distance, bins='auto')
plt.title("Shortest distance  Distribution")
plt.show()

#12 : Diameter
print(max([max(j.values()) for (i,j) in nx.shortest_path_length(G)]))

#13: Is the graph strongly connected? If so, compute the strongly connected compnent size distribution
print(nx.is_strongly_connected(G))

#14: Is the graph weakly connected? If so, compute the weakly connected component size distribution
print(nx.is_weakly_connected(G))


# 17 Number of nodes in I n(v) for five random nodes

i = 0
while i<5:

  in_nodes =[]
  node   = random.randint(0, G.number_of_nodes())
  distance = 0
  for d in G.nodes():
   try:
    distance = nx.shortest_path_length(G,source=node,target=d)
   except:
     distance = 0
   if(distance>0):
      in_nodes.append(d)
  print(len(in_nodes))    
  i= i+1; 
 
# 18 Number of nodes in Out(v) for five random nodes

i = 0
while i<5:
  out_nodes =[]
  node   = random.randint(0, G.number_of_nodes())
  distance = 0
  for d in G.nodes():
   try:
    distance = nx.shortest_path_length(G,source=d,target=node)
   except:
     distance = 0
   if(distance>0):
      out_nodes.append(d)
  print(len(out_nodes))    
  i= i+1; 


# 19 Clustering coefficient for five random nodes



i = 0
while i<5:
  node   = random.randint(0, G.number_of_nodes())
  print(nx.clustering(G, node))  
  i= i+1; 


#20 Clustering coefficient distribution

i = 0
res = []
while i<5:
  node   = random.randint(0, G.number_of_nodes())
  res.append(nx.clustering(G, node))  
  i= i+1; 
  
plt.hist(res)
plt.title("coefficient distribution")
plt.show()

#  21 Average clustering coefficient

res = 0
for node in G.nodes():
  res = res + nx.clustering(G, node)
print(res/G.number_of_nodes())



