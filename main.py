#Main.py

import tkinter 
from UI import UI



# se guarda la funcion de ventana de tkinter en la variable ventana
ventana = tkinter.Tk()

# El tamaño de la ventana (px)
ventana.geometry("500x550")
ventana.title("NutriSense")


UI(ventana)

#ACTIVA LA VENTANA MAIN
ventana.mainloop()