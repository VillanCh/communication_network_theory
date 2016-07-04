#encoding:utf-8
from calcpath import *

if __name__ == '__main__':

    G = randomgraph.get_barabasi_albert_graph(18,3)
    print 'the graph is ', G.edge
    tmp = PathCalc(G = G, start_point=3, end_point=1)
    
    """
    calc the dijkstraAlg
    the cost of executing dial alg 1000 times
    """
    start = int(time.time()*1000)
    for i in range(1000):
        tmp.dijkstra_calc(field='weight',capability_min=0)
    stop = int(time.time()*1000)
    print 'dijkstra 1000 times cost %d ms' % (stop - start)
    print 'the route is ',tmp.get_path()
    print 'the min of weight',tmp.get_weight()  
    nx.drawing.draw_networkx(G)    
    
    tmp = PathCalc(G = G, start_point=3, end_point=1)
    """
    calc the dialAlg
    the cost of executing dial alg 1000 times  
    """
    start = int(time.time()*1000)
    for i in range(1000):
        tmp.dial_calc(field='weight',capability_min=0)
    stop = int(time.time()*1000)
    print 'dial 1000 times cost %d ms' % (stop - start)
    
    print 'the route is ',tmp.get_path()
    print 'the min of weight',tmp.get_weight()     


    ply.show()
    print tmp.get_distance()    