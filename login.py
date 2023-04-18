import os;
import Admin;
import Clientes;
import mariadb;
import time;
from datetime import datetime;
import random;

class MenuPrincipal():
    def limpioPantalla(self):
            sisOper = os.name
            if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
                os.system("clear")
            elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
                os.system("cls")

    def login(self):
        
            
            self.limpioPantalla()
            print("Bienvenido/a a Safety in Life A&A - Seguridad electrónica")
            opcion=int(input('''¿a que sección desea ingresar?

                                1 - Iniciar sesión
                                2 - Si no tenes cuenta, Regístrate aquí
                                3 - ingrese como consumidor final sin registrarse
                                4 - Salir del sistema
                                
                                ingrese la opción: '''))
                                # menu funciona correctamente
                                # 1 funciona correctamente
                                # 2 funciona correctamente
                                # 3 funciona -> falta carrito de compras
                                # 4 funciona correctamente
            if opcion == 1:
                self.limpioPantalla()
                print("Bienvenido/a a Safety in Life A&A - Seguridad electrónica")
                self.usuario =input("Ingrese su nombre de usuario: ")
                self.contraseña =input("Ingrese su contraseña: ")
               
                mydb = mariadb.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root", 
                    database = "SafetyInLife"
                    )
                mycursor = mydb.cursor()
                sql = "SELECT usuario FROM usuarios where usuario LIKE '"+self.usuario+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT usuario FROM usuarios where usuario LIKE '"+self.usuario+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        print(ind)
                        self.ind= ind
                else: self.ind = "vacio"
                
                mycursor = mydb.cursor()
                sql = "SELECT contraseña FROM usuarios where contraseña LIKE '"+self.contraseña+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT contraseña FROM usuarios where contraseña LIKE '"+self.contraseña+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind2 in myresultado:
                        print(ind2)
                        self.ind2= ind2
                else: self.ind2 = "vacio"

            

                if self.ind == self.usuario and self.ind2 == self.contraseña:
                    mycursor = mydb.cursor()
                    sql = "SELECT tipoUsuario FROM usuarios WHERE usuario = \'"+self.usuario+"\' AND contraseña LIKE \'%"+self.contraseña+"%\'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind2 in myresultado:
                        #print(ind2)
                        self.tipoUsuario= ind2
                    
                    
                    if self.tipoUsuario == "cliente":
                       
                        cliente = Clientes.Cliente()
                        cliente.menuCliente()
                        
                        
                    elif self.tipoUsuario == "administrador":
                        new = Admin.Admin()
                        new.menuAdmin()
                else: 
                    print("usuario y contraseña no coinciden")
                    time.sleep(2)
                    self.login()
                    
                    
            elif opcion == 2:
                self.limpioPantalla()
                
                self.tipoUsuario = "cliente"
                self.dni= int(input("Ingrese su dni: "))
                #validar que no haya otro dni igual
                #si hay un dni igual informar que ya hay un usuario con su mismo dni
                #dar la opcion de recuperar contraseña o Salir
                #pedir nueva contraseña
                #poner query para modificar contraseña de la base
                #llamar al menú principal
                self.usuario = input("ingrese nombre de usuario: ")
                #validar que no haya otro nombre de usuario igual
                #si lo hay dar aviso 
                self.contraseña = input ("ingrese contraseña: ")
                self.nombre= input("Ingrese su nombre: ")
                self.apellido=input ("Ingrese su apellido: ")
                self.direccion=input("Ingrese su dirección domiciliaria: ")
                self.telefono=input("Ingre su su número de teléfono: ")
                self.email=input("ingrese su email: ")
                self.situacionIva=int(input('''Ingrese su situación frente al I.V.A
                                        1 - Responsable Inscripto
                                        2 - Monotributista
                                        3 - Excento
                                        4 - Consumidor final
                                        
                                        ingrese la opción: '''))
                if self.situacionIva == 1:
                    self.situacionIva = "responsable inscripto"
                elif self.situacionIva == 2:
                    self.situacionIva = "monotributista"
                elif self.situacionIva == 3:
                    self.situacionIva = "exento"
                elif self.situacionIva == 4:
                    self.situacionIva = "consumidor final"

                mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
                mycursor = mydb.cursor()
                sql = "INSERT INTO usuarios (nombre, apellido, dni, direccion, telefono, usuario, contraseña, email, sitIva, tipoUsuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (self.nombre, self.apellido, self.dni, self.direccion, self.telefono, self.usuario, self.contraseña, self.email, self.situacionIva, self.tipoUsuario)
                mycursor.execute(sql, val)
                mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
                print("Usted se registro exitosamente en nuestro sistema")  # muestro mensaje para saber que se insertaron bien
                time.sleep(3)
                self.login()

            elif opcion ==3:
                self.limpioPantalla()
                print("Bienvenido a Safety in LIfe A&A")
                print("Usuario no registrado")
                self.nombre=input("ingrese su nombre para la facturación: ")
                self.apellido= input("ingrese su apellido para la facturación: ")
                self.dni = input("ingrese su dni: ")
                self.menuVentas()
                
            elif opcion == 4:
                self.limpioPantalla()
                print("MUCHAS GRACIAS POR UTILIZAR NUESTRO SISTEMA - Safety in Life A&A ")
               

    
    def menuVentas(self):
       
        self.limpioPantalla()
        print("Bienvenido a Safety in LIfe A&A")
        print(f"la facturación sera emitida a nombre de {self.nombre} {self.apellido}")
        opcion=int(input(f'''¿que acción desea realizar {self.nombre}?

                            1 - Añadir productos al carrito de compras
                            2 - Mostrar listado completo de articulos
                            3 - Volver a menú principal
                            4 - Salir del sistema
                                
                                ingrese la opción: '''))
                           
        if opcion == 1:
            respuesta = "si"
            self.total = 0
            self.subtotal = 0
            self.codVenta = random.randint(1, 244)
            self.fecha = datetime.now()
            while respuesta =="si":
                
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
                    
                        
                                
                            
                            self.precioUnitario =  self.precio * 1.21
                            self.subtotal = (self.stock * self.precio) * 1.21
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
            self.login()
        elif opcion == 4:
            self.limpioPantalla()
            print("Muchas gracias por utilizar nuestro servicio.\nVuelva pronto. Safety in Life A&A")
            
                 