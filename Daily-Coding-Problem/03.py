class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Node) -> str:
    """
    Serialize a binary tree to a string
    """
    if root is None:
        return "None"  # Special character denoting a null node
    left_subtree = serialize(root.left)
    right_subtree = serialize(root.right)
    return str(root.val) + ',' + left_subtree + ',' + right_subtree

def deserialize(s: str) -> Node:
    """
    Deserialize a string to a binary tree
    """
    def deserialize_helper(nodes: List[str]) -> Tuple[Node, List[str]]:
        """
        Recursive helper function for deserializing a binary tree
        """
        val = nodes.pop(0)
        if val == "None":  # Null node
            return None, nodes
        root = Node(val)
        root.left, nodes = deserialize_helper(nodes)
        root.right, nodes = deserialize_helper(nodes)
        return root, nodes
    
    nodes = s.split(',')
    root, _ = deserialize_helper(nodes)
    return root


# Create a binary tree
node = Node('root', Node('left', Node('left.left')), Node('right'))

# Serialize the binary tree
serialized_tree = serialize(node)
print(serialized_tree)
# Expected output
expected_output = "root,left,left.left,None,None,None,right,None,None"

# Compare the serialized tree with the expected output
assert serialized_tree == expected_output