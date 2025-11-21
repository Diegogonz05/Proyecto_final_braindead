#UI.py

import tkinter
from logica import registrar_comidas, obtener_nombres_comidas, calcular_exceder
from tkinter import ttk


def UI(ventana):
    ventana.configure(background = "#282929") 


    #CREACION DE MENU DESPEGABLE
    seleccion_alimento_label = tkinter.Label(
        ventana, 
        text="Selecciona el alimento:", 
        background="#282929", 
        foreground="white", 
        font=("Arial", 12)
        )
    seleccion_alimento_label.place(
            x=20, 
            y=10
            )
    
    combo_alimentos = ttk.Combobox(
        ventana,
        values=obtener_nombres_comidas(),
        state="readonly",
        width=30
        )
    combo_alimentos.place(
        x=20,
        y=40
    ) #QUE ES STATE??? Evita que escribas en la lista despegable


    #CREACION DE ENTRADA PARA GRAMOS (creo)
    entrada_gramos_label = tkinter.Label(
        ventana, 
        text="Cantidad (gramos):", 
        bg="#282929", 
        fg="white", 
        font=("Segoe UI", 12)
        )
    entrada_gramos_label.place(
            x=20, 
            y=80
            )
    
    entrada_gramos = tkinter.Entry(
        ventana,
        width=10
        )
    entrada_gramos.place(
        x=20,
        y=110
    )


    texto_error = tkinter.Label(
        ventana,
        text="",
        font=("Arial", 12),
        foreground="red",
        background="#282929"
    )
    texto_error.place(
        x=20,
        y=145
    )


    #Mostrar calorias totales
    calorias_label = tkinter.Label(
        ventana, 
        text="Calorías:", 
        background="#282929", 
        foreground="white", 
        font=("Arial", 12)
        )
    calorias_label.place(x=20 , y=170)
    

    texto_calorias_resultado = tkinter.Label(
        ventana,
        text="",
        font= ("Arial", 12),
        foreground="black",
        background="white",
        width=10
    )
    texto_calorias_resultado.place(
        x=110,
        y=170
    )


    texto_calorias_aldia = tkinter.Label(
        ventana, 
        text="", 
        font=("Arial", 12), 
        foreground="black", 
        background="#ffffff"
        )
    texto_calorias_aldia.place(
        x=20,
        y=210
    )




    #HISTORIAL DE COMIDAS (LISTBOX: Le podes poner una lista)

    historial_comidas_label = tkinter.Label(
        ventana,
        text="Historial de comidas:",
        font=("Arial", 12),
        background="#282929",
        foreground="white"
        )
    historial_comidas_label.place(
            x=20,
            y=250
        )
    


    historial = tkinter.Listbox(
        ventana,
        width=55,
        height=8
    )
    historial.place(
        x=20,
        y=280
    )



    #BOTONES
    boton_enter = tkinter.Button(
        ventana,
        text="Calcular",
        background="white",
        font=("Arial", 12),
        command=lambda: registrar_comidas(combo_alimentos, texto_error, texto_calorias_resultado, entrada_gramos, historial)
    )
    boton_enter.place(
        x=20,
        y=480
    )




    boton_exceder = tkinter.Button(
        ventana,
        text="Calcular el exceso",
        background="white",
        font=("Arial", 12),
        command=lambda: calcular_exceder(texto_calorias_aldia)
    )
    boton_exceder.place(
        x=120,
        y=480
    )


