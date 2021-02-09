# Práctica de Python - Inteligencia Artificial.
# Alexander Carrillo

nombre = "Alexander"
apellido = "Carrillo"

print("Ingresa primero tu nombre y luego tu apellido.")

entradaName = input()
entradaApellido = input()

if entradaName == nombre and entradaApellido == apellido:
    print("################################## \n")
    print(f"Bienvenido {nombre} {apellido} !!! \n")
    print("##################################")
else: 
    print("¡¡Intruso, no eres Alexander!!")

## Condicional para comprobar si el usuario es correcto.