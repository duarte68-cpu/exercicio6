


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

class carro:
    def __init__(self, marca, fabricacao, pintura, modelo):
        self.marca = marca
        self.fabricacao = fabricacao
        self.pintura = pintura
        self.modelo = modelo
    def  informacao(self):
        print(f'O modelo do veiculo: {self.modelo} Ano de frabricação {self.fabricacao} Cor do veiculo {self.pintura}')
        
veiculo1 = carro(input('Digite o modelo do veiculo: '),input('digite a fabricação de veiculo: '),input('Digite a cor do veiculo: '),input('digite o modelo do veiiculo: '))

veiculo1.informacao()        


class pessoa:
    def __init__(self, nome_completo, data_nascimento, rg, cpf, cidade, ):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.rg = rg
        self.cpf = cpf
        self.cidade = cidade
    
    def informacao(self):
        print(f'Nome: {self.nome_completo}')
        print(f'Data de nascimento: {self.data_nascimento}')
        print(f'Rg da pessoa: {self.rg}')
        print(f'insira o cpf: {self.cpf}')
        print(f'cidade onde nasceu: {self.cidade}')

pessoa1 = pessoa(input('informe o nome completo: '), input('data de nascimento: '), input('insira rg: '), input('insira CPF: '), input('cidade onde nasceu: '))

pessoa1.informacao()      



