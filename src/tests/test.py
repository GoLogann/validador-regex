import unittest
import logging
from src.validador.mascaras import Mascaras

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class TestMascaras(unittest.TestCase):

    exemplos = {
        "nome": {
            "aceitas": ["Alan Turing"],
            "rejeitadas": ["1Alan"]
        },
        "email": {
            "aceitas": ["divulga@ufpa.br"],
            "rejeitadas": ["a@.br"]
        },
        "senha": {
            "aceitas": ["ropsSoq0"],
            "rejeitadas": ["1234567HI"]
        },
        "cpf": {
            "aceitas": ["000.000.000-00"],
            "rejeitadas": ["111.111.11-11"]
        },
        "telefone": {
            "aceitas": ["(91) 99999-9999", "91 999999999"],
            "rejeitadas": ["(91) 59999-9999"]
        }
    }

    def test_mascara_nome(self):
        for item in self.exemplos['nome']['aceitas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_nome(item)
                logger.debug(f"Testando nome aceito: {item} - Resultado: {result}")
                self.assertTrue(result, f"Falha ao aceitar '{item}'")
        for item in self.exemplos['nome']['rejeitadas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_nome(item)
                logger.debug(f"Testando nome rejeitado: {item} - Resultado: {result}")
                self.assertFalse(result, f"Falha ao rejeitar '{item}'")

    def test_mascara_email(self):
        for item in self.exemplos['email']['aceitas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_email(item)
                logger.debug(f"Testando email aceito: {item} - Resultado: {result}")
                self.assertTrue(result, f"Falha ao aceitar '{item}'")
        for item in self.exemplos['email']['rejeitadas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_email(item)
                logger.debug(f"Testando email rejeitado: {item} - Resultado: {result}")
                self.assertFalse(result, f"Falha ao rejeitar '{item}'")

    def test_mascara_senha(self):
        for item in self.exemplos['senha']['aceitas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_senha(item)
                logger.debug(f"Testando senha aceita: {item} - Resultado: {result}")
                self.assertTrue(result, f"Falha ao aceitar '{item}'")
        for item in self.exemplos['senha']['rejeitadas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_senha(item)
                logger.debug(f"Testando senha rejeitada: {item} - Resultado: {result}")
                self.assertFalse(result, f"Falha ao rejeitar '{item}'")

    def test_mascara_cpf(self):
        for item in self.exemplos['cpf']['aceitas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_cpf(item)
                logger.debug(f"Testando CPF aceito: {item} - Resultado: {result}")
                self.assertTrue(result, f"Falha ao aceitar '{item}'")
        for item in self.exemplos['cpf']['rejeitadas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_cpf(item)
                logger.debug(f"Testando CPF rejeitado: {item} - Resultado: {result}")
                self.assertFalse(result, f"Falha ao rejeitar '{item}'")

    def test_mascara_telefone(self):
        for item in self.exemplos['telefone']['aceitas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_telefone(item)
                logger.debug(f"Testando telefone aceito: {item} - Resultado: {result}")
                self.assertTrue(result, f"Falha ao aceitar '{item}'")
        for item in self.exemplos['telefone']['rejeitadas']:
            with self.subTest(item=item):
                result = Mascaras.mascara_telefone(item)
                logger.debug(f"Testando telefone rejeitado: {item} - Resultado: {result}")
                self.assertFalse(result, f"Falha ao rejeitar '{item}'")

if __name__ == '__main__':
    unittest.main()
