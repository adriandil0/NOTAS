import os

def regAlumno()->dict:
    codigo = input("Ingrese el codigo del estudiante : ")
    nombre = input("Ingrese el nombre del estudiante : ")
    edad = int(input("Ingrese el edad del estudiante : "))
    alumno ={
        "codigo" : codigo,
        "nombre" : nombre,
        "edad" : edad,
        "notas":{
            "paciales":[],
            "quices":[],
            "trabajos" :[]
        }
    }
    return {codigo : alumno}

def buscarAlumno(codAlumno : str,alumnos : dict):
    data = alumnos.get(codAlumno,-1)
    if (type(data) == dict):
        for llave,valor in data.items():
            print(f"{llave} : {valor}")
        os.system("pause")
    else:
        print(f"No se encontro el estudiante con el codigo {codAlumno}")
        os.system("pause")

        #hhss