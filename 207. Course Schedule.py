class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cmap={i : [] for i in range (numCourses)}

        visited =set()

        for c,p in prerequisites:
            cmap[c].append(p)


        def dfs(c):
            if c in visited:
                return False
            if cmap[c]==[]:
                return True
            visited.add(c)

            for p in cmap[c]:
                if not dfs(p):
                    return False
            visited.remove(c)

            cmap[c]=[]
            return True

        for c in range (numCourses):
            if not dfs(c):
                return False
        return True                            

