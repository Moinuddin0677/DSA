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

#  Blace Binary Tree = difference between left and right subtrees should not grater then 1 



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


def childrenSum(node):
    if node == None or (node.left == None and node.right == None):
        return True
    sum=0
    if node.left != None:
        sum+=node.left.data
    if node.right != None:
        sum+=node.right.data
    return (node.data==sum and childrenSum(node.left) and childrenSum(node.right))

def isBlanced(node): # O(n^2)
    if node is None:
        return True
    lh=heightTree(node.left)
    rh=heightTree(node.right)
    return (abs(lh-rh)<=1) and isBlanced(node.left) and isBlanced(node.right)   

def isBlanced1(node): # O(n)
    if node is None:
        return 0
    lh=isBlanced(node.left)
    if lh==-1:
        return -1
    rh=isBlanced(node.right)
    if rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    else:
        return max(lh,rh)+1


def widthofTree(node):
    if node is None:
        return
    queue = []
    queue.append(node)
    maxsize=0
    while queue:
        size=len(queue)
        maxsize=max(maxsize,size)
        for i in range(size):
            current=queue.pop(0)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
    return maxsize

def spiralLevelOrder(node):
    if node is None:
        return
    queue = []
    tempdata=[]
    tempindex = []
    queue.append(node)

    while queue:
        size=len(queue)
        tempindex.append(size)
        for i in range(size):
            current=queue.pop(0)
            tempdata.append(current.data)
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)

    mini=0
    Bool=True
    while tempindex:
        maxi=tempindex.pop(0)
        if Bool:
            for i in tempdata[mini:mini+maxi]:
                print(i,end=" ")
            Bool=False
        else:
            for i in reversed(tempdata[mini:mini+maxi]):
                print(i,end=" ")
            Bool=True
        mini+=maxi


    
    

        
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
    print("\nThis Binary Tree follows Children Sum Property: ",childrenSum(root))
    print("\nThis Binary Tree follows the Property of Blanced BinaryTree method1: ",isBlanced(root))
    ans=True
    if isBlanced1(root)==-1:
        ans=False
    else:
        ans=True

    print("\nThis Binary Tree follows the Property of Blanced BinaryTree method2: ",ans)
    print("\nWidth of the BinaryTree method2: ",widthofTree(root))
    print("\nSprial Level Order traversal: ",end=" ")
    spiralLevelOrder(root)

    print("\n")




    








    # root =Node(20)
    # root.left=Node(8)
    # root.right=Node(12)
    # root.right.left=Node(3)
    # root.right.right=Node(8)