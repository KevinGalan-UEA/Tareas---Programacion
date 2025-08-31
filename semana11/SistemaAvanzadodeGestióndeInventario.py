import json
import os


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y setters
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):
        """Convierte el producto a un diccionario para serialización"""
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un producto desde un diccionario"""
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self):
        # Usamos un diccionario para acceso rápido por ID
        self._productos = {}
        # Usamos un conjunto para mantener un índice de nombres (en minúsculas para búsquedas case-insensitive)
        self._nombres_index = set()
        self._archivo = "inventario.json"
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.get_id() in self._productos:
            print("Error: Ya existe un producto con ese ID.")
            return False

        nombre_lower = producto.get_nombre().lower()
        if nombre_lower in self._nombres_index:
            print("Error: Ya existe un producto con ese nombre.")
            return False

        self._productos[producto.get_id()] = producto
        self._nombres_index.add(nombre_lower)
        self.guardar_en_archivo()
        print("Producto añadido exitosamente.")
        return True

    def eliminar_producto(self, id):
        if id not in self._productos:
            print("Error: No existe un producto con ese ID.")
            return False

        producto = self._productos[id]
        self._nombres_index.remove(producto.get_nombre().lower())
        del self._productos[id]
        self.guardar_en_archivo()
        print("Producto eliminado exitosamente.")
        return True

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id not in self._productos:
            print("Error: No existe un producto con ese ID.")
            return False

        producto = self._productos[id]
        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)

        self.guardar_en_archivo()
        print("Producto actualizado exitosamente.")
        return True

    def buscar_por_nombre(self, nombre):
        # Usamos una lista para almacenar los resultados de la búsqueda
        resultados = []
        nombre_lower = nombre.lower()

        # Buscamos en todos los productos
        for producto in self._productos.values():
            if nombre_lower in producto.get_nombre().lower():
                resultados.append(producto)

        return resultados

    def mostrar_todos(self):
        # Usamos una lista ordenada por ID para mostrar los productos
        productos_ordenados = sorted(self._productos.values(), key=lambda p: p.get_id())
        return productos_ordenados

    def guardar_en_archivo(self):
        try:
            with open(self._archivo, 'w') as f:
                # Convertimos todos los productos a diccionarios y los guardamos como JSON
                datos = [producto.to_dict() for producto in self._productos.values()]
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"Error al guardar en archivo: {e}")

    def cargar_desde_archivo(self):
        if not os.path.exists(self._archivo):
            return

        try:
            with open(self._archivo, 'r') as f:
                datos = json.load(f)
                for item in datos:
                    producto = Producto.from_dict(item)
                    self._productos[producto.get_id()] = producto
                    self._nombres_index.add(producto.get_nombre().lower())
        except Exception as e:
            print(f"Error al cargar desde archivo: {e}")


def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto")
    print("4. Buscar productos por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))

                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para ID, cantidad y precio.")

        elif opcion == "2":
            try:
                id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: Ingrese un ID válido.")

        elif opcion == "3":
            try:
                id = int(input("Ingrese el ID del producto a actualizar: "))

                # Preguntar qué desea actualizar
                print("¿Qué desea actualizar?")
                print("1. Cantidad")
                print("2. Precio")
                print("3. Ambos")
                sub_opcion = input("Seleccione una opción: ")

                cantidad = None
                precio = None

                if sub_opcion in ["1", "3"]:
                    cantidad = int(input("Ingrese la nueva cantidad: "))

                if sub_opcion in ["2", "3"]:
                    precio = float(input("Ingrese el nuevo precio: "))

                inventario.actualizar_producto(id, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nProductos encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            productos = inventario.mostrar_todos()

            if productos:
                print("\nTodos los productos en el inventario:")
                for producto in productos:
                    print(producto)
            else:
                print("El inventario está vacío.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    main()