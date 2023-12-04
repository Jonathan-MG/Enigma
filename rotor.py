from constantes import alfabeto
class Rotor:
    def __init__(self, id, posicao_inicial):
        self.alfabeto_esquerda = alfabeto
        match id:
            case 1:
                self.alfabeto_direita = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
                self.entalhe = "Q"
            case 2:
                self.alfabeto_direita = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
                self.entalhe = "E"
            case 3:
                self.alfabeto_direita = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
                self.entalhe = "V"
            case 4:
                self.alfabeto_direita = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
                self.entalhe = "J"
            case 5:
                self.alfabeto_direita = "VZBRGITYUPSDNHLXAWMJQOFECK"
                self.entalhe = "Z"
            case _:
                self.alfabeto_direita = alfabeto
                self.entalhe = "A"
        self.alfabeto_esquerda = self.alfabeto_esquerda[posicao_inicial:]+self.alfabeto_esquerda[:posicao_inicial]
        self.alfabeto_direita = self.alfabeto_direita[posicao_inicial:]+self.alfabeto_direita[:posicao_inicial]

    def entrada(self, sinal):
        letra = self.alfabeto_direita[sinal]
        sinal = self.alfabeto_esquerda.find(letra)
        return sinal

    def saida(self, sinal):
        letra = self.alfabeto_esquerda[sinal]
        sinal = self.alfabeto_direita.find(letra)
        return sinal
    
    def rodar(self):
        self.alfabeto_esquerda = self.alfabeto_esquerda[1:]+self.alfabeto_esquerda[0]
        self.alfabeto_direita = self.alfabeto_direita[1:]+self.alfabeto_direita[0] 
    
    def exibir(self):
        print(self.alfabeto_esquerda)
        print(self.alfabeto_direita)
        print(" ")