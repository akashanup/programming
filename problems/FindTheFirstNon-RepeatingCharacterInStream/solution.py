from collections import deque


class Solution:
    def firstNonRepeatingCharacter(self, stream):
        result = ""
        lookup = {}
        queue = deque([])
        for ch in stream:
            # Store the elements from stream into a queue
            queue.append(ch)
            # Store the count of the element to check for repeated ones
            if ch not in lookup:
                lookup[ch] = 0
            lookup[ch] += 1
            """
            This would guarantee that top of queue would always be a non repeating characters. 
            If not then keep dequeueing till we have non repeating character.
            """
            while queue and queue[0] in lookup and lookup[queue[0]] > 1:
                queue.popleft()
            result += queue[0] if queue else '#'
        return result