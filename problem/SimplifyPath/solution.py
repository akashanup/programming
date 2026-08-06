"""
Logic:
    Since any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. So let's split the given path using '/' as the separator which will ease out the processing of path as now we don't need to deal with '/'. We can now treat the element at next index as a next directory or file.
    Initialize a stack which will hold the canonical path upto any index of splitted string.
    Now iterate over the splitted string and handle just two cases:
        If the current element is '..' then goto one directory up(simply pop from stack)
        If the current element is not "." then simply push the current element into stack with prefix "/"(explained above because every next element can be treated as the next directory or file)
        If the current element is "." then do nothing as it simply means to stay in same directory.
    At the end, if stack is not empty the join it and return or else if stack is empty then just return the root directory("/")
"""


def simplifyPath(path: str) -> str:
    path = path.split('/')
    path = [_ for _ in path if _]
    stack = []
    for ch in path:
        if ch == "..":
            if stack:
                stack.pop()
        elif ch != ".":
            stack.append("/"+ch)
    return "".join(stack) if stack else "/"


class Solution:
    pass
