# Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido em Python orientado a objetos para gerenciar o acervo, o cadastro de usuários (Alunos e Professores), o controle de empréstimos e a geração de relatórios de uma biblioteca acadêmica.

---

## Arquitetura e Estrutura de Pastas

O projeto está organizado em módulos para garantir a separação de responsabilidades:

```text
minha_biblioteca/
│
├── main.py                    # Ponto de entrada do sistema
├── README.md                  # Documentação do projeto
│
├── biblioteca/                # Gerenciamento central do sistema
│   ├── __init__.py
│   └── biblioteca.py          # Classe Biblioteca (agrega livros, pessoas e empréstimos)
│
├── livros/                    # Domínio de Livros
│   ├── __init__.py
│   └── livro.py               # Classe Livro
│
├── pessoas/                   # Hierarquia de Pessoas
│   ├── __init__.py
│   ├── pessoa.py              # Classe base (Pessoa)
│   ├── aluno.py               # Subclasse Aluno
│   └── professor.py           # Subclasse Professor
│
├── emprestimos/               # Controle de Empréstimos
│   ├── __init__.py
│   └── emprestimo.py          # Classe Empréstimo
│
└── relatorios/                # Geração de Relatórios
    ├── __init__.py
    └── relatorio.py           # Classe Relatório (listagem de empréstimos)
```

# Modelagem de Classes (Baseado no UML)

## 1. Pessoa (Classe Base)
Atributos:

- str nome

- str matricula

### Métodos:

+ apresentar() : str

## 2. Aluno (Herda de Pessoa)
Atributos:

- str curso

### Métodos:

+ apresentar() : str

## 3. Professor (Herda de Pessoa)
Atributos:

- str departamento

### Métodos:

+ apresentar() : str

## 4. Livro
Atributos:

- int codigo

- str titulo

- str autor

- bool disponivel

### Métodos:

+ __str__() : str

## 5. Empréstimo
Atributos:

- Pessoa pessoa

- Livro livro

- bool ativo

### Métodos:

+ devolver() : void

## 6. Biblioteca
Atributos:

- list[Livro] livros

- list[Pessoa] pessoas

- list[Empréstimo] emprestimos

### Métodos:

+ adicionar_livro(Livro livro) : void

+ adicionar_pessoa(Pessoa pessoa) : bool

+ buscar_livro(int codigo) : Livro

+ buscar_pessoa(str matricula) : Pessoa

+ fazer_emprestimo(int codigo, str matricula) : bool

+ devolver_livro(int codigo) : bool

## 7. Relatório

### Métodos:

+ listar_emprestimos(list[Empréstimo] emprestimos) : str

# Conceitos de Orientação a Objetos (POO) Aplicados
## Herança:
A classe Pessoa atua como superclasse, contendo os atributos comuns (nome e matricula). As classes Aluno e Professor herdam essas características, evitando duplicação de código.

## Polimorfismo: 
Evidenciado pelo método apresentar(), implementado na classe base e sobrescrito nas subclasses para exibir detalhes específicos de cada tipo de usuário.

## Composição: 
A Biblioteca possui uma relação de forte dependência estrutural (composição) com seus registros principais (livros, pessoas e emprestimos).

## Associação: 
A classe Empréstimo se conecta diretamente e associa instâncias de Pessoa e Livro.

## Dependência: 
A classe Relatório depende da classe Empréstimo para processar e formatar a listagem dos empréstimos ativos no sistema.

# Como Executar
Navegue até o diretório raiz do projeto (minha_biblioteca/).

Execute o arquivo principal via terminal:

## Bash
python main.py
