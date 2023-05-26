class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]

        col=set()
        posdiag=set()
        negdiag=set()

        board=[['.']*n for i in range (n)]

        def backtrack(r):

            if r==n:
                t=["".join(row) for row in board]
                ans.append(t)
                return

            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue

                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c]='Q'

                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c]='.'

            return
        backtrack(0)

        return(ans)    