#Updated code
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inputFunction():
    root = None
    while True:
        values = input("Enter values or Q to stop: ")
        if values != "Q":
            values = int(values)
            root = insert(root, values)
        else:
            break
    return root

def insert(root, data):
    if not root:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    if data > root.data:
        root.right = insert(root.right, data)
    return root

def divisibleby_5(root):
    if root is None:
        return 0
    sum = 0
    if root.data % 5 == 0:
        sum = sum + root.data
    sum = sum + divisibleby_5(root.left) + divisibleby_5(root.right)
    return sum

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)


root = inputFunction()
print("Inorder traversal of the Binary Search Tree:")
printInorder(root)
print("\nSum of nodes that are divisible by 5:", divisibleby_5(root))
