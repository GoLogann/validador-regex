from src.validador.mascaras import Mascaras


class Validador:
    @staticmethod
    def validar_nome(nome):
        if Mascaras.mascara_nome(nome):
            return True, "Nome válido."
        return False, "Nome inválido. Deve conter nome e sobrenome com letras maiúsculas e minúsculas."

    @staticmethod
    def validar_email(email):
        if Mascaras.mascara_email(email):
            return True, "E-mail válido."
        return False, "E-mail inválido. Deve seguir o formato exemplo@exemplo.com ou exemplo@exemplo.com.br."

    @staticmethod
    def validar_senha(senha):
        if Mascaras.mascara_senha(senha):
            return True, "Senha válida."
        return False, "Senha inválida. Deve conter pelo menos 1 letra maiúscula, 1 número e ter exatamente 8 caracteres."

    @staticmethod
    def validar_cpf(cpf):
        if Mascaras.mascara_cpf(cpf):
            return True, "CPF válido."
        return False, "CPF inválido. Deve estar no formato xxx.xxx.xxx-xx."

    @staticmethod
    def validar_telefone(telefone):
        if Mascaras.mascara_telefone(telefone):
            return True, "Telefone válido."
        return False, "Telefone inválido. Deve seguir o formato (xx) 9xxxx-xxxx, (xx) 9xxxxxxxx ou xx 9xxxxxxxx."

    @staticmethod
    def validar(tipo, entrada):
        validadores = {
            "nome": Validador.validar_nome,
            "email": Validador.validar_email,
            "senha": Validador.validar_senha,
            "cpf": Validador.validar_cpf,
            "telefone": Validador.validar_telefone,
        }
        if tipo not in validadores:
            return False, f"Tipo de validação '{tipo}' não suportado."
        return validadores[tipo](entrada)
