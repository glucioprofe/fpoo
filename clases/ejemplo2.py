# Sistema de registro de autos considerando el control de velocidad

class vehiculo:
    #Desde Aqui se incician los atributos de la clase
    id = 0
    marca='' # Privado
    velocidadActual = 0 # La velocidad del vehiculo en el momento T
    velocidadMaxima = 0 # El limite que puede alcanzar el auto
    color = '' #Publico
    pais = 'Colombia' # Protegido
    #Metodo Constructor
    def __init__(self, diccionario):
        self.id = diccionario["id"]
        self.marca = diccionario["marca"]
        self.color = diccionario["color"]
        if(diccionario["pais"]!=''):
            self.pais = diccionario["pais"]
        self.velocidadMaxima = diccionario["maxima"]
        
    #Metodos: Desde aqui se inician los metodos de la clase Vehiculo
    def setVelocidadMaxima(self, cant):
        self.velocidadMaxima = cant
    def setVelocidad(self, cant):
        self.velocidadActual = self.velocidadActual + cant
        if(self.velocidadActual<0):
            self.velocidadActual = 0
        elif(self.velocidadActual > self.velocidadMaxima):
            self.velocidadActual = self.velocidadMaxima        
    def getMarca(self):
        return self.marca 
    def getVelocidad(self):
        return self.velocidadActual 

def mostrar():
    for elem in listaAutos:
        print( elem.id, elem.marca, elem.pais, elem.color, elem.velocidadMaxima, elem.velocidadActual )
def cambiarVelocidad(id, cant):
    for elem in listaAutos:
        if(id==elem.id):
            elem.setVelocidad(cant)

    
# COMO HAGO PARA PODER IDENTIFICAR CADA CARRO
# COMO PODRIA HACER PARA ESCOGE EL CARRO QUE VAMOS A CONDUCIR ....


# AQUI COMIENZA A EJECUTARSE EL PROGRAMA
coche = { 'id': 0, 'marca': '', 'color': '','pais': '','maxima': 0 }
listaAutos = [] #Para Guardar todos los carros
opc = 0
while opc!=5:
    opc = int(input("1. Registrar\n2. Mostrar\n3. Acelerar\n4. Desacelerar\n5. Salir\nSeleccione opcion: "))
    if(opc==1):
        coche["marca"] = input("Registre Marca: ")
        coche["color"] = input("Registre Color: ")
        coche["pais"] = input("Registre Pais: ")
        coche["maxima"] = int(input("Registre Velocidad Maxima: "))
        coche['id'] = int(len(listaAutos)) + 1
        obj = vehiculo(coche)
        listaAutos.append(obj)
    elif(opc==2):
        mostrar()
    elif(opc==3 or opc==4):
        mostrar()
        selectId = int(input("Seleccione el id del auto: "))        
        if(opc==3):
            acelerar = int(input("Cuanto desea acelerar: "))
        else:
            acelerar = int(input("Cuanto desea frenar: "))
            acelerar = acelerar * -1
        cambiarVelocidad(selectId, acelerar)        
