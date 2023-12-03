from constantes import alfabeto
class Teclado:
    def entrada(self, letra):
        sinal = alfabeto.find(letra.upper())
        return sinal
    
    def saida(self, sinal):
        letra = alfabeto[sinal]
        return letra.upper()