class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjaceny_map = defaultdict(list)

        for u,v in prerequisites:
            adjaceny_map[u].append(v)

        output = []
        curr_cycle, visited = set(), set()

        def dfs(course):
            if course in curr_cycle:
                return False
            if course in visited:
                return True
            curr_cycle.add(course)

            for neighbour in adjaceny_map[course]:
                if not dfs(neighbour):
                    return False
            visited.add(course)
            output.append(course)
            curr_cycle.remove(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output