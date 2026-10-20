
# 📋 Gestor de Tareas

Un gestor de tareas simple pero eficiente desarrollado con **Python y Tkinter**, 
con una interfaz gráfica intuitiva para organizar y gestionar tus tareas diarias.

## ✨ Características

- **Interfaz gráfica amigable** - Diseño limpio y fácil de usar con Tkinter
- **Crear tareas** - Añade nuevas tareas con descripciones
- **Marcar como completadas** - Marca tareas como realizadas
- **Eliminar tareas** - Borra tareas que ya no necesitas
- **Persistencia de datos** - Guarda tus tareas en un archivo JSON
- **Visualización en tiempo real** - Ve todas tus tareas organizadas en una lista
- **Interfaz responsiva** - Se adapta a diferentes tamaños de ventana

## 🚀 Requisitos

- Python 3.6 o superior
- Tkinter (incluido por defecto en Python)
- Ninguna dependencia externa adicional

## 📦 Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/alberto2005-coder/Gestor-de-tareas.git
   cd Gestor-de-tareas
   ```

2. **Verifica que tengas Python instalado**
   ```bash
   python --version
   ```

3. **Ejecuta la aplicación**
   ```bash
   python main.py
   ```

## 📁 Estructura del Proyecto

```
Gestor-de-tareas/
├── main.py              # Punto de entrada de la aplicación
├── gui.py               # Interfaz gráfica (Tkinter)
├── persistencia.py      # Gestión de almacenamiento en JSON
├── tareas.json          # Archivo de datos de tareas
├── dist/                # Ejecutable compilado (opcional)
├── README.md            # Este archivo
└── LICENSE              # Licencia MIT
```

## 🎯 Cómo Usar

1. **Abre la aplicación** ejecutando `python main.py`
2. **Añade una tarea** escribiendo en el campo de entrada y haciendo clic en "Agregar"
3. **Marca como completada** seleccionando una tarea y haciendo clic en "Completar"
4. **Elimina tareas** seleccionando una tarea y haciendo clic en "Eliminar"
5. **Las tareas se guardan automáticamente** en `tareas.json`

## 🔧 Tecnologías Utilizadas

- **Python 3.6+** - Lenguaje de programación
- **Tkinter** - Framework para interfaz gráfica
- **JSON** - Almacenamiento de datos

## 📝 Módulos Principales

### `main.py`
- Punto de entrada de la aplicación
- Inicializa la ventana principal
- Maneja la ejecución del programa

### `gui.py`
- Construye la interfaz gráfica con Tkinter
- Gestiona los eventos de usuario
- Actualiza visualmente la lista de tareas

### `persistencia.py`
- Lee y escribe datos en `tareas.json`
- Carga las tareas guardadas al iniciar
- Guarda cambios automáticamente

## 💾 Formato de Datos

Las tareas se guardan en `tareas.json` con la siguiente estructura:

```json
[
  {
    "id": 1,
    "titulo": "Comprar leche",
    "descripcion": "Ir al supermercado",
    "completada": false
  },
  {
    "id": 2,
    "titulo": "Hacer tarea",
    "descripcion": "Matemáticas capítulo 5",
    "completada": true
  }
]
```

## 🛠️ Posibles Mejoras Futuras

- [ ] Categorías para tareas (trabajo, personal, etc.)
- [ ] Fechas de vencimiento
- [ ] Prioridades (alta, media, baja)
- [ ] Búsqueda y filtrado de tareas
- [ ] Temas oscuro/claro
- [ ] Sincronización en la nube
- [ ] Notificaciones locales
- [ ] Exportar a PDF o Excel

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'tkinter'"

En Ubuntu/Debian:
```bash
sudo apt-get install python3-tk
```

En Fedora:
```bash
sudo dnf install python3-tkinter
```

### Las tareas no se guardan

Verifica que tienes permisos de escritura en la carpeta del proyecto:
```bash
chmod 755 .
```

### Ventana no se muestra

Intenta ejecutar con:
```bash
python3 main.py
```

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**alberto2005-coder** - GitHub: [@alberto2005-coder](https://github.com/alberto2005-coder)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/MiCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/MiCaracteristica`)
5. Abre un Pull Request

