from pymongo import MongoClient
from modelo import CampanaPruebas

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["huilasoft"]

defectos = []
for doc in db.defectos_semanales.find().sort("semana", 1):
    defectos.append(doc["defectos"])

print("defectos por semana:", defectos)

campana = CampanaPruebas(defectos)
a, b = campana.ajustar()

print("Acumulados:", campana.acumulados)
print("a =", round(a, 2))
print("b =", round(b, 4))
print("defectos sin descubrir:", round(campana.restantes(), 1))
print("semana del 95%:", round(campana.semana_95(), 1))

campana.graficar("graficas/resultado.png")
print("grafica guardada")