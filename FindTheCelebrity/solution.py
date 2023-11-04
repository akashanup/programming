class Solution:
    def findCelebrity(self, n, graph):
        stack = [_ for _ in range(n)]
        while len(stack) > 1:
            a, b = stack.pop(), stack.pop()
            if graph[a][b] == 1:
                # Person a knows person b
                stack.append(b)
            elif graph[b][a] == 1:
                # Person b knows person a
                stack.append(a)

        potentialCelebrity = stack.pop()
        # Check whether everyone knows the potentialCelebrity
        for i in range(len(graph)):
            if graph[i][potentialCelebrity] == 0:
                return -1
        # Check whether potentialCelebrity doesn't know anyone except him/her self
        for i in range(len(graph)):
            if i != potentialCelebrity and graph[potentialCelebrity][i] == 1:
                return -1

        return potentialCelebrity


