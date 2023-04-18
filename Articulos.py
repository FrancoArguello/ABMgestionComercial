import os;
import mariadb;
import time;
import Admin;


class Articulos():
    def limpioPantalla(self):
            sisOper = os.name
            if sisOper == "posix":   # si fuera UNIX, mac para Apple, java para maquina virtual Java
                os.system("clear")
            elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
                os.system("cls")

    def menuStock(self):
        self.limpioPantalla()
        print("Control de Stock")
        opcion=int(input('''¿que acción desea realizar?

                        1 - ingresar nuevo producto al inventario manuealmente (solo excepciones)
                        2 - eliminar producto del inventario
                        3 - Mostrar articulos sin stock
                        4 - Mostrar listado completo de articulos
                        5 - Volver a menú principal
                        6 - Cerrar sesión
                            
                            ingrese la opción: '''))
        if opcion == 1:
            self.limpioPantalla()
            print ("Ingrese información del nuevo producto")
            self.nombre = input("ingrese el nombre del producto: ")
            self.marca = input("ingrese la marca del producto: ")
            self.proveedor= input("ingrese el proveedor del producto: ")
            self.precio= int(input("ingrese el precio del producto: "))
            self.stock= int(input ("igrese el stock del producto: "))
            
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
                sql = "UPDATE articulos SET stock = '"+str(self.nuevoStock)+"' , precio = '"+str(self.precio)+"' WHERE nombre = \'"+self.nombre+"\' AND marca LIKE \'"+self.marca+"\'"
                mycursor.execute(sql)
                mydb.commit()
                print("Se registro exitosamente en nuestro sistema el ingreso de los productos")
                time.sleep(3)
                self.menuStock()
                self.limpioPantalla()

            else: 
                
                mycursor = mydb.cursor()
                sql = "INSERT INTO articulos (nombre, marca, proveedor, precio, stock) VALUES (%s, %s, %s, %s, %s)"
                val = (self.nombre, self.marca, self.proveedor, self.precio, self.stock)
                mycursor.execute(sql, val)
                mydb.commit()   # ---> IMPORTANTE NO OLVIDAR COLOCAR EL COMMIT, sino los cambios no se hacen
                print("Se registro exitosamente en nuestro sistema el nuevo producto")  # muestro mensaje para saber que se insertaron bien
                time.sleep(3)
                self.menuStock()
                self.limpioPantalla()  
            


            

        elif opcion == 2:
            self.limpioPantalla()
            mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            database = "SafetyInLife"
            )
            self.nombre= input("Ingrese el nombre del producto que desea eliminar del inventario: ")
            self.marca = input("Ingrese la marca del producto que desea eliminar del inventario: ")

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
                    self.ind2= ind2
            else: self.ind2 = "vacio"

           


            if self.ind == self.nombre and self.ind2 == self.marca:
                mycursor = mydb.cursor()
                sql = "DELETE FROM articulos WHERE nombre = \'"+self.nombre+"\' AND marca LIKE \'%"+self.marca+"%\'"
                mycursor.execute(sql)
                mydb.commit()
                print(f"se borro los datos del producto {self.nombre} de marca {self.marca} de nuestro sistema ")
                time.sleep(2)
                self.limpioPantalla()
                self.menuStock()
            else:
                print("no se puede borrar, los datos no coinciden")
                time.sleep(2)
                self.limpioPantalla()
                self.menuStock()
        elif opcion == 3:
            self.limpioPantalla()
            print("LISTADO DE ARTICULOS SIN STOCK\n")
            mydb = mariadb.connect(
            host="127.0.0.1",
            user="root",
            password="root", 
            database = "SafetyInLife"
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM articulos WHERE stock = 0"
            mycursor.execute(sql)
            myresultado = mycursor.fetchall()
            for ind in myresultado:
                print(ind)
            time.sleep(5)
            self.menuStock()
        elif opcion == 4:
            self.limpioPantalla()
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
            self.menuStock()
        elif opcion == 5:
            self.limpioPantalla()
            new = Admin.Admin()
            new.menuAdmin()
        elif opcion == 6:
            self.limpioPantalla()
            print("Muchas gracias por utilizar nuestro servicio.\nVuelva pronto. Safety in Life A&A")
      