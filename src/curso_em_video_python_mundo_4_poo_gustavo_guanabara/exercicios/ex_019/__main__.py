from crud import *


def exibir_menu():
    print("\n" + "=" * 30)
    print("     SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Atualizar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)


def main():

    if not criar_banco():
        print("Algum problema aconteceu ao criar o banco.")
        raise SystemExit

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":  # cadastrar pessoa
                if not cadastrar_pessoa():
                    print("\n[ERRO] Não foi possível cadastrar a pessoa.")

            case "2":  # listar pessoas
                if not listar_pessoa():
                    print("\n[ERRO] Não foi possível listar as pessoas.")

            case "3":  # atualizar pessoa
                if not atualizar_pessoa():
                    print("\n[ERRO] Não foi possível atualizar a pessoa.")

            case "4":  # excluir pessoa
                if not excluir_pessoa():
                    print("\n[ERRO] Não foi possível excluir a pessoa.")

            case "5":  # busca por nome
                if not buscar_pessoa_por_nome():
                    print("\n[ERRO] Não foi possível buscar a pessoa.")

            case "0":  # sair
                print("\nEncerrando o sistema...")
                break

            case _:
                print("\n[ERRO ]Opção inválida! Escolha um valor entre 0 e 5.")

        input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
