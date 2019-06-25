b=[]
for a in range(6):
    a = int(input("ingrese un numero: "))
    if a >= 1 and a <= 10:
        b.append(a)
    else:
        print("ingrese un número entre 1 y 10")

print(b)

