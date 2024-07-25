from unittest import TestCase
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from dominio import Lance, Leilao, Usuario

class TestLeilao(TestCase):

    def setUp(self):
        self.afonso = Usuario('Afonso')
        self.alice = Usuario('Alice')
        self.alita = Usuario('Alita')

        self.lance_da_alice = Lance(self.alice, 250)
        self.lance_do_afonso = Lance(self.afonso, 200)
        self.lance_da_alita = Lance(self.alita, 500)
        self.leilao = Leilao('celular')

    def test_avalia(self):
        self.leilao.propoe(self.lance_da_alice)
        self.leilao.propoe(self.lance_do_afonso)

        menor_valor_esperado = 200.0
        maior_valor_esperado = 250.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_avalia2(self):
        self.leilao.propoe(self.lance_do_afonso)
        self.leilao.propoe(self.lance_da_alice)

        menor_valor_esperado = 200.0
        maior_valor_esperado = 250.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        joao = Usuario('joão')
        lance = Lance(joao, 200)
        leilao = Leilao('celular')
        leilao.propoe(lance)

        self.assertEqual(200.0, leilao.menor_lance)
        self.assertEqual(200.0, leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        self.leilao.propoe(self.lance_do_afonso)
        self.leilao.propoe(self.lance_da_alice)
        self.leilao.propoe(self.lance_da_alita)

        menor_valor_esperado = 200.0
        maior_valor_esperado = 500.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_da_alice)
        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        jeova = Usuario('Jeová')
        lance_jeova = Lance(jeova, 200)

        self.leilao.propoe(self.lance_da_alice)
        self.leilao.propoe(lance_jeova)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_da_alice200 = Lance(self.alice, 200)
        self.leilao.propoe(self.lance_da_alice)
        self.leilao.propoe(lance_da_alice200)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

if __name__ == '__main__':
    import unittest
    unittest.main()