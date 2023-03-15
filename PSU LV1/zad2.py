x = float(input("Unesite broj: "))

while x > 1.0 or x < 0.0:
    x = float(input("Broj nije u intervalu [0.0, 1.0]! Probajte ponovno: "))

if x >= 0.9:
    print("A")
elif x >= 0.8:
    print("B")
elif x >= 0.7:
    print("C")
elif x >= 0.6:
    print("D")
else:
    print("F")

#dodati try i expect