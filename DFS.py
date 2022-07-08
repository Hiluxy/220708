def dfs(graph, v, visited):

    #현재 방문한 노드 참
    visited[v]=True
    print(v,end=' ')

    for i in graph[v]: #현재 노드와 인접 노드 중
        if not visited[i]: #방문 리스트에 없으면
            dfs(graph,i,visited)

#각 노드마다 연결된 노드 (2차원)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]]

visited = [False]*9

dfs(graph,1,visited)

