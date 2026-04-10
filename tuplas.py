# Definição implícita de uma tupla
tupla_implicita = (1, 2, 3, 4)

# Definição explícita de uma tupla
lista = [5, 6, 7, 8]
tupla_explicita = tuple(lista)

print("Tupla implícita:", tupla_implicita, "| Tipo:", type(tupla_implicita))
print("Tupla explícita:", tupla_explicita, "| Tipo:", type(tupla_explicita))

# Cria uma tupla
empresas = ("Google", "Facebook", "Amazon") 
# Tentativa de alteração 
empresas[1] = "Samsung" 

frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")

print(frutas)

frutas = ["maçã", "banana", "laranja", "banana"]
frutas.remove("banana")

print(frutas)

# Definição de uma tupla
frutas = ("maçã", "banana", "laranja", "uva")

# Encontra o índice do elemento "laranja" na tupla
indice_laranja = frutas.index("laranja")

print("O índice de 'laranja' é:", indice_laranja)

