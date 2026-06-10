
texto = ""

# =========================================
def ingresser_texto():
    global texto
    print("=========================")
    print("    REGISTRAR TEXTO")
    print("=========================")
    texto = input("Ingrese la frase o texto a analizar: ")

    print


# =========================================
def analis(texto):
    print("=========================")
    print("   ANALISIS DE TEXTO")
    print("=========================")

    




# =========================================
opcion = 0

while opcion != 3:

    print("==================================")
    print("       ANALISIS DE TEXTO")
    print("==================================")
    print("1. ingreser texto para su analisis")
    print("2. Análisis del texto ingresado")
    print("3. salir")
    print("==================================")

    opcion = str(input("Seleccione: "))

    print("==================================")

    if opcion == "1":
        print("ingrese su texto")
        texto = str(input(">> "))
    
    elif opcion == "2":
        analis(texto)

    elif opcion == "3":
        print("Saliendo...")

    else:
        print("no valido...")

print("==================================")

