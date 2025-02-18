
# File:     redblack.py
# Author:   John Longley
# Date:     October 2024

# Template file for Inf2-IADS (2024-25) Coursework 1, Part B:
# Implementation of dictionaries by red-black trees, space-saving version.

# Provided code:

from enum import Enum

Colour = Enum('Colour', ['Red','Black'])
Red, Black = Colour.Red, Colour.Black

def colourStr(c):
    return 'R' if c==Red else 'B'

Dir = Enum('Dir', ['Left','Right'])
Left, Right = Dir.Left, Dir.Right

def opposite(d):
    if d==Left: return Right
    else: return Left

def branchLabel(d):
    if d==Left: return 'l'
    else: return 'r'

class Node():
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.colour = Red
        self.left = None
        self.right = None
        
    def getChild(self,branch):
        if branch==Left:
            return self.left
        else:
            return self.right

    def setChild(self,branch,y):
        if branch==Left:
            self.left = y
        else:
            self.right = y

    def __repr__(self):
        return str(self.key) +':'+ str(self.value) +':'+ colourStr(self.colour)

# Use None for all trivial leaf nodes

def colourOf(x):
    if x is None:
        return Black
    else:
        return x.colour


class RedBlackTree():

    def __init__ (self):
        self.root = None
        self.stack = []


# TODO: Task 1.
#   lookup(self,key)

    def lookup(self,key):
        node = self.root

        while node is not None:
            if node.key == key:         # find key
                return node.value
            
            elif key < node.key:        # key < node.key, go left
                node = node.left
            
            elif key > node.key:        # key > node.key, go right
                node = node.right
        
        return None






    # TODO: Task 2.
    #   plainInsert(self,key,value)
    def plainInsert(self,key,value):
        insertNode = Node(key,value)
        self.stack = []

        if self.root == None:
            self.root = insertNode
            self.stack.append(self.root)
            return

        current = self.root
        while True:
            self.stack.append(current)
            if key < current.key:                       # key < current.key, go left and record direction
                self.stack.append(Left)
                if current.left == None:
                    current.setChild(Left,insertNode)   # no further node in left of current node, add
                    self.stack.append(insertNode)
                    break
                current = current.getChild(Left)
            
            elif key > current.key:                       # key > current.key, go right and record direction
                self.stack.append(Right)
                if current.right == None:
                    current.setChild(Right,insertNode)  # no further node in right of current node, add
                    self.stack.append(insertNode)
                    break
                current = current.getChild(Right)

            else:
                current.value = value
                return



# TODO: Task 3.
#   tryRedUncle(self)
#   repeatRedUncle(self):

    def tryRedUncle(self):
        if len(self.stack) < 5:
            self.root.colour = Black
            return False
        
        son_node = self.stack[-1]               # get son, father, grand father
        father_node = self.stack[-3]
        direction = self.stack[-4] 
        grandfather_node = self.stack[-5] 
                                  
        uncle_node = grandfather_node.getChild(opposite(direction)) # get uncle in oppsite direction


        if  colourOf(son_node) == Red and colourOf(father_node) == Red and colourOf(uncle_node) == Red:
                # if satisify red-uncle
                father_node.colour = Black
                uncle_node.colour  = Black
                grandfather_node.colour = Red
                if(self.root == grandfather_node):
                    grandfather_node.colour = Black

                # select father node to next current node
                self.stack.pop()    # delete current node
                self.stack.pop()    # delete direction of current node
                self.stack.pop()    # delete father node
                self.stack.pop()    # delete direction of father node

                return True  
        return False  
                
    def repeatRedUncle(self):
        while self.tryRedUncle():
            pass 
        
            

# Provided code to support Task 4:

    def toNextBlackLevel(self,node):
        # inspect subtree down to the next level of blacks
        # and return list of components (subtrees or nodes) in L-to-R order
        # (in cases of interest there will be 7 components A,a,B,b,C,c,D).
        if colourOf(node.left)==Black:  # node.left may be None
            leftHalf = [node.left]
        else:
            leftHalf = self.toNextBlackLevel(node.left)
        if colourOf(node.right)==Black:
            rightHalf = [node.right]
        else:
            rightHalf = self.toNextBlackLevel(node.right)
        return leftHalf + [node] + rightHalf

    def balancedTree(self,comps):
        # build a new (balanced) subtree from list of 7 components
        [A,a,B,b,C,c,D] = comps
        a.colour = Red
        a.left = A
        a.right = B
        c.colour = Red
        c.left = C
        c.right = D
        b.colour = Black
        b.left = a
        b.right = c
        return b


# TODO: Task 4.
#   endgame(self)
#   insert(self,key,value)
    def endgame(self):
        if len(self.stack) < 5:
            self.root.colour = Black
            return 
        
        son_node = self.stack[-1]                   # get son, father, grandfather and beinsert_node(greatgrandfather)
        father_node = self.stack[-3]      
        direction = self.stack[-4] 
        grandfather_node = self.stack[-5] 
        beinsert_node = self.stack[-7] if len(self.stack) >= 7 else None
        insert_direction = self.stack[-6] if len(self.stack) >= 7 else None
        uncle_node = grandfather_node.getChild(opposite(direction))# get uncle in oppsite direction


        if  colourOf(son_node) == Red and colourOf(father_node) == Red and colourOf(uncle_node) == Black:
            comp = self.toNextBlackLevel(grandfather_node)      # get comp
            balanced_tree = self.balancedTree(comp) # bulid balanced tree
            if beinsert_node is None:       # if no beinsert_node(greatgrandfather), means only three node in the tree
                self.root = balanced_tree
                self.root.colour = Black
            else:
                if insert_direction == Dir.Left:            # replace orginal node by balanced tree
                    beinsert_node.left = balanced_tree
                elif insert_direction == Dir.Right:
                    beinsert_node.right = balanced_tree    
        else:
            return
        
        
        
  
    
    def insert(self,key,value):
        self.plainInsert(key, value)
        
        self.repeatRedUncle()

        self.endgame()
        


        

# Provided code:

    # Printing tree contents
    
    def __str__(self,x):
        if x==None:
            return 'None:B'
        else:
            leftStr = '[ ' + self.__str__(x.left) + ' ] '
            rightStr = ' [ ' + self.__str__(x.right) + ' ]'
            return leftStr + x.__str__() + rightStr

    def __repr__(self):
        return self.__str__(self.root)

    def showStack(self):
        return [x.__str__() if isinstance(x,Node) else branchLabel(x)
                for x in self.stack]

    # All keys by left-to-right traversal
    
    def keysLtoR_(self,x):
        if x==None:
            return []
        else:
            return self.keysLtoR_(x.left) + [x.key] + self.keysLtoR_(x.right)

    def keysLtoR(self):
        return self.keysLtoR_(self.root)

# End of class RedBlackTree


# Creating a tree by hand:

sampleTree = RedBlackTree()
sampleTree.root = Node(2,'two')
sampleTree.root.colour = Black
sampleTree.root.left = Node(1,'one')
sampleTree.root.left.colour = Black
sampleTree.root.right = Node(4,'four')
sampleTree.root.right.colour = Red
sampleTree.root.right.left = Node(3,'three')
sampleTree.root.right.left.colour = Black
sampleTree.root.right.right = Node(6,'six')
sampleTree.root.right.right.colour = Black
# For fun: sorting algorithm using trees
# Will remove duplicates (not good)

def treeSort(L):
    T = RedBlackTree()
    for x in L:
        T.insert(x,None)
    return T.keysLtoR()

# End of file
