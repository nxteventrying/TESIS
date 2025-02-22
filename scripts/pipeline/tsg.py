import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp
import pandas as pd

class Sistema:

    """
    Clase para resolver ecuaciones diferenciales ordinarias (EDOs).

    Parámetros:
      - f: función que define el sistema de ecuaciones diferenciales (dy/dt = f(t, y)).
      - y0: condición inicial (puede ser un número o un array para sistemas).
      - t: array de tiempos donde se evaluará la solución.
      - metodo: método numérico para la integración (por defecto "RK45").
    """


    def __init__(self, f, y0, t, metodo = "RK45"):
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
    
    def graficar(self):
        """Grafica la solución obtenida de la EDO."""
        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")

        # plt.figure(figsize=(8, 5))
        # for i in range(self.solucion.y.shape[0]):
        #     plt.plot(self.solucion.t, self.solucion.y[i], label=f"Variable {i+1}")
        # plt.xlabel("Tiempo")
        # plt.ylabel("Valor")
        # plt.title(f"Solución de la EDO usando {self.metodo}")
        # plt.legend()
        # plt.grid()
        # plt.show()

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(self.solucion.y[0], self.solucion.y[1], self.solucion.y[2], color='purple', lw=0.5)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title('Lorenz Attractor (3D)')

        ax.view_init(elev=30, azim=60)
        plt.tight_layout()
        plt.show()





    def graficar_series_tiempo(self):
        """Grafica la serie de tiempo de la solución o todas."""

        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")

        # Create subplots and share the x-axis
        fig, axs = plt.subplots(self.solucion.y.shape[0], 1, figsize=(10, 8), sharex=True)
         
        labels = ['x', 'y', 'z']
        colors = ['r', 'g', 'b'] 

        # Plot each series in the solution
        for i in range(self.solucion.y.shape[0]):
            axs[i].plot(self.solucion.t, self.solucion.y[i],color=colors[i])
            axs[i].set_ylabel(labels[i])
            axs[i].grid()

        axs[-1].set_xlabel("Time")  # Set xlabel for the last subplot only

        # Set the title for the entire figure
        fig.suptitle(f"Series de Tiempo de {self.f.__name__}")

        plt.tight_layout()
        plt.show()

    def dataframe(self):
        """Devuelve el dataframe de la series de tiempo """
        pass