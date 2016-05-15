#encoding:utf-8
import networkx as nx
import random
import time
import matplotlib.pyplot as ply
import threading

def start_thread(func):
    ret = threading.Thread(target=func)
    ret.daemon = True
    ret.start()

random.seed(a=time.time())


#random graph
G = nx.random_graphs.barabasi_albert_graph(n = 9, m = 4)

ret = G.edges()

#random weight or other attrs
#def fill_random_attr(attr='', flag = 'int', ):
"""
    elif flag == per:
        var = random.randint(0,100)/100.0
    elif flag == ran, range:
        var = random.randint(range[0],range[1])
"""
for i in range(len(ret)):
    tag_pair = ret[i]
    G[tag_pair[0]][tag_pair[1]]['passing_rate'] = random.randint(0,100)/100.0
    G[tag_pair[0]][tag_pair[1]]['weight'] = random.randint(0,50)
    

class CPath(object):
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
        
    def dijstra_calc(self, field = ''):

        tmp_end = -1
        
        
        while True:
            if tmp_end == self._end_point:
                break
            else:
                
                """get the next finest jump"""
                tmp_edge_dict = {}
                for i in self._visited_point:
                    for nghbr_point in self._graph.neighbors(i):
                        if nghbr_point in self._visited_point:
                            pass
                        else:
                            tmp_edge_dict[i] = (nghbr_point,self._graph[i][nghbr_point][field])
                if field == 'passing_rate':                    
                    nxt_jump = max(tmp_edge_dict.items(),key=lambda x: x[1][1])
                elif field == 'weight':
                    nxt_jump = min(tmp_edge_dict.items(),key=lambda x: x[1][1])
                
                
                """Pick the jump"""
                
                
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
    
    def get_distance(self):
        return len(self._route)-1
    
    
if __name__ == '__main__':
    print G.edge
    tmp = CPath(G = G, start_point=3, end_point=4)
    tmp.dijstra_calc(field='passing_rate')
    nx.drawing.draw_networkx(G)
    print tmp.get_path()
    print tmp.get_passing_rate()
    
    ply.show()
    print tmp.get_distance()
    
    
        
        