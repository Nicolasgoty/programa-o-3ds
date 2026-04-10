import functools

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __repr__(self):
        return f'{self.nome}: {self.nota}'

def comparar_alunos(a, b):
    return (a.nota > b.nota) - (a.nota < b.nota)

alunos = [Aluno('Ana', 88), Aluno('Rafael', 92), Aluno('Paulo', 78)]
alunos_ordenados = sorted(alunos, key=functools.cmp_to_key(comparar_alunos))
print(alunos_ordenados)
