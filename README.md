# 🔍 Buscador Local de Documentos con Similitud de Jaccard


Este proyecto implementa un buscador local en ambiente web utilizando Python y Flask.

El sistema trabaja sobre una colección de 200 documentos de texto generados automáticamente. Cada documento contiene entre 5 y 10 palabras sin tildes ni signos de puntuación.

La búsqueda se realiza utilizando la técnica de similitud de Jaccard, permitiendo ordenar los documentos según su grado de coincidencia con la consulta ingresada por el usuario.

---


---

# ⚙️ Tecnologías utilizadas

- Python
- Flask
- HTML
- CSS
- GitHub
- Render

---

# 🏗️ Estructura del proyecto

```
BuscadorJaccard/

├── documentos/
├── indice/
├── static/
├── templates/

├── app.py
├── generar_documentos.py
├── indexador.py

├── requirements.txt
├── Procfile
└── README.md
```

---

# 📚 Fase Offline

La fase offline se ejecuta una sola vez y tiene como objetivo preparar la colección documental para las búsquedas.

### 1. Generación de documentos

Archivo:

```bash
generar_documentos.py
```

Genera automáticamente 200 documentos de texto.

Cada documento contiene entre 5 y 10 palabras seleccionadas desde un vocabulario predefinido.

---

### 2. Indexación

Archivo:

```bash
indexador.py
```

Lee todos los documentos y construye un índice que posteriormente será utilizado por el buscador.

El índice se almacena en:

```bash
indice/indice.pkl
```

---

# 🌐 Fase Online

Archivo:

```bash
app.py
```

Permite al usuario:

- Ingresar una consulta.
- Calcular similitud de Jaccard.
- Ordenar resultados.
- Mostrar los 10 documentos más relevantes.

---

# 🧮 Similitud de Jaccard

La similitud entre la consulta y cada documento se calcula mediante:

J(A,B) = |A ∩ B| / |A ∪ B|

Donde:

- A = palabras de la consulta.
- B = palabras del documento.

El resultado se expresa como porcentaje de similitud.

---

# 🚀 Instalación

## Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar a la carpeta:

```bash
cd BuscadorJaccard
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecutar aplicación

```bash
python app.py
```

Abrir navegador:

```text
http://127.0.0.1:5000
```

---

# 👨‍💻 Trabajo colaborativo

Cada integrante debe trabajar en una rama propia.

Crear rama:

```bash
git checkout -b nombre_integrante
```

Subir cambios:

```bash
git add .
git commit -m "descripcion del cambio"
git push origin nombre_integrante
```

No realizar modificaciones directamente sobre la rama principal (`main`).

---

# 📈 Funcionalidades implementadas

✅ Generación automática de 200 documentos

✅ Indexación de documentos

✅ Almacenamiento del índice

✅ Búsqueda mediante similitud de Jaccard

✅ Consultas de una o múltiples palabras

✅ Ordenamiento por relevancia

✅ Top 10 resultados

✅ Interfaz web con Flask

✅ Diseño responsivo mediante CSS

✅ Mensaje cuando no existen coincidencias

---

# 📄 Licencia

Proyecto académico desarrollado con fines educativos.
