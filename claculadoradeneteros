def multiplicar(primero, segundo):
    digitos = max(len(str(primero)), len(str(segundo)))
    if digitos <= 1:
        return primero * segundo
 
    base = 10 ** (digitos // 2)
    alta1, baja1 = primero // base, primero % base
    alta2, baja2 = segundo // base, segundo % base
 
    return (multiplicar(alta1, alta2) * base ** 2
            + (multiplicar(alta1, baja2) + multiplicar(baja1, alta2)) * base
            + multiplicar(baja1, baja2))
 
 
def calculadora():
    primero = int(input("Ingrese el primer entero: "))
    segundo = int(input("Ingrese el segundo entero: "))
 
    resultado = multiplicar(primero, segundo)
 
    print(f"El resultado de multiplicar {primero} y {segundo} es: {resultado}")
 
 
if __name__ == "__main__":
    calculadora()