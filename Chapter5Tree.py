class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def InsertPreorder(root, data):
    if root is None:
        return Node(data)
    if root.data > data:
        root.left = InsertPreorder(root.left, data)
    else:
        root.right = InsertPreorder(root.right, data)
    return root

def PostorderTraversal(root):
    if root == None:
        return
    PostorderTraversal(root.left)
    PostorderTraversal(root.right)
    print(root.data, end=" ")

if __name__ == '__main__':
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    print("Inorder traversal before insertion: ", end = "")
    PostorderTraversal(root)
    print()
    data = 6
    root = InsertPreorder(root, data)
    print("Inorder traversal after insertion: ", end="")
    PostorderTraversal(root)
    print()
