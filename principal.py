import os
import menus as menu
import alumnos as st

alumnos ={}
isActive = True
opMenu=0

while (isActive) :
    os.system("cls")
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if(opMenu == 1):
            rta = "S"
            while (rta in ["S","s"]):
                os.system("cls")
                alumnos.update(st.regAlumno())
                rta = input("Desea registrar otro Alumno S(si) o N(No)").upper()
        
        elif (opMenu == 2):
            menu.menuNotas()
            
        elif (opMenu == 3):
            codAlumno = input("Ingrese el codigo a buscar :")
            st.buscarAlumno(codAlumno,alumnos)
        elif (opMenu == 4):
            isActive = False
            