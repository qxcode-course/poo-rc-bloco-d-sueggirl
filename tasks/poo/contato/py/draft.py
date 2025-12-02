class Fone:
    def __init__(self, id: str, number:str):
        self.id = id
        self.number = number

    def getId(self):
        return self.id
    def getNumber(self):
        return self.number
    
    def eValido(self) -> bool:
        if not self.id or not self.number:
            return False 
        if any(p.isalpha() for p in self.number):
            return False
        return True
    
    def __str__(self):
        return f"{self.id}:{self.number}"
    

class Contato:
    def __init__(self, nome: str, fone: list[Fone] = []):
        self.fone = fone
        self.nome = nome 
        self.favorito: bool = False

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if not fone.eValido():
            print("fail: invalid number")
            return 
        self.fone.append(fone)

    def delFone(self, index: int):
        self.fone.pop(index)
    
    def trocarFavorito(self):
        if self.favorito == False:
            self.favorito = True
            return
        else:
            self.favorito = False

    def eFavorito(self) -> bool:
        if self.favorito == True:
            return True
        else:
            return False
        
    def getFones(self):
        return self.fone
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome: str):
        self.nome = nome

    def __str__(self):
        fone = ", ".join([str(x) for x in self.fone])
        if self.favorito == True:
            return f"@ {self.nome} [{fone}]"
        else:
            return f"- {self.nome} [{fone}]"
        
def main():
    contatos = Contato("")
    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split()
        if args[0] == "end":
            break 
        elif args[0] == "show":
            print(contatos)
        elif args[0] == "init":
            nome = args[1]
            contatos.setNome(nome)
        elif args[0] == "add":
            id = args[1]
            number = args[2]
            contatos.addFone(id, number)
        elif args[0] == "rm":
            index = int(args[1])
            contatos.delFone(index)
        elif args[0] == "tfav":
            contatos.trocarFavorito()
main()


