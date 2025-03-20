import math
import copy


# DO NOT EDIT AdjNode
class AdjNode:
    def __init__(self,value):
        self.node = value
        self.next = None

class Graph:
    # DO NOT EDIT
    # Basic initialisation where we don't have file input.
    def __init__(self, num):
        self.n = num
        self.weights = [None] * self.n
        self.graph = [None] * self.n
        self.degs = [0] * self.n

    # Initialisation where we got the graph input from a file,
    # might be weighted or unweighted.  It is your responsibility
    # to complete this method as your work for Part B.
    def __init__(self,num,filename,weighted): 
    # Add code here
        self.n = num
        self.weights = [1] * self.n
        self.graph = [None] * self.n
        self.degs = [0] * self.n
        file = open(filename, "r", encoding="utf-8")
        # if gragh is weighted, record W
        if weighted:
            for i in range(self.n):
                line = file.readline().strip()
                if not line:  
                    break
                node, weight = map(int, line.split())
                self.weights[node] = weight

        # bulid graph
        for line in file:
            if line.strip() and line[0] != '-':# skip -------------------------------------------------------------
                start_node, goal_node = map(int, line.split())
                # start ---> goal
                node_g = AdjNode(goal_node)
                node_g.next = self.graph[start_node]
                self.graph[start_node] = node_g
                
                # goal ---> start
                node_s = AdjNode(start_node)
                node_s.next = self.graph[goal_node]
                self.graph[goal_node] = node_s


        # calculate degree
        for node in range(self.n):
            degree = 0
            temp = self.graph[node]
            while temp:
                degree += 1
                temp = temp.next
            self.degs[node] = degree


        file.close()
    
    
    
    # DO NOT EDIT
    # This is a given method to assist with building the Adjacency
    # list structure.  
    def add_edge(self, u, v):
        self.degs[u] += 1
        self.degs[v] += 1
        Adju = self.graph[u]
        vNode = AdjNode(v)
        vNode.next = Adju
        self.graph[u] = vNode
        Adjv = self.graph[v]
        uNode = AdjNode(u)
        uNode.next = Adjv
        self.graph[v] = uNode
   
                           
    # DO NOT EDIT
    # This method can be used to display the Adjacency list structure
    # to assist in debugging 
    def print_out_graph(self):
        for i in range(self.n):
            print("Vertex " + str(i) + "(weight " + str(self.weights[i]) + "):", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.node), end="")
                temp = temp.next
            print(" \n")

# It is your responsibility to complete this method as your
# work for Part C.  You should work with criterion (a) for
# this implementation, covering both weighted and unweighted
# cases (unweighted being modelled with ``all 1s" in self.weights

def GreedyIS(myGraph):
    # Make sure you create a deepcopy of myGraph, to not destroy the input graph. 
    Cgraph = copy.deepcopy(myGraph)
    numNode = Cgraph.n
    nodeDegs = Cgraph.degs
    weights = Cgraph.weights
    IS = [0 for n in range(numNode)]
    
    while 0 in IS:
        maxWD = 0
        for j in range(numNode): # get u by (a)
            if nodeDegs[j] == 0:
               WD = float('inf')
            else:
                WD = weights[j]/nodeDegs[j]
            if WD > maxWD:
                maxWD = WD
                u = j

        IS[u] = 1  # update process node in IS list
        adjchain =  Cgraph.graph[u] # get the adjnode of u in graph

        # find neighbours
        while adjchain:
            neighbour = adjchain.node  # get neighbour
            IS[neighbour] = -1  # mark neighbour in IS to -1
            Cgraph.degs[neighbour] = float('inf')
            adjchain = adjchain.next
        Cgraph.degs[u] = float('inf')
        

        # update graph by remove neighbour
        for n in range(numNode): # go through all node in graph
            ch = Cgraph.graph[n]
            prev = None
            while ch: # go through all neighbours of node
                current_node = ch.node
                if IS[current_node] == -1:
                    if prev is None: # if head node is -1, delete head
                        Cgraph.graph[n] = ch.next
                        Cgraph.degs[n] -= 1
                        ch = Cgraph.graph[n]
                    else:   # if middle node is -1, delete middle node
                        prev.next = ch.next
                        Cgraph.degs[n] -= 1
                        ch = ch.next
                else: # go to next neightbour of current node 
                    prev = ch
                    ch = ch.next

    # tidy
    for i in range(numNode):
        IS[i] = max(0, IS[i])

    return IS 
        
        

# It is your responsibility to complete this method as your
# work for Part C.  You should work with criterion (b) for                 
# this implementation.

def GreedyIS_b(myGraph):
    Cgraph = copy.deepcopy(myGraph)
    numNode = Cgraph.n
    nodeDegs = Cgraph.degs
    weights = Cgraph.weights
    IS = [0 for _ in range(numNode)]  

    while 0 in IS:  
        maxWeight = -1  
        u = -1  
        for j in range(numNode): # find vertex with gratest weight
            if IS[j] == 0 and weights[j] > maxWeight:
                maxWeight = weights[j]
                u = j
        if u == -1:
            break
        IS[u] = 1

        # find neighbours
        adjchain = Cgraph.graph[u]   
        while adjchain:
            neighbour = adjchain.node 
            IS[neighbour] = -1  
            adjchain = adjchain.next


        for n in range(numNode): # go through all node in graph
            ch = Cgraph.graph[n]
            prev = None
            while ch: # go through all neighbours of node
                current_node = ch.node
                if IS[current_node] == -1:  
                    if prev is None: # if head node is -1, delete head
                        Cgraph.graph[n] = ch.next
                        Cgraph.degs[n] -= 1  
                        ch = Cgraph.graph[n]  
                    else: # if middle node is -1, delete middle node
                        prev.next = ch.next
                        Cgraph.degs[n] -= 1 
                        ch = ch.next 
                else: # go to next neightbour of current node 
                    prev = ch
                    ch = ch.next

    # tidy
    for i in range(numNode):
        IS[i] = max(0, IS[i])

    return IS
   