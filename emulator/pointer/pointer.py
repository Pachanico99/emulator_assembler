class Pointer:
    def __init__(self, index:int = 0):
        self.index = index

    def get_index(self) -> int:
        return self.index

    def increment(self):
        self.index += 1

    def set_index(self, index:int):
        self.index = index