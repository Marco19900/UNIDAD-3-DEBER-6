import tkinter as tk
from tkinter import messagebox, scrolledtext

class FeedbackApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Sistema de Retroalimentación')  # Cambié el título
        self.master.geometry('600x300')  # Aumenté el tamaño de la ventana

        # Etiqueta y campo de entrada para el nombre
        self.name_label = tk.Label(master, text='Tu Nombre:', font=('Arial', 12))
        self.name_label.pack(pady=5)  # Añadí un margen vertical
        self.name_entry = tk.Entry(master, font=('Arial', 12))  # Cambié la fuente
        self.name_entry.pack(pady=5)

        # Etiqueta y campo de texto para el comentario
        self.comment_label = tk.Label(master, text='Tu Comentario:', font=('Arial', 12))
        self.comment_label.pack(pady=5)
        self.comment_text = scrolledtext.ScrolledText(master, height=8, font=('Arial', 12))  # Cambié la altura y la fuente
        self.comment_text.pack(pady=5)

        # Botón para enviar el comentario
        self.submit_button = tk.Button(master, text='Enviar Comentario', command=self.submit_comment, bg='green', fg='white')  # Cambié el texto y el color
        self.submit_button.pack(pady=10)

        # Botón para limpiar los campos de entrada
        self.clear_button = tk.Button(master, text='Borrar Campos', command=self.clear_fields, bg='red', fg='white')  # Cambié el texto y el color
        self.clear_button.pack(pady=5)

    def submit_comment(self):
        # Recoge los valores de los campos de entrada
        name = self.name_entry.get()
        comment = self.comment_text.get("1.0", tk.END).strip()
        if name and comment:
            messagebox.showinfo("Comentario Enviado", f"Gracias {name}, tu comentario ha sido recibido.")
            self.clear_fields()
        else:
            messagebox.showwarning("Faltan Datos", "Por favor, completa todos los campos antes de enviar.")

    def clear_fields(self):
        # Limpia los campos de texto y área de texto
        self.name_entry.delete(0, tk.END)
        self.comment_text.delete('1.0', tk.END)

# Ejecutar la aplicación
if __name__ == '__main__':
    root = tk.Tk()
    app = FeedbackApp(root)  # Cambié el nombre de la clase a FeedbackApp
    root.mainloop()