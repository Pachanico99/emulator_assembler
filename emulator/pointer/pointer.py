class Pointer:
    def __init__(self, index:int):
        self.index = index

    def nextLine(self):
        self.index += 1

    def jumpLine(self, index):
        self.index = index

    def getIndex() -> int:
        return self.index