class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            adjaceny_map = defaultdict(list)
            for i in range(len(prerequisites)):
                adjaceny_map[prerequisites[i][0]].append(prerequisites[i][1])

            def dfs(course_num,visited):
                if course_num in visited:
                    return False
                if not adjaceny_map[course_num]:
                    return True 
                
                visited.add(course_num)
                for pre_req in adjaceny_map[course_num]:
                    if not dfs(pre_req,visited):
                        return False
                visited.remove(course_num)
                adjaceny_map[course_num] = []
                return True
            
            for i in range(numCourses):
                if not dfs(i,set()):
                    return False
            return True 



                
                