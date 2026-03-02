
# Define unha funcion para sumar dous numeros
def sumar(a, b):
    return a + b
# Define unha funcion para restar dous numeros
def restar(a, b):
    return a - b
# Define unha funcion para multiplicar dous numeros
def multiplicar(a, b):
    return a + b

print("Calculadora simple")
# Pide numeros ao usuario e converteos a decimal
num1 = float(input("Introduce o primero número: "))
num2 = float(input("Introduce o segundo número: "))
# Chama ás funcions e amosa os resultados
print("Suma:", sumar(num1, num2))
print("Resta:", restar(num1, num2)) 
print("Multiplicación:", multiplicar(num1, num2))
