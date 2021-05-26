class Solution:
    def minPartitions(self, n: str) -> int:
        n = sorted(n, reverse=True)
        return n[0]

    '''
    For Building Concept But Will Work Within Integer Range:
    def minPartitions(self, n: str) -> int:
        n = int(n)
        partitions = []
        while n:
            temp = n
            multiplier = 1
            divisor = 0
            while temp:
                remainder = temp % 10
                if remainder:
                    divisor += multiplier
                temp = int(temp / 10)
                multiplier *= 10
            partitions.append(divisor)
            n = n - divisor
        return len(partitions)
    '''
