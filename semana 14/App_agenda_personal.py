import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x550")
        self.root.resizable(True, True)

        # Configurar el estilo
        self.setup_styles()

        # Crear los frames principales
        self.create_frames()

        # Crear la lista de eventos
        self.create_event_list()

        # Crear el formulario de entrada
        self.create_input_form()

        # Crear los botones de acción
        self.create_action_buttons()

    def setup_styles(self):
        """Configurar estilos para los widgets"""
        style = ttk.Style()
        style.configure("Title.TLabel", font=("Arial", 14, "bold"))
        style.configure("Header.Treeview", font=("Arial", 10, "bold"))
        style.configure("TButton", font=("Arial", 10))
        style.configure("TLabel", font=("Arial", 10))

    def create_frames(self):
        """Crear los frames para organizar la interfaz"""
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar pesos de filas y columnas
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        # Título
        title_label = ttk.Label(self.main_frame, text="Agenda Personal", style="Title.TLabel")
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 15))

    def create_event_list(self):
        """Crear la lista de eventos con Treeview"""
        # Frame para la lista de eventos
        list_frame = ttk.LabelFrame(self.main_frame, text="Eventos Programados", padding="5")
        list_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Crear Treeview
        columns = ('fecha', 'hora', 'descripcion')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=10)

        # Definir encabezados
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')

        # Definir anchos de columnas
        self.tree.column('fecha', width=100, anchor=tk.CENTER)
        self.tree.column('hora', width=80, anchor=tk.CENTER)
        self.tree.column('descripcion', width=300, anchor=tk.W)

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Colocar widgets
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    def create_input_form(self):
        """Crear el formulario para ingresar nuevos eventos"""
        # Frame para el formulario
        form_frame = ttk.LabelFrame(self.main_frame, text="Nuevo Evento", padding="5")
        form_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        form_frame.columnconfigure(1, weight=1)

        # Etiqueta y campo para la fecha
        ttk.Label(form_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.fecha_var = tk.StringVar()
        fecha_frame = ttk.Frame(form_frame)
        fecha_frame.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        self.fecha_entry = ttk.Entry(fecha_frame, textvariable=self.fecha_var, width=12)
        self.fecha_entry.grid(row=0, column=0, sticky=tk.W)

        ttk.Button(fecha_frame, text="Hoy", width=5,
                   command=lambda: self.fecha_var.set(datetime.now().strftime("%d/%m/%Y"))).grid(row=0, column=1,
                                                                                                 padx=(5, 0))

        # Etiqueta y campo para la hora
        ttk.Label(form_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.hora_var = tk.StringVar()
        hora_entry = ttk.Entry(form_frame, textvariable=self.hora_var, width=10)
        hora_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Etiqueta y campo para la descripción
        ttk.Label(form_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.desc_var = tk.StringVar()
        desc_entry = ttk.Entry(form_frame, textvariable=self.desc_var, width=40)
        desc_entry.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

        # Tooltips para ayudar al usuario
        self.fecha_entry.insert(0, "DD/MM/AAAA")
        hora_entry.insert(0, "HH:MM")

    def create_action_buttons(self):
        """Crear los botones de acción"""
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)

        ttk.Button(button_frame, text="Agregar Evento",
                   command=self.agregar_evento).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Eliminar Evento",
                   command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        ttk.Button(button_frame, text="Salir",
                   command=self.root.quit).grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        """Agregar un nuevo evento a la lista"""
        fecha = self.fecha_var.get()
        hora = self.hora_var.get()
        desc = self.desc_var.get()

        # Validar campos
        if not fecha or not hora or not desc:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos")
            return

        # Validar formato de fecha
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            messagebox.showwarning("Advertencia", "Formato de fecha incorrecto. Use DD/MM/AAAA")
            return

        # Validar formato de hora
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showwarning("Advertencia", "Formato de hora incorrecto. Use HH:MM")
            return

        # Agregar evento a la lista
        self.tree.insert('', tk.END, values=(fecha, hora, desc))

        # Limpiar campos
        self.fecha_var.set('')
        self.hora_var.set('')
        self.desc_var.set('')

    def eliminar_evento(self):
        """Eliminar el evento seleccionado"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")
            return

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?"):
            self.tree.delete(selected)


def main():
    """Función principal para ejecutar la aplicación"""
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()