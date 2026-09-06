# Calculadora de Consumo Elétrico Inteligente
# Projeto desenvolvido para o Fichário da Agenda 05 - TI I

print("=" * 40)
print("     CALCULADORA DE CONSUMO ELÉTRICO     ")
print("=" * 40)

# Entrada de dados solicitada no enunciado
aparelho = input("Nome do aparelho (ex: Geladeira): ")
potencia = float(input("Potência do aparelho em Watts (W): "))
horas_dia = float(input("Tempo médio de uso diário (em horas): "))

# Cálculo obrigatório do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Dica de ouro para nota máxima: Cálculo de custo em reais (Tarifa média de R$ 0,75 por kWh)
tarifa_kwh = 0.75
custo_estimado = consumo_mensal * tarifa_kwh

# Exibição dos resultados formatados
print("\n" + "-" * 15 + " RESULTADO " + "-" * 15)
print(f"• Aparelho: {aparelho}")
print(f"• Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"• Custo mensal estimado: R$ {custo_estimado:.2f}")
print("-" * 41)
