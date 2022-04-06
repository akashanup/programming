class Solution:
    def fact(self, num, lookup):
        if num <= 1:
            return 1
        if num not in lookup:
            lookup[num] = num * self.fact(num-1, lookup)
        return lookup[num]

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        hashmap = {}
        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1


        arr.sort()
        triplets = set()
        for index,num in enumerate(arr):
            start = index+1
            end = len(arr)-1
            while start < end:
                tripletSum = num + arr[start] + arr[end]
                if tripletSum == target:
                    triplets.add((num, arr[start], arr[end]))
                    start += 1
                    end -= 1
                elif tripletSum < target:
                    start += 1
                else:
                    end -= 1

        count = 0

        lookup = {}

        # Use the fact of choosing r things from n things => nCr => n!/(n-r)!r!
        for i,j,k in triplets:
            if i != j != k:
                # If all are different
                count += (hashmap[i] * hashmap[j] * hashmap[k])
            elif i == j != k:
                # If two nums are same then choose 2 from total count of num
                count += (hashmap[k] * (self.fact(hashmap[i], lookup)//(2*self.fact(hashmap[i]-2, lookup))))
            elif i != j == k:
                # If two nums are same then choose 2 from total count of num
                count += (hashmap[i] * (self.fact(hashmap[j], lookup)//(2*self.fact(hashmap[j]-2, lookup))))
            else:
                # All are different then choose 3 from total count of num
                count += (self.fact(hashmap[i], lookup)//(6*self.fact(hashmap[i]-3, lookup)))

        return count % ((10**9)+7)
