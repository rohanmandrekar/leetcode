class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS=len(grid),len(grid[0])
        visited=set()
        ans=0

        def bfs(r,c):
            
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                direc=[[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in direc:
                    r,c=row+dr,col+dc
                    if(r in range (ROWS) and c in range (COLS) and (r,c) not in visited 
                    and grid[r][c]=='1'):
                        q.append([r,c])
                        visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    ans+=1
        return ans                    
                