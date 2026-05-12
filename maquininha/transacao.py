class Transacao:
    def __init__(self, valor, metodo, parcelas=1):
        self.valor = valor
        self.metodo = metodo  # "debito" ou "credito"
        self.parcelas = parcelas

    def calcular_valor_final(self):
        if self.metodo == "debito":
            return self.valor  # sem acréscimo
        elif self.metodo == "credito":
            if self.parcelas == 1:
                return self.valor
            elif self.parcelas <= 3:
                return self.valor * 1.02  # 2% de acréscimo
            elif self.parcelas <= 6:
                return self.valor * 1.04  # 4% de acréscimo
            else:
                return self.valor * 1.06  # 6% de acréscimo
        else:
            raise ValueError("Método inválido")

    def valor_parcela(self):
        valor_final = self.calcular_valor_final()
        return valor_final / self.parcelas

    def __str__(self):
        valor_final = self.calcular_valor_final()
        return f"""
--- Resumo da transação ---
Valor original: R$ {self.valor:.2f}
Método: {self.metodo.upper()}
Parcelas: {self.parcelas}
Valor final: R$ {valor_final:.2f}
Valor por parcela: R$ {self.valor_parcela():.2f}
"""