import tkinter as tk
from tkinter import ttk, messagebox

class Aplicacion:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Gestor de Datos Básico")  # Título descriptivo
        self.ventana.geometry("500x400")  # Dimensiones iniciales

        # Crear componentes
        self.crear_widgets()

    def crear_widgets(self):
        # Etiqueta instructiva
        etiqueta = ttk.Label(
            self.ventana,
            text="Ingrese un dato:",
            font=("Arial", 10)
        )
        etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Campo de texto
        self.entrada_texto = ttk.Entry(self.ventana, width=40)
        self.entrada_texto.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )
        self.entrada_texto.bind("<Return>", lambda e: self.agregar_dato())  # Enter para agregar

        # Botón Agregar
        boton_agregar = ttk.Button(
            self.ventana,
            text="Agregar",
            command=self.agregar_dato
        )
        boton_agregar.grid(row=0, column=2, padx=10, pady=10)

        # Tabla para mostrar datos
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("dato",),
            show="headings",
            height=15
        )
        self.tabla.heading("dato", text="Datos Ingresados")
        self.tabla.grid(
            row=1,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(
            self.ventana,
            orient="vertical",
            command=self.tabla.yview
        )
        self.tabla.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky="ns", pady=10)

        # Botón Limpiar
        boton_limpiar = ttk.Button(
            self.ventana,
            text="Limpiar Todo",
            command=self.limpiar_datos
        )
        boton_limpiar.grid(row=2, column=1, pady=10)

        # Configurar grid para expansión responsive
        self.ventana.columnconfigure(1, weight=1)
        self.ventana.rowconfigure(1, weight=1)

    def agregar_dato(self):
        contenido = self.entrada_texto.get().strip()  # Obtener texto y eliminar espacios
        if contenido:  # Verificar que no esté vacío
            self.tabla.insert("", "end", values=(contenido,))  # Insertar en la tabla
            self.entrada_texto.delete(0, "end")  # Limpiar campo
        else:
            messagebox.showwarning(
                "Campo Vacío",
                "Por favor ingrese un dato válido"
            )

    def limpiar_datos(self):
        if self.tabla.get_children():  # Verificar si hay elementos
            self.tabla.delete(*self.tabla.get_children())  # Eliminar todos los elementos
        self.entrada_texto.delete(0, "end")  # Limpiar campo de texto

# Punto de entrada de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()  # Iniciar bucle principal de eventos