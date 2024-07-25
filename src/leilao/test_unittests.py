from unittest import TestCase
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from dominio import Avaliador, Lance, Leilao, Usuario


class TestAvaliador(TestCase):

    def test_avalia(self):
        
        afonso = Usuario('Afonso')
        alice = Usuario('Alice')

        lance_da_alice = Lance(alice, 250)
        lance_do_afonso = Lance(afonso, 200)


        leilao = Leilao('celular')

        leilao.lances.append(lance_da_alice)
        leilao.lances.append(lance_do_afonso)


        avaliador = Avaliador()
        avaliador.avalia(leilao)
        print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')

        menor_valor_esperado = 100.0
        maior_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)