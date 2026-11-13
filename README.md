# Gestor de Tareas

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFD43B?logo=python&logoColor=black)](https://docs.python.org/3/library/tkinter.html)
[![Matplotlib](https://img.shields.io/badge/Gráficas-Matplotlib-11557C)](https://matplotlib.org/)
[![MIT](https://img.shields.io/badge/Licencia-MIT-green)](LICENSE)

[Español](#español) · [English](#english)

---

## Español

### Índice

- [Descripción](#descripción)
- [Características](#características)
- [Captura del flujo](#captura-del-flujo)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Formato de datos](#formato-de-datos)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Limitaciones conocidas](#limitaciones-conocidas)
- [Solución de problemas](#solución-de-problemas)
- [Licencia](#licencia)

### Descripción

Aplicación de escritorio para organizar tareas diarias con **Python** y **Tkinter**. Cada tarea guarda nombre, descripción, fecha límite, prioridad, categoría y estado, y se persiste automáticamente en un archivo **JSON**. Incluye una ventana de **estadísticas** con gráficas de estado y prioridad.

### Características

- **Tabla de tareas** con seis columnas: nombre, descripción, fecha, prioridad, categoría y estado.
- **Crear tareas** mediante un formulario con validación de campos obligatorios.
- **Actualizar tareas** seleccionando una fila de la tabla.
- **Eliminar tareas** con confirmación por mensaje.
- **Estados**: `pendiente`, `en progreso` y `completada`.
- **Prioridades**: `alta`, `media` y `baja`.
- **Validación de fecha** en formato `YYYY-MM-DD`.
- **Estadísticas** con gráfico circular por estado y gráfico de barras por prioridad.
- **Persistencia automática** en `tareas.json`; no requiere base de datos.

### Captura del flujo

1. **Crear tarea** → rellena los seis campos → **Guardar Tarea**.
2. La fila aparece al instante en la tabla principal.
3. Selecciona una fila y usa **Actualizar tarea** o **Eliminar tarea**.
4. Pulsa **Estadísticas** para ver el reparto por estado y prioridad.

### Requisitos

- **Python 3.8** o superior.
- **Tkinter** (viene con Python en Windows y macOS; en Linux suele ser un paquete aparte).
- **Matplotlib** para la ventana de estadísticas.

### Instalación

```bash
git clone https://github.com/alberto2005-coder/Gestor-de-tareas.git
cd Gestor-de-tareas

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install matplotlib
python main.py
```

Si tu distribución Linux no trae Tkinter:

```bash
sudo apt install python3-tk        # Debian / Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

También hay un ejecutable de Windows ya compilado en `dist/main.exe` (sin instalación, pero sin las ventajas de ejecutar el código).

### Uso

| Botón | Qué hace |
|---|---|
| **Crear tarea** | Abre el formulario; todos los campos son obligatorios |
| **Actualizar tarea** | Edita la tarea seleccionada (avisa si no hay selección) |
| **Eliminar tarea** | Borra la tarea seleccionada (avisa si no hay selección) |
| **Estadísticas** | Gráficas de tareas por estado y por prioridad |

La ventana principal mide 900×600 y la tabla se expande con ella. Las tareas se cargan al arrancar y se guardan tras cada alta, edición o borrado.

### Formato de datos

`tareas.json` contiene una lista de objetos:

```json
[
  {
    "nombre": "Comprar leche",
    "descripcion": "Ir al supermercado",
    "fecha_limite": "2026-05-20",
    "prioridad": "media",
    "categoria": "Personal",
    "estado": "pendiente"
  },
  {
    "nombre": "Entregar práctica",
    "descripcion": "Capítulo 5 de matemáticas",
    "fecha_limite": "2026-05-22",
    "prioridad": "alta",
    "categoria": "Estudios",
    "estado": "en progreso"
  }
]
```

Si el archivo no existe, la aplicación lo crea vacío al iniciar. El archivo se guarda con `UTF-8` y `ensure_ascii=False`, así que los acentos se conservan legibles.

### Estructura del proyecto

```text
Gestor-de-tareas/
├── main.py           # Punto de entrada: ventana principal y bucle de Tkinter
├── gui.py            # Interfaz: tabla, formularios y estadísticas
├── persistencia.py   # Lectura y escritura de tareas.json
├── tareas.json       # Datos de ejemplo / almacenamiento local
├── dist/             # Ejecutable de Windows y su propio tareas.json
├── LICENSE
└── README.md
```

### Limitaciones conocidas

- **Tkinter no es hilo-seguro**: la interfaz se actualiza solo desde el hilo principal; no hay operaciones en segundo plano.
- **Edición y borrado por coincidencia de campos**: la fila seleccionada se identifica por `nombre` + `descripcion`. Si tienes dos tareas idénticas en ambos campos, se modificará o borrará la primera que aparezca.
- **Sin identificador único**: al no haber `id`, las tareas no se pueden enlazar de forma estable (útil si planeas añadir recordatorios o sincronización).
- **Matplotlib es obligatorio**: aunque solo se usa en `Estadísticas`, el import está en la cabecera de `gui.py`; sin él la aplicación no arranca.
- **Los datos viven junto al script**: ejecutar desde otra carpeta crea un `tareas.json` distinto. `dist/main.exe` usa su propio archivo dentro de `dist/`.

### Solución de problemas

| Síntoma | Causa probable | Solución |
|---|---|---|
| `ModuleNotFoundError: No module named 'tkinter'` | Tkinter no instalado | Instala `python3-tk` / `python3-tkinter` |
| `ModuleNotFoundError: No module named 'matplotlib'` | Falta la dependencia | `pip install matplotlib` |
| Las tareas no se guardan | Permisos de escritura en la carpeta | Ejecuta desde una carpeta con permisos o revisa `tareas.json` |
| La ventana no aparece | Entorno sin pantalla (SSH, WSL sin servidor gráfico) | Usa un escritorio o el `.exe` de `dist/` |
| Error de fecha | Formato incorrecto | Usa exactamente `YYYY-MM-DD` |

### Licencia

**MIT** — consulta [LICENSE](LICENSE).

---

## English

### Table of contents

- [Overview](#overview)
- [Features](#features)
- [Typical flow](#typical-flow)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Data format](#data-format)
- [Project structure](#project-structure)
- [Known limitations](#known-limitations)
- [Troubleshooting](#troubleshooting)
- [License](#license)

### Overview

A desktop app for organising daily tasks with **Python** and **Tkinter**. Each task stores a name, description, due date, priority, category and status, and is persisted automatically to a **JSON** file. It ships a **statistics** window with status and priority charts.

### Features

- **Task table** with six columns: name, description, date, priority, category and status.
- **Create tasks** through a form with required-field validation.
- **Update tasks** by selecting a row in the table.
- **Delete tasks** with a message-box confirmation.
- **Statuses**: `pendiente` (pending), `en progreso` (in progress) and `completada` (done).
- **Priorities**: `alta`, `media`, `baja` (high, medium, low).
- **Date validation** in `YYYY-MM-DD` format.
- **Statistics** with a pie chart by status and a bar chart by priority.
- **Automatic persistence** to `tareas.json`; no database needed.

### Typical flow

1. **Create task** → fill in all six fields → **Save task**.
2. The row appears immediately in the main table.
3. Select a row and use **Update task** or **Delete task**.
4. Click **Statistics** to see the breakdown by status and priority.

### Requirements

- **Python 3.8** or later.
- **Tkinter** (bundled with Python on Windows and macOS; usually a separate package on Linux).
- **Matplotlib** for the statistics window.

### Installation

```bash
git clone https://github.com/alberto2005-coder/Gestor-de-tareas.git
cd Gestor-de-tareas

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install matplotlib
python main.py
```

If your Linux distribution lacks Tkinter:

```bash
sudo apt install python3-tk        # Debian / Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

A prebuilt Windows executable is also available at `dist/main.exe` (no setup, but without the benefits of running the source).

### Usage

| Button | What it does |
|---|---|
| **Create task** | Opens the form; every field is required |
| **Update task** | Edits the selected task (warns when nothing is selected) |
| **Delete task** | Removes the selected task (warns when nothing is selected) |
| **Statistics** | Charts of tasks by status and by priority |

The main window is 900×600 and the table grows with it. Tasks are loaded on start-up and saved after every create, edit or delete.

### Data format

`tareas.json` holds a list of objects:

```json
[
  {
    "nombre": "Buy milk",
    "descripcion": "Go to the supermarket",
    "fecha_limite": "2026-05-20",
    "prioridad": "media",
    "categoria": "Personal",
    "estado": "pendiente"
  },
  {
    "nombre": "Submit assignment",
    "descripcion": "Maths chapter 5",
    "fecha_limite": "2026-05-22",
    "prioridad": "alta",
    "categoria": "Studies",
    "estado": "en progreso"
  }
]
```

If the file is missing, the app creates an empty one on start-up. It is written with `UTF-8` and `ensure_ascii=False`, so accents stay readable.

### Project structure

```text
Gestor-de-tareas/
├── main.py           # Entry point: main window and Tkinter loop
├── gui.py            # UI: table, forms and statistics
├── persistencia.py   # Reading and writing tareas.json
├── tareas.json       # Sample data / local storage
├── dist/             # Windows executable and its own tareas.json
├── LICENSE
└── README.md
```

### Known limitations

- **Tkinter is not thread-safe**: the UI is only updated from the main thread; there are no background operations.
- **Edit and delete match on field values**: the selected row is identified by `nombre` + `descripcion`. If two tasks share both, the first match is edited or deleted.
- **No unique identifier**: without an `id`, tasks cannot be linked stably (relevant if you plan reminders or sync).
- **Matplotlib is mandatory**: although it is only used in **Statistics**, the import sits at the top of `gui.py`; without it the app will not start.
- **Data lives next to the script**: running from another folder creates a different `tareas.json`. `dist/main.exe` uses its own file inside `dist/`.

### Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'tkinter'` | Tkinter not installed | Install `python3-tk` / `python3-tkinter` |
| `ModuleNotFoundError: No module named 'matplotlib'` | Missing dependency | `pip install matplotlib` |
| Tasks are not saved | No write permission in the folder | Run from a writable folder or check `tareas.json` |
| Window does not appear | Headless environment (SSH, WSL without a display server) | Use a desktop session or the `dist/` executable |
| Date error | Wrong format | Use exactly `YYYY-MM-DD` |

### License

**MIT** — see [LICENSE](LICENSE).
