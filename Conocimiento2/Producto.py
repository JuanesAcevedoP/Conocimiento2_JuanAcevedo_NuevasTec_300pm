class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__costo = costo
        self.__cantidad = cantidad
        self.__margen_de_venta = margen_de_venta
        self.__precio_de_venta = None

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, nuevo_costo):
        self.__costo = nuevo_costo
        self.calcular_precio_venta()

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad

    @property
    def precio_de_venta(self):
        return self.__precio_de_venta

    def calcular_precio_venta(self):
        if self.__margen_de_venta > 0:
            self.__precio_de_venta = self.__costo / (1 - self.__margen_de_venta)


    def registrar(self):
        self.__id = input("ID: ")
        self.__nombre = input("Nombre: ")
        self.__descripcion = input("Descripción: ")
        self.__costo = float(input("Costo: "))
        self.__cantidad = int(input("Cantidad: "))
        self.__margen_de_venta = float(input("Margen de Venta (porcentaje): ")) / 100
        self.calcular_precio_venta()

    def ver_registro(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Costo: {self.costo}, " \
              f"Cantidad: {self.cantidad}, Precio de Venta: {round(self.precio_de_venta, 2)}")
