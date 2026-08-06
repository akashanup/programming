"""
Logic:
    1.This problem resembles with Longest Increasing Subsequence so we will use a similar logic of building the longest increasing subsequence in the most optimal way(in O(NlogN) time).
    2. Since the given envelopes are in random order so the first thing that we have to do is to sort those envelopes in ascending order of their width (and descending order of their height in case of same width) or vice versa.
    3. The above sorting is done in a particular mentioned way so as to build the lis(our answer variable) as follows:
        i. While iterating over envelopes(sorted as per point #2), for width[i] if width[i-1] < width[i] and if height[i-1] < height[i] then we add the ith envelope in lis, if height[i-1] >= height[i] then we check for next envelope.
        ii. While iterating over envelopes(sorted as per point #2), for width[i] if width[i-1] == width[i] then we take only that envelope of width[i] whose height is just greater than envelope j where width[j] is just small than width[i]
    4. Point #3 basically means that we have to build lis over the heights of envelope and widths will be already taken care of because of particular (mentioned in point #2) way of sorting.
"""


class Solution:
    def binarySearch(self, heights, minHeight):
        start = 0
        end = len(heights)
        while start < end:
            mid = start + ((end - start) // 2)
            if heights[mid] < minHeight:
                start = mid + 1
            else:
                end = mid
        return start

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        heights = [h for _, h in envelopes]
        lis = []
        
        for height in heights:
            idx = self.binarySearch(lis, height)
            if idx == len(lis):
                lis.append(height)
            else:
                lis[idx] = height

        return len(lis)
