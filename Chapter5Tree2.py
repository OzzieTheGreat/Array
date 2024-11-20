#3rd try updating python code
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def functionInput():
    root = None
    dataVal = int(input("Enter values or -1 to finish: "))
    while dataVal != -1:
        root = insertFunction(root, dataVal)
        dataVal = int(input("Enter values or -1 to finish: "))
    return root

def insertFunction(root, val):
    if root is None:
        return Node(val)
    if root.data == val:
        return root
    if root.data < val:
        root.right = insertFunction(root.right, val)
    else:
        root.left = insertFunction(root.left, val)
    return  root

def calculateSum(root):
    if root is None:
        return 0
    sum = 0
    if root.data % 5 == 0:
        sum += root.data
    sum += calculateSum(root.left)
    sum += calculateSum(root.right)
    return sum

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

root = functionInput()
print("Inorder traversal of BST")
inorder(root)
print("\nSum of nodes that are divisible by 5:", calculateSum(root))
