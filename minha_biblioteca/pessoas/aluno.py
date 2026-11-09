from pessoas.pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso):
        super().__init__(nome, matricula)
        self.curso = curso

    def apresentar(self):
        return f"Aluno: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}"
