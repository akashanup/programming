class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        i = 0
        # If i become be equal to len(version1) and len(version2) then loop would terminate.
        while i < len(version1) or i < len(version2):
            # If i == len(version1) then i would definitely be less than len(version2) or else loop would have been terminated before.
            if i >= len(version1):
                # version1[i] can be considered as 0.
                if int(version2[i]) > 0:
                    return -1
            # If i == len(version2) then i would definitely be less than len(version1) or else loop would have been terminated before.
            elif i >= len(version2):
                # version2[i] can be considered as 0.
                if int(version1[i]) > 0:
                    return 1
            # If at any point the current revision of both versions mismatch then return accordingly.
            else:
                v1 = int(version1[i])
                v2 = int(version2[i])
                if v1 < v2:
                    return -1
                if v1 > v2:
                    return 1
            i += 1
        return 0
