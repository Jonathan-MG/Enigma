from constantes import alfabeto
from plugs import Plug
from refletor import Refletor
from rotor import Rotor
from teclado import Teclado
class Enigma:
    def __init__(self,Lista_de_Plugs,Primeiro_Rotor,Segundo_Rotor,Terceiro_Rotor):
        self.teclado = Teclado()
        self.plug = Plug(Lista_de_Plugs)
        self.primeiro_Rotor = Rotor(Primeiro_Rotor[0], Primeiro_Rotor[1] if Primeiro_Rotor.__len__() > 1 else 0)
        self.segundo_rotor = Rotor(Segundo_Rotor[0], Segundo_Rotor[1] if Segundo_Rotor.__len__() > 1 else 0)
        self.terceiro_rotor = Rotor(Terceiro_Rotor[0], Terceiro_Rotor[1] if Terceiro_Rotor.__len__() > 1 else 0)
        self.refletor = Refletor()
        self.primeiro_Rotor.exibir()
        self.segundo_rotor.exibir()
        self.terceiro_rotor.exibir()

    def digitar(self,mensagem):
        criptografia = ""
        for letra in mensagem:
            if letra == " ":
                criptografia = criptografia + letra
            else: 
                criptografia = criptografia + self.teclado.saida(self.plug.saida(self.primeiro_Rotor.saida(self.segundo_rotor.saida(self.terceiro_rotor.saida(self.refletor.tratar_sinal(self.terceiro_rotor.entrada(self.segundo_rotor.entrada(self.primeiro_Rotor.entrada(self.plug.entrada(self.teclado.entrada(letra)))))))))))
                self.primeiro_Rotor.rodar()
                if self.primeiro_Rotor.alfabeto_esquerda[-1] == self.primeiro_Rotor.entalhe:
                    self.segundo_rotor.rodar()
                    if self.segundo_rotor.alfabeto_esquerda[-1] == self.segundo_rotor.entalhe:
                        self.terceiro_rotor.rodar()
        return criptografia