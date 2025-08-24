import os
import traceback


class Producto:
    """
    Clase que representa un producto en el inventario.

    Atributos:
        id (str): Identificador único del producto
        nombre (str): Nombre del producto
        cantidad (int): Cantidad disponible en inventario
        precio (float): Precio unitario del producto
    """

    def __init__(self, id: str, nombre: str, cantidad: int, precio: float):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self) -> str:
        return self.id

    def get_nombre(self) -> str:
        return self.nombre

    def get_cantidad(self) -> int:
        return self.cantidad

    def get_precio(self) -> float:
        return self.precio

    # Setters
    def set_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad: int):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float):
        self.precio = nuevo_precio

    def to_dict(self) -> dict:
        """Convierte el producto a un diccionario para serialización"""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @staticmethod
    def from_dict(data: dict):
        """Crea un producto a partir de un diccionario"""
        return Producto(
            data['id'],
            data['nombre'],
            data['cantidad'],
            data['precio']
        )

    def __str__(self) -> str:
        """Representación amigable del producto"""
        return f"ID: {self.id} | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    """
    Clase que gestiona una colección de productos con persistencia en archivo.

    Atributos:
        productos (dict): Diccionario de productos (ID como clave)
        archivo (str): Nombre del archivo para guardar/recuperar datos
    """

    def __init__(self, archivo='inventario.txt'):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga los productos desde el archivo, manejando posibles excepciones"""
        try:
            # Verificar si el archivo existe
            if not os.path.exists(self.archivo):
                print(f"El archivo {self.archivo} no existe. Se creará uno nuevo al guardar.")
                return True

            # Leer el archivo
            with open(self.archivo, 'r') as f:
                lineas = f.readlines()

            # Procesar cada línea
            for linea in lineas:
                datos = linea.strip().split('|')
                if len(datos) == 4:
                    id, nombre, cantidad, precio = datos
                    try:
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self.productos[id] = producto
                    except ValueError:
                        print(f"Advertencia: Formato incorrecto en línea: {linea}")

            print(f"Inventario cargado exitosamente desde {self.archivo}")
            return True

        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo} no fue encontrado.")
            return False
        except PermissionError:
            print(f"Error: No tiene permisos para leer el archivo {self.archivo}.")
            return False
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {str(e)}")
            print(traceback.format_exc())
            return False

    def guardar_en_archivo(self):
        """Guarda los productos en el archivo, manejando posibles excepciones"""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    linea = f"{producto.get_id()}|{producto.get_nombre()}|{producto.get_cantidad()}|{producto.get_precio()}\n"
                    f.write(linea)

            print(f"Inventario guardado exitosamente en {self.archivo}")
            return True

        except PermissionError:
            print(f"Error: No tiene permisos para escribir en el archivo {self.archivo}.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {str(e)}")
            print(traceback.format_exc())
            return False

    def añadir_producto(self, producto: Producto) -> bool:
        """Añade un nuevo producto verificando ID único y guarda en archivo"""
        if producto.get_id() in self.productos:
            print("\nError: Ya existe un producto con ese ID")
            return False

        self.productos[producto.get_id()] = producto

        # Guardar en archivo
        if self.guardar_en_archivo():
            print("\nProducto añadido exitosamente")
            return True
        else:
            # Revertir cambios si falla la escritura
            del self.productos[producto.get_id()]
            print("\nError: No se pudo guardar el producto en el archivo")
            return False

    def eliminar_producto(self, id: str) -> bool:
        """Elimina un producto por ID y guarda en archivo"""
        if id not in self.productos:
            print("\nError: Producto no encontrado")
            return False

        producto_eliminado = self.productos[id]
        del self.productos[id]

        # Guardar en archivo
        if self.guardar_en_archivo():
            print("\nProducto eliminado exitosamente")
            return True
        else:
            # Revertir cambios si falla la escritura
            self.productos[id] = producto_eliminado
            print("\nError: No se pudo eliminar el producto del archivo")
            return False

    def actualizar_producto(self, id: str, cantidad: int = None, precio: float = None) -> bool:
        """Actualiza cantidad y/o precio de un producto y guarda en archivo"""
        if id not in self.productos:
            print("\nError: Producto no encontrado")
            return False

        producto = self.productos[id]
        # Guardar valores anteriores por si hay que revertir
        cantidad_anterior = producto.get_cantidad()
        precio_anterior = producto.get_precio()

        if cantidad is not None:
            producto.set_cantidad(cantidad)
        if precio is not None:
            producto.set_precio(precio)

        # Guardar en archivo
        if self.guardar_en_archivo():
            print("\nProducto actualizado exitosamente")
            return True
        else:
            # Revertir cambios si falla la escritura
            producto.set_cantidad(cantidad_anterior)
            producto.set_precio(precio_anterior)
            print("\nError: No se pudo actualizar el producto en el archivo")
            return False

    def buscar_por_nombre(self, nombre: str) -> list:
        """Busca productos por coincidencia parcial en el nombre (case-insensitive)"""
        resultados = []
        nombre = nombre.lower()
        for producto in self.productos.values():
            if nombre in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_productos(self):
        """Muestra todos los productos en formato de tabla"""
        if not self.productos:
            print("\nInventario vacío")
            return

        print("\n=== INVENTARIO ===")
        for producto in self.productos.values():
            print(producto)
        print("==================")


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "=" * 40)
    print("SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("=" * 40)
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    print("=" * 40)


def main():
    # Inicializar inventario con el archivo por defecto 'inventario.txt'
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        # Opción 1: Añadir producto
        if opcion == "1":
            print("\n" + "-" * 30)
            print("AÑADIR NUEVO PRODUCTO")
            print("-" * 30)
            id = input("ID del producto: ").strip()
            nombre = input("Nombre: ").strip()

            try:
                cantidad = int(input("Cantidad inicial: "))
                precio = float(input("Precio unitario: "))
            except ValueError:
                print("\nError: Cantidad y precio deben ser valores numéricos")
                continue

            nuevo_producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo_producto)

        # Opción 2: Eliminar producto
        elif opcion == "2":
            print("\n" + "-" * 30)
            print("ELIMINAR PRODUCTO")
            print("-" * 30)
            id = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id)

        # Opción 3: Actualizar producto
        elif opcion == "3":
            print("\n" + "-" * 30)
            print("ACTUALIZAR PRODUCTO")
            print("-" * 30)
            id = input("ID del producto: ").strip()

            try:
                # Leer cantidad (puede ser vacío)
                cant_str = input("Nueva cantidad (dejar vacío para no cambiar): ").strip()
                cantidad = int(cant_str) if cant_str else None

                # Leer precio (puede ser vacío)
                precio_str = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
                precio = float(precio_str) if precio_str else None
            except ValueError:
                print("\nError: Valores inválidos (deben ser números)")
                continue

            # Si ambos son None, no se cambia nada
            if cantidad is None and precio is None:
                print("\nNo se realizaron cambios. Debe ingresar al menos un valor a actualizar.")
            else:
                inventario.actualizar_producto(id, cantidad, precio)

        # Opción 4: Buscar por nombre
        elif opcion == "4":
            print("\n" + "-" * 30)
            print("BUSCAR PRODUCTO")
            print("-" * 30)
            nombre = input("Nombre a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\nResultados de búsqueda:")
                for producto in resultados:
                    print(producto)
            else:
                print("\nNo se encontraron productos")

        # Opción 5: Mostrar todos
        elif opcion == "5":
            inventario.mostrar_productos()

        # Opción 6: Salir
        elif opcion == "6":
            print("\n¡Gracias por usar el sistema!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente")


if __name__ == "__main__":
    main()