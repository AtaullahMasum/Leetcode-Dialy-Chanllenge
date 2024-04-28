# Brute Force Solution
# Time Complexity is O(n^2)
# Space Complexity is O(n)
from types import List
from collections import deque, defaultdict
class Solution:
    def bfs (self, graph, N, start):
        distances = [0]*N
        visited = [False]*N
        queue = deque([(start, 0)])
        visited[start] = True
        while queue:
            node , distance = queue.popleft()
            distances[node] = distance
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    queue.append((neighbor, distance+1))
                    visited[neighbor] = True
        return distances
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        result = [0]*N
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        for i in range(N):
            distance = self.bfs(graph, N, i)
            result[i] = sum(distance)
        return result
# Optimal Solution
# Time Complexity is O(n)
# Space Complexity is O(n)
class Solution:
    def postorder(self, graph,countNodes, sumDist, node, parent=None):
        for child in graph[node]:
            if child == parent:
                continue
            self.postorder(graph, countNodes, sumDist, child, node)
            countNodes[node] += countNodes[child]
            sumDist[node] += sumDist[child] + countNodes[child]

    def preorder(self,N, graph,countNodes, sumDist, node, parent=None):
        for child in graph[node]:
            if child == parent:
                continue
            sumDist[child] = sumDist[node] - countNodes[child] + N - countNodes[child]
            self.preorder(N, graph, countNodes, sumDist, child, node)

    
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        sumDist = [0]*N
        countNodes = [1]*N
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.postorder(graph,countNodes, sumDist, 0)
        self.preorder(N, graph,countNodes, sumDist, 0)
        return sumDist
       
