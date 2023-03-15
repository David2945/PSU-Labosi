radni_sati = float(input("Radni sati: "))
placa_po_satu = float(input("eura/h: "))

def total_euro(x, y):
    return x * y

print("Ukupno:", total_euro(radni_sati, placa_po_satu), "eura")