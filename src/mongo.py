# -- coding: utf-8 --

import pymongo
#from pprint import pprint

# Conexión a la base de datos de MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/mi_base_de_datos")
db = client["mi_base_de_datos"]
collection = db["mis_pedidos"]

# Función para crear un nuevo pedido
def crear_pedido(nombre, tipo_comida, precio):
    pedido = {"nombre": nombre, "tipo_comida": tipo_comida, "precio": precio}
    collection.insert_one(pedido)
    print("Pedido creado exitosamente.")

# Función para mostrar todos los pedidos
def mostrar_pedidos():
    pedidos = collection.find()
    for pedido in pedidos:
        print(pedido)

# Función para actualizar un pedido
def actualizar_pedido(nombre_antiguo, nombre_nuevo, tipo_comida_nuevo, precio_nuevo):
    query = {"nombre": nombre_antiguo}
    nuevos_valores = {"$set": {"nombre": nombre_nuevo, "tipo_comida": tipo_comida_nuevo, "precio": precio_nuevo}}
    collection.update_one(query, nuevos_valores)
    print("Pedido actualizado exitosamente.")

# Función para eliminar un pedido
def eliminar_pedido(nombre):
    query = {"nombre": nombre}
    collection.delete_one(query)
    print("Pedido eliminado exitosamente.")

# Función principal
def main():
    while True:
        print("\nMenu:")
        print("1. Crear Pedido")
        print("2. Mostrar Pedidos")
        print("3. Actualizar Pedido")
        print("4. Eliminar Pedido")
        print("5. Salir")
        opcion = raw_input("Seleccione una opcion: ")  # Utilizamos raw_input() en Python 2.x

        if opcion == '1':
            nombre = raw_input("Ingrese nombre del cliente: ")
            tipo_comida = raw_input("Ingrese tipo de comida: ")
            precio = float(raw_input("Ingrese precio a pagar: "))  # Convertimos a float
            crear_pedido(nombre, tipo_comida, precio)
        elif opcion == '2':
            mostrar_pedidos()
        elif opcion == '3':
            nombre_antiguo = raw_input("Ingrese el nombre del cliente que desea actualizar: ")
            nombre_nuevo = raw_input("Ingrese el nuevo nombre del cliente: ")
            tipo_comida_nuevo = raw_input("Ingrese el nuevo tipo de comida: ")
            precio_nuevo = float(raw_input("Ingrese el nuevo precio a pagar: "))  # Convertimos a float
            actualizar_pedido(nombre_antiguo, nombre_nuevo, tipo_comida_nuevo, precio_nuevo)
        elif opcion == '4':
            nombre = raw_input("Ingrese el nombre del cliente que desea eliminar: ")
            eliminar_pedido(nombre)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()