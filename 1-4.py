mayores = 0
menores = 0

for x in range(10):
    nota = int (input("ingrese una nota: "))
    if nota >= 7:
        mayores = mayores + 1
    else:
        menores = menores + 1
print("")
print("Mayores a 7: ", mayores)
print("")
print("Menores a 7: ", menores)
print("")

