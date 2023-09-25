# _ Protected
# __ Private
class vehiculo:
    #Desde Aqui se incician los atributos de la clase
    __marca = 'Audi' # Privado
    __velocidad = 0 # Privad
    color = '' #Publico
    _pais = 'Colombia' # Protegido
    #Metodos: Desde aqui se inician los metodos de la clase Vehiculo
    def setVelocidad(self, cant):
        self.__velocidad = self.__velocidad + cant
    def getVelocidad(self):
        return self.__velocidad 

obj1 = vehiculo
#obj1.color = input("Cual es el color de Vehiculo: ")
#print(obj1.color)
opc = 0
while opc!=5:
    opc = int(input("1. Acelerar, 2. Mostrar, 3. Desacelerar opcion: "))
    if(opc==1):
        obj1.setVelocidad(obj1, 15)
    if(opc==2):
        vel = obj1.getVelocidad(obj1)
        print(vel)
    if(opc==3):
        obj1.setVelocidad(obj1, -15)
