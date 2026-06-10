from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Cargar índice al iniciar
with open("indice/indice.pkl", "rb") as f:
    indice = pickle.load(f)


def similitud_jaccard(consulta, documento):
    interseccion = len(consulta.intersection(documento))
    union = len(consulta.union(documento))

    if union == 0:
        return 0

    return interseccion / union


@app.route("/", methods=["GET", "POST"])
def inicio():

    resultados = []

    if request.method == "POST":

        consulta_texto = request.form["consulta"]

        consulta = set(consulta_texto.lower().split())

        for nombre_doc, palabras_doc in indice.items():

            similitud = similitud_jaccard(
                consulta,
                palabras_doc
            )

            with open(
                f"documentos/{nombre_doc}",
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read()

            resultados.append({
                "documento": nombre_doc,
                "titulo": nombre_doc.replace(".txt", "").replace("_", " ").title(),
                "similitud": round(similitud * 100, 2),
                "contenido": contenido
            })

        resultados.sort(
            key=lambda x: x["similitud"],
            reverse=True
        )

        resultados = [
            r for r in resultados
            if r["similitud"] > 0
        ]

        resultados = resultados[:10]

    return render_template(
        "index.html",
        resultados=resultados
    )


@app.route("/documento/<nombre>")
def ver_documento(nombre):

    with open(
        f"documentos/{nombre}",
        "r",
        encoding="utf-8"
    ) as archivo:

        contenido = archivo.read()

    return render_template(
        "documento.html",
        nombre=nombre,
        contenido=contenido
    )


if __name__ == "__main__":
    app.run(debug=True)