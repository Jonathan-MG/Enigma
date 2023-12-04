from constantes import alfabeto
from plugs import Plug
from refletor import Refletor
from rotor import Rotor
from teclado import Teclado
class Enigma:
    def __init__(self,Lista_de_Plugs,Primeiro_rotor,Segundo_Rotor,Terceiro_Rotor):
        self.teclado = Teclado()
        self.plug = Plug(Lista_de_Plugs)
        self.primeiro_rotor = Rotor(Primeiro_rotor[0], Primeiro_rotor[1] if Primeiro_rotor.__len__() > 1 else 0)
        self.segundo_rotor = Rotor(Segundo_Rotor[0], Segundo_Rotor[1] if Segundo_Rotor.__len__() > 1 else 0)
        self.terceiro_rotor = Rotor(Terceiro_Rotor[0], Terceiro_Rotor[1] if Terceiro_Rotor.__len__() > 1 else 0)
        self.refletor = Refletor()
        # print("-----------------------------------------")
        # self.primeiro_rotor.exibir()
        # self.segundo_rotor.exibir()
        # self.terceiro_rotor.exibir()
        # print("-----------------------------------------")

    def digitar(self,mensagem):
        criptografia = ""
        for letra in mensagem:
            if letra == " ":
                criptografia = criptografia + letra
            else: 
                criptografia = criptografia + self.teclado.saida(self.plug.saida(self.primeiro_rotor.saida(self.segundo_rotor.saida(self.terceiro_rotor.saida(self.refletor.tratar_sinal(self.terceiro_rotor.entrada(self.segundo_rotor.entrada(self.primeiro_rotor.entrada(self.plug.entrada(self.teclado.entrada(letra)))))))))))
                # print("-----------------------------------------")
                self.primeiro_rotor.rodar()
                # print("Primeiro Rotor")
                # self.primeiro_rotor.exibir()
                if self.primeiro_rotor.alfabeto_esquerda[-1] == self.primeiro_rotor.entalhe:
                    self.segundo_rotor.rodar()
                    # print("Segundo Rotor")
                    # self.segundo_rotor.exibir()
                    if self.segundo_rotor.alfabeto_esquerda[-1] == self.segundo_rotor.entalhe:
                        self.terceiro_rotor.rodar()
                        # print("Terceiro Rotor")
                        # self.terceiro_rotor.exibir()
                # print(mensagem)
                # print(criptografia)
                # print("-----------------------------------------")
        return criptografia