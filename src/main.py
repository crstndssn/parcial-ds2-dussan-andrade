import os

from pymongo import MongoClient

from modelo import CampanaPruebas

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")

def leer_datos():
    cliente = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
    db = cliente["matriculapp"]

    semanas = []
    defectos = []
    for doc in db.defectos_semanales.find({"version": "1.0"}):
        semanas.append(doc["semana"])
        defectos.append(doc["defectos"])
    
    cliente.close()
    return semanas, defectos

def main():
    # leer mongo
    semanas, defectos = leer_datos()
    print("semanas: ", semanas)
    print("defectos: ", defectos)
    print()

    #crear el objeto y ajustar el modelo
    campana = CampanaPruebas(semanas, defectos)
    a, b = campana.ajustar()
    print(f"modelo: d(t) = {a:.2f} * e^({b:.4f} * t)")
    print()

    # predicción
    print(f"defectos esperados semnana 9: {campana.predecir(9):.1f}")
    print(f"defectos esperados semnana 10: {campana.predecir(10):.1f}")

    #grafica
    ruta = campana.graficar('graficas/resultado.png')
    print(f"grafica guardada en {ruta}")

    if __name__ == "__main__":
        main()
