import os
import pickle

# Diccionario donde guardaremos los documentos
indice = {}

# Carpeta donde están los txt
carpeta = "documentos"

# Recorrer todos los archivos
for archivo in os.listdir(carpeta):

    ruta = os.path.join(carpeta, archivo)

    with open(ruta, "r", encoding="utf-8") as f:

        contenido = f.read()

        palabras = set(contenido.split())

        indice[archivo] = palabras

# Guardar índice en disco
with open("indice/indice.pkl", "wb") as f:
    pickle.dump(indice, f)

print("Indice generado correctamente.")
print(f"Cantidad de documentos indexados: {len(indice)}")