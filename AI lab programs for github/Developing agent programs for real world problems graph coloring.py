#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Graph:
    # Constructor
    def __init__(self, edges, N):
        
        self.adj = [[] for _ in range(N)]

        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)
def colorGraph(graph):
    result = {}
    # assign color to vertex one by one
    for u in range(N):

        assigned = set([result.get(i) for i in graph.adj[u] if i in result])

        # check for first free color
        color = 1
        for c in assigned:
            if color != c:
                break
            color = color + 1

        # assigns vertex u the first available color
        result[u] = color

    for v in range(N):
        print("Color assigned to vertex", v, "is", colors[result[v]])


colors = [ "","BLUE","GREEN","RED","YELLOW","ORANGE","PINK","BLACK","BROWN","WHITE",
          "PURPLE","VIOLET"]

    #  of graph edges as per above diagram
edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]

    # Set number of vertices in the graph
N = 6
    
graph = Graph(edges, N)

colorGraph(graph)


# In[ ]:




