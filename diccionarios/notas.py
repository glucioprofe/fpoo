#Realice un programa que permita registrar estudiantes y sus respectivas notas. Se pueden modificar notas  y se calcula la nota final

# estudiante: nota 1, nota 2, nota 3. Nombre.
import os
import time

alumno = { 'nombre': ''}
alumnos = []
def menu():
    opc = 0
    while(opc<1)or(opc>5):
        os.system('cls')
        print("Menu")
        print("1. Registrar Alumno")
        print("2. Registrar Notas")
        print("3. Mostrar Alumnos Alumno")
        print("4. Modificar nota")
        print("5. Salir")
        opc = int(input("Ingrese Opción: "))
    return opc

def registrar():
    os.system('cls')
    nombre = input("Registre nombre completo del estudiante: ")
    alumno = {
        'id': len(alumnos) + 1,
        'nombre': nombre
    }
    alumnos.append(alumno)
    
def mostrar():
    os.system('cls')
    for item in alumnos:
        print("Id: ", item["id"], "Alumno: ", item["nombre"])
    time.sleep(5)

opcion = 0
while (opcion!=5):
    opcion = menu()
    if opcion==1:
        registrar()
    elif opcion==3:
        mostrar()