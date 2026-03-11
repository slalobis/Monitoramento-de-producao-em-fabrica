lista = []
producao_total = 0
queda_producao = 0

for i in range (16):
    producao = int(input("Digite a produção da hora "))
    lista.append (producao)

    producao_total += producao

    media = producao_total / len(lista)

    hora_mais_produtiva = lista[0]
    hora_menos_produtiva = lista[0]

for i in lista:
    if producao > hora_mais_produtiva:
        hora_mais_produtiva = producao

    if producao < hora_menos_produtiva:
        hora_menos_produtiva = producao

for i in range(1, len(lista)):
    if lista[i] < lista[i - 1]:
        queda_producao += 1

print(producao_total)
print(media)
print(hora_mais_produtiva)
print(hora_menos_produtiva)
print(queda_producao)