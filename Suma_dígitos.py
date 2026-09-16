def suma_digitos(n):
    if n<10:
        return n
    else:
        ultimo = n%10
        resto=n//10
        return ultimo+suma_digitos(resto)
numero=int(input("Dígite un número entero: "))
print("suma de dígitos:", suma_digitos(numero))