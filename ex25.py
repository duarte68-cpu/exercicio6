


# classes e objeto 25/10/2024 exercicio 6

class usuarios:
    def __init__(self, nome, sobrenome, idade, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self. cidade = cidade
        
    def informacao(self):
        print(f'Meu nome é {self.nome} sobre nome é {self.sobrenome} minha idade {self.idade} minha cidade natal é {self.cidade} ')

usuario1 = usuarios(input('digite nome: '),input('sobrenome: '), input('idade: '),input('cidade natal: '))
usuario2 = usuarios(input('digite nome: '),input('sobrenome: '), input('idade: '),input('cidade natal: ') )
usuario3 = usuarios(input('digite nome: '),input('sobrenome: '), input('idade: '),input('cidade natal: '))

usuario1.informacao()
usuario2.informacao()
usuario3.informacao()            



