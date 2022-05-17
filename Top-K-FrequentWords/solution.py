import heapq

from sortedcontainers import SortedList


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        for word in words:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1

        heap = [[-freq, word] for word, freq in hashmap.items()]
        heapq.heapify(heap)

        frequentWords = {}
        i = 0
        while i < k:
            freq, word = heapq.heappop(heap)
            if -freq not in frequentWords:
                frequentWords[-freq] = SortedList()
            frequentWords[-freq].add(word)
            i += 1

        ans = [None] * k
        i = 0
        for freq in frequentWords:
            for word in frequentWords[freq]:
                ans[i] = word
                i += 1

        return ans
