import random
 
 
def generar_lista(cantidad):
    if cantidad == 0:
        return []
    numero = random.randint(10, 99)
    return [numero] + generar_lista(cantidad - 1)
 
 
def suma_multiplos_tres(lista):
    if not lista:
        return 0
    cabeza, *resto = lista
    aporte = cabeza if cabeza % 3 == 0 else 0
    return aporte + suma_multiplos_tres(resto)
 
 
def main():
    cantidad = int(input("ingrese la cantidad de numeros a contar: "))
    numeros = generar_lista(cantidad)
    print(f"los numeros son: {numeros}")
 
    resultado = suma_multiplos_tres(numeros)
    print(f"la suma de los múltiplos de 3: {resultado}")
 
 
if __name__ == "__main__":
    main()