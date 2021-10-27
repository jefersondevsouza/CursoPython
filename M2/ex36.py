valorCasa = float(input("Qual o valor da casa: R$"))
salario = float(input("Qual o valor do salário: R$"))
anos = int(input("Em quantos anos pretende pagar a casa: "))
prestacao = valorCasa / (anos * 12)
maxParcela = float(salario / 100 * 30)
print("O valor da prestacao será {}".format(prestacao))
print("A parcela máxima poderá ser de {}".format(maxParcela))
if prestacao > maxParcela:
    print("O valor da parcela será maior que 30% do seu salário. IMPRESTIMO NEGADO")
elif prestacao == maxParcela:
    print("O valor da parcela será o máximo permitido. 30% do salário. PARABENS")
else:
    print("O emprestimo será concedido! PARABENS")
