from logica import registrar_comidas

def UI(ventana):
    import tkinter
    
    caja_comidas = tkinter.Entry(
        ventana,
        width= 10,
        font= ("Garamond", 20)
    )
    caja_comidas.place(
    
        x= 50,
        y= 220
    )
    caja_cantidades = tkinter.Entry(
        ventana,
        width= 10,
        font= ("Garamond", 20),
    )
    caja_cantidades.place(
    
        x= 50,
        y= 300
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
        text= "Calorias:",
        font= ("Garamond", 15),
        foreground = "red",
        background= "white"
        
    )
    texto_calorias.place(
        
        x= 50,
        y= 130
        
    )
    texto_calorias_resultado = tkinter.Label(
        
        ventana,
        text= "",
        font= ("Garamond", 15),
        foreground = "red",
        background= "white"
    )
    texto_calorias_resultado.place(
        
        x= 140,
        y= 130
        
    )
    
    boton_enter = tkinter.Button(
        ventana,
        background= "White",
        font= ("Garamond", 14),
        text= "Aceptar",
        command= lambda: registrar_comidas(caja_comidas, caja_cantidades, texto_error, texto_calorias_resultado)
    
        )

    boton_enter.place(
    
        x= 80,
        y= 400
    )