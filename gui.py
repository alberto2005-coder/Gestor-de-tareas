import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

from persistencia import cargar_tareas, guardar_tareas, inicializar_archivo

PRIORIDADES = ["alta", "media", "baja"]
ESTADOS = ["pendiente", "en progreso", "completada"]

class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 Gestor de Tareas")
        self.root.geometry("900x600")

        # Botones de menú
        frame_menu = tk.Frame(root)
        frame_menu.pack(pady=10)
        tk.Button(frame_menu, text="Crear tarea", command=self.crear_tarea, width=15).grid(row=0, column=0, padx=5)
        tk.Button(frame_menu, text="Actualizar tarea", command=self.actualizar_tarea, width=15).grid(row=0, column=1, padx=5)
        tk.Button(frame_menu, text="Eliminar tarea", command=self.eliminar_tarea, width=15).grid(row=0, column=2, padx=5)
        tk.Button(frame_menu, text="Estadísticas", command=self.mostrar_estadisticas, width=15).grid(row=0, column=3, padx=5)

        # Tabla para mostrar tareas
        self.tree = ttk.Treeview(root, columns=("Nombre","Descripción","Fecha","Prioridad","Categoría","Estado"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=20)

        # Inicializamos archivo JSON
        inicializar_archivo()
        self.ver_tareas()

    def validar_fecha(self, fecha_str):
        try:
            datetime.strptime(fecha_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def crear_tarea(self):
        form_win = tk.Toplevel(self.root)
        form_win.title("📝 Crear Tarea")
        form_win.geometry("400x450")

        # Campos
        tk.Label(form_win, text="Nombre:").pack(pady=5)
        entry_nombre = tk.Entry(form_win, width=40)
        entry_nombre.pack()

        tk.Label(form_win, text="Descripción:").pack(pady=5)
        entry_desc = tk.Entry(form_win, width=40)
        entry_desc.pack()

        tk.Label(form_win, text="Fecha límite (YYYY-MM-DD):").pack(pady=5)
        entry_fecha = tk.Entry(form_win, width=40)
        entry_fecha.pack()

        tk.Label(form_win, text="Prioridad:").pack(pady=5)
        combo_prioridad = ttk.Combobox(form_win, values=PRIORIDADES, state="readonly")
        combo_prioridad.pack()
        combo_prioridad.current(1)  # valor por defecto "media"

        tk.Label(form_win, text="Categoría:").pack(pady=5)
        entry_categoria = tk.Entry(form_win, width=40)
        entry_categoria.pack()

        tk.Label(form_win, text="Estado:").pack(pady=5)
        combo_estado = ttk.Combobox(form_win, values=ESTADOS, state="readonly")
        combo_estado.pack()
        combo_estado.current(0)  # valor por defecto "pendiente"

        def guardar():
            nombre = entry_nombre.get().strip()
            descripcion = entry_desc.get().strip()
            fecha = entry_fecha.get().strip()
            prioridad = combo_prioridad.get()
            categoria = entry_categoria.get().strip()
            estado = combo_estado.get()

            if not nombre or not descripcion or not fecha or not prioridad or not categoria or not estado:
                messagebox.showerror("❌ Error", "Todos los campos son obligatorios!")
                return

            if not self.validar_fecha(fecha):
                messagebox.showerror("❌ Error", "La fecha debe tener formato YYYY-MM-DD")
                return

            tarea = {
                "nombre": nombre,
                "descripcion": descripcion,
                "fecha_limite": fecha,
                "prioridad": prioridad,
                "categoria": categoria,
                "estado": estado
            }

            tareas = cargar_tareas()
            tareas.append(tarea)
            guardar_tareas(tareas)
            messagebox.showinfo("✅ Éxito", "Tarea creada con éxito!")
            form_win.destroy()
            self.ver_tareas()

        tk.Button(form_win, text="Guardar Tarea", command=guardar, bg="#4CAF50", fg="white").pack(pady=20)

    def ver_tareas(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        tareas = cargar_tareas()
        for t in tareas:
            self.tree.insert("", "end", values=(t["nombre"], t["descripcion"], t["fecha_limite"],
                                                t["prioridad"], t["categoria"], t["estado"]))

    def actualizar_tarea(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("⚠️", "Selecciona una tarea para actualizar")
            return

        tareas = cargar_tareas()
        values = self.tree.item(selected[0], "values")
        nombre_sel, desc_sel = values[0], values[1]

        for t in tareas:
            if t["nombre"] == nombre_sel and t["descripcion"] == desc_sel:
                form_win = tk.Toplevel(self.root)
                form_win.title("✏️ Actualizar Tarea")
                form_win.geometry("400x450")

                # Campos
                tk.Label(form_win, text="Nombre:").pack(pady=5)
                entry_nombre = tk.Entry(form_win, width=40)
                entry_nombre.pack()
                entry_nombre.insert(0, t["nombre"])

                tk.Label(form_win, text="Descripción:").pack(pady=5)
                entry_desc = tk.Entry(form_win, width=40)
                entry_desc.pack()
                entry_desc.insert(0, t["descripcion"])

                tk.Label(form_win, text="Fecha límite (YYYY-MM-DD):").pack(pady=5)
                entry_fecha = tk.Entry(form_win, width=40)
                entry_fecha.pack()
                entry_fecha.insert(0, t["fecha_limite"])

                tk.Label(form_win, text="Prioridad:").pack(pady=5)
                combo_prioridad = ttk.Combobox(form_win, values=PRIORIDADES, state="readonly")
                combo_prioridad.pack()
                combo_prioridad.set(t["prioridad"])

                tk.Label(form_win, text="Categoría:").pack(pady=5)
                entry_categoria = tk.Entry(form_win, width=40)
                entry_categoria.pack()
                entry_categoria.insert(0, t["categoria"])

                tk.Label(form_win, text="Estado:").pack(pady=5)
                combo_estado = ttk.Combobox(form_win, values=ESTADOS, state="readonly")
                combo_estado.pack()
                combo_estado.set(t["estado"])

                def guardar():
                    nombre = entry_nombre.get().strip()
                    descripcion = entry_desc.get().strip()
                    fecha = entry_fecha.get().strip()
                    prioridad = combo_prioridad.get()
                    categoria = entry_categoria.get().strip()
                    estado = combo_estado.get()

                    if not nombre or not descripcion or not fecha or not prioridad or not categoria or not estado:
                        messagebox.showerror("❌ Error", "Todos los campos son obligatorios!")
                        return

                    if not self.validar_fecha(fecha):
                        messagebox.showerror("❌ Error", "La fecha debe tener formato YYYY-MM-DD")
                        return

                    t["nombre"] = nombre
                    t["descripcion"] = descripcion
                    t["fecha_limite"] = fecha
                    t["prioridad"] = prioridad
                    t["categoria"] = categoria
                    t["estado"] = estado
                    guardar_tareas(tareas)
                    messagebox.showinfo("✅ Éxito", "Tarea actualizada!")
                    form_win.destroy()
                    self.ver_tareas()

                tk.Button(form_win, text="Guardar Cambios", command=guardar, bg="#4CAF50", fg="white").pack(pady=20)
                return

    def eliminar_tarea(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("⚠️", "Selecciona una tarea para eliminar")
            return

        tareas = cargar_tareas()
        values = self.tree.item(selected[0], "values")
        nombre_sel, desc_sel = values[0], values[1]

        nuevas = [t for t in tareas if not (t["nombre"]==nombre_sel and t["descripcion"]==desc_sel)]
        guardar_tareas(nuevas)
        messagebox.showinfo("✅ Éxito", f"Tarea '{nombre_sel}' eliminada")
        self.ver_tareas()

    def mostrar_estadisticas(self):
        tareas = cargar_tareas()
        if not tareas:
            messagebox.showwarning("⚠️", "No hay tareas registradas!")
            return

        completadas = sum(1 for t in tareas if t["estado"]=="completada")
        en_progreso = sum(1 for t in tareas if t["estado"]=="en progreso")
        pendientes = sum(1 for t in tareas if t["estado"]=="pendiente")

        alta = sum(1 for t in tareas if t["prioridad"]=="alta")
        media = sum(1 for t in tareas if t["prioridad"]=="media")
        baja = sum(1 for t in tareas if t["prioridad"]=="baja")

        win = tk.Toplevel(self.root)
        win.title("📊 Estadísticas")
        win.geometry("700x500")

        fig, axs = plt.subplots(1,2, figsize=(8,4))
        axs[0].pie([completadas, en_progreso, pendientes],
                   labels=["Completadas","En progreso","Pendientes"],
                   autopct='%1.1f%%', colors=['#4CAF50','#FFC107','#F44336'], startangle=140)
        axs[0].set_title("Tareas por estado")

        axs[1].bar(["Alta","Media","Baja"], [alta, media, baja], color=['#F44336','#FFC107','#4CAF50'])
        axs[1].set_title("Tareas por prioridad")
        axs[1].set_ylabel("Cantidad")

        plt.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
