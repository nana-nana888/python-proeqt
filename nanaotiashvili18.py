class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printLeafNodes(node):
    if node is None:
        return
    
    
    if node.left is None and node.right is None:
        print(node.value)
    
    
    if node.left:
        printLeafNodes(node.left)
    if node.right:
        printLeafNodes(node.right)

def countEdges(node):
    if node is None:
        return 0
    
    
    left_edges = countEdges(node.left)
    right_edges = countEdges(node.right)
    
    return left_edges + right_edges + (1 if node.left or node.right else 0)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)


print("Leaf Nodes:")
printLeafNodes(root)


edges = countEdges(root)
print(f"Total Edges: {edges}")
