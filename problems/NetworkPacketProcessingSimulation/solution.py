class Buffer:
    def __init__(self, size, requests):
        self.size = size
        self.requests = requests

    def process(self):
        queue = []
        queueSize = 0
        for request in self.requests:
            while queueSize and queue[0] <= request[0]:
                # Pop all executed packets
                queue.pop(0)
                queueSize -= 1
            if queueSize < self.size:
                if queueSize == 0:
                    print(request, " : ", request[0])
                    queue.append(request[0] + request[1])
                else:
                    print(request, " : ", queue[-1])
                    queue.append(queue[-1] + request[1])
                queueSize += 1
            else:
                # Packet Dropped
                print(request, " : ", -1)


obj = Buffer(2, [[0, 2], [1, 4], [5, 3]])
# obj = Buffer(2, [[0, 1], [0, 1], [0, 1]])
obj.process()
