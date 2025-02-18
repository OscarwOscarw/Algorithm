import math
import random
import heapq

class Graph:

# Assumes that the nnode are {0, 1, ..., n-1}.  'dir' is a Boolean flag
# to indicate whether it's a directed graph, or undirected (if dir is 0).
# self.n, self.adj_list need to be set up with the appropriate entries.
# For self.adj_list, you need to take note of the value of 'directed'.
    def __init__(self,n,directed,filename):
        self.n = n
        self.adj_list = {}
        allpath = []
        file =  open(filename,'r') 
        lines = file.readlines()
        for l in range(self.n):
            self.adj_list[l] = []
# You need to complete this method to add the edges (and their weights) 
# to self.adj_list.  You should add (v,x) to the list self.adj_list[u]
# to mean "There is an edge from u to v with weight w".
            
            for line in lines:
                u,v,w = line.split()
                u = int(u)
                v = int(v)
                w = float(w)
                if u == l:
                    self.adj_list[l].append((v,w))
                if not directed:
                    self.adj_list[v].append((u,w))

    def showGraph(self):
        node = 0  # 确保初始化 n
        nodenum = len(self.adj_list)  # 获取节点数目
        while node < nodenum:  # 遍历所有节点
            print(f"{node}: {self.adj_list[node]}")  # 打印节点及其邻接列表
            node += 1  # 更新 n，遍历下一个节点





# Your job is to implement this method from scratch. I have done the 
# initialisation of the most important variables (but you may want to 
# introduce some more 
    def DijkstraSimple(self,s):
        dists = [float('inf') for j in range(self.n)]
        pi = [None for j in range(self.n)]
        dists[s]=0
        S = {s}
        print("start")
        
        while len(S) < self.n:
            for node in S:                 
                for neighbor,distance in self.adj_list[node]:
                    if distance + dists[node]  < dists[neighbor]: 
                        dists[neighbor] = dists[node] + distance
                        pi[neighbor] = node
          
            min_node = None
            min_dist = float('inf')
            for node in range(self.n):
                if node not in S and dists[node] < min_dist:
                    min_node = node
                    min_dist = dists[node]
            
            if min_node is not None:
                S.add(min_node)                             
# below is the return statement you should have for DijkstraSimple
        return dists, pi
                
                       

# Your job is to implement this method from scratch. I have done the 
# initialisation of the most important variables (but you may want to 
# introduce some more 
    def Dijkstra(self,s):
        dists = [float('inf') for j in range(self.n)]
        pi = [None for j in range(self.n)]
        myheap = []
        dists[s]=0


# below is the return statement you should have for Dijkstra
        return dists, pi
                

# This may be helpful later (when you have your methods working)
def printPath(arr, v):
    l = len(arr)
    if arr[v] == None:
        print(v,end='')
    else:
        printPath(arr, arr[v])
        print(" -> "+str(v),end='') 


def main():
             
    if __name__ == '__main__':
        main()

