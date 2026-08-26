"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def dfsCopy(self, node, seen):
        if not node: return None
        if node in seen: return seen[node]
        ## given an unseen node, make a new copy of the node, add it seen, look at it's neighbors recursivly
        new_node= Node(node.val,[])
        seen[node] = new_node
        for n in node.neighbors:
            new_node.neighbors.append(self.dfsCopy(n,seen))
        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        return self.dfsCopy(node,seen)