class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[]for i in range(numCourses)]
        ind=[0]*numCourses
        for s,d in prerequisites:
            adj[s].append(d)
            ind[d]+=1
        queue=deque()
        for i in range(numCourses):
            if ind[i]==0:
                queue.append(i)
        count=0
        while queue:
            node=queue.popleft()
            count+=1
            for ne in adj[node]:
                ind[ne]-=1
                if ind[ne]==0:
                    queue.append(ne)
        return count==numCourses
