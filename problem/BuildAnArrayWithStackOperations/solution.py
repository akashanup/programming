class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        i = 0
        num = 1
        while i < len(target) and num <= n:
            operations.append("Push")
            if num == target[i]:
                num += 1
                i += 1
            else:
                operations.append("Pop")
                num += 1
        return operations