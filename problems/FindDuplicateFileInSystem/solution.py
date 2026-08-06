class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        lookupDict = {}
        for path in paths:
            dirContents = path.split(' ')
            for file in dirContents[1:]:
                content = file[file.index('txt(') + 4:-1]
                filePath = dirContents[0] + "/" + file[:file.index('txt(') + 3]
                if content in lookupDict:
                    lookupContent = lookupDict[content]
                    lookupContent.append(filePath)
                    lookupDict[content] = lookupContent
                else:
                    lookupDict[content] = [filePath]
        return [lookupDict[content] for content in lookupDict if len(lookupDict[content]) > 1]
