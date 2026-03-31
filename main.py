lista = []
producao_total = 0
queda_producao = 0

for i in range (3):
    producao = int(input("Digite a produção da hora "))
    lista.append (producao)

    producao_total += producao

    media = producao_total / len(lista)
    
hora_mais_produtiva = lista[0]    
hora_menos_produtiva = lista[0]

for producao in lista:
    if producao > hora_mais_produtiva:
        hora_mais_produtiva = producao
    
    if producao < hora_menos_produtiva:
        hora_menos_produtiva = producao
        
for i in range(1, len(lista)):
    if lista[i] < lista[i - 1]:
        queda_producao += 1

print(f"A produção total foi de: {producao_total}")
print(f"A média da produção é de: {media}")
print(f"A hora mais produtiva teve o valor de: {hora_mais_produtiva}")
print(f"A hora menos produtiva teve o valor de: {hora_menos_produtiva}")
print(f"A quantidade de quedas de produção foi de: {queda_producao}")
