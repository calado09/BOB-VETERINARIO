class Responsavel:
    """
    Representa o tutor/responsável por um ou mais animais.
    A relação com os animais é uma AGREGAÇÃO: a lista de pacientes
    guarda referências aos objetos Animal, mas quem realmente
    'dá baixa' nesses objetos é a classe Veterinaria.
    """

    def __init__(self, nome, telefone, email, endereco):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._endereco = endereco
        self._pacientes = []  # agregação: lista de objetos Animal associados

    def adicionar_paciente(self, animal):
        self._pacientes.append(animal)

    def listar_pacientes(self):
        if not self._pacientes:
            print(f'{self._nome} ainda não possui pacientes cadastrados.')
        else:
            print(f'Pacientes de {self._nome}:')
            for animal in self._pacientes:
                print(f'  - {animal}')

    def __str__(self):
        return (f'Responsável: {self._nome} | Telefone: {self._telefone} | '
                f'Email: {self._email} | Endereço: {self._endereco}')

    def exibir_info(self):
        print('-' * 100)
        print(self)
        self.listar_pacientes()
