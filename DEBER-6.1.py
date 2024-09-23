import tkinter as tk  # Importa la librería tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa el módulo para mostrar cuadros de mensaje

# Función que se ejecuta al hacer clic en el botón "Guardar"
def on_save_clicked():
    # Aquí se ejecutaría la lógica de guardar los datos
    # Por ejemplo, podrías guardar los datos en un archivo o en una base de datos
    # Para este ejemplo, simplemente mostraremos un messagebox
    messagebox.showinfo("Guardar", "Los datos han sido guardados correctamente.")

# Crear la ventana principal
root = tk.Tk()  # Inicializa la ventana principal
root.title("Ejemplo de Escuchadores de Eventos")  # Título de la ventana
root.geometry("400x200")  # Cambia el tamaño de la ventana (ancho x alto)

# Crear un botón y registrar el escuchador de eventos para el evento de clic
save_button = tk.Button(root, text="Guardar", command=on_save_clicked)  # Crea un botón con el texto "Guardar"
save_button.pack(pady=30)  # Añade el botón a la ventana con un margen vertical

# Iniciar el bucle principal de la GUI
root.mainloop()  # Mantiene la ventana abierta y espera eventos del usuario