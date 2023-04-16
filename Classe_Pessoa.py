class pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado="Vivo", estado_civil="Solteiro", conjuge=None):
        self.nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjuge = conjuge

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        print('Sem permissão')
    
    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, valor):
        print('Sem permissão')
    
    @property
    def altura(self):
        return f'{self.__altura} cm'
    @altura.setter
    def altura(self, valor):
        print('Sem permissão')
        
    @property
    def sexo(self):
        return self.__sexo
    @sexo.setter
    def sexo(self, valor):
        print('Sem permissão')
        
    
    def envelhecer(self):
        if self.estado == 'Vivo':
            self.__idade += 1
            if self.__idade <= 21:
                self.__altura += 0.5
                print(f'{self.nome} está com {self.idade} anos e {self.altura} cm de altura')
            else:
                print(f'{self.nome} está com {self.idade} anos e {self.altura} cm de altura')
        elif self.sexo == 'M':
            print(f'{self.nome} está morto.')
        else:
            print(f'{self.nome} está morta.')

    def engordar(self, valor):
        if self.estado == 'Vivo':
            self.__peso += valor
        elif self.sexo == 'M':
            print(f'Operação não realizada. {self.nome} está morto.')
        else:
            print(f'Operação não realizada. {self.nome} está morta.')
    
    def emagrecer(self, valor):
        if self.estado == 'Vivo':
            self.__peso -= valor
        elif self.sexo == 'M':
            print(f'Operação não realizada. {self.nome} está morto.')
        else:
            print(f'Operação não realizada. {self.nome} está morta.')
    
    def crescer(self, valor):
        if self.estado == 'Vivo':
            if self.__idade < 21:
                self.__altura += valor 
                pass
            else:
                print(f'{self.nome} não pode mais crescer, pois está com 21 anos ou mais.')
        elif self.sexo == 'M':
                print(f'Operação não realizada. {self.nome} está morto.')
        else:
            print(f'Operação não realizada. {self.nome} está morta.')

    def casar(self, conjuge):
        if self.estado == 'Vivo' and conjuge.estado == 'Vivo':
            if self.__idade >=18 and conjuge.__idade >= 18:
                if self.estado_civil != 'Casado' and conjuge != 'Casado':
                    self.estado_civil = 'Casado'
                    self.conjuge = conjuge
                    conjuge.estado_civil = 'Casado'
                    conjuge.conjuge = self
                else:
                    if self.estado_civil != 'Casado':
                        print(f'Casamento não realizado. {self.nome} é casado.')
                    else:
                        print(f'Casamento não realizado. {conjuge.nome} é casada.')
            else:
                if self.__idade <18:
                    print(f'Casamento não permitido. {self.nome} é de menor')
                else:
                    print(f'Casamento não permitido. {conjuge.nome} é de menor')
        elif self.sexo == 'M' or conjuge.sexo == 'M':
            if self.estado == 'Morto':
                print(f'Casamento não realizado. {self.nome} está morto.')
            else:
                print(f'Casamento não realizado. {conjuge.nome} está morto.')
        else:
            if self.estado == 'Morto':
                print(f'Casamento não realizado. {self.nome} está morta.')
            else:
                print(f'Casamento não realizado. {conjuge.nome} está morta.')


            
            
    def morrer(self, conjuge):
        if self.estado == 'Vivo':
            self.estado = 'Morto'
            if self.estado_civil == 'Casado':
                conjuge.estado_civil = 'Viúvo'
                conjuge.conjuge = None
                print(f'{self.nome} morreu.')
            else:
                print(f'{self.nome} morreu.')
        elif self.sexo == 'M':
                print(f'Operação não realizada. {self.nome} já está morto.')
        else:
                print(f'Operação não realizada. {self.nome} já está morta.')
            
            
        
def menu():
    while True:
        try:
            print('_'*55)
            print('1 - Listar pessoas')
            print('2 - Nova pessoa')
            print('3 - Envelhecer')
            print('4 - Engordar')
            print('5 - Emagrecer')
            print('6 - Crescer')
            print('7 - Casar')
            print('8 - Morrer')
            print('9 - Alterar dados de uma pessoa')
            print('_'*55)
            resp = int(input('Escolha uma opção acima:\n>>> '))
            if resp > 0 and resp < 10 and resp != str and resp == float:
                return resp            
        except:
            print('Ação não encontrada. Tente novamente.')
            
def nova_pessoa(l):
    while True:
        try:
            nome = input('Nome da pessoa: ')
            idade = int(input('Idade: '))
            peso = float(int('Peso: '))
            altura = int(input('Altura(cm): '))
            preco = 300
            l.append(consulta(data, nome, area_med, nome_med, preco))
            consulta_atual = l[-1]
            print(consulta_atual)
        except:
            print('Houve um erro. Por favor, preencha os campos novamente.')
            
#def __init__(self, nome, idade, peso, altura, sexo, estado="Vivo", estado_civil="Solteiro", conjuge=None):
#CÓDIGO PRINCIPAL
def main():
    pessoas = [pessoa('João', 18, 63, 179, 'M'), 
         pessoa('Pedro', 13, 54, 156, 'M'),
         pessoa('Patricia', 30, 51, 165, 'F'),
         pessoa('Fatima', 21, 57, 170, 'F'), 
         pessoa('Laura', 50, 46, 147, 'F'),
         pessoa('Petunia', 27, 64, 165, 'M'), 
         pessoa('Leo', 17, 51, 175, 'M'),
         pessoa('Patricia', 40, 71, 175, 'F')]

    for i in range(8):
        print(f'Nome: {pessoas[i].nome}')
        print(f'Idade: {pessoas[i].idade}')
        print(f'Peso: {pessoas[i].peso} kg')
        print(f'Altura: {pessoas[i].altura} cm')
        print(f'Sexo(M/F): {pessoas[i].sexo}')
        print(f'Estado: {pessoas[i].estado}')
        print(f'Estado civil: {pessoas[i].estado_civil}')
        print(f'Conjuge: {pessoas[i].conjuge}')
        print()

    print('Idade:')
    print(pessoas[1].idade)
    pessoas[1].envelhecer()
    pessoas[1].idade = 18
    print(pessoas[1].idade)
    pessoas[3].envelhecer()

    print('\nPeso:')
    print(pessoas[3].peso)
    pessoas[3].engordar(3)
    pessoas[3].peso = 200
    print(pessoas[3].peso)
    print(pessoas[2].peso)
    pessoas[2].emagrecer(2)
    print(pessoas[2].peso)


    print('\nAltura:')
    print(pessoas[6].altura)
    pessoas[6].crescer(2)
    pessoas[6].altura = 120
    print(pessoas[6].altura)

    pessoas[0].casar(pessoas[5])
    pessoas[1].casar(pessoas[3])
    pessoas[3].casar(pessoas[5])
    print(pessoas[0].estado_civil)
    print(pessoas[5].estado_civil)
    pessoas[0].casar(pessoas[7])
    pessoas[0].morrer(pessoas[5])
    print(pessoas[5].estado_civil)
    pessoas[0].casar(pessoas[6])
    pessoas[3].casar(pessoas[5])

    





    
    #while True:
        #try:
            #r = menu()
            #if r == 1

            

        #except:

if __name__ == '__main__':
    main()


