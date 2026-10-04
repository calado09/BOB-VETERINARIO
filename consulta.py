class Consulta:
    """
    Representa uma consulta veterinária realizada para um paciente.
    """

    PORCENTAGEM_ADICIONAL = 0.10  # 10% de acréscimo para quem não tem plano

    def __init__(self, nome, responsavel, valor, tempo, plano):
        self._nome = nome
        self._responsavel = responsavel
        self._valor = float(valor)
        self._tempo = tempo
        self._plano = plano

    def __str__(self):
        return f'{self._nome} | {self._responsavel} | R$ {self._valor:.2f} | {self._tempo} | {self._plano}'

    def verificar_plano(self, plano_respondido):
        if plano_respondido == 1:
            print('Plano associado: o cliente possui um plano associado e terá cobertura.')
        elif plano_respondido == 2:
            valor_total = self._valor + (self._valor * Consulta.PORCENTAGEM_ADICIONAL)
            print(f'O cliente não possui plano. Valor original: R$ {self._valor:.2f} '
                  f'| Com adicional de 10%: R$ {valor_total:.2f}')
        else:
            print('Opção inválida. Selecione 1 ou 2.')

    def exibir_info(self):
        print('-' * 100)
        print(f'Consulta: {self._nome} | Responsável: {self._responsavel} | '
              f'Valor: R$ {self._valor:.2f} | Tempo estimado: {self._tempo} | Plano: {self._plano}')
