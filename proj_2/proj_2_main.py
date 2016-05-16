#encoding:utf-8
import networkx as nx
import matplotlib.pyplot as ply

#in this module named 'randomgraph', it can generate a
# random graph complex networkx, and fill the
#'weight' ,'passing_rate' and 'capability' field
# you can fill any value you want to test the program
import randomgraph

#the algorithm in the dijkstracalc module
from dijkstracalc import DijkstraCalc


#random.seed(a=time.time())
"""
First of all , 
you need have installed the numpy , 
matplotlib and the networkx module.
"""


"""
in this module,
you can call the completed module to 
calc the route you want 



MAN:

    #encoding:utf-8
    import networkx as nx
    import matplotlib.pyplot as ply
    import randomgraph
    from dijkstracalc import DijkstraCalc

    G = randomgraph.get_barabasi_albert_grahp(12,5) 
    #the param you can input what you want but remember : the first param is larger than the second
    #the first param is the number of the nodes in this graph
    #the second param must be less than the first and larger than ZERO
    
    
    calc_obj = DijkstraCalc(G = G, start_point=4, end_point=7) 
    #just input the start and the end 
    #G is the graph you generated
    
    calc_obj.dijstra_calc(field='weight',capability_min=0)
    #This method need 2 argvs:
    #    the first param field is the 'passing_rate' or 'weight', it shows the method you want
    #to calculate the route. if you choose passing_rate, you should know if can compute the route
    #by the max passing rate. Also, you choose the weight , take a measure by the min weight.
    #    the second param 'capability' is for the project 2_3, you input the capability and if there
    #is some route that reached your need, you can check the result. but if there is an exception, 
    #perhaps there are no routes existing.
    
    
    
    
    #the following step is showing the result.
    print tmp.get_path()
    #print tmp.get_passing_rate()
    print tmp.get_weight()
    nx.drawing.draw_networkx(G)
    ply.show()
    


example:

NOTE:
    <strong>YOU HAVE TO KNOW THAT THE THE GRAPH IS RAMDOM
    YOU CAN DEFINE A YOUR OWN GRAPH OR JUST USE THE RANDOM GRAPH
    WHATEVER YOU LIKE ,BUT IF YOUR CHOOSE IS RANDOM, YOU WILL GET A 
    RANDOM RESULT.</strong>


    2_1:
    
    
    in:
    <code>
    G = randomgraph.get_barabasi_albert_graph(6,2)
    print G.edge
    tmp = DijkstraCalc(G = G, start_point=3, end_point=1)
    tmp.dijstra_calc(field='weight',capability_min=0)
    nx.drawing.draw_networkx(G)
    print 'the route is ',tmp.get_path()
    #print tmp.get_passing_rate()
    print 'the min of weight',tmp.get_weight()
    ply.show()
    </code>
    
    out:
    <code>
    the graph is  {0: {2: {'capability': 26, 'passing_rate': 0.07, 'weight': 26}}, 1: {2: {'capability': 50, 'passing_rate': 0.31, 'weight': 18}, 3: {'capability': 23, 'passing_rate': 0.59, 'weight': 37}, 4: {'capability': 44, 'passing_rate': 0.08, 'weight': 9}, 5: {'capability': 17, 'passing_rate': 0.74, 'weight': 42}}, 2: {0: {'capability': 26, 'passing_rate': 0.07, 'weight': 26}, 1: {'capability': 50, 'passing_rate': 0.31, 'weight': 18}, 3: {'capability': 29, 'passing_rate': 0.91, 'weight': 34}, 4: {'capability': 22, 'passing_rate': 0.01, 'weight': 14}, 5: {'capability': 7, 'passing_rate': 0.82, 'weight': 5}}, 3: {1: {'capability': 23, 'passing_rate': 0.59, 'weight': 37}, 2: {'capability': 29, 'passing_rate': 0.91, 'weight': 34}}, 4: {1: {'capability': 44, 'passing_rate': 0.08, 'weight': 9}, 2: {'capability': 22, 'passing_rate': 0.01, 'weight': 14}}, 5: {1: {'capability': 17, 'passing_rate': 0.74, 'weight': 42}, 2: {'capability': 7, 'passing_rate': 0.82, 'weight': 5}}}
    Success!
    /usr/lib/pymodules/python2.7/matplotlib/collections.py:608: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      if self._edgecolors_original != 'face':
    the route is  [3, 2, 4, 1]
    the min of weight 57
    </code>
    
    
    
    
    2_2: 
    get the route that have the max passing rate
    
    in:
    G = randomgraph.get_barabasi_albert_graph(6,2)
    print 'the graph is ', G.edge
    tmp = DijkstraCalc(G = G, start_point=3, end_point=1)
    tmp.dijstra_calc(field='passing_rate',capability_min=0)
    nx.drawing.draw_networkx(G)
    print 'the route is ',tmp.get_path()
    print 'the max of passing rate',tmp.get_passing_rate()
    #print 'the min of weight',tmp.get_weight()
    ply.show()
    
    out:
    
    the graph is  {0: {2: {'capability': 30, 'passing_rate': 0.26, 'weight': 32}, 3: {'capability': 20, 'passing_rate': 0.62, 'weight': 25}, 5: {'capability': 3, 'passing_rate': 0.86, 'weight': 6}}, 1: {2: {'capability': 35, 'passing_rate': 0.94, 'weight': 17}}, 2: {0: {'capability': 30, 'passing_rate': 0.26, 'weight': 32}, 1: {'capability': 35, 'passing_rate': 0.94, 'weight': 17}, 3: {'capability': 22, 'passing_rate': 0.35, 'weight': 31}, 4: {'capability': 14, 'passing_rate': 0.36, 'weight': 6}, 5: {'capability': 1, 'passing_rate': 0.38, 'weight': 20}}, 3: {0: {'capability': 20, 'passing_rate': 0.62, 'weight': 25}, 2: {'capability': 22, 'passing_rate': 0.35, 'weight': 31}, 4: {'capability': 41, 'passing_rate': 0.86, 'weight': 20}}, 4: {2: {'capability': 14, 'passing_rate': 0.36, 'weight': 6}, 3: {'capability': 41, 'passing_rate': 0.86, 'weight': 20}}, 5: {0: {'capability': 3, 'passing_rate': 0.86, 'weight': 6}, 2: {'capability': 1, 'passing_rate': 0.38, 'weight': 20}}}
    Success!
    /usr/lib/pymodules/python2.7/matplotlib/collections.py:608: FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
      if self._edgecolors_original != 'face':
    the route is  [3, 4, 0, 1]
    the max of passing rate 0.501208
    
    
    
    2_3:
    
    in:
        G = randomgraph.get_barabasi_albert_graph(15,2)
        print 'the graph is ', G.edge
        tmp = DijkstraCalc(G = G, start_point=3, end_point=1)
        try:
            tmp.dijstra_calc(field='weight',capability_min=25)
            print 'the route is ',tmp.get_path()
            #print 'the max of passing rate',tmp.get_passing_rate()
            print 'the min of weight',tmp.get_weight()        
        except StandardError:
            print 'Fail! NO PATH'
        nx.drawing.draw_networkx(G)
        ply.show()
    
    
    out:
    The first execute:
        the graph is  {0: {8: {'capability': 19, 'passing_rate': 0.25, 'weight': 47}, 2: {'capability': 4, 'passing_rate': 0.37, 'weight': 32}, 3: {'capability': 30, 'passing_rate': 0.17, 'weight': 3}, 5: {'capability': 8, 'passing_rate': 0.34, 'weight': 7}, 7: {'capability': 9, 'passing_rate': 0.16, 'weight': 32}}, 1: {2: {'capability': 21, 'passing_rate': 0.71, 'weight': 26}, 10: {'capability': 50, 'passing_rate': 0.89, 'weight': 9}, 5: {'capability': 5, 'passing_rate': 0.37, 'weight': 29}}, 2: {0: {'capability': 4, 'passing_rate': 0.37, 'weight': 32}, 1: {'capability': 21, 'passing_rate': 0.71, 'weight': 26}, 3: {'capability': 24, 'passing_rate': 0.29, 'weight': 50}, 4: {'capability': 15, 'passing_rate': 0.91, 'weight': 11}, 6: {'capability': 10, 'passing_rate': 0.83, 'weight': 33}, 9: {'capability': 50, 'passing_rate': 0.47, 'weight': 47}, 13: {'capability': 30, 'passing_rate': 0.76, 'weight': 44}}, 3: {0: {'capability': 30, 'passing_rate': 0.17, 'weight': 3}, 8: {'capability': 22, 'passing_rate': 0.31, 'weight': 16}, 2: {'capability': 24, 'passing_rate': 0.29, 'weight': 50}, 4: {'capability': 24, 'passing_rate': 0.95, 'weight': 39}, 6: {'capability': 48, 'passing_rate': 0.58, 'weight': 20}}, 4: {2: {'capability': 15, 'passing_rate': 0.91, 'weight': 11}, 3: {'capability': 24, 'passing_rate': 0.95, 'weight': 39}}, 5: {0: {'capability': 8, 'passing_rate': 0.34, 'weight': 7}, 1: {'capability': 5, 'passing_rate': 0.37, 'weight': 29}, 7: {'capability': 24, 'passing_rate': 0.13, 'weight': 25}, 9: {'capability': 31, 'passing_rate': 0.71, 'weight': 50}, 11: {'capability': 12, 'passing_rate': 0.57, 'weight': 43}, 14: {'capability': 32, 'passing_rate': 0.61, 'weight': 44}}, 6: {2: {'capability': 10, 'passing_rate': 0.83, 'weight': 33}, 3: {'capability': 48, 'passing_rate': 0.58, 'weight': 20}}, 7: {0: {'capability': 9, 'passing_rate': 0.16, 'weight': 32}, 12: {'capability': 13, 'passing_rate': 0.45, 'weight': 20}, 5: {'capability': 24, 'passing_rate': 0.13, 'weight': 25}}, 8: {0: {'capability': 19, 'passing_rate': 0.25, 'weight': 47}, 10: {'capability': 50, 'passing_rate': 0.93, 'weight': 27}, 3: {'capability': 22, 'passing_rate': 0.31, 'weight': 16}, 12: {'capability': 26, 'passing_rate': 0.43, 'weight': 45}}, 9: {2: {'capability': 50, 'passing_rate': 0.47, 'weight': 47}, 11: {'capability': 43, 'passing_rate': 0.79, 'weight': 13}, 5: {'capability': 31, 'passing_rate': 0.71, 'weight': 50}, 14: {'capability': 11, 'passing_rate': 0.41, 'weight': 50}}, 10: {8: {'capability': 50, 'passing_rate': 0.93, 'weight': 27}, 1: {'capability': 50, 'passing_rate': 0.89, 'weight': 9}}, 11: {9: {'capability': 43, 'passing_rate': 0.79, 'weight': 13}, 5: {'capability': 12, 'passing_rate': 0.57, 'weight': 43}, 13: {'capability': 46, 'passing_rate': 0.05, 'weight': 15}}, 12: {8: {'capability': 26, 'passing_rate': 0.43, 'weight': 45}, 7: {'capability': 13, 'passing_rate': 0.45, 'weight': 20}}, 13: {2: {'capability': 30, 'passing_rate': 0.76, 'weight': 44}, 11: {'capability': 46, 'passing_rate': 0.05, 'weight': 15}}, 14: {9: {'capability': 11, 'passing_rate': 0.41, 'weight': 50}, 5: {'capability': 32, 'passing_rate': 0.61, 'weight': 44}}}
        Fail! NO PATH
        
    The second execute:
        the graph is  {0: {2: {'capability': 22, 'passing_rate': 0.2, 'weight': 30}, 4: {'capability': 42, 'passing_rate': 0.98, 'weight': 20}, 6: {'capability': 5, 'passing_rate': 0.24, 'weight': 23}, 9: {'capability': 40, 'passing_rate': 0.26, 'weight': 38}, 10: {'capability': 46, 'passing_rate': 0.8, 'weight': 10}, 13: {'capability': 43, 'passing_rate': 0.36, 'weight': 4}}, 1: {2: {'capability': 10, 'passing_rate': 0.87, 'weight': 44}, 3: {'capability': 40, 'passing_rate': 0.12, 'weight': 49}, 5: {'capability': 21, 'passing_rate': 0.99, 'weight': 8}, 8: {'capability': 31, 'passing_rate': 0.88, 'weight': 42}, 11: {'capability': 37, 'passing_rate': 0.55, 'weight': 48}, 14: {'capability': 18, 'passing_rate': 0.39, 'weight': 49}}, 2: {0: {'capability': 22, 'passing_rate': 0.2, 'weight': 30}, 1: {'capability': 10, 'passing_rate': 0.87, 'weight': 44}, 3: {'capability': 42, 'passing_rate': 0.94, 'weight': 26}, 4: {'capability': 17, 'passing_rate': 0.81, 'weight': 28}, 5: {'capability': 26, 'passing_rate': 0.55, 'weight': 49}, 7: {'capability': 17, 'passing_rate': 0.57, 'weight': 47}, 9: {'capability': 22, 'passing_rate': 0.84, 'weight': 44}, 10: {'capability': 37, 'passing_rate': 0.44, 'weight': 11}}, 3: {1: {'capability': 40, 'passing_rate': 0.12, 'weight': 49}, 2: {'capability': 42, 'passing_rate': 0.94, 'weight': 26}}, 4: {0: {'capability': 42, 'passing_rate': 0.98, 'weight': 20}, 2: {'capability': 17, 'passing_rate': 0.81, 'weight': 28}, 11: {'capability': 13, 'passing_rate': 0.37, 'weight': 3}, 13: {'capability': 22, 'passing_rate': 0.17, 'weight': 32}, 7: {'capability': 42, 'passing_rate': 0.36, 'weight': 34}}, 5: {8: {'capability': 17, 'passing_rate': 0.26, 'weight': 7}, 1: {'capability': 21, 'passing_rate': 0.99, 'weight': 8}, 2: {'capability': 26, 'passing_rate': 0.55, 'weight': 49}, 14: {'capability': 36, 'passing_rate': 0.2, 'weight': 3}, 6: {'capability': 28, 'passing_rate': 0.99, 'weight': 22}}, 6: {0: {'capability': 5, 'passing_rate': 0.24, 'weight': 23}, 5: {'capability': 28, 'passing_rate': 0.99, 'weight': 22}}, 7: {2: {'capability': 17, 'passing_rate': 0.57, 'weight': 47}, 4: {'capability': 42, 'passing_rate': 0.36, 'weight': 34}}, 8: {1: {'capability': 31, 'passing_rate': 0.88, 'weight': 42}, 5: {'capability': 17, 'passing_rate': 0.26, 'weight': 7}}, 9: {0: {'capability': 40, 'passing_rate': 0.26, 'weight': 38}, 2: {'capability': 22, 'passing_rate': 0.84, 'weight': 44}}, 10: {0: {'capability': 46, 'passing_rate': 0.8, 'weight': 10}, 2: {'capability': 37, 'passing_rate': 0.44, 'weight': 11}, 12: {'capability': 36, 'passing_rate': 0.42, 'weight': 8}}, 11: {1: {'capability': 37, 'passing_rate': 0.55, 'weight': 48}, 4: {'capability': 13, 'passing_rate': 0.37, 'weight': 3}, 12: {'capability': 2, 'passing_rate': 0.69, 'weight': 29}}, 12: {10: {'capability': 36, 'passing_rate': 0.42, 'weight': 8}, 11: {'capability': 2, 'passing_rate': 0.69, 'weight': 29}}, 13: {0: {'capability': 43, 'passing_rate': 0.36, 'weight': 4}, 4: {'capability': 22, 'passing_rate': 0.17, 'weight': 32}}, 14: {1: {'capability': 18, 'passing_rate': 0.39, 'weight': 49}, 5: {'capability': 36, 'passing_rate': 0.2, 'weight': 3}}}
        Success!
        the route is  [3, 2, 10, 0, 4, 5, 1]
        the min of weight 165
        
    Another time:
        the graph is  {0: {2: {'capability': 43, 'passing_rate': 0.57, 'weight': 5}, 3: {'capability': 42, 'passing_rate': 0.99, 'weight': 33}, 5: {'capability': 41, 'passing_rate': 0.38, 'weight': 7}, 8: {'capability': 45, 'passing_rate': 0.94, 'weight': 22}, 10: {'capability': 16, 'passing_rate': 0.54, 'weight': 17}, 12: {'capability': 42, 'passing_rate': 0.23, 'weight': 40}, 13: {'capability': 3, 'passing_rate': 0.05, 'weight': 3}}, 1: {2: {'capability': 16, 'passing_rate': 0.72, 'weight': 49}}, 2: {0: {'capability': 43, 'passing_rate': 0.57, 'weight': 5}, 1: {'capability': 16, 'passing_rate': 0.72, 'weight': 49}, 3: {'capability': 30, 'passing_rate': 0.24, 'weight': 35}, 4: {'capability': 49, 'passing_rate': 0.33, 'weight': 5}, 6: {'capability': 49, 'passing_rate': 0.28, 'weight': 1}, 7: {'capability': 47, 'passing_rate': 0.26, 'weight': 6}, 10: {'capability': 1, 'passing_rate': 0.15, 'weight': 8}, 12: {'capability': 1, 'passing_rate': 0.57, 'weight': 16}, 13: {'capability': 4, 'passing_rate': 0.17, 'weight': 27}, 14: {'capability': 47, 'passing_rate': 0.77, 'weight': 39}}, 3: {0: {'capability': 42, 'passing_rate': 0.99, 'weight': 33}, 2: {'capability': 30, 'passing_rate': 0.24, 'weight': 35}, 4: {'capability': 46, 'passing_rate': 0.6, 'weight': 35}, 6: {'capability': 30, 'passing_rate': 0.08, 'weight': 1}}, 4: {2: {'capability': 49, 'passing_rate': 0.33, 'weight': 5}, 3: {'capability': 46, 'passing_rate': 0.6, 'weight': 35}, 5: {'capability': 48, 'passing_rate': 0.6, 'weight': 10}}, 5: {0: {'capability': 41, 'passing_rate': 0.38, 'weight': 7}, 4: {'capability': 48, 'passing_rate': 0.6, 'weight': 10}}, 6: {8: {'capability': 37, 'passing_rate': 0.7, 'weight': 42}, 9: {'capability': 17, 'passing_rate': 0.27, 'weight': 8}, 2: {'capability': 49, 'passing_rate': 0.28, 'weight': 1}, 3: {'capability': 30, 'passing_rate': 0.08, 'weight': 1}, 7: {'capability': 39, 'passing_rate': 0.42, 'weight': 37}}, 7: {2: {'capability': 47, 'passing_rate': 0.26, 'weight': 6}, 11: {'capability': 42, 'passing_rate': 0.61, 'weight': 38}, 6: {'capability': 39, 'passing_rate': 0.42, 'weight': 37}}, 8: {0: {'capability': 45, 'passing_rate': 0.94, 'weight': 22}, 9: {'capability': 15, 'passing_rate': 0.76, 'weight': 20}, 6: {'capability': 37, 'passing_rate': 0.7, 'weight': 42}}, 9: {8: {'capability': 15, 'passing_rate': 0.76, 'weight': 20}, 14: {'capability': 44, 'passing_rate': 0.85, 'weight': 39}, 6: {'capability': 17, 'passing_rate': 0.27, 'weight': 8}}, 10: {0: {'capability': 16, 'passing_rate': 0.54, 'weight': 17}, 2: {'capability': 1, 'passing_rate': 0.15, 'weight': 8}, 11: {'capability': 50, 'passing_rate': 0.92, 'weight': 5}}, 11: {10: {'capability': 50, 'passing_rate': 0.92, 'weight': 5}, 7: {'capability': 42, 'passing_rate': 0.61, 'weight': 38}}, 12: {0: {'capability': 42, 'passing_rate': 0.23, 'weight': 40}, 2: {'capability': 1, 'passing_rate': 0.57, 'weight': 16}}, 13: {0: {'capability': 3, 'passing_rate': 0.05, 'weight': 3}, 2: {'capability': 4, 'passing_rate': 0.17, 'weight': 27}}, 14: {9: {'capability': 44, 'passing_rate': 0.85, 'weight': 39}, 2: {'capability': 47, 'passing_rate': 0.77, 'weight': 39}}}
        Fail! NO PATH
        
    One more time:
        the graph is  {0: {2: {'capability': 19, 'passing_rate': 0.5, 'weight': 18}, 3: {'capability': 26, 'passing_rate': 0.6, 'weight': 14}, 5: {'capability': 32, 'passing_rate': 0.39, 'weight': 43}, 6: {'capability': 25, 'passing_rate': 0.19, 'weight': 38}, 9: {'capability': 18, 'passing_rate': 0.71, 'weight': 12}, 12: {'capability': 50, 'passing_rate': 0.57, 'weight': 47}, 14: {'capability': 41, 'passing_rate': 0.51, 'weight': 11}}, 1: {2: {'capability': 8, 'passing_rate': 0.23, 'weight': 45}, 11: {'capability': 38, 'passing_rate': 0.48, 'weight': 23}, 4: {'capability': 29, 'passing_rate': 0.25, 'weight': 45}, 10: {'capability': 39, 'passing_rate': 0.57, 'weight': 13}}, 2: {0: {'capability': 19, 'passing_rate': 0.5, 'weight': 18}, 1: {'capability': 8, 'passing_rate': 0.23, 'weight': 45}, 3: {'capability': 32, 'passing_rate': 0.09, 'weight': 50}, 4: {'capability': 42, 'passing_rate': 0.96, 'weight': 6}, 5: {'capability': 48, 'passing_rate': 0.19, 'weight': 21}, 6: {'capability': 13, 'passing_rate': 0.2, 'weight': 29}, 7: {'capability': 36, 'passing_rate': 0.32, 'weight': 47}, 8: {'capability': 41, 'passing_rate': 0.38, 'weight': 50}, 11: {'capability': 43, 'passing_rate': 0.97, 'weight': 49}, 14: {'capability': 24, 'passing_rate': 0.7, 'weight': 46}}, 3: {0: {'capability': 26, 'passing_rate': 0.6, 'weight': 14}, 2: {'capability': 32, 'passing_rate': 0.09, 'weight': 50}, 13: {'capability': 16, 'passing_rate': 0.61, 'weight': 5}, 7: {'capability': 14, 'passing_rate': 0.49, 'weight': 28}}, 4: {1: {'capability': 29, 'passing_rate': 0.25, 'weight': 45}, 2: {'capability': 42, 'passing_rate': 0.96, 'weight': 6}, 9: {'capability': 30, 'passing_rate': 0.03, 'weight': 18}}, 5: {0: {'capability': 32, 'passing_rate': 0.39, 'weight': 43}, 2: {'capability': 48, 'passing_rate': 0.19, 'weight': 21}, 13: {'capability': 6, 'passing_rate': 0.93, 'weight': 27}}, 6: {0: {'capability': 25, 'passing_rate': 0.19, 'weight': 38}, 2: {'capability': 13, 'passing_rate': 0.2, 'weight': 29}}, 7: {8: {'capability': 46, 'passing_rate': 0.63, 'weight': 35}, 2: {'capability': 36, 'passing_rate': 0.32, 'weight': 47}, 3: {'capability': 14, 'passing_rate': 0.49, 'weight': 28}, 12: {'capability': 5, 'passing_rate': 0.47, 'weight': 9}}, 8: {2: {'capability': 41, 'passing_rate': 0.38, 'weight': 50}, 10: {'capability': 25, 'passing_rate': 0.76, 'weight': 17}, 7: {'capability': 46, 'passing_rate': 0.63, 'weight': 35}}, 9: {0: {'capability': 18, 'passing_rate': 0.71, 'weight': 12}, 4: {'capability': 30, 'passing_rate': 0.03, 'weight': 18}}, 10: {8: {'capability': 25, 'passing_rate': 0.76, 'weight': 17}, 1: {'capability': 39, 'passing_rate': 0.57, 'weight': 13}}, 11: {1: {'capability': 38, 'passing_rate': 0.48, 'weight': 23}, 2: {'capability': 43, 'passing_rate': 0.97, 'weight': 49}}, 12: {0: {'capability': 50, 'passing_rate': 0.57, 'weight': 47}, 7: {'capability': 5, 'passing_rate': 0.47, 'weight': 9}}, 13: {3: {'capability': 16, 'passing_rate': 0.61, 'weight': 5}, 5: {'capability': 6, 'passing_rate': 0.93, 'weight': 27}}, 14: {0: {'capability': 41, 'passing_rate': 0.51, 'weight': 11}, 2: {'capability': 24, 'passing_rate': 0.7, 'weight': 46}}}
        Success!
        the route is  [3, 0, 11, 1]
        the min of weight 86
"""

    
if __name__ == '__main__':
    
    """
    random get a barabasi albert grahp as the example
    fill passing_rate & weight & capability in randomgraph.py
    if you want to change the var , you can enter the randomgraph.py 
    to fill the fields you want
    """
    G = randomgraph.get_barabasi_albert_graph(15,2)
    print 'the graph is ', G.edge
    tmp = DijkstraCalc(G = G, start_point=3, end_point=1)
    try:
        tmp.dijstra_calc(field='weight',capability_min=25)
        print 'the route is ',tmp.get_path()
        #print 'the max of passing rate',tmp.get_passing_rate()
        print 'the min of weight',tmp.get_weight()        
    except StandardError:
        print 'Fail! NO PATH'
    nx.drawing.draw_networkx(G)

    ply.show()
    print tmp.get_distance()
    
    
    
    
    
        
        