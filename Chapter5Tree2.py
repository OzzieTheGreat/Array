class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def inputFunction():
    root = None
    while True:
        data = int(input("Enter values or enter -1 to stop: "))
        if data <= -1:
            break
        node = Node(data)
        if not root:
            root = node
        else:
            curr = root
            parent = None
            while curr:
                parent = curr
                if data < curr.data:
                    curr = curr.left
                else:
                    curr = curr.right
            if data < parent.data:
                parent.left = node
            else:
                parent.right = node

    return root

def divisibleby_5(root):
    if root is None:
        return 0
    sum = 0
    if root.data % 5==0:
        sum += root.data
    sum += divisibleby_5(root.left)
    sum += divisibleby_5(root.right)
    return sum

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)


root = inputFunction()
print("Inorder traversal of the Binary Search Tree:")
printInorder(root)
print("\n Sum of nodes that are divisible by 5:", divisibleby_5(root))
