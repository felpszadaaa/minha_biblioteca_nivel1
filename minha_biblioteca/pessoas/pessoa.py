class Pessoa:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def apresentar(self):
        return f"{self.nome} - Matrícula: {self.matricula}"
