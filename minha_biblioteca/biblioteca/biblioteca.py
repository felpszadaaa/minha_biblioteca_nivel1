class Biblioteca:
    def __init__(self):
        # A biblioteca mantém e controla os objetos que fazem parte do sistema.
        self.livros = []
        self.pessoas = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_pessoa(self, pessoa):
        if self.buscar_pessoa(pessoa.matricula) is not None:
            return False
        self.pessoas.append(pessoa)
        return True

    def buscar_livro(self, codigo):
        for livro in self.livros:
            if livro.codigo == codigo:
                return livro
        return None

    def buscar_pessoa(self, matricula):
        for pessoa in self.pessoas:
            if pessoa.matricula == matricula:
                return pessoa
        return None

    def fazer_emprestimo(self, codigo, matricula):
        livro = self.buscar_livro(codigo)
        pessoa = self.buscar_pessoa(matricula)

        if livro is None or pessoa is None or not livro.disponivel:
            return False

        from emprestimos.emprestimo import Emprestimo
        self.emprestimos.append(Emprestimo(pessoa, livro))
        return True

    def devolver_livro(self, codigo):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.codigo == codigo and emprestimo.ativo:
                emprestimo.devolver()
                return True
        return False
