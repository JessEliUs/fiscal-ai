from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle, os

DATASET = [
    ("gasolina para el coche", "transporte"),
    ("factura de gasolina", "transporte"),
    ("uber para ir al trabajo", "transporte"),
    ("taxi al aeropuerto", "transporte"),
    ("pasaje de avion", "transporte"),
    ("caseta autopista", "transporte"),
    ("estacionamiento oficina", "transporte"),
    ("renta de auto", "transporte"),
    ("boleto de camion", "transporte"),
    ("metro mensual", "transporte"),
    ("laptop para trabajo", "equipo"),
    ("computadora de escritorio", "equipo"),
    ("monitor para oficina", "equipo"),
    ("impresora", "equipo"),
    ("teclado y mouse", "equipo"),
    ("telefono celular trabajo", "equipo"),
    ("tablet", "equipo"),
    ("disco duro externo", "equipo"),
    ("camara fotografica trabajo", "equipo"),
    ("audifonos para videollamadas", "equipo"),
    ("internet mensual", "servicios"),
    ("electricidad oficina", "servicios"),
    ("agua oficina", "servicios"),
    ("telefono fijo oficina", "servicios"),
    ("servicio de contabilidad", "servicios"),
    ("honorarios abogado", "servicios"),
    ("diseno grafico", "servicios"),
    ("hosting web", "servicios"),
    ("software suscripcion", "servicios"),
    ("limpieza oficina", "servicios"),
    ("renta de oficina", "oficina"),
    ("papeleria", "oficina"),
    ("folder y hojas", "oficina"),
    ("tinta para impresora", "oficina"),
    ("sello empresa", "oficina"),
    ("escritorio", "oficina"),
    ("silla de oficina", "oficina"),
    ("archivero", "oficina"),
    ("pizarron", "oficina"),
    ("cafetera oficina", "oficina"),
    ("comida con cliente", "alimentacion"),
    ("desayuno de negocios", "alimentacion"),
    ("cena reunion trabajo", "alimentacion"),
    ("cafe con proveedor", "alimentacion"),
    ("ropa personal", "personal"),
    ("zapatos personales", "personal"),
    ("gimnasio personal", "personal"),
    ("netflix", "personal"),
    ("spotify", "personal"),
    ("videojuegos", "personal"),
    ("salon de belleza", "personal"),
    ("vacaciones", "personal"),
    ("cine", "personal"),
    ("consulta medica", "salud"),
    ("medicamentos recetados", "salud"),
    ("lentes graduados", "salud"),
    ("dentista", "salud"),
    ("analisis clinicos", "salud"),
]

texts = [d[0] for d in DATASET]
labels = [d[1] for d in DATASET]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
    ("clf", LogisticRegression(max_iter=1000)),
])
pipeline.fit(texts, labels)

output_path = os.path.join(os.path.dirname(__file__), "classifier.pkl")
with open(output_path, "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Modelo entrenado y guardado en classifier.pkl")
for t in ["factura gasolina", "netflix personal", "renta oficina"]:
    pred = pipeline.predict([t])[0]
    conf = pipeline.predict_proba([t]).max()
    print(f"  '{t}' → {pred} ({conf:.0%})")
