#encoding:utf-8
"""
python build-in type:
dict 
list
"""


node_0 = 0
node_1 = 1
node_2 = 2
node_3 = 3
node_4 = 4
node_5 = 5

"""
Use the grahp in 1_1
"""

list_0 = [1,2,3,4,5]
list_1 = [0,4,3]
list_2 = [0,4,5]
list_3 = [0,1,4]
list_4 = [0,1,2,3]
list_5 = [0,2]

"""Built the map"""

graph_1 = {}
for index in range(6):
    graph_1[eval('node_%d' % index)] = eval('list_%d' % index)
    
    
for i in graph_1.items():
    print i