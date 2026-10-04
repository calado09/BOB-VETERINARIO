class ItemBanco:
    """
    Superclasse genérica que representa qualquer 'item' guardado no banco
    de dados da clínica (um animal, um responsável, etc).
    Concentra os atributos mais básicos que todo registro precisa ter.
    """

    def __init__(self, nome, idade):
        self._nome = nome      # encapsulado (atributo "protegido")
        self._idade = idade

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def __str__(self):
        return f'Nome: {self._nome} | Idade: {self._idade}'
