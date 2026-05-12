from transacao import Transacao
from utils import input_float, input_int

def main():
    print("=== MAQUININHA DE CARTÃO SIMULADA ===\n")
    
    valor = input_float("💵 Valor da compra: R$ ")
    
    print("\n[1] Débito")
    print("[2] Crédito")
    opcao = input_int("Escolha o método (1 ou 2): ")
    
    if opcao == 1:
        metodo = "debito"
        parcelas = 1
    elif opcao == 2:
        metodo = "credito"
        parcelas = input_int("Número de parcelas (1 a 12): ")
        if parcelas < 1:
            parcelas = 1
        if parcelas > 12:
            parcelas = 12
    else:
        print("❌ Opção inválida")
        return
    
    transacao = Transacao(valor, metodo, parcelas)
    print(transacao)

if __name__ == "__main__":
    main()