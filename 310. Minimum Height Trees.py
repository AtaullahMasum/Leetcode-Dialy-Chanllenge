# Time Complexity is O(n)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Special case: Only one node, it's the root of MHT

        # Build the adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize a queue with leaf nodes (degree 1) as starting points
        leaves = deque(node for node in range(n) if len(graph[node]) == 1)

        # Perform BFS until there are <= 2 nodes left
        remaining_nodes = n
        while remaining_nodes > 2:
            # Number of nodes to process in this level (leaf nodes)
            level_size = len(leaves)
            remaining_nodes -= level_size

            # Process all nodes at this level (leaf nodes)
            for _ in range(level_size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop(0)  # Remove the only neighbor
                graph[neighbor].remove(leaf)  # Remove the back edge
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)  # Add new leaf node

        # The remaining nodes are the roots of the MHTs
        return list(leaves)