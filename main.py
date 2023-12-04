from enigma import Enigma

plugs_utilizados = ["ai","tj","cp","re","sm"]
primeiro_rotor = [1, 20]
segundo_rotor = [2, 15]
terceiro_rotor = [3, 10]

enigma = Enigma(plugs_utilizados,primeiro_rotor,segundo_rotor,terceiro_rotor)

mensagem = "Isso e so mais um teste normal"
# mensagem = "YVUJ R JF IHLK DZ XHMNQ RBSXNP"
criptografia = enigma.digitar(mensagem)
print(mensagem)
print(criptografia)