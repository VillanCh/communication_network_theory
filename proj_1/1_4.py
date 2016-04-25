#encoding:utf-8

"""
1_4
use the graph in 1_3
"""

class Edge():
    """
    So the empty Edge can use Edge()
    the specific Edge can be defined as Edge(num = Number) 
    """
    def __init__(self, num = False):
        if num == False:
            pass
        else:
            if isinstance(num, int):
                self.num = num 
            else:
                pass
            
    def set_num(self, num):
        if not isinstance(num, int ):
            raise TypeError('[!] Error ! num need a int , but got a %s' % type(
                                                                              num))
        self.num = num
        
    def __str__(self):
        try:
            return str(self.num)
        except:
            return str('NULL')

graph = []
for count in range(6):
    graph.append(list())
    for sub_count in range(6):
        graph[count].append(Edge())

def fill_edge(node1, node2, edge_num):
    graph[node1][node2].set_num(edge_num)
    graph[node2][node1].set_num(edge_num)
    
fill_edge(0,1,0)
fill_edge(0,3,1)
fill_edge(0,4,2)
fill_edge(0,2,3)
fill_edge(0,5,4)
fill_edge(1,4,8)
fill_edge(1,3,7)
fill_edge(2,4,6)
fill_edge(2,5,5)

for i in graph:
    print "{}-{}-{}-{}-{}-{}".format(i[0],i[1],i[2],i[3],i[4],i[5])
    
    
    
"""
build a list containing the edges related to a specific node 
"""
def get_relevent_edges_by_node(node, graph):
    result_set = set()
    for _ in range(6):
        val = graph[_][node].__str__()
        if val == "NULL":
            pass
        else:
            result_set.add(val)
            
    return list(result_set)
"""
output the result
"""
for i in range(6):
    print eval('get_relevent_edges_by_node(node = %d, graph = graph)' % i)
        