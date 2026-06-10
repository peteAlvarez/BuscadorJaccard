import os
import random

os.makedirs("documentos", exist_ok=True)

palabras = [
    "perro", "gato", "casa", "mesa", "silla", "lapiz", "cuaderno", "auto", "camino", "puerta",
    "ventana", "techo", "piso", "playa", "arena", "mar", "rio", "montana", "bosque", "flor",
    "arbol", "sol", "luna", "estrella", "nube", "lluvia", "viento", "fuego", "tierra", "agua",
    "rojo", "azul", "verde", "amarillo", "negro", "blanco", "gris", "naranja", "morado", "rosa",
    "futbol", "tenis", "correr", "saltar", "caminar", "jugar", "leer", "escribir", "estudiar", "trabajar",
    "computador", "teclado", "pantalla", "mouse", "internet", "codigo", "programa", "python", "datos", "archivo",
    "telefono", "reloj", "cocina", "comida", "pan", "leche", "queso", "fruta", "manzana", "platano",
    "hospital", "escuela", "universidad", "profesor", "alumno", "clase", "libro", "biblioteca", "examen", "tarea",
    "ciudad", "pueblo", "parque", "plaza", "edificio", "avenida", "calle", "semaforo", "bicicleta", "bus",
    "musica", "cancion", "guitarra", "piano", "pelicula", "serie", "actor", "teatro", "arte", "foto"
]

for i in range(1, 201):

    cantidad_palabras = random.randint(5, 10)

    contenido = random.sample(palabras, cantidad_palabras)

    nombre_archivo = f"documentos/doc{i}.txt"

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(" ".join(contenido))

print("Se generaron 200 documentos correctamente.")