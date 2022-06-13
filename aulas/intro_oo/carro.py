#CamelCase
class Carro:
    """"Representa um carro"""

    #metodo  construtor
    def __init__(self, modelo, motor, cor):
        self.modelo = modelo
        self.motor = motor
        self.cor = cor
        self.velocidade = 0
        self.esta_ligado = False


    def __repr__(self):
        return self.modelo + " " + self.motor + " " + self.cor
    
    def ligar(self):
        self.esta_ligado = True
        print(f"O carro {self.modelo} está ligado")

    def desligar(self):
        self.esta_ligado = False 
        print(f"O carro {self.modelo} esta desligado")

    def acelerar (self, velocidade_atingida):
        """Acelera o carro até uma velocidade."""
        self.velocidade = velocidade_atingida
        if self.esta_ligado == True:
            print(f"Acelerou o carro {self.modelo} até {velocidade_atingida}km/h")
        else:
            print(f"Não é possivel, o carro {self.modelo} esta desligado")

carro_novo = Carro("Monza", "V6", "azul")

print(carro_novo.modelo)
print(carro_novo.cor)
carro_novo.ligar()
print(carro_novo.velocidade)
carro_novo.acelerar(90)
print(carro_novo.velocidade)

outro_carro = Carro("gol", "v8", "Preto")

print(outro_carro.modelo)
print(outro_carro)

carro_novo.acelerar(90)
