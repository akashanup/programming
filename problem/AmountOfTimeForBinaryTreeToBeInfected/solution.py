from collections import defaultdict, deque


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        self.__dfs(root, graph)
        visited = set()
        queue = deque([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                current_node = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return time

    def __dfs(self, node, graph):
        if node is None:
            return
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
        self.__dfs(node.left, graph)
        self.__dfs(node.right, graph)