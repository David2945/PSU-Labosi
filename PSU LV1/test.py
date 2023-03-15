"""
a = 2
lista = [1, 2, 3, 6]
var = {'a':2,'b':3,'c':10}
print(lista)
print(var['b'])
print(a)

flag = True
if(flag is True):
    print(a)

if(6 in lista):
    print(lista[3])
else:
    print("Nije u listi")

if a > 0:
    print("Veci od 0")
elif a < 0:
    print("Manje od 0")
else:
    print("Jednak je 0")

var = range(0,6)
print(var)

for i in range(0,6):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

lista.append(7) dodaje na kraj liste
lista.pop(0) miče broj na nultom indeksu (1)
    
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
a.append(b) # lista b ce postati element liste a - lista u listi
print(a)
print(c) # elementi liste a i b će biti zajedno kao jedna lista
print(max(c))
print(min(c))

polje = "Neki string"
print(polje[0]) # ispisati će 'N'
print(polje.count("i")) # koliko puta se i ponavlja u stringu


f = open("example.txt","w")

for line in f:
    print(line)

f.close()

"""

x = input("Unos: ")
print(int(x))