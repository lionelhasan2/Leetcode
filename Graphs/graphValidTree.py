class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n -1:
            return False
        tree = defaultdict(list)

        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)
        

        visited = set()        
        def dfs(node, parent):
            visited.add(node)
            for neighbor in tree[node]:
                if neighbor == parent:  # Skip the parent edge
                    continue
                if neighbor in visited:
                    return False  # Real cycle detected
                if not dfs(neighbor, node):
                    return False
            return True
        
        dfs(0,-1)

        return len(visited) == n            

        
