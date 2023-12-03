from enigma import Enigma

enigma = Enigma(["ai","tj","cp","re","sm"],[1,20],[2,18],[3,15])
mensagem = "Muito burra pra fazer medicina"
# mensagem = "XEHLL WEIQX FYB XWCQP DYOUHPTM"
criptografia = enigma.digitar(mensagem)
print(mensagem)
print(criptografia)