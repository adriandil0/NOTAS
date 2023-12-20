import os

menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir"
subMenuNotas = "1.Parciales\n2.Quices\n3.Trabajos\n4.Regresar al menu principal"
hasError = True
def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError == True):
        try:
            #hasError = False
            return int(input(":)"))
        except ValueError:
            hasError = True

def menuNotas() -> int:
    os.system('cls')
    header = """
    ********************************
    *   MENU REGISTRO DE NOTAS     *
    ********************************
    """
    global hasError
    print(header)
    print(subMenuNotas)
    while (hasError == True):
        try:
            return int(input(":)"))
        except ValueError:
            hasError = True