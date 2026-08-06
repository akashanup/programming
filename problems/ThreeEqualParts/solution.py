class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        arr = [str(i) for i in arr]
        noOf1s = arr.count("1")
        # If count of 1 is not a multiple of three then breaking the arr into three equal parts is not possible.
        if noOf1s % 3:
            return [-1, -1]
        arrLen = len(arr)
        noOf1s //= 3
        parts = []
        count = 0
        # Break the arr into three parts having equal number of 1 in each part and save the index as per requirement.
        for m in range(arrLen):
            if arr[m] == "1":
                count += 1
            if count == noOf1s:
                parts.append(m)
                if len(parts) == 2:
                    parts[1] += 1
                    break
                count = 0

        '''
            As per the logic above,
            -> int value of part1 will be less than or equal to part2
            -> int value of part2 will be less than or equal to part3
            So, if we can make part3 equal to part2 by moving the leading zeros of part3 to part2 and then make part2 equal to part1 by moving the leading zeros of part2 to part1, we can get three equal parts
            Else return [-1, -1]
        '''

        # Modify part2 and part3 to become equal
        part2 = int("".join(arr[parts[0] + 1:parts[1]]), 2)
        part3 = int("".join(arr[parts[1]:]), 2)
        while part3 > part2:
            # Check for leading zero in part3
            if arr[parts[1]:][0] == "0" and parts[1] < arrLen - 1:
                parts[1] += 1
                part2 = int("".join(arr[parts[0] + 1:parts[1]]), 2)
            else:
                return [-1, -1]
        if part3 != part2:
            return [-1, -1]

        # Modify part1 and part2 to become equal
        part1 = int("".join(arr[:parts[0] + 1]), 2)
        while part2 > part1:
            # Check for leading zero in part2
            if arr[parts[0] + 1:parts[1]][0] == "0":
                parts[0] += 1
                part1 = int("".join(arr[:parts[0] + 1]), 2)
            else:
                return [-1, -1]
        if part2 != part1:
            return [-1, -1]

        return parts
