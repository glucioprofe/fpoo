class personaje:
    #Desde Aqui se incician los atributos de la clase
    id = 0
    name='' 
    coins=98
    life=3
    size=1 # 1 Pequeño / 2 Grande
    world = 1 # 8 Mundos
    level = 1 # 4 Niveles
    shoot = False
    #Metodo Constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):        
        tam = ("Pequeño", "Grande")[self.size==2] # Operador Ternario if self.size==1 tam = else tam grande
        cadena=self.name+". Coins: "+str(self.coins)+" Vidas: "+str(self.life)+" Level: "+str(self.world)+"-"+str(self.level)+" Tamaño: "+tam
        return cadena
    #Metodos: Desde aqui se inician los metodos de la clase Vehiculo
    #El tamaño cambia al recoger hongos de crecimiento.
    def setSize(self):
        self.size = 2
    #Si el personaje esta grande puede recoger flores que le dan el poder de disparar.
    def setShoot(self):
        self.shoot = True
        
    #Si el personaje recoge 100 monedas estas se canjean automáticamente por una vida.
    def setCoins(self):
        self.coins = self.coins + 1
        if self.coins == 100:
            self.coins = 0
            self.life = self.life + 1
    #El personaje se enfrenta a dos incidentes que son sencillo y grave.
    # Si type = 1 Sencillo, type = 2 Grave
    def setEvent(self, type):
        if(self.size==1):
            self.life = self.life - 1
        elif(self.size==2 and type==1):
            self.size = 1
            self.shoot = False
        elif(self.size==2 and type==2):
            self.life = self.life - 1
            self.size = 1
            self.shoot = False
        
    def setLife(self):
        self.life = 2
    def setLevel(self):
        self.level = self.level + 1
        if (self.level==5):
            self.level = 1
            if(self.world<8):
                self.world = self.world  + 1
            else:
                self.world = 1
opc = 0
player = personaje 
print("Video Juego MB V0.0001")
while opc!=10:
    if(player.id!=0):
        print(player)
            
    print("1. Iniciar Juego")
    if(player.id!=0):
        print("2. Recoger Monedas")
        print("3. Recoger Hongo Crecimiento")
        if(player.size==2):
            print("4. Recoger Flor")
        print("5. Avanzar Nivel")
        print("6. Incidente")
    opc = int(input("Seleccione opcion: "))
    if(opc==1):
        player = personaje(1, "Mario")
    elif(opc==2):
        player.setCoins()
    elif(opc==3):
        player.setSize()
    elif(opc==4):
        player.setShoot()
    elif(opc==5):
        player.setLevel()
    elif(opc==6):
        incidente = 0
        while(incidente!=1 and incidente!=2):
            incidente = int(input("Seleccione opcion -> 1. Sencillo / 2. Grave: "))
        player.setEvent(incidente)