from Producto import Producto

producto1 = Producto(id = None,
                     nombre=None,
                     descripcion=None,
                     costo=None,
                     cantidad=None,
                     margen_de_venta=None)

producto1.registrar()
producto1.calcular_precio_venta()
producto1.ver_registro()

