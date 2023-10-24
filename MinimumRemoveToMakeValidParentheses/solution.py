class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        totalClosed = s.count(')')
        exhaustedClosed = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] in ('(', ')'):
                if s[i] == ')':
                    # If there are any open '(' i.e, open > 0 then use the current ')' to close it.
                    # Else open <= 0 then remove the current ')'
                    if open > 0:
                        # A pair is found.
                        stack.append(s[i])
                        open -= 1
                    else:
                        exhaustedClosed += 1
                else:
                    # If the current '(' can be mapped to further ')' then map it.
                    # Else (totalClosed - exhaustedClosed <= 0) then remove the current '(' as its corresponding pair will not be found.
                    if totalClosed > exhaustedClosed:
                        # A pair will be found.
                        stack.append(s[i])
                        open += 1
                        exhaustedClosed += 1
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
