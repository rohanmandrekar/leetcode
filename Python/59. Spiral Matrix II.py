class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        l,r=0,n
        t,b=0,n
        x=1
        print(mat)
        while l<r and t<b and x<=n*n:
            for i in range(l,r):
                mat[t][i]=x
                x+=1
            t+=1  
            for i in range(t,b):
                mat[i][r-1]=x
                x+=1
            r-=1

            if not l<r and t<b:
                break

            for i in range(r-1,l-1,-1):
                mat[b-1][i]=x
                x+=1
            b-=1
            for i in range(b-1,t-1,-1):
                mat[i][l]=x
                x+=1
            l+=1
        return mat                
