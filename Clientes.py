import os;
import mariadb;
import time;
from datetime import datetime;
import random;



class Cliente():
    def limpioPantalla(self):
            sisOper = os.name
            if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
                os.system("clear")
            elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
                os.system("cls")
    

    def menuCliente(self):
        self.limpioPantalla()
        print("Bienvenido al menú de Clientes")
        opcion=int(input('''¿que acción desea realizar?

                        
                        1 - Realizar una compra
                        2 - Eliminar tus datos de nuestro sistema
                        3 - Modifica tus datos de cliente
                        4 - Ver todos mis datos
                        5 - Salir del sistema 
                            
                            ingrese la opción: '''))
                        
        if opcion == 1:
            self.menuVentas()
            
        elif opcion == 2:
            self.limpioPantalla()
            print("ingrese los siguientes datos para poder borrar su información de nuestros registros")
            self.dni = int(input("Ingrese su número de DNI: "))
            self.nombre = input("ingrese su nombre: ")
            self.apellido = input("ingrese su apellido: ")

            mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
            mycursor = mydb.cursor()
            sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            if len(myresultado) >0:
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchone()
                for ind in myresultado:
                    #print(ind)
                    self.ind= ind
            else: self.ind = "vacio"
            
            mycursor = mydb.cursor()
            sql = "SELECT nombre FROM usuarios where nombre LIKE '"+self.nombre+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            if len(myresultado) >0:
                mycursor = mydb.cursor()
                sql = "SELECT nombre FROM usuarios where nombre LIKE '"+self.nombre+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchone()
                for ind2 in myresultado:
                    #print(ind2)
                    self.ind2= ind2
            else: self.ind2 = "vacio"
   
            mycursor = mydb.cursor()
            sql = "SELECT apellido FROM usuarios where apellido LIKE '"+self.apellido+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            
            if len(myresultado) >0:
                mycursor = mydb.cursor()
                sql = "SELECT apellido FROM usuarios where apellido LIKE '"+self.apellido+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchone()
                for ind3 in myresultado:
                    #print(ind3)
                    self.ind3= ind3
            else: self.ind3 = "vacio"         
            time.sleep(1)

            if self.ind == str(self.dni) and self.ind2 == self.nombre and self.ind3 == self.apellido:
                mycursor = mydb.cursor()
                sql = "DELETE FROM usuarios WHERE dni LIKE '%"+str(self.dni)+"%'"
                mycursor.execute(sql)
                mydb.commit()
                print("se borraron todos sus datos de nuestra base de datos")
                time.sleep(2)
                self.limpioPantalla()
                print("Muchas gracias por utilizar nuestro servicio.\nVuelva pronto. Safety in Life A&A")
            else:
                print("no se puede borrar los datos no coinciden")
                self.menuCliente()
                    

        elif opcion == 3:
            self.limpioPantalla()
            item = int(input('''
                ¿Que dato desea modificar?:
                
                1 - Dirección 
                2 - Telefono
                3 - Email
                4 - Situación frente al IVA
                5 - volver a menú principal
                6 - Salir del Sistema
                
                Ingrese la opción deseada: '''))              

            if item == 1:
                self.limpioPantalla()
                print("Actualizar dirección\n")
                self.dni =int(input("ingrese su DNI: "))
                self.direccion = input("ingrese su nueva dirección: ")
                mydb = mariadb.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root", 
                    database = "SafetyInLife"
                    )
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.ind= ind
                else: self.ind = "vacio"

               
                if self.ind == str(self.dni):
                    mycursor = mydb.cursor()
                    sql = "UPDATE usuarios SET direccion = '"+self.direccion+"' WHERE dni = "+str(self.dni)
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Se modifico exitosamente su dirección")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()
                else: 
                    print("no se pudo actualizar dirección, ya que el dni no se encuentra registrado")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()

                
            elif item == 2:
                self.limpioPantalla()
                print("Actualizar número telefónico\n")
                self.dni =int(input("ingrese su DNI: "))
                self.telefono = input("ingrese su nuevo número telefónico: ")
                mydb = mariadb.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root", 
                    database = "SafetyInLife"
                    )
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.ind= ind
                else: self.ind = "vacio"

               
                if self.ind == str(self.dni):
                    mycursor = mydb.cursor()
                    sql = "UPDATE usuarios SET telefono = '"+self.telefono+"' WHERE dni = "+str(self.dni)
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Se modifico exitosamente su número telefónico")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()
                else: 
                    print("no se pudo actualizar su número telefónico, ya que el dni no se encuentra registrado")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()
                
            elif item == 3:
                
                self.limpioPantalla()
                print("Actualizar email\n")
                self.dni =int(input("ingrese su DNI: "))
                self.email = input("ingrese su nuevo email: ")
                mydb = mariadb.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root", 
                    database = "SafetyInLife"
                    )
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.ind= ind
                else: self.ind = "vacio"

               
                if self.ind == str(self.dni):
                    mycursor = mydb.cursor()
                    sql = "UPDATE usuarios SET email = '"+self.email+"' WHERE dni = "+str(self.dni)
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Se modifico exitosamente su email")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()
                else: 
                    print("no se pudo actualizar su email, ya que el dni no se encuentra registrado")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()

                
            elif item == 4:
                
                self.limpioPantalla()
                print("Actualizar Situación frente al IVA\n")
                self.dni =int(input("ingrese su DNI: "))
                self.situacionIva=int(input('''Ingrese su nueva situación frente al I.V.A
                                    4 - Consumidor Final
                                    
                                    ingrese la opción: '''))
                if self.situacionIva == 1:
                    self.situacionIva = "responsable inscripto"
                elif self.situacionIva == 2:
                    self.situacionIva = "monotributista"
                elif self.situacionIva == 3:
                    self.situacionIva = "excento"
                elif self.situacionIva == 4:
                    self.situacionIva = "consumidor final"
                mydb = mariadb.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root", 
                    database = "SafetyInLife"
                    )
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.ind= ind
                else: self.ind = "vacio"

               
                if self.ind == str(self.dni):
                    mycursor = mydb.cursor()
                    sql = "UPDATE usuarios SET sitIva = '"+self.situacionIva+"' WHERE dni = "+str(self.dni)
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Se modifico exitosamente su situación frente al iva")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()
                else: 
                    print("no se pudo actualizar su situacion frente al iva, ya que el dni no se encuentra registrado")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuCliente()



            elif item == 5:
                self.limpioPantalla()
                self.menuCliente()
            elif item == 6:
                self.limpioPantalla()
                print("Muchas gracias por utilizar nuestro servicio.\nVuelva pronto. Safety in Life A&A")
            
        elif opcion == 4:
            self.limpioPantalla()
            print("para ver su personales\n")
            self.dni =int(input("Ingrese su DNI: "))
            
            mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
            mycursor = mydb.cursor()
            sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            if len(myresultado) >0:
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchone()
                for ind in myresultado:
                    #print(ind)
                    self.ind= ind
            else: self.ind = "vacio"


            if self.ind == str(self.dni):
                    mycursor = mydb.cursor()
                    sql = "SELECT nombre, apellido, dni, direccion, telefono, email, usuario FROM usuarios where dni = "+str(self.dni)
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    for ind in myresultado:
                        print(ind)
                    time.sleep(4)
                    self.limpioPantalla()
                    self.menuCliente()
            else: print("no se puede mostrar los datos el dni no se encuentra registrado en nuestro sistema")

        elif opcion == 5:
            self.limpioPantalla()
            print("Muchas gracias por utilizar nuestro servicio.\nVuelva pronto. Safety in Life A&A")









    def menuVentas(self):
        self.limpioPantalla()
        print("Carrito de compras")

        opcion=int(input('''¿que acción desea realizar?

                        1 - Añadir productos al carrito de compras
                        2 - Mostrar listado completo de articulos
                        3 - Volver a menú principal
                        4 - Salir del sistema
                            
                            ingrese la opción: '''))
                            # menu funciona correctamente
                            # 1 no lo hice
                            # 2 funciona correctamente
                            # 3 funciona correctamente
                            # 4 funciona correctamente
        if opcion == 1:
            self.limpioPantalla()
            self.dni = input("ingrese nuevamente su dni por seguridad fiscal: ")
            self.fecha = datetime.now()


            mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            database = "SafetyInLife"
            )

            mycursor = mydb.cursor()
            sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            if len(myresultado) >0:
                mycursor = mydb.cursor()
                sql = "SELECT dni FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchone()
                for ind in myresultado:
                    #print(ind)
                    self.ind= ind
            else: self.ind = "vacio"

            if self.ind ==self.dni:
                mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
                mycursor = mydb.cursor()
                sql = "SELECT nombre FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT nombre FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.nombre= ind
                
                
                mycursor = mydb.cursor()
                sql = "SELECT apellido FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT apellido FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.apellido= ind

                mycursor = mydb.cursor()
                sql = "SELECT sitIva FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT sitIva FROM usuarios where dni LIKE '"+str(self.dni)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.sitIva= ind
            else:
                print("el dni ingresado no corresponde")
                self.menuVentas()

            self.limpioPantalla()
            print("Bienvenido a Safety in LIfe A&A")
            print(f"la facturación sera emitida a nombre de {self.nombre} {self.apellido}")
            respuesta = "si"
            self.total = 0
            self.subtotal = 0
            self.codVenta = random.randint(1, 244)
            while respuesta =="si":
                self.total = self.total + self.subtotal
                
                mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
                self.articulo = input("ingrese el articulo que desea comprar: ")

                mycursor = mydb.cursor()
                sql = "SELECT nombre FROM articulos where nombre LIKE '"+str(self.articulo)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT nombre FROM articulos where nombre LIKE '"+str(self.articulo)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.nombreArticulo= ind
                mycursor = mydb.cursor()
                sql = "SELECT precio FROM articulos where nombre LIKE '"+str(self.articulo)+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT precio FROM articulos where nombre LIKE '"+str(self.articulo)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.precio= int(ind)
                    
                if self.nombreArticulo == self.articulo:
                    self.stock = int(input("ingrese la cantidad: "))
                    mycursor = mydb.cursor()
                    sql = "SELECT stock FROM articulos where nombre LIKE '"+str(self.articulo)+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchall()
                    if len(myresultado) >0:
                        mycursor = mydb.cursor()
                        sql = "SELECT stock FROM articulos where nombre LIKE '"+str(self.articulo)+"'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchone()
                        for ind in myresultado:
                            #print(ind)
                            self.stockDispo= int(ind)
                    
                        if self.stockDispo > 0 and self.stockDispo> self.stock:
                            if self.sitIva == "responsable inscripto" or self.sitIva == "monotributista" or self.sitIva == "exento":
                                self.iva = 1.10
                            elif self.sitIva == "consumidor final":
                                self.iva = 1.21
                                
                            
                            self.precioUnitario =  self.precio * self.iva
                            self.subtotal = (self.stock * self.precio) * self.iva
                            print(f"el precio total de los {self.stock} {self.articulo} es: ${self.subtotal}")
                            
                            
                            self.total = self.total + self.subtotal
                            print(f"el subtotal acumulado al momento es de ${self.total}")

                            

                            respuesta = input("¿Desea agregar un nuevo producto si o no?\nIngrese su respuesta: ")

                            self.nuevoStock = self.stockDispo - self.stock

                            mydb = mariadb.connect(
                            host="127.0.0.1",
                            user="root",
                            password="root", 
                            database = "SafetyInLife"
                            )


                            mycursor = mydb.cursor()
                            sql = "UPDATE articulos SET stock = '"+str(self.nuevoStock)+"'  WHERE nombre = \'"+self.articulo+"\'"
                            mycursor.execute(sql)
                            mydb.commit()

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO ventas (codVenta, articulo, precioUnitario, dniCliente, cantidadArticulos, subtotal, fecha, nombreCliente, apellidoCliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (self.codVenta, self.articulo,  self.precioUnitario,self.dni, self.stock, self.subtotal, self.fecha, self.nombre, self.apellido)
                            mycursor.execute(sql, val)
                            mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
                            
                            time.sleep(1)
                            



                            if respuesta == "no":
                                self.limpioPantalla()
                                print(f"el total a abonar es de ${self.total}")
                                print("Pase por caja para abonar, muchas gracias por utilizar nuestro servicio, vuelva pronto - Safety in Life A&A")

                    else: 
                        print("el producto seleccionado no esta en nuestra base de datos")
                        self.menuVentas()




        elif opcion == 2:
            print("LISTADO COMPLETO DE ARTICULOS \n")
            mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            database = "SafetyInLife"
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM articulos"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            for ind in myresultado:
                print(ind)
            time.sleep(5)
            self.menuVentas()
        elif opcion == 3:
            self.limpioPantalla()
            self.menuCliente()
        elif opcion == 4:
            self.limpioPantalla()
            print("Muchas gracias por utilizar nuestro servicio.\nVuelva pronto. Safety in Life A&A")