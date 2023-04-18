import os;
import Articulos;
import mariadb;
import time;
from datetime import datetime;
from datetime import date;






class Admin():
    def limpioPantalla(self):
            sisOper = os.name
            if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
                os.system("clear")
            elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
                os.system("cls")

    def menuAdmin(self):
        self.limpioPantalla()
        opcion = int(input('''Hola Administrador
                            
                            1 - proveedores
                            2 - productos
                            3 - remitos
                            4 - Ver ventas realizadas 
                            5 - Dar de alta a un nuevo Administrador
                            6 - Cerrar sesión

                            ingrese la opción: '''))

                            

                           
          
        if opcion == 1:
            self.limpioPantalla()
            opcion = int(input(''' 
                            Menú administración proveedores

                            1 - Dar de alta proveedor
                            2 - Dar de baja proveedor
                            3 - Modificar datos de proveedor
                            4 - Ver proveedores
                            5 - volver al menú anterior
                            
                            ingrese una opción: '''))
            if opcion == 1: 
                self.limpioPantalla()    
                
                self.nombre= input("Ingrese el nombre del proveedor: ")
                self.cuit = input("ingrese el cuit")
                self.direccion=input("Ingrese la dirección domiciliaria: ")
                self.telefono=input("Ingre el número de teléfono: ")
                self.email=input("ingrese el email: ")

                mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
                mycursor = mydb.cursor()
                sql = "INSERT INTO proveedores (nombre, cuit, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s)"
                val = (self.nombre, self.cuit, self.direccion, self.telefono, self.email)
                mycursor.execute(sql, val)
                mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
                print("Se registro exitosamente el proveedor en nuestro sistema")  # muestro mensaje para saber que se insertaron bien
                time.sleep(3)
                self.limpioPantalla()
                self.menuAdmin()
            elif opcion == 2:
                self.limpioPantalla()
                mydb = mariadb.connect(
                    host="127.0.0.1",
                    user="root",
                    password="root", 
                    database = "SafetyInLife"
                    )
                self.nombre= input("Ingrese el nombre del proveedor que desea eliminar: ")

                mycursor = mydb.cursor()
                sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                if len(myresultado) >0:
                    mycursor = mydb.cursor()
                    sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                    mycursor.execute(sql)
                    myresultado = mycursor.fetchone()
                    for ind in myresultado:
                        #print(ind)
                        self.ind= ind
                else: self.ind = "vacio"

                if self.ind == self.nombre :
                    mycursor = mydb.cursor()
                    sql = "DELETE FROM proveedores WHERE nombre LIKE '%"+self.nombre+"%'"
                    mycursor.execute(sql)
                    mydb.commit()
                    print(f"se borraron los datos del proveedor {self.nombre} de nuestro sistema ")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuAdmin()
                else:
                    print("no se puede borrar, los datos no coinciden")
                    time.sleep(2)
                    self.limpioPantalla()
                    self.menuAdmin()
            elif opcion == 3:
                    self.limpioPantalla()
                    item = int(input('''
                    Que dato del proveedor desea modificar:
                    1 - Telefono del proveedor
                    2 - Dirección del proveedor
                    3 - Email del proveedor
                    4 - volver a menú principal
                    5 - Salir del Sistema
                    
                    Ingrese la opción deseada: '''))

                    if item == 1:
                        self.limpioPantalla()
                        print("Actualizar número telefónico\n")
                        self.nombre =input("ingrese el nombre del proveedor: ")
                        self.telefono = input("ingrese su nuevo número telefónico: ")
                        mydb = mariadb.connect(
                            host="127.0.0.1",
                            user="root",
                            password="root", 
                            database = "SafetyInLife"
                            )
                        mycursor = mydb.cursor()
                        sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        if len(myresultado) >0:
                            mycursor = mydb.cursor()
                            sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            myresultado = mycursor.fetchone()
                            for ind in myresultado:
                                #print(ind)
                                self.ind= ind
                        else: self.ind = "vacio"

                    
                        if self.ind == self.nombre:
                            mycursor = mydb.cursor()
                            sql = "UPDATE proveedores SET telefono = '"+self.telefono+"' WHERE nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            mydb.commit()
                            print("Se modifico exitosamente el número telefónico")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()
                        else: 
                            print("no se pudo actualizar el número telefónico, ya que el proveedor no se encuentra registrado")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()
                    
                    elif item == 2:
                        self.limpioPantalla()
                        print("Actualizar dirección\n")
                        self.nombre =input("ingrese el nombre del proveedor: ")
                        self.direccion = input("ingrese su nueva dirección: ")
                        mydb = mariadb.connect(
                            host="127.0.0.1",
                            user="root",
                            password="root", 
                            database = "SafetyInLife"
                            )
                        mycursor = mydb.cursor()
                        sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        if len(myresultado) >0:
                            mycursor = mydb.cursor()
                            sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            myresultado = mycursor.fetchone()
                            for ind in myresultado:
                                #print(ind)
                                self.ind= ind
                        else: self.ind = "vacio"

                    
                        if self.ind == self.nombre:
                            mycursor = mydb.cursor()
                            sql = "UPDATE proveedores SET direccion = '"+self.direccion+"' WHERE nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            mydb.commit()
                            print("Se modifico exitosamente la dirección del proveedor")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()
                        else: 
                            print("no se pudo actualizar la dirección, ya que el proveedor no se encuentra registrado")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()
                        
                    elif item == 3:
                        self.limpioPantalla()
                        print("Actualizar dirección\n")
                        self.nombre =input("ingrese el nombre del proveedor: ")
                        self.email = input("ingrese su nuevo email: ")
                        mydb = mariadb.connect(
                            host="127.0.0.1",
                            user="root",
                            password="root", 
                            database = "SafetyInLife"
                            )
                        mycursor = mydb.cursor()
                        sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        if len(myresultado) >0:
                            mycursor = mydb.cursor()
                            sql = "SELECT nombre FROM proveedores where nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            myresultado = mycursor.fetchone()
                            for ind in myresultado:
                                #print(ind)
                                self.ind= ind
                        else: self.ind = "vacio"

                    
                        if self.ind == self.nombre:
                            mycursor = mydb.cursor()
                            sql = "UPDATE proveedores SET email = '"+self.email+"' WHERE nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            mydb.commit()
                            print("Se modifico exitosamente el mail del proveedor")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()
                        else: 
                            print("no se pudo actualizar el mail, ya que el proveedor no se encuentra registrado")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()
            
                    elif item == 4:
                        self.limpioPantalla()
                        self.menuAdmin()

                    elif item == 5:
                        self.limpioPantalla()
                        print("MUCHAS GRACIAS POR UTILIZAR NUESTRO SISTEMA - Safety in Life A&A ")                   
            elif opcion == 4:
                self.limpioPantalla()
                print("LISTADO COMPLETO DE PROVEEDORES \n")
                mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
                mycursor = mydb.cursor()
                sql = "SELECT * FROM proveedores"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                for ind in myresultado:
                    print(ind)
                time.sleep(5)
                self.limpioPantalla()
                self.menuAdmin()
            elif opcion == 5:
                self.limpioPantalla()
                self.menuAdmin()

        elif opcion == 2:
            self.limpioPantalla()
            newArticulo = Articulos.Articulos()
            newArticulo.menuStock()


        elif opcion == 3:
            self.limpioPantalla()
            item = int(input('''¿Que desea realizar?
                            
                            1 - ver remitos
                            2 - ingresar remito
                            
                            ingrese la opcion: '''))

            if item == 1:
                self.limpioPantalla()
                print("VER REMITO")
                self.numRemito = int(input("ingrese el número de remito que desea ver: "))
                print("")
                print("")

                mydb = mariadb.connect(
                host="127.0.0.1",
                user="root",
                password="root", 
                database = "SafetyInLife"
                )
                mycursor = mydb.cursor()
                sql = "SELECT numRemito, articulo, marcaArticulo, cantidad, precioArticulo, subTotal,proveedor, fecha  FROM remitos WHERE numRemito LIKE \'"+str(self.numRemito)+"\'"
                mycursor.execute(sql)
                myresultado = mycursor.fetchall()
                for ind in myresultado:
                    print(ind)
                time.sleep(5)
                self.limpioPantalla()
                self.menuAdmin()

            if item == 2:
                self.limpioPantalla()
                print("Sistema de ingreso de remitos")
                self.numRemito = int(input("ingrese número de remito: "))
                self.proveedor= input("ingrese el proveedor del producto: ")
                respuesta = "si"
                while respuesta == "si":
                    print("")
                    opcion = input("¿el producto que va a ingresar ya lo tenemos en el sistema? SI o NO: ")

                    if opcion== "no":
                        self.limpioPantalla()
                        print("Sistema de ingreso de remitos")
                        print ("Ingrese información del nuevo producto")
                        self.nombre = input("ingrese el nombre del producto: ")
                        self.marca = input("ingrese la marca del producto: ")
                        self.precio= int(input("ingrese el precio del producto: ")) #modifica la tabla remitos
                        self.stock= int(input ("igrese el stock del producto: "))
                        self.precioVenta = self.precio * 1.5  #modifica el precio de la tabla producto
                        self.subtotal = self.stock * self.precio
                        self.fecha = datetime.now()
                        
                        mydb = mariadb.connect(
                        host="127.0.0.1",
                        user="root",
                        password="root", 
                        database = "SafetyInLife"
                        )
                        #actualiza tabla articulos
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO articulos (nombre, marca, proveedor, precio, stock) VALUES (%s, %s, %s, %s, %s)"
                        val = (self.nombre, self.marca, self.proveedor, self.precioVenta, self.stock)
                        mycursor.execute(sql, val)
                        mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen

                        #actualiza tabla remitos
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO remitos (numRemito,articulo, marcaArticulo, proveedor, precioArticulo, cantidad, subtotal, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                        val = (self.numRemito, self.nombre, self.marca, self.proveedor, self.precio, self.stock, self.subtotal, self.fecha)
                        mycursor.execute(sql, val)
                        mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
                        print("Se registro exitosamente en nuestro sistema el nuevo producto")  # muestro mensaje para saber que se insertaron bien
                        time.sleep(3)
                        self.limpioPantalla()
        


                    elif opcion == "si": #actualiza la tabla de productos, se crea registro en la tabla de remitos
                        self.limpioPantalla()
                        print("Sistema de ingreso de remitos")
                        print ("Ingrese información del producto")
                        self.nombre = input("ingrese el nombre del producto: ")
                        self.marca = input("ingrese la marca del producto: ")
                        self.precio= int(input("ingrese el precio del producto: ")) #modifica la tabla remitos
                        self.stock= int(input ("igrese el stock del producto: "))
                        self.precioVenta = self.precio * 1.5  #modifica el precio de la tabla producto
                        self.subtotal = self.stock * self.precio
                        self.fecha = datetime.now()
                        
                        mydb = mariadb.connect(
                        host="127.0.0.1",
                        user="root",
                        password="root", 
                        database = "SafetyInLife"
                        )
                        mycursor = mydb.cursor()
                        sql = "SELECT nombre FROM articulos where nombre LIKE '"+self.nombre+"'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        if len(myresultado) >0:
                            mycursor = mydb.cursor()
                            sql = "SELECT nombre FROM articulos where nombre LIKE '"+self.nombre+"'"
                            mycursor.execute(sql)
                            myresultado = mycursor.fetchone()
                            for ind in myresultado:
                                #print(ind)
                                self.ind= ind
                        else: self.ind = "vacio"

                        mycursor = mydb.cursor()
                        sql = "SELECT marca FROM articulos where marca LIKE '"+self.marca+"'"
                        mycursor.execute(sql)
                        myresultado = mycursor.fetchall()
                        if len(myresultado) >0:
                            mycursor = mydb.cursor()
                            sql = "SELECT marca FROM articulos where marca LIKE '"+self.marca+"'"
                            mycursor.execute(sql)
                            myresultado = mycursor.fetchone()
                            for ind2 in myresultado:
                                #print(ind2)
                                self.ind2= ind2
                        else: self.ind2 = "vacio"


                        if self.ind == self.nombre and self.ind2 == self.marca:
                            mycursor = mydb.cursor()
                            sql = "SELECT stock FROM articulos WHERE nombre = \'"+self.nombre+"\' AND marca LIKE \'"+self.marca+"\'"
                            mycursor.execute(sql)
                            myresultado = mycursor.fetchone()
                            for ind in myresultado:
                                    #print(ind)
                                    myresultado = ind
                            
                            self.nuevoStock = myresultado + self.stock
                            

                            mycursor = mydb.cursor()
                            sql = "UPDATE articulos SET stock = '"+str(self.nuevoStock)+"' , precio = '"+str(self.precioVenta)+"' WHERE nombre = \'"+self.nombre+"\' AND marca LIKE \'"+self.marca+"\'"
                            mycursor.execute(sql)
                            mydb.commit()

                            mycursor = mydb.cursor()
                            sql = "INSERT INTO remitos (numRemito,articulo, marcaArticulo, proveedor, precioArticulo, cantidad, subtotal, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                            val = (self.numRemito, self.nombre, self.marca, self.proveedor, self.precio, self.stock, self.subtotal, self.fecha)
                            mycursor.execute(sql, val)
                            mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
                            print("Se registro exitosamente en nuestro sistema el ingreso")  # muestro mensaje para saber que se insertaron bien
                            time.sleep(3)
                            self.limpioPantalla()
                            
                        else: 
                            print("no se pudo actualizar el producto ingresado, ya que los datos ingresados no corresponde a un articulo en nuestro sistema")
                            time.sleep(2)
                            self.limpioPantalla()
                            self.menuAdmin()


                    respuesta = input("desea ingresar otro producto? SI - NO: ")
                self.menuAdmin()



      
        #menu ventas
        elif opcion ==4 :
            self.limpioPantalla()
            print("Estas son las ventas que se realizaron el día de la fecha")
            self.fecha = date.today()
            
            mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            database = "SafetyInLife"
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM ventas where fecha = '"+str(self.fecha)+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            for ind in myresultado:
                print(ind)

            mycursor = mydb.cursor()
            sql = "SELECT SUM(subtotal) FROM ventas where fecha = '"+str(self.fecha)+"'"
            mycursor.execute(sql)
            myresultado = mycursor.fetchone()
            for ind in myresultado:
                self.totalVendido = ind

            print(f"El total vendido en el dia de la fecha es de: ${self.totalVendido}")
            time.sleep(5)
            self.menuAdmin()


        elif opcion == 5:
            self.limpioPantalla()
            print("Sistema de registro de nuevo administrador\n")
            self.tipoUsuario = "administrador"
            self.situacionIva= "s/i"
            self.dni= int(input("Ingrese su dni: "))
            self.usuario = input("ingrese nombre de usuario: ")
            self.contraseña = input ("ingrese contraseña: ")
            self.nombre= input("Ingrese su nombre: ")
            self.apellido=input ("Ingrese su apellido: ")
            self.direccion=input("Ingrese su dirección domiciliaria: ")
            self.telefono=input("Ingre su su número de teléfono: ")
            self.email=input("ingrese su email: ")
            

            mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            database = "SafetyInLife"
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO usuarios (nombre, apellido, dni, direccion, telefono, usuario, contraseña, email, tipoUsuario, sitIva) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (self.nombre, self.apellido, self.dni, self.direccion, self.telefono, self.usuario, self.contraseña, self.email, self.tipoUsuario, self.situacionIva)
            mycursor.execute(sql, val)
            mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
            print("Usted registro exitosamente un nuevo administrador en nuestro sistema")  # muestro mensaje para saber que se insertaron bien
            time.sleep(3)
            self.menuAdmin()

        elif opcion == 6:
            self.limpioPantalla()
            print("MUCHAS GRACIAS POR UTILIZAR NUESTRO SISTEMA - Safety in Life A&A ")
