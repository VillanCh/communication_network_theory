#encoding:utf-8
"""
Because of the traits of python

we can use the build-in type 'dict' to complete the first task:
"""

"""
First of all :
define the No.n of node
"""

node_0 = 0
node_1 = 1
node_2 = 2
node_3 = 3
node_4 = 4
node_5 = 5

"""
Second
define the degrees of every node
"""

node_de_0 = 5
node_de_1 = 3
node_de_2 = 3
node_de_3 = 3
node_de_4 = 4
node_de_5 = 2

"""
Build the map
"""
pairs = {}
for _ in range(6):
    print _
    pairs[eval('node_{}'.format(_))] = eval('node_de_{}'.format(_))
    
for k,v in pairs.items():
    print k , ' = ' ,v


"""
sort
"""    
ret = sorted(pairs.items(), key = lambda d:d[1], reverse = True)
for i in ret:
    print i