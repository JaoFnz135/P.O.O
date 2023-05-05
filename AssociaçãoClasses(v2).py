from datetime import *
class Paciente:
    def __init__(self,id_pac,nome_pac,dt_nasc,contato):
        self.__id_paciente = id_pac
        self.nome_paciente = nome_pac 
        self.__dt_nasc = dt_nasc
        self.__contato = contato

    @property
    def id_paciente(self):
        return self.__id_paciente
    @property
    def dt_nasc(self):
        return self.__dt_nasc
    @property
    def contato(self):
        return self.__contato

class Medico:
    def __init__(self,id_medico,crm,nome_medico,esp):
        self.__id_medico = id_medico
        self.__crm = crm
        self.nome_medico = nome_medico
        self.especialidade = esp

    @property
    def id_medico(self):
        return self.__id_medico
    @property
    def crm(self):
        return self.__crm

class ConsultaMedica:
    def __init__(self,id_consulta,medico,paciente,data,pago=False):
        self.__id_consulta = id_consulta
        if type(medico)==Medico:
            self.__medico = medico
        else:
            raise "Error!"
        if type(paciente)==Paciente:
            self.__paciente = paciente
        else:
            raise "Error!"
        self.__data = data # fazer a validação de data
        self.__pago = pago
        self.__data_retorno = None

    @property
    def id_consulta(self):
        return self.__id_consulta
    @property
    def medico(self):
        return self.__medico
    @property
    def paciente(self):
        return self.__paciente
    @property
    def pago(self):
        return self.__pago
    @property
    def data_retorno(self):
        return self.__data_retorno


    def __str__(self):
        v1 = f'Consulta marcada para a data: {self.__data}\nPaciente:{self.__paciente.nome_paciente}\nMédico:{self.__medico.nome_medico}'
        return v1

def menu():
    print("1 - Cadastrar Paciente")
    print("2 - Cadastrar Médico")
    print("3 - Marcar consulta")
    print("4 - Pagar consulta")
    print("5 - Cancelar consulta")
    print("6 - Marcar retorno")
    print("7 - Sair")
    op = int(input("Entre com a opção:"))
    if op > 0 and op < 8:
        return op
    else:
        raise ValueError

def escolher_data():
    fds = [5, 6]
    while True:
        try:
            d = datetime.strptime(input("Data da consulta/Retorno:\n"),"%d/%m/%Y").date()
            if d <= date.today() or d.weekday() in fds:
                raise ValueError("Data de consulta menor que data atual ou caiu em um final de semana.")
            else:
                data = d.strftime("%d/%m/%Y")
                break
        except:
            print('Digite a data desse modo dd/mm/aa!!')      
    return data

def cadastrarPaciente():
    cpf = input('CPF do paciente: ')
    nome = input('Nome do paciente: ')
    data_nasc = input('Data de Nascimento: ')
    contato = input('Contato: ')
    return Paciente(cpf, nome, data_nasc, contato)
    
def cadastrarMedico():
    pass
def marcarConsulta():
    pass

def main():
    while True:
        op = menu()
        if op==1:
            pass
            # dar os inputs para os atributos
            # criar o objeto
            # inserir na lista
        elif op == 2:
            pass
            # dar os inputs para os atributos
            # criar o objeto
            # inserir na lista 
        elif op==3:
            pass            
            # dar os inputs para os atributos
            # pegar o nome do paciente
            # buscar na lista de pacientes o objeto correspondente
            # pegar o nome do medico
            #buscar na lista de médicos o objeto correspondente
            #criar o objeto ConsultaMedica
            # inserir na lista de consultas médicas
        elif op==4:
            pass
            # pegar na lista de consultas (por data, por nome do paciente ou por nome do médico)
            # retornar o objeto correspondente ao critério da pesquisa

if __name__ == '__main__':
    main()