from item_banco import ItemBanco


class Animal(ItemBanco):
    """
    Classe Animal herda de ItemBanco (nome e idade).
    Adiciona os atributos específicos de um paciente da clínica veterinária.
    """

    def __init__(self, nome, idade, sintomas, doente, alergia, raca, responsavel):
        super().__init__(nome, idade)   # reaproveita o construtor da superclasse
        self._sintomas = sintomas
        self._doente = doente
        self._alergia = alergia
        self._raca = raca
        self._responsavel = responsavel  # nome do responsável (composição feita pela classe Veterinaria)

    def verificar_saude(self):
        if str(self._doente).lower() == 'sim':
            print(f'Situação de saúde: {self._nome} está doente.')
        else:
            print(f'Situação de saúde: {self._nome} não está doente.')

    def exibir_info(self):
        print('-' * 100)
        print(f'Paciente: {self._nome} | Idade: {self._idade} | Raça: {self._raca}')
        print(f'Sintomas: {self._sintomas} | Alergia: {self._alergia}')
        print(f'Responsável: {self._responsavel}')

    def __str__(self):
        return f'{self._nome} ({self._raca}) - Responsável: {self._responsavel}'


class Cachorro(Animal):
    """
    Subclasse de Animal. Demonstra herança + polimorfismo:
    adiciona o atributo 'porte' e sobrescreve exibir_info().
    """

    def __init__(self, nome, idade, sintomas, doente, alergia, raca, responsavel, porte):
        super().__init__(nome, idade, sintomas, doente, alergia, raca, responsavel)
        self._porte = porte  # pequeno, médio, grande

    def exibir_info(self):
        super().exibir_info()
        print(f'Tipo: Cachorro | Porte: {self._porte}')


class Gato(Animal):
    """
    Subclasse de Animal. Demonstra herança + polimorfismo:
    adiciona o atributo 'ambiente' e sobrescreve exibir_info().
    """

    def __init__(self, nome, idade, sintomas, doente, alergia, raca, responsavel, ambiente):
        super().__init__(nome, idade, sintomas, doente, alergia, raca, responsavel)
        self._ambiente = ambiente  # indoor ou outdoor

    def exibir_info(self):
        super().exibir_info()
        print(f'Tipo: Gato | Ambiente: {self._ambiente}')
