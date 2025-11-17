import tkinter 
from UI import UI
from tkinter import ttk



# se guarda la funcion de ventana de tkinter en la variable ventana
ventana = tkinter.Tk()


# El tamaño de la ventana (px)
ventana.geometry("300x600")

ventana.configure(background= "#565758")
tkinter.Wm.title(ventana, "NutriSense")


UI(ventana)

#ACTIVA LA VENTANA MAIN
ventana.mainloop()
