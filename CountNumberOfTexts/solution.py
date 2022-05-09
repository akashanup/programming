class Solution:
    COMBINATIONS = {'2', '22', '222', '3', '33', '333', '4', '44', '444', '5', '55', '555', '6', '66', '666', '7', '77', '777', '7777', '8', '88', '888', '9', '99', '999', '9999'}
    
    def combinations(self, pressedKeys, idx, lookup):
        if idx >= len(pressedKeys):
            return 1
        if idx not in lookup:
            ans = 0
            i = idx+1
            while i <= len(pressedKeys) and pressedKeys[idx:i] in Solution.COMBINATIONS:
                ans += self.combinations(pressedKeys, i, lookup) % 1000000007
                i += 1
            lookup[idx] = ans
        return lookup[idx] % 1000000007
        
    def countTexts(self, pressedKeys: str) -> int:
        return self.combinations(pressedKeys, 0, {})
