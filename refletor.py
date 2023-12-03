from constantes import alfabeto
class Refletor:
    def __init__(self):
        self.alfabeto_direita = "EJMZALYXVBWFCRQUONTSPIKHGD"
        self.alfabeto_esquerda = alfabeto

    def tratar_sinal(self, sinal):
        letra = self.alfabeto_direita[sinal]
        sinal = self.alfabeto_esquerda.find(letra)
        letra = self.alfabeto_direita[sinal]
        sinal = self.alfabeto_direita.find(letra)
        return sinal
