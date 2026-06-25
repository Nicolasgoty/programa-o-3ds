def calcular_custo_total_viagem(veiculos, distancia=200):
    """
    Calcula o custo total de uma viagem para uma lista de veículos.
    """
    custo_total = 0
    
    for veiculo in veiculos:
        # Assume-se que o objeto tem um atributo 'custo_por_km'
        custo_total += veiculo.custo_por_km * distancia
        
    return custo_total

# Exemplo de como estruturar os objetos e usar a função:
class Veiculo:
    def __init__(self, nome, custo_por_km):
        self.nome = nome
        self.custo_por_km = custo_por_km

# Criando instâncias de diferentes veículos
carro = Veiculo("Carro", 0.50)  # R$ 0,50 por km
caminhao = Veiculo("Caminhão", 1.20)  # R$ 1,20 por km
moto = Veiculo("Moto", 0.20)  # R$ 0,20 por km

frota = [carro, caminhao, moto]

# Chamada da função
total = calcular_custo_total_viagem(frota)
print(f"O custo total para os veículos percorrerem 200 km é: R$ {total:.2f}")
