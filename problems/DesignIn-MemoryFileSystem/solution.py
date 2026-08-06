from abc import ABC, abstractmethod
from typing import List


class FileStructure(ABC):
    @abstractmethod
    def getType(self) -> bool:
        pass

    @abstractmethod
    def getChildren(self) -> List[str]:
        pass

    def size(self) -> int:
        pass


class File(FileStructure):
    name: str
    content: str

    def __init__(self, name: str) -> None:
        self.name = name
        self.content = ""

    def getType(self) -> str:
        return "File"

    def getChildren(self) -> List[str]:
        return [self.name]

    def read(self) -> str:
        return self.content

    def write(self, val: str) -> None:
        self.content += val


class Directory(FileStructure):
    name: str
    children: dict[str, FileStructure]

    def __init__(self, name: str) -> None:
        self.name = name
        self.children = {}

    def getType(self) -> str:
        return "Directory"

    def getChildren(self) -> list:
        children: list = []
        for child in self.children.values():
            children.append(child.name)
        return sorted(children)

    def addChild(self, name: str, fileStructure: FileStructure):
        self.children[name] = fileStructure


class FileStructureManager(ABC):
    @abstractmethod
    def create(self, directory: FileStructure, path: list):
        pass


class FileManager(FileStructureManager):
    def create(self, directory: Directory, path: str) -> File:
        file: File = File(path)
        directory.addChild(path, file)
        return file


class DirectoryManager(FileStructureManager):
    def create(self, directory: Directory, path: str) -> Directory:
        if not path:
            return directory
        currDir: Directory = directory
        for p in path:
            newDir: Directory = Directory(p)
            currDir.addChild(p, newDir)
            currDir = newDir
        return currDir


class FileSystem:

    def __init__(self):
        self.root: Directory = Directory("")
        self.fileManager: FileStructureManager = FileManager()
        self.directoryManager: FileStructureManager = DirectoryManager()

    @staticmethod
    def __getProcessedPath(path: str) -> list:
        path: list = path.split("/")
        if path[-1] == "":
            path = path[:-1]
        return path[1:]

    def __traversePath(self, path: list[str]) -> tuple[int, FileStructure]:
        fs: FileStructure = self.root
        idx = 0
        while idx < len(path):
            p = path[idx]
            if fs.__class__ is Directory and p in fs.children:
                fs = fs.children[p]
            else:
                break
            idx += 1
        return idx, fs

    def ls(self, path: str) -> List[str]:
        path: list = FileSystem.__getProcessedPath(path)
        _, fs = self.__traversePath(path)
        return fs.getChildren()

    def mkdir(self, path: str) -> None:
        path: list = FileSystem.__getProcessedPath(path)
        idx, fs = self.__traversePath(path)
        self.directoryManager.create(fs, path[idx:])

    def addContentToFile(self, filePath: str, content: str) -> None:
        path: list = FileSystem.__getProcessedPath(filePath)
        idx, fs = self.__traversePath(path)
        if fs.__class__ is File:
            fs.write(content)
        else:
            destinationDirectory: Directory = self.directoryManager.create(fs, path[idx:-1])
            file: File = self.fileManager.create(destinationDirectory, path[-1])
            file.write(content)

    def readContentFromFile(self, filePath: str) -> str:
        path: list = FileSystem.__getProcessedPath(filePath)
        _, fs = self.__traversePath(path)
        if fs.__class__ is File:
            return fs.read()


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

obj = FileSystem()
# print(obj.ls("/"))
# print(obj.mkdir("/aa/bbbb/cccc"))
# print(obj.addContentToFile("/aa/b/c/dddd", "hello"))
# print(obj.ls("/aa"))
# print(obj.readContentFromFile("/aa/b/c/dddd"))
print(obj.ls("/"))
print(obj.mkdir("/gh"))
print(obj.mkdir("/e"))
print(obj.mkdir("/jfo"))
print(obj.mkdir("/gh/znflyvnd"))
print(obj.ls("/gh"))
print(obj.addContentToFile("/mhdmck", "v"))
print(obj.readContentFromFile("/mhdmck"))
print(obj.addContentToFile("/gh/bbigs", "kzdi"))
print(obj.readContentFromFile("/gh/bbigs"))
