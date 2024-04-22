class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        if target == "0000":
            return 0
        
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        while queue:
            node, steps = queue.popleft()
            for i in range(4):
                for d in (-1, 1): #(9, 1)
                    new_digit = (int(node[i]) + d) % 10
                    new_node = node[:i] + str(new_digit) + node[i+1:]
                    if new_node not in visited and new_node not in deadends_set:
                        if new_node == target:
                            return steps + 1
                        queue.append((new_node, steps + 1))
                        visited.add(new_node)
        return -1
        