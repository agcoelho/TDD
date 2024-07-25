from dominio import Avaliador, Usuario, Lance, Leilao

afonso = Usuario('Afonso')
alice = Usuario('Alice')

lance_da_alice = Lance(alice, 250)
lance_do_afonso = Lance(afonso, 200)


leilao = Leilao('celular')

leilao.lances.append(lance_da_alice)
leilao.lances.append(lance_do_afonso)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')

