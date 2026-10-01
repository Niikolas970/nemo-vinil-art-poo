import tkinter as tk
from tkinter import messagebox
import sqlite3


# ==========================================
# CLASE CLIENTE
# ==========================================

class Cliente:

    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - CC {self.cedula} - Tel {self.telefono}"

    def guardar(self):
        conexion = sqlite3.connect("nemo_vinil_art.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO clientes (nombre, cedula, telefono)
            VALUES (?, ?, ?)
        """, (self.nombre, self.cedula, self.telefono))

        conexion.commit()
        conexion.close()

    @staticmethod
    def listar_todos():
        conexion = sqlite3.connect("nemo_vinil_art.db")
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT nombre, cedula, telefono
            FROM clientes
        """)

        filas = cursor.fetchall()

        conexion.close()

        return [
            Cliente(nombre, cedula, telefono)
            for nombre, cedula, telefono in filas
        ]

    def actualizar(self):
        conexion = sqlite3.connect("nemo_vinil_art.db")
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE clientes
            SET nombre = ?, telefono = ?
            WHERE cedula = ?
        """, (self.nombre, self.telefono, self.cedula))

        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(cedula):
        conexion = sqlite3.connect("nemo_vinil_art.db")
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM clientes
            WHERE cedula = ?
        """, (cedula,))

        conexion.commit()
        conexion.close()


# ==========================================
# CREAR TABLA SI NO EXISTE
# ==========================================

conexion = sqlite3.connect("nemo_vinil_art.db")
cursor = conexion.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        nombre TEXT,
        cedula TEXT PRIMARY KEY,
        telefono TEXT
    )
""")

conexion.commit()
conexion.close()


# ==========================================
# VENTANA
# ==========================================

ventana = tk.Tk()
ventana.title("Nemo Vinil Art - Clientes")
ventana.geometry("600x450")


# ==========================================
# CAMPOS
# ==========================================

tk.Label(ventana, text="Nombre:").grid(
    row=0,
    column=0,
    padx=10,
    pady=10,
    sticky="e"
)

entry_nombre = tk.Entry(ventana, width=35)
entry_nombre.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


tk.Label(ventana, text="Cédula:").grid(
    row=1,
    column=0,
    padx=10,
    pady=10,
    sticky="e"
)

entry_cedula = tk.Entry(ventana, width=35)
entry_cedula.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


tk.Label(ventana, text="Teléfono:").grid(
    row=2,
    column=0,
    padx=10,
    pady=10,
    sticky="e"
)

entry_telefono = tk.Entry(ventana, width=35)
entry_telefono.grid(
    row=2,
    column=1,
    padx=10,
    pady=10
)


# ==========================================
# LISTA DE CLIENTES
# ==========================================

lista = tk.Listbox(
    ventana,
    width=70,
    height=10
)

lista.grid(
    row=5,
    column=0,
    columnspan=3,
    padx=10,
    pady=15
)


# Guarda los objetos en el mismo orden
# en que aparecen en el Listbox.

clientes_actuales = []


# ==========================================
# LIMPIAR CAMPOS
# ==========================================

def limpiar_campos():

    entry_nombre.delete(0, tk.END)
    entry_cedula.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)


# ==========================================
# REFRESCAR LISTA
# ==========================================

def refrescar_lista():

    lista.delete(0, tk.END)

    clientes_actuales.clear()

    for cliente in Cliente.listar_todos():

        clientes_actuales.append(cliente)

        lista.insert(
            tk.END,
            str(cliente)
        )


# ==========================================
# GUARDAR
# ==========================================

def guardar():

    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    telefono = entry_telefono.get()

    if not nombre or not cedula:
        messagebox.showwarning(
            "Datos incompletos",
            "Nombre y cédula son obligatorios."
        )
        return

    try:

        cliente = Cliente(
            nombre,
            cedula,
            telefono
        )

        cliente.guardar()

        limpiar_campos()
        refrescar_lista()

    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Error",
            "Ya existe un cliente con esa cédula."
        )


# ==========================================
# SELECCIONAR CLIENTE
# ==========================================

def al_seleccionar(evento):

    seleccion = lista.curselection()

    if not seleccion:
        return

    indice = seleccion[0]

    cliente = clientes_actuales[indice]

    entry_nombre.delete(0, tk.END)
    entry_nombre.insert(0, cliente.nombre)

    entry_cedula.delete(0, tk.END)
    entry_cedula.insert(0, cliente.cedula)

    entry_telefono.delete(0, tk.END)
    entry_telefono.insert(0, cliente.telefono)


# ==========================================
# ACTUALIZAR
# ==========================================

def actualizar():

    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    telefono = entry_telefono.get()

    if not nombre or not cedula:
        messagebox.showwarning(
            "Datos incompletos",
            "Nombre y cédula son obligatorios."
        )
        return

    cliente = Cliente(
        nombre,
        cedula,
        telefono
    )

    cliente.actualizar()

    limpiar_campos()
    refrescar_lista()


# ==========================================
# ELIMINAR
# ==========================================

def eliminar():

    cedula = entry_cedula.get()

    if not cedula:
        messagebox.showwarning(
            "Dato faltante",
            "Selecciona un cliente."
        )
        return

    Cliente.eliminar(cedula)

    limpiar_campos()
    refrescar_lista()


# ==========================================
# BOTONES
# ==========================================

tk.Button(
    ventana,
    text="Guardar",
    command=guardar,
    width=12
).grid(
    row=3,
    column=0,
    padx=5,
    pady=10
)


tk.Button(
    ventana,
    text="Actualizar",
    command=actualizar,
    width=12
).grid(
    row=3,
    column=1,
    padx=5,
    pady=10,
    sticky="w"
)


tk.Button(
    ventana,
    text="Eliminar",
    command=eliminar,
    width=12
).grid(
    row=4,
    column=0,
    padx=5,
    pady=10
)


tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar_campos,
    width=12
).grid(
    row=4,
    column=1,
    padx=5,
    pady=10,
    sticky="w"
)


# ==========================================
# DETECTAR SELECCIÓN DE LA LISTA
# ==========================================

lista.bind(
    "<<ListboxSelect>>",
    al_seleccionar
)


# ==========================================
# CARGAR CLIENTES AL ABRIR
# ==========================================

refrescar_lista()


# ==========================================
# EJECUTAR VENTANA
# ==========================================

ventana.mainloop()