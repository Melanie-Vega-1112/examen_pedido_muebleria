print("----EXAMEN----")

class Pedido:
    # Constructor
    def __init__(self, id_pedido, fecha_pedido, id_cliente, total_pedido, estado_pedido, fecha_entrega, direccion_entrega):
        self.id_pedido = id_pedido
        self.fecha_pedido = fecha_pedido
        self.id_cliente = id_cliente
        self.total_pedido = total_pedido
        self.estado_pedido = estado_pedido
        self.fecha_entrega = fecha_entrega
        self.direccion_entrega = direccion_entrega

    def mostrar_datos(self):
        print(f"ID_PEDIDO: {self.id_pedido}")
        print(f"FECHA_PEDIDO: {self.fecha_pedido}")
        print(f"ID_CLIENTE: {self.id_cliente}")
        print(f"TOTAL_PEDIDO: {self.total_pedido}")
        print(f"ESTADO_PEDIDO: {self.estado_pedido}")
        print(f"FECHA_ENTREGA: {self.fecha_entrega}")
        print(f"DIRECCION_ENTREGA: {self.direccion_entrega}")

    def lista(self):
        print ("----LISTAS----")
        idd_pedido = {"id_pedido 1": 1, "id_pedido 2": 2, "id_pedido 3": 3}
        print(idd_pedido)
        for key, value in idd_pedido.items():
            print(f"{key}: {value}")

    def tupla(self):
        print("----TUPLAS----")
        fecha_pedido = ("fecha del pedido 1: 01-09-22", "fecha del pedido 2: 01-09-22", "fecha del pedido 3: 01-09-22")
        print(fecha_pedido)
        for fecha in fecha_pedido:
            print(fecha)
    
    def dic(self):
        print("----DICCIONARIO----")
        print("ID CLIENTE")
        pedido_m = {
            "id_cliente 1": "12568",
            "total_pedido": "$250",
            "estado_pedido": "nuevo",
            "fecha_entrega": "02-09-2024",
            "direccion_entrega": "calle 4"
        }
        for x, y in pedido_m.items():
            print(f"{x}: {y}")

pedido1 = Pedido(1, "01-09-2023", 12568, 250.0, "nuevo", "02-09-2024", "calle 4")

#llamada a funciones
pedido1.mostrar_datos()
pedido1.lista()
pedido1.tupla()
pedido1.dic()


