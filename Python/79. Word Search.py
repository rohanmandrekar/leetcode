class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        visited=set()

        def dfs(r,c,i):
            if i>=len(word):
                return True
                print(r,c,i)
            if (r<0 or 
                c<0 or 
                r>=row or 
                c>=col or 
                word[i] != board[r][c] or 
                (r,c) in visited ):
                return False

            visited.add((r,c))
            ans=(dfs(r+1,c,i+1) or
                 dfs(r-1,c,i+1) or
                 dfs(r,c+1,i+1) or
                 dfs(r,c-1,i+1) )  
            visited.remove((r,c))
            return ans

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False 