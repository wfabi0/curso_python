pagamento = float(input("Digite o valor do pagamento: "))
MENSALIDADE = 100.0

if pagamento < MENSALIDADE:
    print("Pagamento abaixo da mensalidade.")
    multa = MENSALIDADE - pagamento
    multa *= 1.1
    print(f"Uma multa foi gerada no valor de: R$ {multa:.2f}")
elif pagamento == MENSALIDADE:
    print("Pagamento efetuado com sucesso, nossa equipe agradece.")
else:
    print("Pagamento acima da mensalidade.")
    troco = pagamento - MENSALIDADE
    print(f"Troco gerado no valor de: R$ {troco:.2f}")

print("Tenha um bom treino!")
