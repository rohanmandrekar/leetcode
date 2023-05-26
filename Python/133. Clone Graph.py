"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        s={}

        def dfs(node):
            if node in s:
                return s[node]
            
            new=Node(node.val)
            s[node]=new

            for n in node.neighbors:
                new.neighbors.append(dfs(n))
            return new

        return dfs(node) if node else None            


        