class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # Create a graph with bus stopes as nodes and buses as edges
        busRoutes = {}
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in busRoutes:
                    busRoutes[stop] = set()
                busRoutes[stop].add(bus)

        visitedStops = set()
        visitedStops.add(source)
        # Add bus stop and number of buses taken in queue.
        queue = deque([(source, 0)])
        while queue:
            currentStop, busesTakenCount = queue.popleft()
            # Check for all the buses going through the current stop
            for bus in busRoutes[currentStop]:
                # Check for all the stops, the current bus goes to
                for stop in routes[bus]:
                    if target == stop:
                        return busesTakenCount + 1
                    if stop not in visitedStops:
                        visitedStops.add(stop)
                        queue.append((stop, busesTakenCount + 1))
                # Mark the current bus as visited to avoid duplicate processing
                routes[bus] = []
        return -1