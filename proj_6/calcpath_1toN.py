#encoding:utf-8
import networkx as nx
import random
import time
import matplotlib.pyplot as ply
import threading
import randomgraph

import time

class CalcPath_1toN():
    def __init__(self, G, start, end):
        self.G = G
        self.start = start
        if isinstance(end, list):
            pass
        else:
            raise TypeError('end have to be a list , got a %s' % type(end))
        self.end = end
    
        self.result = {}
        for i in end:
            self.result[i] = []
    
        self.found = set()
        self.route = {}
        
    def calc_path(self):
        visited = []
        num = 0
        
        self.route[self.start] = (0, self.start)
        #default : check all nodes and end
        length = len(self.G.nodes())
        while num <= length:
            num = num + 1
            if self.start not in visited:
                visited.append(self.start)
            else:
                pass
            weight_pre = {}
            for visited_point in visited:
                neighbors = self.G.neighbors(visited_point)
                for j in neighbors:
                    if j in visited:
                        continue
                    weight = self.G[visited_point][j]['weight']
                    if weight_pre.has_key(j):
                        pass
                    else:
                        weight_pre[j] = []
                    
                    weight_pre[j].append([self.route[visited_point][0] + weight, visited_point])
                    
            all_node_info = []
            for i,k in weight_pre.items():
                for j in k:
                    all_node_info.append((i,j))
            
            if all_node_info == []:
                break
                    
                    
            nxt_jump = None
            ret = None
            for i in all_node_info:
                if ret == None:
                    ret = i
                    
                if i[1][0] <= ret:
                    ret = i[1][0]
                    nxt_jump = i
            
            now_pre = nxt_jump[1][1]
            nxt_jump_node = nxt_jump[0]
            nxt_jump_value = nxt_jump[1][0]
            self.route[nxt_jump_node] = (nxt_jump_value, now_pre)
            visited.append(nxt_jump_node)            
            
            if nxt_jump_node in self.end:
                self.found.add(nxt_jump[0])
            
            if self.found == set(self.end):
                break
            
        return self.route
    
    def show_result(self):
        
        for i in self.end:
            route = []
            verpath = []    
            verpath.append(i)
            pre = self.route[i][1]
            while pre != self.start:
                verpath.append(pre)
                pre = self.route[pre][1]
            verpath.append(pre)
            
            
            for _ in range(len(verpath)):
                route.append(verpath.pop())
            
            self.result[i] = route
        return self.result
    
if __name__ == '__main__':
    G = randomgraph.get_barabasi_albert_graph(n=7, m=3)
    ret = CalcPath_1toN(G=G, start=1, end=[2,4,6])
    """
    Clac the period 1000 times
    """
    start = int(time.time()*1000)
    for _ in range(1000):
        ret.calc_path()
    stop = int(time.time()*1000)
    period = stop - start
    r = ret.show_result()
    print 'Designed by my Alg! cost %d ms per 1000 times' % period
    for i,k in r.items():
        print ret.start,'--->',i,'PATH:',str(k),'WEIGHT',ret.route[i][0]
    
    
    
    print '------------------DEFAULT ALG-------------------'  
    start = int(time.time()*1000)
    for _ in range(1000):
        ret1 = nx.all_pairs_dijkstra_path(G)
    stop = int(time.time()*1000)
    period = stop - start
    print 'Dijkstra Alg! cost %d ms per 1000 times' % period
    for i in ret.end:
        route = ret1[ret.start][i]
        print ret.start,'--->',i,'PATH:',str(route)