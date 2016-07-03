#encoding:utf-8
import networkx as nx
import matplotlib.pyplot as ply

import time

if __name__ == "__main__":
    digraph = nx.DiGraph()
    digraph.add_weighted_edges_from(ebunch = [(1,2,2),
                                              (1,4,4),
                                              (2,3,7),
                                              (4,5,3),
                                              (3,9,2),
                                              (5,6,3),
                                              (5,7,2),
                                              (6,9,2),
                                              (6,8,4),
                                              (7,8,6),
                                              (9,8,1)], weight='weight')
    
    for i in digraph.nodes():
        for j in digraph[i].items():
            digraph[i][j[0]]['capability'] = 1
            
    for i in digraph.nodes():
        for j in digraph[i].items():
            print i,'-->',j[0],digraph[i][j[0]]
            
            
            
    nx.drawing.draw_networkx(digraph)
        
    ply.show()
           