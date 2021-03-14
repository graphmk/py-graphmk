from py_graphmk import PyGraphMk
import networkx as nx

datalogQuery = """
Nodes(ID, Name) :- Author(ID, Name).
Edges(ID1, ID2) :- AuthorPublication(ID1, PubID), AuthorPublication(ID2, PubID).
"""

gg = PyGraphMk("network","localhost","5432","postgres","123")

fname = gg.generateGraph(datalogQuery,"dblp-graph", PyGraphMk.GML)

G = nx.read_gml(fname,'id')
print ("Graph Loaded into NetworkX! Running PageRank...")

print(nx.pagerank(G))
print ("Done!")
