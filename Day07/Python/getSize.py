from functools import reduce


class File:
    def __init__(self, fileSize: int, fileName: str) -> None:
        self.fileName = fileName
        self.fileSize = fileSize


class DirTree:
    class Node:
        def __init__(self, dirName: str, parent=None) -> None:
            self.dirName = dirName
            self.parent = parent
            self.childrenFiles = []
            self.childrenDirs = []

        def ls(self) -> list:
            return self.childrenDirs + self.childrenFiles

        def addFile(self, fileSize: int, fileName: str) -> None:
            self.childrenFiles.append(File(fileSize, fileName))

        def addDir(self, dirName: str, parent) -> None:
            self.childrenDirs.append(DirTree.Node(dirName, parent))

        def getTotalSize(self) -> int:
            total = reduce(lambda x, y: x + y.fileSize, self.childrenFiles)
            total += sum([i.getTotalSize() for i in self.childrenDirs])

            return total

    def __init__(self) -> None:
        self.root = self.Node('/')

    def findDir(self, dirName: str, node: Node) -> Node | None:
        if (node == None):
            return

        if (node.dirName == dirName):
            return node

        for child in node.childrenDirs:
            nodeFound = self.findDir('a', child)
            if nodeFound != None:
                return nodeFound

        return None


class FileHandler:
    def __init__(self, system: DirTree) -> None:
        self.system = system
        self.currDir = system.root

    def cd(self, path: str) -> None:
        if path == '..':
            self.currDir = self.currDir.parent
            return

        for node in self.currDir.childrenDirs:
            if node.dirName == path:
                self.currDir = node
                break

    def ls(self, files: list[str]) -> None:
        for item in files:
            item = self.sanitizeInput(item)

            if type(item) == DirTree.Node:
                if not (item in self.currDir.childrenDirs):
                    self.currDir.childrenDirs.append(item)
                    continue
                continue

            if not (item in self.currDir.childrenFiles):
                self.currDir.childrenFiles.append(item)

    def sanitizeInput(self, file: str) -> File | DirTree.Node:
        if file.startswith('dir'):
            folder = DirTree.Node(file.split(' ')[-1], self.currDir)
            return folder

        file = file.split(' ')
        return File(int(file[0]), file[1])


Filepath = DirTree()
fileHandler = FileHandler(Filepath)

with open('./Day07/input.txt', 'r') as file:
    commands = file.read().splitlines()

listOfNonCommands = []
for i in range(len(commands)):
    if commands[i].startswith('$'):
        listOfNonCommands.append(i - 1)
        if commands[i].startswith('$ ls'):
            listOfNonCommands.append(i + 1)

listOfNonCommands.append(len(commands) - 1)
listOfNonCommands = list(
    filter(lambda c: not commands[c].startswith('$'), listOfNonCommands))

listOfNonCommands = [commands[i] for i in listOfNonCommands]

print(listOfNonCommands.__len__())

# for command in commands:
#     if command.startswith('$'):
#         if 'cd' in command:
#             fileHandler.cd(command.split(' ')[-1])
#         else:
#             fileHandler.ls()