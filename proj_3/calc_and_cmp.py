#encoding:utf-8
import networkx as nx
import matplotlib.pyplot as ply
import randomgraph
from calcpath import PathCalc

if __name__ == '__main__':

    G = randomgraph.get_barabasi_albert_graph(15,2)
    print 'the graph is ', G.edge
    tmp = PathCalc(G = G, start_point=3, end_point=1)

    tmp.dijkstra(field='weight',capability_min=0)
    print 'the route is ',tmp.get_path()
    print 'the min of weight',tmp.get_weight()    
    tmp.dial_calc(field='weight',capability_min=0)
    print 'the route is ',tmp.get_path()
    print 'the min of weight',tmp.get_weight()    
    nx.drawing.draw_networkx(G)

    ply.show()
    print tmp.get_distance()