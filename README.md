# BOB Veterinária — Sistema de Gerenciamento

Sistema em Python (terminal) para gerenciar pacientes, responsáveis e consultas
de uma clínica veterinária. Projeto final da disciplina, focado em
Programação Orientada a Objetos.

## Como executar

```
python3 app.py
```

O sistema já carrega alguns dados de exemplo (3 responsáveis, 3 animais e
3 consultas) para você poder testar imediatamente as opções de listagem.

## Estrutura de arquivos

- `item_banco.py` — superclasse `ItemBanco`
- `animal.py` — classe `Animal` e subclasses `Cachorro` / `Gato`
- `responsavel.py` — classe `Responsavel`
- `consulta.py` — classe `Consulta`
- `veterinaria.py` — classe `Veterinaria` (orquestra tudo)
- `app.py` — menu principal / interface de terminal

## Conceitos de POO aplicados

### Classes e instanciação
O projeto tem 6 classes (`ItemBanco`, `Animal`, `Cachorro`, `Gato`,
`Responsavel`, `Consulta`, `Veterinaria`), todas instanciadas e
interagindo entre si através do menu em `app.py`.

### Encapsulamento
Todos os atributos usam `_underscore` (ex: `self._nome`, `self._idade`,
`self._valor`) para indicar que são "protegidos" e não devem ser
acessados diretamente de fora da classe. O acesso aos dados é feito
através de métodos (`exibir_info`, `verificar_plano`, `get_nome`, etc).

### Herança
- `Animal` herda de `ItemBanco` (reaproveita `nome` e `idade` através de
  `super().__init__()`).
- `Cachorro` e `Gato` herdam de `Animal`, cada um acrescentando seu
  próprio atributo específico (`porte` para o cachorro, `ambiente`
  para o gato) e **sobrescrevendo** o método `exibir_info()` — isso é
  polimorfismo: o mesmo método se comporta de forma diferente
  dependendo da subclasse que o chama.

```
ItemBanco
   └── Animal
          ├── Cachorro
          └── Gato
```

### Composição / Agregação
- A classe `Veterinaria` é "dona" das listas `_animais`, `_responsaveis`
  e `_consultas` — ela cria, armazena e gerencia esses objetos
  (composição: se a Veterinaria "morre", as listas também morrem).
- A classe `Responsavel` mantém uma lista `_pacientes` com referências
  aos objetos `Animal` associados a ela (agregação: o `Animal` existe
  de forma independente, mas é referenciado pelo responsável).

## Funcionalidades do menu

1. Cadastrar paciente (escolhendo Cachorro ou Gato)
2. Listar pacientes (com opção de ver detalhes de um específico)
3. Cadastrar responsável
4. Listar responsáveis
5. Cadastrar consulta
6. Listar consultas (com cálculo automático de acréscimo de 10% para
   quem não tem plano)
7. Sair
