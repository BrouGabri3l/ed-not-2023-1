#Lista
frutas = ["laranja","maça","uva","pera","mamão","abacate","amora"]

for f in frutas:
    print(f)

print("-"*80)

#percorrer a lista em ordem inversa
for f in reversed(frutas):
    print(f)

print("-"*80)
#Se precisarmos da posição do item da lista além da informação
#devemos usar range

for pos in range(len(frutas)):
    print(f"fruta: {frutas[pos]}, posição: {pos}")

print("-"*80)

#percorrendo lista inversa
for pos in range(len(frutas)-1,-1,-1):
    print(f"fruta: {frutas[pos]}, posição: {pos}")
