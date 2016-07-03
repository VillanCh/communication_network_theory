#encoding:utf-8
import networkx as nx
import random
import time
import matplotlib.pyplot as ply
import threading
import randomgraph

import time


class PathCalc(object):
    def __init__(self, G, start_point, end_point):
        #attr
        self._graph = G
        self._start_point = start_point
        self._end_point = end_point
        self._route = []
        self._route_val_list = []
        #temporal var
        #distance 
        self._dstns = 0
        
        self._visited_point = []

        self._pass_rate = 0.0
        self._total_weight = 0
        
        self.route = {}
        
        self.__init_field()
        
    def __init_field(self):
        self._visited_point.append(self._start_point)
        self._route.append(self._start_point)
    
    def dial_calc(self, field = '', capability_min = 0 ):
        rank = 0
        self.route[self._start_point] = (0, self._start_point)
        num = 0
        
        while num <= len(self._graph.nodes()):
            num = num + 1
            if self._start_point not in self._visited_point:
                self._visited_point.append(self._start_point)
            else:
                pass
            weight_pre = {}
            for visited_point in self._visited_point:
                neighbors = self._graph.neighbors(visited_point)
                for j in neighbors:
                    if j in self._visited_point:
                        continue
                    capability = self._graph[visited_point][j]['capability']
                    if capability <= capability_min:
                        continue
                    weight = self._graph[visited_point][j]['weight']
                    if weight_pre.has_key(j):
                        pass
                    else:
                        weight_pre[j] = []
                        
                    weight_pre[j].append([self.route[visited_point][0] + weight, visited_point])
                    
            if field == 'passing_rate':  
                nxt_jump = object
                all_node_info = []
                for i,k in weight_pre.items():
                    for j in k:
                        all_node_info.append((i,j))
                        

                
                nxt_jump = max(all_node_info,key=lambda x: x[1][0])
                

            elif field == 'weight':
                
                all_node_info = []
                for i,k in weight_pre.items():
                    for j in k:
                        all_node_info.append((i,j))
                if all_node_info == []:
                    break
                nxt_jump = min(all_node_info,key=lambda x: x[1][0])

            
            now_pre = nxt_jump[1][1]

            nxt_jump_node = nxt_jump[0]
            nxt_jump_value = nxt_jump[1][0]
            self.route[nxt_jump_node] = (nxt_jump_value, now_pre)
            self._visited_point.append(nxt_jump_node)
            
            self._route
            
        #print self.route

        
    def dijkstra_calc(self, field = '', capability_min = 0):
        rank = 0
        self.route[self._start_point] = (0, self._start_point)
        num = 0
        
        while num <= len(self._graph.nodes()):
            num = num + 1
            if self._start_point not in self._visited_point:
                self._visited_point.append(self._start_point)
            else:
                pass
            weight_pre = {}
            for visited_point in self._visited_point:
                neighbors = self._graph.neighbors(visited_point)
                for j in neighbors:
                    if j in self._visited_point:
                        continue
                    capability = self._graph[visited_point][j]['capability']
                    if capability <= capability_min:
                        continue
                    weight = self._graph[visited_point][j]['weight']
                    if weight_pre.has_key(j):
                        pass
                    else:
                        weight_pre[j] = []
                        
                    weight_pre[j].append([self.route[visited_point][0] + weight, visited_point])
                    
            if field == 'passing_rate':  
                
                all_node_info = []
                for i,k in weight_pre.items():
                    for j in k:
                        all_node_info.append((i,j))
                #nxt_jump = max(all_node_info,key=lambda x: x[1][0])
                nxt_jump = None
                ret = None
                for i in all_node_info:
                    #nxt_jump = min(all_node_info,key=lambda x: x[1][0])
                    if ret == None:
                        ret = i
                        
                    if i[1][0] >= ret:
                        ret = i[1][0]
                        nxt_jump = i                

            elif field == 'weight':
                
                all_node_info = []
                for i,k in weight_pre.items():
                    for j in k:
                        all_node_info.append((i,j))
                if all_node_info == []:
                    break
                
                nxt_jump = None
                ret = None
                for i in all_node_info:
                    #nxt_jump = min(all_node_info,key=lambda x: x[1][0])
                    if ret == None:
                        ret = i
                        
                    if i[1][0] <= ret:
                        ret = i[1][0]
                        nxt_jump = i
                        
            
            now_pre = nxt_jump[1][1]

            nxt_jump_node = nxt_jump[0]
            nxt_jump_value = nxt_jump[1][0]
            self.route[nxt_jump_node] = (nxt_jump_value, now_pre)
            self._visited_point.append(nxt_jump_node)
            
            self._route
            
        #print self.route


        
    def get_path(self):
        verpath = []
        verpath.append(self._end_point)
        pre = self.route[self._end_point][1]
        while pre != self._start_point:
            verpath.append(pre)
            pre = self.route[pre][1]
        verpath.append(pre)
        
        self._route = []
        for i in range(len(verpath)):
            self._route.append(verpath.pop())
        return self._route
    
    def get_passing_rate(self):
        ret = 1
        for i in self._route_val_list:
            ret = ret * i

        return ret
    
    def get_weight(self):
        return self.route[self._end_point][0]
    
    def get_distance(self):
        return len(self._route)-1

if __name__ == '__main__':
    
    G = randomgraph.get_barabasi_albert_graph(18,3)
    print 'the graph is ', G.edge
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
    
    """
    calc the dijkstraAlg
    the cost of executing dial alg 1000 times
    """  
    for i in range(1000):
        tmp.dijkstra_calc(field='weight',capability_min=0)
    stop = int(time.time()*1000)
    print 'dijkstra 1000 times cost %d ms' % (stop - start)
    print 'the route is ',tmp.get_path()
    print 'the min of weight',tmp.get_weight()  
    nx.drawing.draw_networkx(G)

    ply.show()
    print tmp.get_distance()    