class Livro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        situacao = "Disponível" if self.disponivel else "Emprestado"
        return f"Código: {self.codigo} | {self.titulo} - {self.autor} | {situacao}"
