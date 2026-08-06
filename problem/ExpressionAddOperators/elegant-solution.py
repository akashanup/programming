class Solution:
    def recur(self, num, n, target, index, lookup, temp):
        if index == n:
            if 'NA' not in temp and eval(temp) == target:
                lookup.append(temp)
        else:
            self.recur(num, n, target, index+1, lookup, temp + '*' + num[index])
            self.recur(num, n, target, index+1, lookup, temp + '+' + num[index])
            self.recur(num, n, target, index+1, lookup, temp + '-' + num[index])
            if temp[-1] == '0' and (len(temp) == 1 or (len(temp) > 1 and temp[-2] in ['*', '+', '-'])):
                self.recur(num, n, target, index+1, lookup, temp + 'NA')
            else:
                self.recur(num, n, target, index+1, lookup, temp + num[index])

    def addOperators(self, num: str, target: int) -> List[str]:
        lookup = []
        self.recur(num, len(num), target, 1, lookup, num[0])
        return lookup
