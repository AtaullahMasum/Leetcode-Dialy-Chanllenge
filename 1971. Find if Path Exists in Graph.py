class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges and not source and not destination:
            return True
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = [source]
        visited = [0]*n
        visited[source] = 1
        while queue:
            node = queue.pop(0)
            for adjacent in graph[node]:
                if not visited[adjacent]:
                    visited[adjacent] = 1
                    queue.append(adjacent)
                if adjacent == destination:
                    return True
        return False
        