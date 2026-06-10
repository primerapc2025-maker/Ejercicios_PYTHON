
texto = ""

# =========================================
def analis(texto):
    print("=========================")
    print("   ANALISIS DE TEXTO")
    print("=========================")

    cant_carac = len(texto)
    print(f"Cantidad de caracteres: ", cant_carac)

    cant_sin_espa = len(texto.replace(" ", ""))
    print(f"Sin espasios: ", cant_sin_espa)

    cant_voc = sum(1 for letra in texto.lower() if letra in "aeiouáéíóúAEIOUÁÉÍÓÚ")
    print(f"Cantidad de vocales: ", cant_voc)

    carac_espe = sum(1 for c in texto if not c.isalnum() and not c.isspace())
    print(f"cantidad de caracteres especiales: ", carac_espe)

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
        print("=========================")
        print("    REGISTRAR TEXTO")
        print("=========================")
        print("ingrese su texto")
        texto = str(input(">> "))
    
    elif opcion == "2":
        analis(texto)

    elif opcion == "3":
        print("Saliendo...")

    else:
        print("no valido...")

print("==================================")

