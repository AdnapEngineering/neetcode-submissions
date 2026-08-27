class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set() #hold coordinates of cells that can flow downhill to pacific
        atlantic = set() #hold coordinates of cells that can flow downhill to Atlantic

        #first row and first column touch Pacific
        #last rot and last column touch the atlantic
        #search inward using dfs to find overlapping regions.
        # As we are reversing it and starting water flow from the oceans, we should check next >= current

        def dfs(r,c,visited_set,prev_height):
            # never check out of bounds.
            if r< 0 or c <0 or r>=ROWS or c >=COLS:
                return
            if (r,c) in visited_set:
                return #don't check already visted
            if heights[r][c] < prev_height:
                return # we don't care about cells with smaller heights
            visited_set.add((r,c))
            #call dfs on all 4 neighbors.
            dfs(r+1, c,visited_set,heights[r][c])
            dfs(r-1, c,visited_set,heights[r][c])
            dfs(r, c+1,visited_set,heights[r][c])
            dfs(r, c-1,visited_set,heights[r][c])
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        ## any coordinate that exists in both pac and atl can flow to both oceans.
        return [[r,c] for r,c in pacific & atlantic]
        