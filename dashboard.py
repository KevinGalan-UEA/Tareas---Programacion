import os
import sys


def mostrar_codigo(ruta_script):
    """Muestra el contenido de un archivo con manejo de errores"""
    try:
        ruta_script = os.path.normpath(ruta_script)
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n{'=' * 80}")
            print(f"📄 CONTENIDO DE: {os.path.basename(ruta_script)}")
            print(f"{'=' * 80}\n")
            print(archivo.read())
            print(f"\n{'=' * 80}")
    except FileNotFoundError:
        print("\n❌ Error: El archivo no se encontró.")
    except Exception as e:
        print(f"\n❌ Error al leer el archivo: {e}")
    input("\nPresiona Enter para continuar...")


def navegar_directorio(ruta_actual):
    """Navega recursivamente por los directorios"""
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print(f"\n📂 DASHBOARD DE TAREAS POO - Directorio: {os.path.relpath(ruta_actual, os.getcwd())}")
        print("=" * 80)

        try:
            items = os.listdir(ruta_actual)
            carpetas = [item for item in items if os.path.isdir(os.path.join(ruta_actual, item))]
            archivos = [item for item in items if
                        os.path.isfile(os.path.join(ruta_actual, item)) and item.endswith('.py')]
            elementos = carpetas + archivos
        except Exception as e:
            print(f"❌ Error accediendo al directorio: {str(e)}")
            input("Presiona Enter para continuar...")
            return

        print("\n📂 CARPETAS:")
        for i, carpeta in enumerate(carpetas, 1):
            print(f"  [{i}] {carpeta}")

        print("\n📄 ARCHIVOS PYTHON:")
        for i, archivo in enumerate(archivos, len(carpetas) + 1):
            print(f"  [{i}] {archivo}")

        print("\n" + "=" * 80)
        print("[<] Volver al directorio anterior")
        print("[0] Salir al menú principal")
        print("=" * 80)

        opcion = input("\nSelecciona una opción: ")

        if opcion == '0':
            return
        elif opcion == '<':
            return

        try:
            opcion_num = int(opcion)
            if opcion_num < 1 or opcion_num > len(elementos):
                raise ValueError
        except ValueError:
            print("\n❌ Opción inválida")
            input("Presiona Enter para continuar...")
            continue

        elemento_seleccionado = elementos[opcion_num - 1]
        ruta_completa = os.path.join(ruta_actual, elemento_seleccionado)

        if opcion_num <= len(carpetas):
            navegar_directorio(ruta_completa)
        else:
            mostrar_codigo(ruta_completa)


def mostrar_menu_principal():
    """Muestra el menú principal del dashboard"""
    while True:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

        print("\n" + "=" * 80)
        print("📋 MENÚ PRINCIPAL - DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS")
        print("=" * 80)
        print("\n[1] Navegar por mi repositorio")
        print("[2] Ver archivo específico por ruta")
        print("[0] Salir")
        print("\n" + "=" * 80)

        opcion = input("\nSelecciona una opción: ")

        if opcion == '0':
            print("\n¡Hasta luego! 👋")
            sys.exit(0)
        elif opcion == '1':
            navegar_directorio(os.getcwd())
        elif opcion == '2':
            ruta = input("\nIngresa la ruta relativa del archivo (ej: 'semana 3/ProgramaP00.py'): ")
            mostrar_codigo(os.path.join(os.getcwd(), ruta))
        else:
            print("\n❌ Opción inválida")
            input("Presiona Enter para continuar...")


# =====================================================================
# PERSONALIZACIÓN PARA KEVIN EDUARDO GALÁN CALDERÓN
# =====================================================================
print("\n" + "=" * 80)
print("DASHBOARD PERSONALIZADO PARA:")
print("NOMBRE: Kevin Eduardo Galán Calderón")
print("MATERIA: Programación Orientada a Objetos")
print("PARALELO: D")
print("NIVEL: Segundo Ciclo")
print("=" * 80)
input("Presiona Enter para comenzar...")

mostrar_menu_principal()