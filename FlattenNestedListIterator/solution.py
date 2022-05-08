# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = nestedList
        self.i = 0
        self.j = 0
        self.hashmap = {}
        for i in range(len(self.list)):
            if self.list[i].isInteger():
                self.hashmap[i] = [self.list[i].getInteger()]
            else:
                flatten = self.flatten(self.list[i].getList(), 0)
                if flatten:
                    self.hashmap[i] = flatten
        self.keys = list(self.hashmap.keys())
            
    
    def flatten(self, nums, i):
        if i == len(nums):
            return []
        ans = []
        if nums[i].isInteger():
            ans += [nums[i].getInteger()]
        else:
            ans += self.flatten(nums[i].getList(), 0)
        ans += self.flatten(nums, i+1)
        return ans
            
    
    def next(self) -> int:
        res = None
        key = self.keys[self.i]
        if self.j < len(self.hashmap[key]):
            res = self.hashmap[key][self.j]
            self.j += 1
        if self.j == len(self.hashmap[key]):
            self.j = 0
            self.i += 1
        return res
        
    
    def hasNext(self) -> bool:
         return self.i < len(self.keys)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
