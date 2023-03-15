lista = []
x = 0
while x != "Done":
    x = input("Unos: ")
    if(x != "Done"):
        lista.append(int(x))
    else: 
        break 

print("Broj elemenata u listi: ", len(lista))

uk = 0

for num in lista:
    uk += num


print("Minimalna vrijednost", min(lista))
print("Maximalna vrijednost", max(lista))
print("Srednja vrijednost: ", uk/len(lista))

print("Lista: ",lista)
lista.sort()
print("Sortirana lista: ",lista)

    