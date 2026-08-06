class Solution:

    def dfs(self, graph, u, visited):
        visited.add(u)
        for v in graph[u]:
            if v not in visited:
                self.dfs(graph, v, visited)

    def createGraph(self, meetings):
        graph = {}
        for p1, p2, t in meetings:
            if t not in graph:
                graph[t] = {}
            if p1 not in graph[t]:
                graph[t][p1] = []
            graph[t][p1].append(p2)
            if p2 not in graph[t]:
                graph[t][p2] = []
            graph[t][p2].append(p1)
        return graph

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        # People will store all the people who knows the secret
        people = set([])
        # Person0 and firstPerson knows the secret from starting or time=0
        people.add(0)
        people.add(firstPerson)

        graph = self.createGraph(meetings)
        """
            graph will have a structure like:
            {
                time1: {p1: [p2,p3], p2:[p1,p3], p3:[p1]....},
                .
                .
                .                
                timen: {p2: [p1,p4], p1:[p2,p4], p4:[p2,p0]...}
            }
        """

        for time in graph:
            # Foreach time, Check for the all connected persons of people set.
            # After this time, persons of people set and their connections will be knowing the secret.
            visited = set([])
            for p in graph[time]:
                if p in people and p not in visited:
                    # Find connections
                    self.dfs(graph[time], p, visited)
            # Update people set as the connections also knows the secret.
            people.update(visited)

        return people
