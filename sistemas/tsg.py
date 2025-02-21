import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

class Sistema:

# Primero, deberiamos de ser capaces de:
#
#  * generar las soluciones del sistema con la ventaja de que podemos decidir
#    - el tipo de solucionador.
#    - condicionces inciales.
#    - intervalo de tiempo.

    """
    Clase para resolver ecuaciones diferenciales ordinarias (EDOs).

    Parámetros:
      - f: función que define el sistema de ecuaciones diferenciales (dy/dt = f(t, y)).
      - y0: condición inicial (puede ser un número o un array para sistemas).
      - t: array de tiempos donde se evaluará la solución.
      - metodo: método numérico para la integración (por defecto "RK45").
    """


    def __init__(self, f, y0, t, metodo="RK45"):
        self.f = f
        self.y0 = np.atleast_1d(y0)
        self.t = t
        self.metodo = metodo
        self.solucion = None

    def set_metodo(self, nuevo_metodo):
        """
        Permite cambiar el método de integración numérica.

        Parámetros:
          - nuevo_metodo: Método de integración (e.g., "RK45", "DOP853").
        """
        self.metodo = nuevo_metodo
        print(f"Método cambiado a {self.metodo}")

    def resolver(self):
        """Resuelve la EDO utilizando el método numérico definido."""
        self.solucion = solve_ivp(self.f, [self.t[0], self.t[-1]], self.y0,
                                    t_eval=self.t, method=self.metodo)
        return self.solucion

#  * una vez que tengamos las soluciones, debemos poder:
#    - plotearlas, separadas y una imagen 3D.
#    - guardarlas como imagen en un folder con su nombre obvio.
#    - crear un dataframe para su posteridad, incluso poder guardarlo seria bueno.
# 
#   algo extra pero no creo que estorbe es poder sacar la info, pero eso luego.



    def graficar(self):
        """Grafica la solución obtenida de la EDO."""
        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")

        plt.figure(figsize=(8, 5))
        for i in range(self.solucion.y.shape[0]):
            plt.plot(self.solucion.t, self.solucion.y[i], label=f"Variable {i+1}")
        plt.xlabel("Tiempo")
        plt.ylabel("Valor")
        plt.title(f"Solución de la EDO usando {self.metodo}")
        plt.legend()
        plt.grid()
        plt.show()

    def graficar_series_tiempo(self):
        """Grafica la serie de tiempo de la solución (para múltiples variables)."""
        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")

        fig, ax = plt.subplots(figsize=(8, 5))
        for i in range(self.solucion.y.shape[0]):
            ax.plot(self.solucion.t, self.solucion.y[i], label=f"Serie {i+1}")
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Valor")
        ax.set_title("Series de Tiempo de la Solución")
        ax.legend()
        ax.grid()
        plt.show()