import networkx as nx
import random
import time

random.seed(time.time())
def get_barabasi_albert_graph(n, m):
    G = nx.random_graphs.barabasi_albert_graph(n = n, m = m)
    
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
        G[tag_pair[0]][tag_pair[1]]['passing_rate'] = random.randint(1,100)/100.0
        G[tag_pair[0]][tag_pair[1]]['weight'] = random.randint(1,50)
        G[tag_pair[0]][tag_pair[1]]['capability'] = random.randint(20,80)
        
        
    return G