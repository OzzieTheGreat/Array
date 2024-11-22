class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def functionInput():
    root = None
    dataVal = int(input("Enter values or -1 to finish: "))
    while dataVal != -1:
        root = insertValues(root, dataVal)
        dataVal = int(input("Enter values or -1 to finish: "))
    return root

def insertValues(root, val):
    if root is None:
        return Node(val)
    if root.data == val:
        return root
    if root.data < val:
        root.right = insertValues(root.right, val)
    else:
        root.left = insertValues(root.left, val)
    return root

def calculatekthlargestElement(root, k, c):
    if root is None:
        return 0
    right_sum = calculatekthlargestElement(root.right, k, c)
    if c > k:
        return right_sum
    c += 1
    return right_sum + root.data + calculatekthlargestElement(root.left, k, c)

def kthlargestElementSum(root, k):
    c = 0
    return calculatekthlargestElement(root, k, c)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

root = functionInput()
print("Inorder traversal of BST")
inorder(root)
k = int(input("\nEnter the value of K: "))
print(f"\nSum of elements larger than or equal to the {k}th largest element:", kthlargestElementSum(root, k))