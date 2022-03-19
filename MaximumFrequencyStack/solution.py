class FreqStack:

    def __init__(self):
        """
            Hashtable to store elements as keys and their frequency as values
            Example: {5:3, 7:2, 4:1}
        """
        self.numsFreq = {}
        """
            Hashtable to store frequencies as keys and list of elements having same frequeny. This structure will ensure the elements are popped which has the max frequency and are closest to top.
            Example: {3: [5], 2:[5,7], 1:[5,7,4]}
        """
        self.freqNums = {}
        # At any time maxFreq will have the maximum frequency of any element
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # Store/Update frequency of each element
        if val in self.numsFreq:
            self.numsFreq[val] += 1
        else:
            self.numsFreq[val] = 1

        # Store/Update max frequency
        self.maxFreq = max(self.maxFreq, self.numsFreq[val])

        # Store/Update frequency wise elements
        if self.numsFreq[val] in self.freqNums:
            self.freqNums[self.numsFreq[val]].append(val)
        else:
            self.freqNums[self.numsFreq[val]] = [val]

    def pop(self) -> int:
        # Pop the element whose frequency matches with maxFreq
        popped = self.freqNums[self.maxFreq].pop()
        # Decrease the frequency of popped element by 1
        self.numsFreq[popped] -= 1
        # If there is no element having frequency as maxFreq then decrease the maxFreq by 1 as the next element that would be popped out will have frequency = maxFreq-1
        if not self.freqNums[self.maxFreq]:
            self.maxFreq -= 1
        return popped

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
