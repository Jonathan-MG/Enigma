from constantes import alfabeto
class Plug:
    def __init__(self, pares):
        self.alfabeto_direito = alfabeto
        self.alfabeto_esquerda = alfabeto
        for par in pares:
            Primeira_Letra = par[0].upper()
            Segunda_Letra = par[1].upper()
            Posicao_Primeira_Letra = alfabeto.find(Primeira_Letra)
            Posicao_Segunda_Letra = alfabeto.find(Segunda_Letra)
            self.alfabeto_esquerda = self.alfabeto_esquerda[:Posicao_Primeira_Letra] + Segunda_Letra + self.alfabeto_esquerda[Posicao_Primeira_Letra+1:]
            self.alfabeto_esquerda = self.alfabeto_esquerda[:Posicao_Segunda_Letra] + Primeira_Letra + self.alfabeto_esquerda[Posicao_Segunda_Letra+1:]

    def entrada(self, sinal):
        letra = self.alfabeto_direito[sinal]
        sinal = self.alfabeto_esquerda.find(letra)
        return sinal

    def saida(self, sinal):
        letra = self.alfabeto_esquerda[sinal]
        sinal = self.alfabeto_direito.find(letra)
        return sinal