import sys
sys.path.append("src")
from modelo import CampanaPruebas

defectos = [28, 23, 22, 17, 16, 12, 12, 9]

def test_goel_cero():
    campana = CampanaPruebas(defectos)
    a, b = campana.ajustar()
    assert campana.goel(0, a, b) == 0

def test_quedan_defectos():
    campana = CampanaPruebas(defectos)
    campana.ajustar()
    assert campana.restantes() > 0

test_goel_cero()
test_quedan_defectos()
print("Pruebas pasaron")
