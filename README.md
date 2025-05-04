# 🏥 Proyecto Hospital Automatizado

Este proyecto simula el flujo de pacientes en un hospital utilizando programación concurrente, paralela y asincrónica en Python. Incluye la generación de diagnósticos, asignación de recursos (camas y doctores), seguimiento y altas médicas. Además, cuenta con un **dashboard web** interactivo para visualizar y simular pacientes desde el navegador.

---

## 📁 Estructura del Proyecto

```
Proyecto_Hospital/ 
│ 
├── app/
│ └── static/
│ └── templates/
│       └── dashboard.html 
│ └── web.py # Servidor Flask para el dashboard
│ 
├── models/
│ └── mock_ai.py # Motor de diagnóstico simulado (AI mock)
│ 
├── reportes/ # Carpeta donde se guardan reportes con timestamp
│ 
├── utils/ 
│ └── generate_report.py # Genera los reportes de las simulaciones
│
├── diagnosis.py # Diagnóstico asíncrono usando síntomas 
├── discharge.py # Simula el alta de pacientes (procesamiento paralelo) 
├── main.py # Script principal que simula el flujo de pacientes 
├── patient.py # Clase paciente y su lógica 
├── resources.py # Gestión de camas y doctores 
│ 
│ 
├── README.md
```

---

## 🚀 Funcionalidades

- ✅ Generación de pacientes con síntomas aleatorios.
- ⏱ Diagnóstico asíncrono (`asyncio`) por síntomas.
- 🛏️ Asignación concurrente de recursos (`threading`).
- 📋 Prioridad médica con cola de prioridad (`queue.PriorityQueue`).
- 📈 Alta y seguimiento usando procesamiento paralelo (`multiprocessing.Pool`).
- 🧾 Generación automática de reportes en `/reportes`.
- 🌐 Dashboard web básico con Flask.

---

## 🛠 Requisitos

- Python 3.10+
- Flask

### Crear entorno virtual y activar

Abre una terminal en VS code y ejecuta:
```bash
python -m venv venv
```

Activa el entorno virtual:

- En Windows:
```bash
.\venv\Scripts\activate
```

- En macOS/Linux:
```bash
source venv/bin/activate
```

### Instalar dependencias:

```bash
pip install flask
pip install aiohttp rich matplotlib
```


## 🧪 Cómo usar el proyecto

1. Ejecutar la simulación desde consola:
```bash
python main.py
```
Esto simula 10 pacientes, genera diagnósticos, seguimiento y un reporte final en la carpeta /reportes.

---

2. Ejecutar el dashboard web:
```bash
python app/web.py
```

Luego abrir tu navegador donde te indique la consola:
```bash
http://localhost:5000
```
Desde el dashboard puedes:

- Simular nuevos pacientes (Con el botón de Simular pacientes)

- Generar nuevos reportes

---

### 📄 Reportes

Cada vez que se ejecuta main.py o desde el dashboard, se genera un archivo de texto en /reportes con:

Cantidad de pacientes admitidos vs retirados.

Estadísticas por nivel de prioridad.

Timestamp único en el nombre del archivo.

---

### 📌 Notas Técnicas

Se usó threading para simular concurrencia en la admisión de pacientes.

asyncio para simulación asíncrona del diagnóstico médico.

multiprocessing.Pool para simular altas en paralelo y no bloquear el sistema.

El dashboard web usa Flask y una plantilla HTML simple con Jinja2.

 ---

### 👨‍💻 Autor

- Desarrollado por Juliana Aguilar García
- Materia: Programación Paralela y Concurrente
- Profesor: Fuentes Cabrera José Gustavo
- Proyecto de simulación hospitalaria con Python 🐍 + Flask 🔥