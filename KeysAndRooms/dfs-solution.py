class Solution:
    def dfs(self, rooms, room, visited):
        if room not in visited:
            visited.add(room)
            for key in rooms[room]:
                self.dfs(rooms, key, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
