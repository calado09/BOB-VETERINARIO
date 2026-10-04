from animal import Cachorro, Gato
from responsavel import Responsavel
from consulta import Consulta


class Veterinaria:
    """
    Classe principal do sistema.
    Demonstra COMPOSIÇÃO/AGREGAÇÃO: a Veterinaria é "dona" das listas
    de pacientes, responsáveis e consultas, controlando a criação e o
    relacionamento entre esses objetos.
    """

    def __init__(self, nome_clinica):
        self._nome_clinica = nome_clinica
        self._animais = []
        self._responsaveis = []
        self._consultas = []

    # ---------------- Responsáveis ----------------
    def buscar_responsavel(self, nome):
        for r in self._responsaveis:
            if r._nome.lower() == nome.lower():
                return r
        return None

    def cadastrar_responsavel(self, nome, telefone, email, endereco):
        responsavel = Responsavel(nome, telefone, email, endereco)
        self._responsaveis.append(responsavel)
        return responsavel

    def listar_responsaveis(self):
        if not self._responsaveis:
            print('Nenhum responsável cadastrado.')
            return
        for i, r in enumerate(self._responsaveis, start=1):
            print(f'{i}. {r}')

    # ---------------- Animais ----------------
    def cadastrar_animal(self, tipo, nome, idade, sintomas, doente, alergia, raca,
                          nome_responsavel, extra):
        responsavel = self.buscar_responsavel(nome_responsavel)
        if responsavel is None:
            print('Responsável não encontrado. Cadastre o responsável primeiro.')
            return None

        if tipo == 'cachorro':
            animal = Cachorro(nome, idade, sintomas, doente, alergia, raca,
                               responsavel._nome, extra)
        else:
            animal = Gato(nome, idade, sintomas, doente, alergia, raca,
                          responsavel._nome, extra)

        self._animais.append(animal)
        responsavel.adicionar_paciente(animal)  # agregação em ação
        return animal

    def listar_animais(self):
        if not self._animais:
            print('Nenhum paciente cadastrado.')
            return
        for i, a in enumerate(self._animais, start=1):
            print(f'{i}. {a}')

    def exibir_animal(self, indice):
        if 0 <= indice < len(self._animais):
            self._animais[indice].exibir_info()
        else:
            print('Paciente não encontrado.')

    # ---------------- Consultas ----------------
    def cadastrar_consulta(self, nome, responsavel, valor, tempo, plano):
        consulta = Consulta(nome, responsavel, valor, tempo, plano)
        self._consultas.append(consulta)
        return consulta

    def listar_consultas(self):
        if not self._consultas:
            print('Nenhuma consulta cadastrada.')
            return
        for i, c in enumerate(self._consultas, start=1):
            print(f'{i}. {c}')

    def exibir_consulta(self, indice):
        if 0 <= indice < len(self._consultas):
            self._consultas[indice].exibir_info()
        else:
            print('Consulta não encontrada.')

    def carregar_dados_exemplo(self):
        """Popula o sistema com alguns dados de exemplo, para já ter algo pra mostrar."""
        carlos = self.cadastrar_responsavel('Carlos Silva', '(11)98765-4321',
                                             'carlosSilva@gmail.com', 'Rua José de Alencar, 1234')
        ana = self.cadastrar_responsavel('Ana Souza', '(11)91234-5678',
                                          'anaSouza@gmail.com', 'Rua Manuel de Oliveira, 5678')
        marcos = self.cadastrar_responsavel('Marcos Oliveira', '(11)99876-5432',
                                             'marcosOliveira@gmail.com', 'Rua Francisco de Assis, 9012')

        self.cadastrar_animal('cachorro', 'Thor', '3 anos', 'Coceira intensa e queda de pelo',
                               'sim', 'Frango', 'Golden Retriever', 'Carlos Silva', 'Grande')
        self.cadastrar_animal('gato', 'Mia', '1 ano', 'Espirros constantes e secreção nasal',
                               'sim', 'Nenhuma detectada', 'Siamês', 'Ana Souza', 'Indoor')
        self.cadastrar_animal('cachorro', 'Bob', '11 anos', 'Dificuldade para andar e cansaço',
                               'sim', 'Dipirona', 'Poodle', 'Marcos Oliveira', 'Pequeno')

        self.cadastrar_consulta('Cirurgia de Castração', 'Dr. Ricardo Mendes', 450.00,
                                 '1 hora e 30 minutos', 'Plano Preventivo Ouro')
        self.cadastrar_consulta('Consulta de Emergência Noturna', 'Dra. Camila Rocha', 300.00,
                                 '40 minutos', 'Particular (Sem Plano)')
        self.cadastrar_consulta('Vacinação Anual', 'Dr. Lucas Silva', 150.00,
                                 '20 minutos', 'Plano Básico Prata')
