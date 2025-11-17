from logica import registrar_comidas
from tkinter import ttk

def UI(ventana):
    import tkinter
    
    caja_comidas = tkinter.Entry(
        ventana,
        width= 10,
        font= ("Garamond", 20)
    )
    caja_comidas.place(
    
        x= 130,
        y= 40
    )
    '''caja_cantidades = tkinter.Entry(
        ventana,
        width=12,
        font=("Segoe UI", 16)
    )
    caja_cantidades.place(
    
        x=130, 
        y=108
    )
    '''
    #LABELS
    comida_label = tkinter.Label(
        ventana,
        font= ("Segoe ui", 14),
        foreground= "white",
        background= "#2d3f4d",
        text= "Comida:"
        
    )
    comida_label.place(
        x = 40,
        y = 42
    )
    cantidad_label = tkinter.Label(
        ventana,
        text="Cantidad:",
        font=("Segoe UI", 14),
        foreground="white",
        background="#2d3f4d"
    ) 
    cantidad_label.place(
        x=40, 
        y=110
    
        
    )
    cantidad_gramos = tkinter.Label(
        ventana,
        text="(en gramos)",
        font=("Segoe UI", 8 ),
        foreground="white",
        background="#2d3f4d"
    )
    cantidad_gramos.place(
        
        x=40, 
        y=141.5
    )
    texto_error = tkinter.Label(
        ventana,
        text= "",
        font= ("Garamond", 10),
        foreground = "red",
        background= "white"
        

    )
    texto_error.place(
        x= 83,
        y= 500
    )
    texto_calorias = tkinter.Label(
        ventana,
        text="Calorías:",
        font=("Segoe UI", 14),
        foreground="white",
        background="#2d3f4d"
        
    )
    texto_calorias.place(
        
        x=40, y=170
        
    )
    texto_calorias_resultado = tkinter.Label(
        
        ventana,
        text= "",
        font= ("Garamond", 15),
        foreground = "black",
        background= "white"
    )
    texto_calorias_resultado.place(
        
        x=130, 
        y=172
        
    )
    #BOTONES
    boton_enter = tkinter.Button(
        ventana,
        background= "White",
        font= ("Garamond", 14),
        text= "Aceptar",
        command= lambda: registrar_comidas(caja_comidas, texto_error, texto_calorias_resultado, dropdown_menu)
    
        )

    boton_enter.place(
    
        x= 120,
        y= 220
    )
    #Boton_menu
    dropdown_menu = ttk.Combobox(
        ventana,
        values= ("50", "100", "150"),
        width=12,
        font=("Segoe UI", 16)

    )
    dropdown_menu.place(
        x=130, 
        y=108
    
    )
    