from biblioteca.biblioteca import Biblioteca
from pessoas.aluno import Aluno
from pessoas.professor import Professor
from livros.livro import Livro
from relatorios.relatorio import Relatorio


def mostrar_menu():
    print("\n===== MINHA BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar aluno")
    print("3 - Cadastrar professor")
    print("4 - Listar livros")
    print("5 - Listar pessoas")
    print("6 - Fazer empréstimo")
    print("7 - Devolver livro")
    print("8 - Ver empréstimos")
    print("0 - Sair")


def main():
    biblioteca = Biblioteca()
    proximo_codigo = 1

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Título do livro: ").strip()
            autor = input("Autor: ").strip()
            if not titulo or not autor:
                print("Preencha o título e o autor.")
                continue
            biblioteca.adicionar_livro(Livro(proximo_codigo, titulo, autor))
            print(f"Livro cadastrado! Código: {proximo_codigo}")
            proximo_codigo += 1

        elif opcao == "2":
            nome = input("Nome do aluno: ").strip()
            matricula = input("Matrícula: ").strip()
            curso = input("Curso: ").strip()
            if not nome or not matricula or not curso:
                print("Preencha todos os campos.")
                continue
            aluno = Aluno(nome, matricula, curso)
            if biblioteca.adicionar_pessoa(aluno):
                print("Aluno cadastrado com sucesso.")
            else:
                print("Já existe uma pessoa com essa matrícula.")

        elif opcao == "3":
            nome = input("Nome do professor: ").strip()
            matricula = input("Matrícula: ").strip()
            departamento = input("Departamento: ").strip()
            if not nome or not matricula or not departamento:
                print("Preencha todos os campos.")
                continue
            professor = Professor(nome, matricula, departamento)
            if biblioteca.adicionar_pessoa(professor):
                print("Professor cadastrado com sucesso.")
            else:
                print("Já existe uma pessoa com essa matrícula.")

        elif opcao == "4":
            if not biblioteca.livros:
                print("Nenhum livro cadastrado.")
            for livro in biblioteca.livros:
                print(livro)

        elif opcao == "5":
            if not biblioteca.pessoas:
                print("Nenhuma pessoa cadastrada.")
            for pessoa in biblioteca.pessoas:
                # Polimorfismo: cada tipo de pessoa apresenta seus próprios dados.
                print(pessoa.apresentar())

        elif opcao == "6":
            try:
                codigo = int(input("Código do livro: "))
            except ValueError:
                print("Digite um código numérico.")
                continue
            matricula = input("Matrícula da pessoa: ").strip()
            if biblioteca.fazer_emprestimo(codigo, matricula):
                print("Empréstimo realizado.")
            else:
                print("Confira o código, a matrícula e a disponibilidade do livro.")

        elif opcao == "7":
            try:
                codigo = int(input("Código do livro que será devolvido: "))
            except ValueError:
                print("Digite um código numérico.")
                continue
            if biblioteca.devolver_livro(codigo):
                print("Livro devolvido com sucesso.")
            else:
                print("Não existe empréstimo ativo para esse livro.")

        elif opcao == "8":
            relatorio = Relatorio()
            print(relatorio.listar_emprestimos(biblioteca.emprestimos))

        elif opcao == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
