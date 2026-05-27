# =============================================
#      Registro Académico de Estudiantes 
# =============================================

# Lista de los Estudiantes registrados

Estudiantes = []

# =============================================
#     Funciones para registrar Estudiantes
# =============================================

def Registro_estudiantes():
    print("===REGISTRAR Estudiante===")

    Nombre = str(input("Nombre del estudiante: "))
    print("Ingreselas notas (no menores a 0.0 y mayores a 5.0)")
    Nota1 = float(input("nota1: "))
    Nota2 = float(input("nota2: "))
    Nota3 = float(input("nota3: "))
    Nota4 = float(input("nota4: "))
    Nota5 = float(input("nota5: "))

    suma_notas = Nota1 + Nota2 + Nota3 + Nota4 + Nota5
    Promedio = suma_notas / 5
    if Promedio > 3.0 < 5.0:
        print("APRUEBA")
                
    else:
        print("REPRUEBA")

    estudiante = (Nombre,Promedio)

    Estudiantes.append(estudiante)
    print("Listo...")

# =============================================
# Funcion para odservar la lista de Estudiantes
# =============================================

def Lista_estudiantes():
    print("\n===LISTA DE SETUDIANTES===")

    if Estudiantes == 0:
        print("No cean registrado nigun estudiante")
        
    else:

        for estudiante in Estudiantes:
            print("=====================")
            print("Nombre:", estudiante[0])
            print("Promedio:", estudiante[1])
            if estudiante[1] > 3.0 < 5.0:
                print("APRUEBA")
                
            else:
                print("REPRUEBA")
    
    print()

# =============================================
#                   BUSCAR
# =============================================

def buscar():
    print("\n===BUSCAR ESTUDIANTE===")
    no = str(input("Nombre del estudiante: "))
    encontrado = False

    for estudiante in Estudiantes:

        if (no.lower() == estudiante[0].lower()):

            print("\nEstudiante encontrado")
            print("Nombre:", estudiante[0])
            print("Promedio:", estudiante[1])

            encontrado = True

    if encontrado == False:
        print("Estudiante no encontrado.")

    print()


# =============================================
#                  INTERFAS
# =============================================
odcion = 0

while odcion != 4:

    print("=============================================")
    print("      Registro Académico de Estudiantes ")
    print("=============================================")
    print("1. Registrar un estudiante")
    print("2. Ver listado de estudiantes")
    print("3. Buscar estudiante")
    print("4. Salir")
    print("=============================================")

    odcion = int(input("> "))

    if odcion == 1:
        Registro_estudiantes()
    
    elif odcion == 2:
        Lista_estudiantes()

    elif odcion == 3:
        buscar()
    
    elif odcion == 4:
        print("Terminando...")

    else: 
        print("!ERROR")