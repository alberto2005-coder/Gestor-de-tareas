import tkinter as tk
from gui import TaskManagerGUI
from persistencia import inicializar_archivo

if __name__ == "__main__":
    # Asegurarse de que exista el archivo JSON
    inicializar_archivo()
    
    # Crear ventana principal
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
