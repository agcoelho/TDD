from dominio import Usuario, Lance, Leilao

afonso = Usuario('Afonso')
alice = Usuario('Alice')

lance_da_alice = Lance(alice, 200)
lance_do_afonso = Lance(afonso, 250)


leilao = Leilao('celular')

leilao.lances.append(lance_da_alice)
leilao.lances.append(lance_do_afonso)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')