class Pointer:
    def __init__(self, index:int = 0):
        self.index = index

    def getIndex(self) -> int:
        return self.index

    def increment(self):
        self.index += 1

    def setIndex(self, index:int):
        self.index = index