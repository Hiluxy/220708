


def dfs(x,y):
    if  x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if a[x][y]==1:
        a[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        #대각선까지
        dfs(x+1,y-1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        return True
    return False



while True:
    m,n=map(int,input().split())
    if m==0 or n==0:
        break
    else:
        result=0
        a=[]
        for i in range(n):
            a.append(list(map(int,input().split())))

        for i in range(n):
            for j in range(m):
                if dfs(i,j)==True:
                    result+=1
        print(result)

        



