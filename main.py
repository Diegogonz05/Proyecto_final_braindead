import tkinter 
from UI import UI



# se guarda la funcion de ventana de tkinter en la variable ventana
ventana = tkinter.Tk()


# El tamaño de la ventana (px)
ventana.geometry("300x600")

ventana.configure(background= "green")
tkinter.Wm.title(ventana, "Programa para contar calorias")


UI(ventana)

#ACTIVA LA VENTANA MAIN
ventana.mainloop()
