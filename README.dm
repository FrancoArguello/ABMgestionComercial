ABM - Gestión Comercial venta de seguridad electrónica

Tendremos las siguientes clases principales: cliente, proveedor, artículo y las que consideren necesarias.
Deberán dar de alta la base de datos teniendo en cuenta la relación entre las tablas a crear.

Menú:
   Proveedores:
         - Alta/Baja/Modificación de Proveedor (DNI, Nombre de Fantasía, Direccion, Telefono, mail, Situacion IVA (Inscripto, Exento, etc..))
         - Pedido de reposición a Proveedor
         - Devolución a proveedor: se podrá realizar una baja de stock de articulos de un proveedor para devolver, habrá que completar un campo Observacion o Estado(vencido, dañado, etc)
   Cliente:
         - Alta/Baja/Modificacion de Cliente (Tendrá un registro con un cliente "Consumidor final" para aquel que cliente que no quiera registrarse) (campos: DNI, ApellidoNombre, Direccion, Telefono, mail, Situacion Iva)
    Articulos:
         - Alta/Baja/Modificacion de Articulo (Codigo de barra, nombre, rubro/categoría, precio, stock, DNI-proveedor)
        - Ingreso de Remito: ingreso de stock de artículos de un proveedor.
         - Listado de Artículos sin Stock
    Ventas:
         - Facturación: dado un cliente, podrá comprar uno o varios artículos mostrando el monto a pagar y descontando del stock en cada artículo.
         - Listado de ventas del día: deberá mostrar todos los artículos vendidos en el día.