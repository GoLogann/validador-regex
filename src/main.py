from validador.validador import Validador
from tabulate import tabulate

def mostrar_tabela(exemplos):
    resultados = []

    for categoria, tipos in exemplos.items():
        for status, cadeias in tipos.items():
            for cadeia in cadeias:
                resultado, _ = Validador.validar(categoria, cadeia)
                resultados.append([
                    categoria,
                    cadeia,
                    "Aceita" if status == "aceitas" else "Rejeitada",
                    "Aceita" if resultado else "Rejeitada"
                ])

    print(tabulate(
        resultados,
        headers=["Categoria", "Cadeia", "Esperado", "Resultado"],
        tablefmt="grid"
    ))

def validar_dados():
    while True:
        print("\nTipos disponíveis: nome, email, senha, cpf, telefone")
        tipo = input("Escolha um tipo de dado para validar (ou digite 'voltar' para retornar ao menu): ").strip().lower()
        if tipo == "voltar":
            break

        if tipo not in ["nome", "email", "senha", "cpf", "telefone"]:
            print("Tipo inválido. Tente novamente.")
            continue

        dado = input(f"Digite o dado para validar como {tipo}: ").strip()
        resultado, mensagem = Validador.validar(tipo, dado)
        print(f"Resultado: {'Válido' if resultado else 'Inválido'} - {mensagem}")

def main():
    exemplos = {
        "nome": {
            "aceitas": ["Alan Turing", "Noam Chomsky", "Ada Lovelace"],
            "rejeitadas": ["1Alan", "Alan", "A1an"]
        },
        "email": {
            "aceitas": ["a@a.br", "divulga@ufpa.br"],
            "rejeitadas": ["@", "a@.br", "T@teste.br"]
        },
        "senha": {
            "aceitas": ["518R2r5e", "F123456A", "1234567T", "ropsSoq0"],
            "rejeitadas": ["F1234567A", "abcdefgH", "1234567HI"]
        },
        "cpf": {
            "aceitas": ["123.456.789-09", "000.000.000-00"],
            "rejeitadas": ["123.456.789-0", "111.111.11-11"]
        },
        "telefone": {
            "aceitas": ["(91) 99999-9999", "(91) 999999999", "91 999999999"],
            "rejeitadas": ["(91) 59999-9999", "99 99999-9999", "(94)95555-5555"]
        }
    }

    while True:
        print("\nMenu:")
        print("1. Mostrar tabela de exemplos")
        print("2. Validar dados manualmente")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            mostrar_tabela(exemplos)
        elif escolha == "2":
            validar_dados()
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
