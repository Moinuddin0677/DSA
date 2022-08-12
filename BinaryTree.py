# The maximum number of nodes at level ‘l’ of a binary tree is 2^l
#size of the binary tree = number of nodes in the tree
# degree of a node is the number of children of a node in the tree
# Internal nodes are the node which not a children or which have 0 degree
#  The Maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1

#  In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is Log2(N+1).

# A Binary Tree with L leaves has at least | Log2L |+ 1   levels. 

# In Binary tree where every node has 0 or 2 children, the number of leaf nodes is always one more thannodes with two children.

# In a non empty binary tree, if n is the total number of nodes and e is the total number of edges, then e = n-1 

# A Binary Tree is a full binary tree if every node has 0 or 2 children.




import queue


class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key


def preOrder(node):

    if node is None:
        return

    print(node.data,end=" ")
    preOrder(node.left)
    preOrder(node.right)


def inOrder(node):

    if node is None:
        return

    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)

def postOrder(node):
    if node is None:
        return

    postOrder(node.left)
    postOrder(node.right)
    print(node.data,end=" ")
    
     
def sizeTree(node):
    if node is None:
        return 0
    return 1+sizeTree(node.left)+sizeTree(node.right)


def maxTree(node):

    if node is None:
        return -999999999999
    
    return max(node.data,max(maxTree(node.left),maxTree(node.right)))

def heightTree(node):
    if node is None:
        return 0
    return max(heightTree(node.left),heightTree(node.right))+1

        
def inOrderwithoutRecursion(node):
    current=node
    stack=[]
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break

def preOrderwithoutRecursion(node):
    current=node
    stack=[]
    while True:
        if current is not None:
            print(current.data,end=" ")
            stack.append(current)
            current=current.left
        elif stack:
            current=stack.pop()
            current=current.right
        else:
            break

def preOrderwithoutRecursion1(node): #best
    current=node
    stack=[]
    while len(stack) or current!=None:
        while current!=None:
            print(current.data,end=" ")
            if current.right!=None:
                stack.append(current.right)
            current=current.left

        if stack:
            current=stack.pop()


def levelOrder(node):
    current=node
    queue=[]
    queue.append(current)
    if node is None:
        return

    while queue:
        current=queue.pop(0)
        print(current.data,end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


def levelOrder1(node):
    if node is None:
        return
    current=node
    queue=[]
    queue.append(current)

    while queue:
        size=len(queue)
        print("-",end=" ")
        for i in range(size):
            current=queue.pop(0)
            print(current.data,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        
def nodeatKthdistance(node, k):
    if node is None:
        return
    if k==0:
        print(node.data,end=" ")

    else:
        nodeatKthdistance(node.left,k-1)
        nodeatKthdistance(node.right,k-1)

def nodeatKthdistance1(node,k):  # by the help of level order traversal
    if node is None:
        return
    current=node
    queue=[]
    queue.append(current)
    cnt=0
    while queue:
        size=len(queue)
        
        for i in range(size):
            current=queue.pop(0)
            if cnt==k:
                print(current.data,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        cnt+=1

def leftView(node): #by the helf of level order traversal (first element of every level)
    if node is None:
        return
    current = node
    queue=[]
    queue.append(node)

    while queue:
        size=len(queue)
        for i in range(size):
            current = queue.pop(0)
            if i==0:
                print(current.data,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)


maxlevel=0
def leftView1(node,currentlevel):
    global maxlevel
    if node is None:
        return
    if maxlevel<currentlevel:
        print(node.data,end=" ")
        maxlevel=currentlevel
    leftView1(node.left,currentlevel+1)
    leftView1(node.right,currentlevel+1)


        
if __name__ =='__main__':
    
    root=Node(10)
    
    root.left=Node(20)
    root.right=Node(30)
    root.left.left=Node(40)
    root.left.right=Node(50)
    root.right.right=Node(60)
    root.left.right.left=Node(70)
    root.left.right.right=Node(80)

    print("\nPreorder Traversal: ",end="")
    preOrder(root)

    print("\nInorder Traversal: ",end=" ")
    inOrder(root)

    print("\nPostorder Traversal: ",end=" ")
    postOrder(root)

    print("\nSize of the Binary Tree: ",end=" ")
    print(sizeTree(root),end=" ")
    print("\nMaximum value in the Binary Tree: ",end=" ")
    print(maxTree(root),end=" ")
    print("\nHeight of the Binary Tree: ",end=" ")
    print(heightTree(root),end=" ")

    print("\nInorder Traversal without recursion: ",end=" ")
    inOrderwithoutRecursion(root)
    print("\nPreorder Traversal without recursion method 1: ",end=" ")
    preOrderwithoutRecursion(root)
    print("\nPreorder Traversal without recursion method 2: ",end=" ")
    preOrderwithoutRecursion1(root)
    print("\nLevelorder Traversal without recursion method 1: ",end=" ")
    levelOrder(root)
    print("\nLevelorder Traversal without recursion method 2: ",end=" ")
    levelOrder1(root)
    distance=int(input("\nEnter distance for kth distance nodes: "))
    print("Node: at kth distance method1: ",end=" ")
    nodeatKthdistance(root,distance)
    print("\nNode: at kth distance method2: ",end=" ")
    nodeatKthdistance1(root,distance)
    print('\nLeft view of the binary tree method 1: ')
    leftView(root)
    print('\nLeft view of the binary tree method 2: ')
    leftView1(root,1)
    print()



    