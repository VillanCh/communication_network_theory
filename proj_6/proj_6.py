#encoding:utf-8
from calcpath_1toN import *

if __name__ == '__main__':
    """
    Cmp All-Pairs!
    """
    
    N = 9
    M = 3
    calc_buffer = []
    G = randomgraph.get_barabasi_albert_graph(n=N, m=M)
    print '-----------------Graph------------------------'
    for _ in G.nodes():
        print _,':',G[_]
    print '----------------------------------------------'
    for _ in range(N):
        ret = CalcPath_1toN(G=G, start=_, end=[0,1,2,3,4,5,6])
        calc_buffer.append(ret)
    """
    Clac the period 100 times
    """
    start = int(time.time()*1000)
    for _ in range(100):
        for i in calc_buffer:
            i.calc_path()
    stop = int(time.time()*1000)
    period = stop - start
    print 'Designed by my Alg! cost %d ms per 100 times' % period
    
    #show result
    for ret in calc_buffer:
        r = ret.show_result()
        for i,k in r.items():
            print ret.start,'--->',i,'PATH:',str(k),'WEIGHT',ret.route[i][0]
    
    
    
    print '------------------DEFAULT ALG-------------------'  
    start = int(time.time()*1000)
    for _ in range(100):
        ret1 = nx.all_pairs_dijkstra_path(G)
    stop = int(time.time()*1000)
    period = stop - start
    print 'Dijkstra Alg! cost %d ms per 100 times' % period
    for ret in calc_buffer:
        for i in ret.end:
            route = ret1[ret.start][i]
            print ret.start,'--->',i,'PATH:',str(route)