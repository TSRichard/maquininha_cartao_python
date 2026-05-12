def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

def input_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Valor inválido. Digite um número.")

def input_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("❌ Número inválido. Digite um inteiro.")