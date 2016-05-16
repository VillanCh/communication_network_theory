#encoding:utf-8
import networkx as nx
import random
import time
import matplotlib.pyplot as ply
import threading
import randomgraph




class DijkstraCalc(object):
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
        
        
        self.__init_field()
        
    def __init_field(self):
        self._visited_point.append(self._start_point)
        self._route.append(self._start_point)
        
    def dijstra_calc(self, field = '', capability_min = 0):

        tmp_end = -1
        
        
        while True:
            if tmp_end == self._end_point:
                break
            else:
                
                #get the all neighber (fit the requirement) jumps
                tmp_edge_dict = {}
                for i in self._visited_point:
                    for nghbr_point in self._graph.neighbors(i):
                        if nghbr_point in self._visited_point:
                            pass
                        else:
                            if self._graph[i][nghbr_point]['capability'] <= capability_min:
                                pass
                            else:
                                tmp_edge_dict[i] = (nghbr_point,self._graph[i][nghbr_point][field])
                                
                #choose the next jump by  passing_rate or weight
                if field == 'passing_rate':  
                    try:
                        nxt_jump = max(tmp_edge_dict.items(),key=lambda x: x[1][1])
                    except:
                        raise StandardError('No PATH!')
                elif field == 'weight':
                    try:
                        nxt_jump = min(tmp_edge_dict.items(),key=lambda x: x[1][1])
                    except:
                        raise StandardError('No PATH!')

                
                
                
                
                #check the next jump's pre-point is the tmp_point ,
                #if yes, just add the jump
                #if no, remove last jump and add this jump
                now_pre = nxt_jump[0]

                nxt_jump_node = nxt_jump[1][0]
                nxt_jump_value = nxt_jump[1][1]
                
                if nxt_jump_node not in self._visited_point:
                    self._visited_point.append(nxt_jump_node)
                else:
                    pass                
                
                if now_pre == self._route[len(self._route)-1]:
                    self._route.append(nxt_jump_node)
                    self._route_val_list.append(nxt_jump_value)
                else:
                    self._route.remove(tmp_end)
                    self._route_val_list.remove(tmp_val)

                    self._route.append(nxt_jump_node)
                    self._route_val_list.append(nxt_jump_value)
                
                tmp_end = nxt_jump_node
                tmp_val = nxt_jump_value

    

        print 'Success!'

        
    def get_path(self):
        return self._route
    
    def get_passing_rate(self):
        ret = 1
        for i in self._route_val_list:
            ret = ret * i

        return ret
    
    def get_weight(self):
        ret = 0
        for i in self._route_val_list:
            ret = ret + i
            
        return ret
    
    def get_distance(self):
        return len(self._route)-1
