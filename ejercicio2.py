import pandas as pd
import matplotlib.pyplot as plt

def ejercicio2():

    df = pd.read_csv("Jonathan Alex Valle Alfaro - Llistat.csv")
    clear = df.dropna()

    re = clear.groupby("NAME")["ABSENCES"].sum()
    print(re)

    plt.figure()
    plt.title("% de faltes DAW2")
    plt.ylabel("Faltes en %")
    plt.xlabel("ALUMNAT")
    plt.plot(re.index, re.values, 'k--')
    plt.show()
ejercicio2()