class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacenyMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjacenyMap[prereq].append(course)
        curr_visiting = set()
        def dfs(course):
            if course in curr_visiting:
                return False
            if adjacenyMap[course] == []:
                return True
            curr_visiting.add(course)
            for neighbor in adjacenyMap[course]:
                if not dfs(neighbor):
                    return False
            curr_visiting.discard(course)
            adjacenyMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True