class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)
        
        res = 0 

        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res 