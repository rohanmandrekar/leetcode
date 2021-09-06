class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        box=[set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=int(board[i][j])
                    row[i].add(num)
                    col[j].add(num)
                    box[i//3 * 3 + j//3].add(num)
        # print(row)            
        
        def backtrack(i,j):
            # print('in')
            nonlocal solved
            if i == 9:
                # print('9')
                solved = True
                return
                
            newi= i + (j+1)//9
            newj = (j+1)%9
            # print(i,newi)
                
            if board[i][j] != '.':
                backtrack(newi,newj)
            else:
                for num in range(1,10):
                    boxid=i//3 * 3 + j//3
                    if num not in row[i] and num not in col[j] and num not in box[boxid]:
                        board[i][j]=str(num)
                        row[i].add(num)
                        col[j].add(num)
                        box[boxid].add(num)
                        # print(row)
                        # print(col)
                        backtrack(newi,newj)
                            
                        if not solved:
                            row[i].remove(num)
                            col[j].remove(num)
                            box[boxid].remove(num)
                            board[i][j]='.'
                                
        solved=False
        backtrack(0,0)