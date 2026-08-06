class Solution:
    def __validateSegment(self, s):
        if not s:
            return False
        if len(s) == 1:
            return True
        if s[0] == "0":
            return False
        return 0 <= int(s) <= 255

    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        A = A.strip()
        n = len(A)
        if n > 12 or n < 4:
            return []
        ipAddresses = []
        i = 1
        while i <= 3 and i < n:
            j = i + 1
            while j <= i + 3 and j < n:
                k = j + 1
                while k <= j + 3 and k < n:
                    a = A[:i]
                    b = A[i:j]
                    c = A[j:k]
                    d = A[k:]

                    if self.__validateSegment(a) and self.__validateSegment(b) and self.__validateSegment(c) and self.__validateSegment(d):
                        ipAddresses.append(a + "." + b + "." + c + "." + d)
                    k += 1
                j += 1
            i += 1
        return ipAddresses


print(Solution().restoreIpAddresses("0100100"))
print(Solution().restoreIpAddresses("0000"))
