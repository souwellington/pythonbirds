class Pessoa:
    def __init__(self,*filhos, nome = None,idade=35):
        self.idade = idade
        self.nome=nome
        self.filhos = list(filhos)


    def cumprimentar(self):
      return f'Olá {id(self)}'


if __name__ == '__main__':
    wellington= Pessoa(nome='wellington')
    ana = Pessoa(wellington,nome='ana')
    print(Pessoa.cumprimentar(ana))
    print(id(ana))
    print(ana.cumprimentar())
    print(ana.nome)
    print(ana.idade)
    for filho in ana.filhos:
        print(filho.nome)
    ana.sobrenome='Ferreira'
    del ana.filhos
    print(ana.__dict__)
    print(wellington.__dict__)







