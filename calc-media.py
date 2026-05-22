class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero

    # Sobrescreve o método __eq__ para comparar contas pelo número
    def __eq__(self, other):
        if not isinstance(other, ContaCorrente):
            return False
        return self.numero == other.numero


# Cria duas contas com o mesmo número
conta_do_gui = ContaCorrente(15)
conta_da_dani = ContaCorrente(15)

# Compara as duas instâncias
if conta_do_gui == conta_da_dani:
    print('São iguais')
else:
    print('São diferentes')
