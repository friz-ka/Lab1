import networkx as nx

edge = [(0, 1), (0, 2), (0, 3)]
G = nx.Graph(edge)

centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
    print(f"c({n})= {centrality[n]:4f}")