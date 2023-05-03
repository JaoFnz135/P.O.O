class Paciente:
    def __init__(self, id_paciente, nome, dt_nasc, contato):
        self.__id_paciente = id_paciente
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.contato = contato
        pass

    def __str__(self):
        return f'\nNome:{self.nome}\nData de nascimento: {self.dt_nasc}\nContato: {self.contato}'

class Medico:
    def __init__(self, id_medico, crm, nome, especialidade) :
        self.__id_medico = id_medico
        self.crm = crm
        self.nome = nome
        self.especialidade = especialidade
    
    def __str__(self):
        return f'\nCRM: {self.crm} \nNome: {self.nome } \nEspecialidade: {self.especialidade}'

class consulta_medica:
    def __init__(self, id_consulta, medico, paciente, data, data_retorno='00/00/0000', pago=True):
        self.__id = id
        if type(medico)== Medico:
            self.__medico = medico
        else:
            raise 'Error!'
        if type(paciente) == Paciente:
            self.__paciente = paciente
        else:
            raise 'Error!'
        self.data = data
        self.pago = pago
        self.data_retorno = data_retorno

    def __str__(self):
        return f'\nData da Consulta: {self.data}\nPaciente: {self.__paciente.nome}\nMédico: {self.__medico.nome} '

Maria = Paciente(32165414521, 'Maria', '14/12/2002', 8699854778)
print(Maria)
João = Medico(32165414521, 'João', 1234, 'Ortopedista')
print(João)
c1 = consulta_medica(1, João, Maria, '02/05/2023')
print(c1)
