import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class CampanaPruebas:

    def __init__(self, defectos):
        self.defectos = defectos
        self.acumulados = np.cumsum(self.defectos)
        self.semanas = np.arange(1, len(defectos) + 1)
        self.a = None
        self.b = None 

    def goel(self, semana, total_defectos, tasa):
        return total_defectos * (1 - np.exp(-tasa * semana))

    def ajustar(self):
        parametros, _ = curve_fit(self.goel, self.semanas, self.acumulados, p0=[200, 0.1])
        self.a = parametros[0]
        self.b = parametros[1]
        return self.a, self.b

    def restantes(self):
        ultima_semana = self.semanas[-1]
        return self.a - self.goel(ultima_semana, self.a, self.b)

    def semana_95(self):
        return np.log(20) / self.b

    def graficar(self, ruta):
        semanas_curva = np.linspace(0, 20, 200)
        curva = self.goel(semanas_curva, self.a, self.b)

        plt.plot(self.semanas, self.acumulados, "o", color="red", label="Defectos reales")
        plt.plot(semanas_curva, curva, color="blue", label="Modelo Goel")
        plt.title("Defectos acumulados version 11.0")
        plt.xlabel("Semana")
        plt.ylabel("Defectos acumulados")
        plt.legend()
        plt.savefig(ruta)
        plt.close()