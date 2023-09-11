#Aqui se definieron  las variables

Nm= input("Digite El Nombre Del Estudiante: " )
Gno= input((" Cual es Tu Genero: M/ F "))
print("BIENVENIDO (A)" , Nm )
Nota1 = float(input("Ingresa La Nota1: "))
Nota2 = float(input("ingresa La Nota2: "))
Nota3 = float(input("Ingresa La Nota3: "))
sm = Nota1 + Nota2 + Nota3 
nf = sm / 3
mod =0
m=0
f=0

#cree un diccionario con El nombre y notas del estudiante

Est = {
    "Nombre" :  Nm,
    "Nota1"  :  Nota1 ,
    "Nota2"  :  Nota2 ,
	"Nota3"   :  Nota3
    	}
# Aqui se suman las notas digitadas por el alumno(a)
 #Aqui se le muestra la nota parcial al estudiante
print("La Suma de tus notas es: " , sm)
print(" ")
print( "La Nota Parcial - Final de" , Nombre, ',' " Es: %.2f " %(nf))
print(" ")
print(Est["Nombre"])
print(" ")
#Se le pregunta por la nota que desea modificar
mod = input("Que nota deseas modificar, Escoje una opcion: 1, 2 o 3 : ")
print(" ")
#Se colocan condicionales para la opcion elejida
if mod == "1" :
	Nota1= float(input(" Ingrese la Nueva Nota: "))
elif mod == "2" :
 	Nota2= float(input(" Ingrese la Nueva Nota: "))
elif mod == "3" :
    Nota3= float(input(" Ingrese la Nueva Nota: "))
else:
    print("No Se Pudo hacer Esta Operacion: ")
    print(" ")
 #Se le muestran las notas actualizadas y el promedio
    
print(" Tus Notas Actuales son: " , Nota1 , Nota2  , Nota3  ) 
sm = Nota1 + Nota2 + Nota3 
nf = sm / 3
print(" ")
print( "Su Nota  final es:  %.2f"  %(nf))
#Mostramos por pantalla el nombre y la nota final
if  nf >= 3 :	
	print("El (La) Alumno(a)" ,Nombre ,"Aprobó la Materia")
	print("***FELICIDADES***")	
elif  nf < 3 :
	print("El (La) Alumno(a)," , Nombre , "No Aprobó la Materia ")
	print("**Debes esforzarte más** ")
else:
	print("FIN")
# Volvemos a pedir el nombre de el siguiente alumno
#A Traves del ciclo While
while Nm==0 or Nota1<=6 or Nota2<=6 or Nota3<=6:
	print("\n")
	Nm= input("Digite El Nombre Del Estudiante : ")
	Saludo = print("BIENVENIDO (A)" , Nm )
	Genero= input((" Cual es Tu Genero: M/ F "))
	Nota1 = float(input("Ingresa La Nota1: "))
	Nota2 = float(input("ingresa La Nota2: "))
	Nota3 = float(input("Ingresa La Nota3: "))
	sm = Nota1 + Nota2 + Nota3 
	nf = sm / 3
	Nombre = Nm
	mod =0
	print("La Suma de tus notas es: " , sm)
	print( "La Nota Parcial - Final de" , Nombre, ',' " Es:  ", nf)
	mod = input("Que nota deseas modificar, Escoje una opcion: 1, 2 o 3 : ")
	print(" ")
	if mod == "1" :
		Nota1= float(input(" Ingrese la Nueva Nota: "))
	elif mod == "2" :
 		Nota2= float(input(" Ingrese la Nueva Nota: "))
	elif mod == "3" :
    		Nota3= float(input(" Ingrese la Nueva Nota: "))
	else:
   	 print("No Se Pudo hacer Esta Operacion: ")
	print(" ")
	print(" Tus Notas Actuales son: " , Nota1 , Nota2  , Nota3  ) 
	sm = Nota1 + Nota2 + Nota3 
	nf = sm / 3
	print(" ")
	print( "Su Nota  final es:  %.2f"  %(nf))


	if  nf >= 3 :	
		print("El (La) Alumno(a) ," ,Nm ,"Aprobó la Materia")
		print("		***FELICIDADES***		")

	elif  nf < 3 :
		print("El (La) Alumno(a)," , Nm , "No Aprobó la Materia ")
	else:
		print("FIN")