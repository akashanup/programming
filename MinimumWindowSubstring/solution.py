class Solution:
    def compareHashmap(self, t, s):
        for ch, frq in t.items():
            if ch not in s or s[ch] < frq:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tHashmap = {}
        for ch in t:
            if ch in tHashmap:
                tHashmap[ch] += 1
            else:
                tHashmap[ch] = 1

        sHashmap = {}
        left, right = 0, 0
        shortest = len(s) + 1
        ans = None
        while left <= right:
            if right < len(s):
                if s[right] in sHashmap:
                    sHashmap[s[right]] += 1
                else:
                    sHashmap[s[right]] = 1
                right += 1

            while self.compareHashmap(tHashmap, sHashmap):
                if shortest > right - left:
                    shortest = right - left
                    ans = s[left:right]
                sHashmap[s[left]] -= 1
                left += 1

            if right == len(s):
                break

        if shortest != len(s) + 1:
            return ans
        return ""
