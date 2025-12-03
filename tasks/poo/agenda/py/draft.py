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

    def isFav(self) -> bool:
        if self.fav == True:
            return True
        else:
            return False
        
    def getFones(self):
        return self.fone
    
    def getName(self):
        return self.name
    
    def setName(self, name: str):
        self.name = name

    def matches(self, pattern: str) -> bool:
        if pattern in self.name:
            return True
        for f in self.fone:
            if pattern in f.id or pattern in f.number:
                return True
        return False

    def __str__(self):
        fone = ", ".join([str(x) for x in self.fone])
        if self.fav == True:
            return f"@ {self.name} [{fone}]"
        else:
            return f"- {self.name} [{fone}]"
        
class Agenda:
    def __init__(self):
        self.contact: list[Contact] = []

    def findPosByName(self, name: str) -> int:
        for i, c in enumerate(self.contact):
            if c.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: list[Fone]):
        pos = self.findPosByName(name)
        if pos == -1:
            contact = Contact(name)
            for f in fones:
                contact.addFone(f.id, f.number)
            self.contact.append(contact)
        else:
            contact = self.contact[pos]
            for f in fones:
                contact.addFone(f.id, f.number)

    def rmContact(self, name: str):
        pos = self.findPosByName(name)
        if pos == -1:
            print("fail: contact not found")
            return
        self.contact.pop(pos)

    def getContact(self, name: str):
        pos = self.findPosByName(name)
        if pos == -1:
            return None
        return self.contact[pos]

    def search(self, pattern: str) -> list[Contact]:
        result = []
        for c in self.contact:
            if c.matches(pattern):
                result.append(c)
        return sorted(result, key=lambda x: x.getName())
    
    def getFavorited(self) -> list[Contact]:
        return [c for c in self.contact if c.isFav()]

    def getContacts(self) -> list[Contact]:
        return self.contact
    
    def __str__(self):
        order = sorted(self.contact, key= lambda x:x.getName())
        return "\n".join(str(contact) for contact in order)
        
def main():
    agenda = Agenda()
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            name = args[1]
            fone = []
            for token in args[2:]:
                try:
                    id, number = token.split(":")
                    fone.append(Fone(id, number))
                except:
                    print("fail: invalid fone format")
            agenda.addContact(name, fone)
        elif args[0] == "rm":
            agenda.rmContact(args[1])
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)
            if contact is None:
                print("fail: contact not found")
            else:
                contact.rmFone(index)
        elif args[0] == "tfav":
            name = args[1]
            contact = agenda.getContact(name)
            if contact is None:
                print("fail: contact not found")
            else:
                contact.toggleFav()
        elif args[0] == "favs":
            for c in agenda.getFavorited():
                print(c)
        elif args[0] == "search":
            pattern = args[1]
            en = agenda.search(pattern)

            for contato in en:
                print(contato)
main()