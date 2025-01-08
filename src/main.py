from validador.validador import Validador
from tabulate import tabulate


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


if __name__ == "__main__":
    main()