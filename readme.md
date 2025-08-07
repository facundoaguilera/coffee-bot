
# Coffee Bot API

API conversacional basada en FastAPI que responde exclusivamente preguntas relacionadas al café, utilizando Gemini API con un enfoque RAG (Retrieval-Augmented Generation).


## Características

- Carga y vectorización de PDFs de recetas de café.
- División en fragmentos, búsqueda por similitud (RAG).
- Integración con Gemini API para respuestas generativas.
- API REST con documentación Swagger.
- Soporte para pruebas unitarias e integración.
- Listo para Docker y CI/CD.

## Tecnologías Utilizadas

- Python 3.11
- FastAPI
- Google Gemini API
- scikit-learn, numpy
- PyPDF 
- Uvicorn
- Docker 
- GitHub Actions (CI)
- pytest + coverage

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/facundoaguilera/coffee-bot.git
cd coffee-bot
```

### 2. Crear archivo `.env`

Crea un archivo `.env` en la raíz con el siguiente contenido:

```env
GEMINI_API_KEY=tu_api_key_aquí
```

### 3. Crear entorno virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar localmente

```bash
uvicorn src.main:app --reload
```

Endpoints de Prueba: http://localhost:8000/docs

## Configuración de Gemini API

1. Ve a: https://aistudio.google.com/
2. Inicia sesión con tu cuenta de Google
3. Genera una API Key (botón de Get API key)
4. Coloca la clave en el archivo `.env` como:

```env
GEMINI_API_KEY=sk-xxxxxx
```

## Testing

Ejecuta las pruebas con:

```bash
pytest
```

Y para ver la cobertura:

```bash
pytest --cov=src
```

## Docker

### Construir imagen

```bash
docker build -t coffee-bot .
```

### Ejecutar contenedor

```bash
docker run --env-file .env -p 8000:8000 coffee-bot
```

## Principios de Arquitectura

Este proyecto sigue principios inspirados en Clean Architecture:

- Separación de responsabilidades
- Inversión de dependencias
- Alta cohesión, bajo acoplamiento
- Inyección de dependencias manual

## CI/CD

Este repositorio está configurado con GitHub Actions para ejecutar:

- Linting
- Tests
- Build Docker

Workflow en `.github/workflows/ci.yml`


