import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0
        directions = [(-1,0), (1,0),(0,-1),(0,1)]

        ## Loop once and count fresh and stuff rotten fruits in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        #bfs to process all fruit rottened in t minute
        while q and fresh >0: 
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr,nc = r + dr, c +dc

                    if 0<= nr < rows and 0<= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 # Rot fruit
                        q.append((nr,nc))
                        fresh -= 1
            time += 1    

        # final check and return
        return time if fresh == 0 else -1