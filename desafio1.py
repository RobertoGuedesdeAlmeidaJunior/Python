# Sequencia
print('oi mundo')

print('passo 2')

# Seleção ( IF )
valor1 = 5

if valor1 > 10:
    print("Valor maior que dez")

if valor1 > 2:
    print("Valor maior que dois")

# Iterações com objeto iterável
lista = list(range(1, 10))

for irineu in lista:
    print("Achei: ")
    print(irineu)
    

lista = list(range(1,10))
lista.append('Leite')
lista.append(list(range(1,10)))
lista.append('Café')

# Exibir via print somente os elementos que sejam do tipo string
for elemento in lista:
    if type(elemento) == str:
        print(elemento)
#desafio 2 colocar entre "|"
for elemento in lista:
    if type(elemento) == str:
        print(elemento)
        for letra in elemento:
            print(letra, '|', end="")
            
nome = input("\n Nome: ")
for letra in nome:
    print(letra, '|', end=" ")

#Tupla é uma lista imutável.
