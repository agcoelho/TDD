from unittest import TestCase
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from dominio import Avaliador, Lance, Leilao, Usuario


class TestAvaliador(TestCase):

    def cria_cenario(self):
        self.afonso = Usuario('Afonso')
        self.alice = Usuario('Alice')
        self.alita = Usuario('Alita')

        self.lance_da_alice = Lance(self.alice, 250)
        self.lance_do_afonso = Lance(self.afonso, 200)
        lance_da_alita = Lance(self.alita, 500)

        
        self.leilao = Leilao('celular')

    def test_avalia(self):



        self.leilao.lances.append(self.lance_da_alice)
        self.leilao.lances.append(self.lance_do_afonso)


        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')

        menor_valor_esperado = 200.0
        maior_valor_esperado = 250.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)



    def test_avalia2(self):

        self.leilao.lances.append(self.lance_do_afonso)
        self.leilao.lances.append(self.lance_da_alice)
      


        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')

        menor_valor_esperado = 200.0
        maior_valor_esperado = 250.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        joao = Usuario('joão')

        lance = Lance(joao, 200)


        leilao = Leilao('celular')
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(200.0, avaliador.menor_lance)
        self.assertEqual(200.0, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):

        self.leilao.lances.append(self.lance_do_afonso)
        self.leilao.lances.append(self.lance_da_alice)
        self.leilao.lances.append(self.lance_da_alita)
      


        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')

        menor_valor_esperado = 200.0
        maior_valor_esperado = 500.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

        




test = TestAvaliador()

test.test_avalia()

test.test_avalia2()

test.test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_o_leilao_tiver_um_lance()

test.test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances()

