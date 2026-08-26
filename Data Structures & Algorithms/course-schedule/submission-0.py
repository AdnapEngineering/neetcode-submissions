class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert prerequisites into AdjacencyMap
        adjMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)

        # visiting set to detect loops:
        visiting = set()

        def dfs(crs):
            if crs in visiting: return False # base case, cycle.
            if adjMap[crs] == []: return True # Base case - safe/no-prereqs
            visiting.add(crs)
            for pre in adjMap[crs]:
                if not dfs(pre): return False
            visiting.remove(crs) # crs is safe
            adjMap[crs] = []
            return True

        for crs in range(numCourses):
            return dfs(crs)