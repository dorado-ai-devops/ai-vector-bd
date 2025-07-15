# 🧠 ai-vector-db

Base de datos vectorial para almacenamiento y recuperación eficiente de embeddings generados por LLMs (Ollama, OpenAI), cumple la funcion de ingestion de la documentacion de cada repositorio del laboratorio.

Ofrece búsquedas semánticas rápidas y precisas, orientadas al ecosistema DevOps `devops-ai-lab`.

---

## 🎯 Propósito

Centralizar el almacenamiento de información semántica y permitir búsquedas avanzadas utilizando modelos de lenguaje.
Actúa como memoria semántica accesible por microservicios y agentes LangChain vía API REST sencilla.

---


## 🔧 Funcionalidad

* Almacenamiento y recuperación de embeddings.
* Búsqueda semántica avanzada basada en similitud de vectores.
* Exposición sencilla mediante API REST.

---

## ⚙️ Estructura del Proyecto

```
ai-vector-db/
├── main.py                  # Aplicación principal (API REST)
├── entrypoint.sh            # Script de inicio para Docker
├── Dockerfile               # Dockerización del servicio
├── Jenkinsfile              # Pipeline CI/CD
├── Makefile                 # Automatización de tareas build/despliegue
├── requirements.txt         # Dependencias Python
├── LICENSE                  # Licencia del proyecto
├── README.md                # Índice multilenguaje
└── .gitignore
```

---

## 🚀 Ejecución Local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

API accesible vía `http://localhost:8000`.

---

## 🌐 Endpoints Principales

* `POST /ingest`: Almacenar embeddings.
* `POST /search`: Realizar búsquedas semánticas.

---

## 🧠 Inteligencia y Modelos

Compatible con embeddings generados por:

* Ollama (modelos locales).
* OpenAI (modelos remotos).

---

## 🔎 Observabilidad y Trazabilidad

* Logs detallados en stdout.
* Integrable con sistema MCP.

---

## 📦 Dependencias principales

```text
fastapi
uvicorn
numpy
requests
pydantic
python-dotenv
```

---

## 📌 Estado actual

* API básica operativa.
* Funcionalidades avanzadas en desarrollo.

---

## 👨‍💻 Autor

**Dani**
[github.com/dorado-ai-devops](https://github.com/dorado-ai-devops)

---

## 🛡 Licencia

Licencia Pública General GNU v3.0
