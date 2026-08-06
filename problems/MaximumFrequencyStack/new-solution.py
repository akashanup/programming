"""
Logic:
    We can use a priority queue to keep the most frequent element on top.
    To implement max priority in Python you can negate the values while pushing them into the queue.
    So when we pop from the queue it will give us the max value.
    I am using a dictionary to keep track of the frequency of the elements and a counter(cnt) to keep track of the order in which the elements are pushed.
    We just push [-freq, -cnt, value] into the queue so when there is a tie for freq it compares the counter cnt.
    The most frequent element will be on the top and we can get it by popping it from the queue every time.
    And when we pop we still have the updated frequency of the element in the queue as we push all versions of the element in the queue.
"""
import collections
import heapq


class FreqStack:

    def __init__(self):
        self.heap = []
        self.dict = collections.defaultdict(int)
        self.cnt = 0

    def push(self, x: int) -> None:
        # represents the order in which we push elements in the queue
        self.cnt += 1
        self.dict[x] += 1
        # push frequency, counter and element in the queue
        heapq.heappush(self.heap, [-self.dict[x], -self.cnt, x])

    def pop(self):
        largest = heapq.heappop(self.heap)
        # largest[2] == element
        self.dict[largest[2]] -= 1
        return largest[2]
