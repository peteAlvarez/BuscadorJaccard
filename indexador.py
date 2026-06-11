import os
import pickle


indice = {}


carpeta = "documentos"


for archivo in os.listdir(carpeta):

    ruta = os.path.join(carpeta, archivo)

    with open(ruta, "r", encoding="utf-8") as f:

        contenido = f.read()

        palabras = set(contenido.split())

        indice[archivo] = palabras


with open("indice/indice.pkl", "wb") as f:
    pickle.dump(indice, f)

print("Indice generado correctamente.")
print(f"Cantidad de documentos indexados: {len(indice)}")