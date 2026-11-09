from pessoas.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, matricula, departamento):
        super().__init__(nome, matricula)
        self.departamento = departamento

    def apresentar(self):
        return (
            f"Professor: {self.nome} | Matrícula: {self.matricula} "
            f"| Departamento: {self.departamento}"
        )
