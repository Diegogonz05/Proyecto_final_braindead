import tkinter
from logica import registrar_comidas, obtener_nombres_comidas, calcular_exceder
from tkinter import ttk


def UI(ventana):
    ventana.configure(background = "#1D1C1C") #esto es para establecer el primer fondo


    #creacion del menu desplegable
    seleccion_alimento_label = tkinter.Label( #.Label es para indicarle al usuario que hacer
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
    
    #ttk combox es para la cracion de los menus desplegables
    combo_alimentos = ttk.Combobox(
        ventana,
        values=obtener_nombres_comidas(),
        state="readonly", #state = readondly sirve para no darle el chance al usuario a escribir y solo elegir
        width=30
        )
    combo_alimentos.place(
        x=20,
        y=40
    ) 


    #donde el usuario escribira la cantidad de gramos
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




    #historial de las comidas 

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



    #botones
    boton_enter = tkinter.Button(
        ventana,
        text="Calcular",
        background="white",
        font=("Arial", 12),
        command=lambda: registrar_comidas(combo_alimentos, texto_error, texto_calorias_resultado, entrada_gramos, historial)
    ) #command funciona para decirle al boton que hacer
      #lambda funciona para que el comando se ejecute solamente si el boton es presionado   
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