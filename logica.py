comidas_registradas = []
calorias_totales = 0
calorias_por_comida = {
    "pupusa": 350,
    "pan": 80,
    "huevo": 70,
    "manzana": 52
}

def registrar_comidas(caja_comidas, caja_cantidades, texto_error, texto_calorias_resultado):
    
    global calorias_totales
    comida = caja_comidas.get().lower()
    cantidades = int(caja_cantidades.get())
    
    if comida == "" or cantidades == "":
        texto_error.config(text= "Llena todos los campos")
        return
    
    comidas_registradas.append(comida)
    comidas_registradas.append(cantidades)
    
    for comidas in comidas_registradas:
        if comidas == "pupusa":
            calorias_totales += calorias_por_comida["pupusa"]
            comidas_registradas.clear()
        if comidas == "pan":
            calorias_totales += calorias_por_comida["pan"]
            comidas_registradas.clear()
        if comidas == "huevo":
            calorias_totales += calorias_por_comida["huevo"]
            comidas_registradas.clear()
        if comidas == "manzana":
            calorias_totales += calorias_por_comida["manzana"]
            comidas_registradas.clear()
        
    
    print(comidas_registradas)
    texto_calorias_resultado.config(text= str(calorias_totales))
    
    caja_comidas.delete(0,"end")
    caja_cantidades.delete(0,"end")
