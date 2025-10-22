# Programa: Calculadora de Stake pelo Lucro Desejado
# Objetivo: Calcular quanto colocar para atingir um lucro específico em diferentes odds

print("=== CALCULADORA DE STAKE POR LUCRO ===")
lucro_desejado = float(input("Digite o valor de lucro que deseja obter (em R$): "))

while True:
    odd = input("\nDigite a odd (ou 'sair' para encerrar): ")

    if odd.lower() == "sair":
        print("\nPrograma encerrado. Até logo!")
        break

    try:
        odd = float(odd)
        if odd <= 1:
            print(" A odd deve ser maior que 1. Tente novamente.")
            continue

        stake = lucro_desejado / (odd - 1)
        retorno_total = stake * odd

        print(f"Para lucrar R${lucro_desejado:.2f} com odd {odd:.2f},")
        print(f"você deve apostar R${stake:.2f}. Retorno total: R${retorno_total:.2f}")

    except ValueError:
        print(" Valor inválido. Digite um número ou 'sair' para encerrar.")
