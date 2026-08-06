class Solution:
    def recur(self, num, n, index, lookup, temp):
        if index == n:
            lookup.append(temp)
        else:
            self.recur(num, n, index+1, lookup, temp + '*' + num[index])
            self.recur(num, n, index+1, lookup, temp + '+' + num[index])
            self.recur(num, n, index+1, lookup, temp + '-' + num[index])
            if temp[-1] == '0' and (len(temp) == 1 or (len(temp) > 1 and temp[-2] in ['*', '+', '-'])):
                self.recur(num, n, index+1, lookup, temp + 'NA')
            else:
                self.recur(num, n, index+1, lookup, temp + num[index])

    def addOperators(self, num: str, target: int) -> List[str]:
        lookup = []
        self.recur(num, len(num), 1, lookup, num[0])
        result = []
        for exp in lookup:
            if 'NA' not in exp and eval(exp) == target:
                result.append(exp)
        return result
