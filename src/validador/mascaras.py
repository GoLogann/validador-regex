import re

class Mascaras:
    @staticmethod
    def valida_regex(match: re.Match, cadeia: str) -> bool:
        if not match:
            return False

        if match.group(0) != cadeia:
            return False
        return True

    @staticmethod
    def mascara_nome(nome: str) -> bool:
        match = re.search(r'[A-Z][a-z]+( [A-Z][a-z]+)? [A-Z][a-z]+', nome)
        return Mascaras.valida_regex(match, nome)

    @staticmethod
    def mascara_email(email: str) -> bool:
        match = re.search(r'[a-z]+@[a-z]+(.com)?.br', email)
        return Mascaras.valida_regex(match, email)

    @staticmethod
    def mascara_senha(senha: str) -> bool:
        if len(senha) != 8:
            return False
        match = re.search(r'(?=.*[A-Z])(?=.*[0-9])[a-z|A-Z|0-9]*', senha)
        return Mascaras.valida_regex(match, senha)

    @staticmethod
    def mascara_cpf(cpf: str) -> bool:
        match = re.search(r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}', cpf)
        return Mascaras.valida_regex(match, cpf)

    @staticmethod
    def mascara_telefone(telefone: str) -> bool:
        match = re.search(r'(\([0-9]{2}\) 9[0-9]{4}-?[0-9]{4})|([0-9]{2} 9[0-9]{8})', telefone)
        return Mascaras.valida_regex(match, telefone)