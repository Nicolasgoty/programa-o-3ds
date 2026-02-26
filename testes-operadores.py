peso = 75

if peso < 50:
    print("Leve")
elif peso < 70:
    print("Médio")
elif peso < 90:
    print("Pesado")
else:
    print("Muito Pesado")

mes = "Julho"

if mes in ["Dezembro", "Janeiro", "Fevereiro"]:
    print("Verão")
elif mes in ["Março", "Abril", "Maio"]:
    print("Outono")
elif mes in ["Junho", "Julho", "Agosto"]:
    print("Inverno")
else:
    print("Primavera")

idade = 28

if idade <= 12:
    print("criança")
elif idade <= 18:
    print("adolescente")
elif idade <= 30:
    print("jovem adulto")
elif idade < 60:
    print("adulto")
else:
    print("idoso")

nota = 85

if nota >= 90:
    print("conceito A")
elif nota >= 80:
    print("conceito B")
elif nota >= 70:
    print("conceito C")
elif nota >= 60:
    print("conceito D")
else:
  print("conceito F")

idade = 16
classificacao = "R"

if classificacao == "G":
    print("Permitido para todas as idades.")
elif classificacao == "PG" and idade >= 10:
    print("Permitido para crianças com mais de 10 anos.")
elif classificacao == "PG-13" and idade >= 13:
    print("Permitido para adolescentes com mais de 13 anos.")
elif classificacao == "R" and idade >= 17:
    print("Permitido para maiores de 17 anos.")
else:
    print("Não permitido.")
