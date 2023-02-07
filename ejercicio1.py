## Importar Librerias Pandas y Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Funcion 1r Ejercicio
def ejercicio1():
    # Lectura del archivo Llistat.csv
    df = pd.read_csv("Jonathan Alex Valle Alfaro - Llistat.csv")
    # Quitar los valores nulls (Tambien se puede con .fillna(0) y en vez de quitar los valores)
    # rellenarlos de 0
    clear = df.dropna()

    # Filtrar las notas por los alumnos y hacer la media
    filter = clear.groupby("NAME")["NOTES"].mean()

    print(filter)

    # Dibujar la grafica
    plt.figure()
    # Añadir un titulo de la grafica
    plt.title("MITJA NOTA ALUMNAT CICLE")
    # Hacer la grafica por el index y los valores del filtrar
    plt.bar(filter.index, filter.values)
    # Poner los label x e y
    plt.ylabel("NOTES")
    plt.xlabel("ALUMNAT")
    plt.legend(["NOTES"])
    # Mostrar Grafica
    plt.show()



