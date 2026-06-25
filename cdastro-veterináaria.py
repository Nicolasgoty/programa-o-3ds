class Veiculo:
    def calcular_custo(self, distancia):
        raise NotImplementedError("Este método deve ser sobrescrito pelas subclasses")

class Carro(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 0.5  # Exemplo: custo de R$0,50 por km

class Bicicleta(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 0.1  # Exemplo: custo de R$0,10 por km

class Caminhao(Veiculo):
    def calcular_custo(self, distancia):
        return distancia * 1.0  # Exemplo: custo de R$1,00 por km

# Uso do polimorfismo
veiculos = [Carro(), Bicicleta(), Caminhao()]
distancia = 100  # Exemplo de distância

for veiculo in veiculos:
    custo = veiculo.calcular_custo(distancia)
    print(f"Custo de viagem com {veiculo.__class__.__name__}: R$ {custo}")
