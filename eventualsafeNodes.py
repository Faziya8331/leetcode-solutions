class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited=[0]*n
        path=[0]*n
        safe=[0]*n
        def dfs(node):
            visited[node]=1
            path[node]=1
            for ne in graph[node]:
                if visited[ne]==0:
                    if dfs(ne):
                        return True
                elif path[ne]==1:
                    return True
            safe[node]=1
            path[node]=0

        for i in range(n):
            if visited[i]==0:
                dfs(i)
        res=[]
        for i in range(n):
            if safe[i]==1:
                res.append(i)
    
        return res
