class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        if not self.id or not self.number:
            return False
        if any(c.isalpha() for c in self.number):
            return False
        return True
    
    def getId(self):
        return self.id
    
    def getNumber(self):
        return self.number
    
    def __str__(self):
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str):
        self.fone: list[Fone] = []
        self.name = name
        self.fav: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if not fone.isValid():
            print("fail: invalid number")
            return
        self.fone.append(fone)
        

    def rmFone(self, index: int):
        self.fone.pop(index)

    def toggleFav(self):
        if self.fav == False:
            self.fav = True
            return
        else:
            self.fav = False
