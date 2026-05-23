
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

📝 DESCRIPCIÓN PARA GITHUB "ABOUT":

Gestor de tareas simple con interfaz gráfica. Python + Tkinter. 
Crea, edita y elimina tareas. Persistencia en JSON.

(108 caracteres - Perfecto para la meta-description)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