## ⭐ Si te fue útil, ¡dale una estrella!

---

**Última actualización:** Mayo 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ TOPICS/TAGS RECOMENDADOS:

TOP 8 (LOS QUE DEBES PONER):

1. python
2. task-manager
3. tkinter
4. gui
5. json
6. desktop-application
7. task-tracking
8. beginner-friendly

OPCIONALES ADICIONALES:

• project-management
• todo-app
• python3
• persistence
• windows
• linux
• macos
• learning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

# English Version

# 📋 Task Manager

A simple yet efficient task manager developed with **Python and Tkinter**,
with an intuitive graphical interface to organize and manage your daily tasks.

## ✨ Features

- **Friendly graphical interface** - Clean, easy-to-use design with Tkinter
- **Create tasks** - Add new tasks with descriptions
- **Mark as completed** - Mark tasks as done
- **Delete tasks** - Remove tasks you no longer need
- **Data persistence** - Your tasks are saved to a JSON file
- **Real-time view** - See all your tasks organized in a list
- **Responsive interface** - Adapts to different window sizes

## 🚀 Requirements

- Python 3.6 or higher
- Tkinter (included by default with Python)
- No additional external dependencies

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alberto2005-coder/Gestor-de-tareas.git
   cd Gestor-de-tareas
   ```

2. **Check that Python is installed**
   ```bash
   python --version
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
Gestor-de-tareas/
├── main.py              # Application entry point
├── gui.py               # Graphical interface (Tkinter)
├── persistencia.py      # JSON storage management
├── tareas.json          # Task data file
├── dist/                # Compiled executable (optional)
├── README.md            # This file
└── LICENSE              # MIT License
```

## 🎯 How to Use

1. **Open the application** by running `python main.py`
2. **Add a task** by typing in the input field and clicking "Agregar" (Add)
3. **Mark as completed** by selecting a task and clicking "Completar" (Complete)
4. **Delete tasks** by selecting a task and clicking "Eliminar" (Delete)
5. **Tasks are saved automatically** to `tareas.json`

## 🔧 Technologies Used

- **Python 3.6+** - Programming language
- **Tkinter** - GUI framework
- **JSON** - Data storage

## 📝 Main Modules

### `main.py`
- Application entry point
- Initializes the main window
- Handles program execution

### `gui.py`
- Builds the graphical interface with Tkinter
- Manages user events
- Visually updates the task list

### `persistencia.py`
- Reads and writes data to `tareas.json`
- Loads saved tasks on startup
- Saves changes automatically

## 💾 Data Format

Tasks are stored in `tareas.json` with the following structure:

```json
[
  {
    "id": 1,
    "titulo": "Comprar leche",
    "descripcion": "Ir al supermercado",
    "completada": false
  },
  {
    "id": 2,
    "titulo": "Hacer tarea",
    "descripcion": "Matemáticas capítulo 5",
    "completada": true
  }
]
```

## 🛠️ Possible Future Improvements

- [ ] Categories for tasks (work, personal, etc.)
- [ ] Due dates
- [ ] Priorities (high, medium, low)
- [ ] Task search and filtering
- [ ] Dark/light themes
- [ ] Cloud sync
- [ ] Local notifications
- [ ] Export to PDF or Excel

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'tkinter'"

On Ubuntu/Debian:
```bash
sudo apt-get install python3-tk
```

On Fedora:
```bash
sudo dnf install python3-tkinter
```

### Tasks are not saved

Check that you have write permissions in the project folder:
```bash
chmod 755 .
```

### Window does not show

Try running with:
```bash
python3 main.py
```

## 📄 License

This project is under the MIT license. See the `LICENSE` file for details.

## 👤 Author

**alberto2005-coder** - GitHub: [@alberto2005-coder](https://github.com/alberto2005-coder)

## 🤝 Contributing

Contributions are welcome. Please:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Open a Pull Request

## ⭐ If it was useful to you, give it a star!

---

**Last updated:** May 2026

