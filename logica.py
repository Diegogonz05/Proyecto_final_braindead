comidas_registradas = []
calorias_totales = 0
calorias_por_comida =  [
    {"alimento": "pupusa de queso", "calorias_100g": 230},
    {"alimento": "pupusa revuelta", "calorias_100g": 260},
    {"alimento": "pupusa de frijol", "calorias_100g": 210},
    {"alimento": "pupusa de chicharrón", "calorias_100g": 270},
    {"alimento": "pupusa loca", "calorias_100g": 300},
    {"alimento": "tamales de elote", "calorias_100g": 190},
    {"alimento": "tamal de gallina", "calorias_100g": 215},
    {"alimento": "tamal de chipilín", "calorias_100g": 180},
    {"alimento": "yuca frita", "calorias_100g": 170},
    {"alimento": "yuca sancochada", "calorias_100g": 120},
    {"alimento": "platanos fritos", "calorias_100g": 200},
    {"alimento": "platanos con crema", "calorias_100g": 240},
    {"alimento": "platanos al horno", "calorias_100g": 158},
    {"alimento": "pastelitos de carne", "calorias_100g": 280},
    {"alimento": "empanadas de leche", "calorias_100g": 250},
    {"alimento": "empanadas de frijol", "calorias_100g": 240},
    {"alimento": "pollo guisado", "calorias_100g": 150},
    {"alimento": "carne guisada", "calorias_100g": 200},
    {"alimento": "sopa de res", "calorias_100g": 85},
    {"alimento": "sopa de gallina", "calorias_100g": 95},
    {"alimento": "arroz blanco", "calorias_100g": 130},
    {"alimento": "frijoles cocidos", "calorias_100g": 140},
    {"alimento": "frijoles refritos", "calorias_100g": 180},
    {"alimento": "tortilla de maíz", "calorias_100g": 218},
    {"alimento": "queso duro blando", "calorias_100g": 320},
    {"alimento": "crema salvadoreña", "calorias_100g": 210},
    {"alimento": "enchiladas", "calorias_100g": 260},
    {"alimento": "garnachas", "calorias_100g": 240},
    {"alimento": "atol de elote", "calorias_100g": 90},
    {"alimento": "atol chuco", "calorias_100g": 80},
    {"alimento": "atol de arroz", "calorias_100g": 110},
    {"alimento": "hamburguesa", "calorias_100g": 260},
    {"alimento": "hamburguesa con queso", "calorias_100g": 280},
    {"alimento": "papas fritas", "calorias_100g": 312},
    {"alimento": "pizza", "calorias_100g": 266},
    {"alimento": "hot dog", "calorias_100g": 290},
    {"alimento": "pollo frito", "calorias_100g": 260},
    {"alimento": "nuggets", "calorias_100g": 290},
    {"alimento": "tacos", "calorias_100g": 240},
    {"alimento": "burrito", "calorias_100g": 240},
    {"alimento": "lasagna", "calorias_100g": 150},
    {"alimento": "pollo asado", "calorias_100g": 180},
    {"alimento": "carne asada", "calorias_100g": 250},
    {"alimento": "costilla de cerdo", "calorias_100g": 290},
    {"alimento": "chuleta de cerdo", "calorias_100g": 260},
    {"alimento": "huevo", "calorias_100g": 155},
    {"alimento": "atun en agua", "calorias_100g": 116},
    {"alimento": "atun en aceite", "calorias_100g": 198},
    {"alimento": "pan francés", "calorias_100g": 285},
    {"alimento": "pan dulce", "calorias_100g": 330},
    {"alimento": "pan blanco", "calorias_100g": 265},
    {"alimento": "pan integral", "calorias_100g": 247},
    {"alimento": "manzana", "calorias_100g": 52},
    {"alimento": "pera", "calorias_100g": 57},
    {"alimento": "banana", "calorias_100g": 89},
    {"alimento": "sandia", "calorias_100g": 30},
    {"alimento": "papaya", "calorias_100g": 43},
    {"alimento": "mango", "calorias_100g": 60},
    {"alimento": "uva", "calorias_100g": 69},
    {"alimento": "piña", "calorias_100g": 50},
    {"alimento": "doritos", "calorias_100g": 490},
    {"alimento": "pringles", "calorias_100g": 520},
    {"alimento": "churritos", "calorias_100g": 480},
    {"alimento": "chocolate", "calorias_100g": 546},
    {"alimento": "galletas", "calorias_100g": 450},
    {"alimento": "tres leches", "calorias_100g": 240},
    {"alimento": "flan", "calorias_100g": 140},
    {"alimento": "pastel de chocolate", "calorias_100g": 360},
    {"alimento": "donas", "calorias_100g": 420},
    {"alimento": "helado", "calorias_100g": 200},
    {"alimento": "café con azúcar", "calorias_100g": 20},
    {"alimento": "café negro", "calorias_100g": 2},
    {"alimento": "horchata", "calorias_100g": 90},
    {"alimento": "cola", "calorias_100g": 42},
    {"alimento": "jugos naturales", "calorias_100g": 45},
    {"alimento": "chocolate caliente", "calorias_100g": 90},

    # Ampliaciones grandes (estimadas)
    {"alimento": "carne adobada", "calorias_100g": 240},
    {"alimento": "chorizo salvadoreño", "calorias_100g": 310},
    {"alimento": "panes con pollo", "calorias_100g": 190},
    {"alimento": "panes con gallina", "calorias_100g": 205},
    {"alimento": "pastel de pollo", "calorias_100g": 260},
    {"alimento": "chilaquiles", "calorias_100g": 220},
    {"alimento": "chirmol", "calorias_100g": 40},
    {"alimento": "curtido", "calorias_100g": 22},
    {"alimento": "casamiento", "calorias_100g": 150},
    {"alimento": "ensalada rusa", "calorias_100g": 120},
    {"alimento": "sopa de pata", "calorias_100g": 140},
    {"alimento": "sopa de pescado", "calorias_100g": 100},
    {"alimento": "pescado frito", "calorias_100g": 220},
    {"alimento": "mojarra frita", "calorias_100g": 210},
    {"alimento": "camarones al ajillo", "calorias_100g": 160},
    {"alimento": "camarones empanizados", "calorias_100g": 240},
    {"alimento": "pizza pepperoni", "calorias_100g": 298},
    {"alimento": "pizza hawaiana", "calorias_100g": 270},
    {"alimento": "alitas de pollo", "calorias_100g": 290},
    {"alimento": "onion rings", "calorias_100g": 411},
    {"alimento": "quesadilla", "calorias_100g": 260},
    {"alimento": "shawarma", "calorias_100g": 230},
    {"alimento": "pechuga de pollo a la plancha", "calorias_100g": 165},
    {"alimento": "muslo de pollo", "calorias_100g": 170},
    {"alimento": "salchichas", "calorias_100g": 300},
    {"alimento": "jamón", "calorias_100g": 145},
    {"alimento": "tocino", "calorias_100g": 540},
    {"alimento": "carne molida de res", "calorias_100g": 250},
    {"alimento": "carne molida de cerdo", "calorias_100g": 290},
    {"alimento": "lentejas cocidas", "calorias_100g": 116},
    {"alimento": "garbanzos cocidos", "calorias_100g": 164},
    {"alimento": "sopa de verduras", "calorias_100g": 45},
    {"alimento": "puré de papa", "calorias_100g": 88},
    {"alimento": "ensalada de repollo", "calorias_100g": 22},
    {"alimento": "croissant", "calorias_100g": 406},
    {"alimento": "baguette", "calorias_100g": 270},
    {"alimento": "pan de ajo", "calorias_100g": 350},
    {"alimento": "tortilla de harina", "calorias_100g": 300},
    {"alimento": "fresa", "calorias_100g": 32},
    {"alimento": "kiwi", "calorias_100g": 61},
    {"alimento": "melon", "calorias_100g": 34},
    {"alimento": "mandarina", "calorias_100g": 53},
    {"alimento": "coco", "calorias_100g": 354},
    {"alimento": "guayaba", "calorias_100g": 68},
    {"alimento": "durazno", "calorias_100g": 39},
    {"alimento": "cereza", "calorias_100g": 63},
    {"alimento": "zanahoria", "calorias_100g": 41},
    {"alimento": "pepino", "calorias_100g": 15},
    {"alimento": "tomate", "calorias_100g": 18},
    {"alimento": "lechuga", "calorias_100g": 14},
    {"alimento": "brocoli", "calorias_100g": 34},
    {"alimento": "coliflor", "calorias_100g": 25},
    {"alimento": "papas cocidas", "calorias_100g": 87},
    {"alimento": "papas al horno", "calorias_100g": 93},
    {"alimento": "elote cocido", "calorias_100g": 96},
    {"alimento": "aguacate", "calorias_100g": 160},
    {"alimento": "cheetos", "calorias_100g": 512},
    {"alimento": "ruffles", "calorias_100g": 520},
    {"alimento": "palomitas de maíz", "calorias_100g": 375},
    {"alimento": "maní salado", "calorias_100g": 585},
    {"alimento": "granola", "calorias_100g": 471},
    {"alimento": "brownie", "calorias_100g": 466},
    {"alimento": "quesadilla salvadoreña", "calorias_100g": 380},
    {"alimento": "budín", "calorias_100g": 250},
    {"alimento": "arroz con leche", "calorias_100g": 160},
    {"alimento": "chocobanano", "calorias_100g": 220},
    {"alimento": "té helado azucarado", "calorias_100g": 27},
    {"alimento": "leche entera", "calorias_100g": 61},
    {"alimento": "leche descremada", "calorias_100g": 35},
    {"alimento": "bebida energética", "calorias_100g": 45},
    {"alimento": "limonada", "calorias_100g": 42},
    {"alimento": "naranjada", "calorias_100g": 45},
    {"alimento": "sándwich de jamón", "calorias_100g": 230},
    {"alimento": "sándwich de pollo", "calorias_100g": 210},
    {"alimento": "wrap de pollo", "calorias_100g": 190},
    {"alimento": "macarrones con queso", "calorias_100g": 164},
    {"alimento": "espaguetis con carne", "calorias_100g": 150},
    {"alimento": "espaguetis a la boloñesa", "calorias_100g": 175},
    {"alimento": "arroz frito", "calorias_100g": 190},
    {"alimento": "chow mein", "calorias_100g": 138},
    {"alimento": "pollo agridulce", "calorias_100g": 190},
    {"alimento": "pollo teriyaki", "calorias_100g": 150},
    {"alimento": "sushi (promedio)", "calorias_100g": 130},
    {"alimento": "ramen instantáneo", "calorias_100g": 440},
    {"alimento": "ceviche", "calorias_100g": 90},
    {"alimento": "tortilla española", "calorias_100g": 154},
    {"alimento": "hummus", "calorias_100g": 166},
    {"alimento": "guacamole", "calorias_100g": 152},
    {"alimento": "arepas", "calorias_100g": 218},
    {"alimento": "berenjena frita", "calorias_100g": 250},
    {"alimento": "sopa minestrone", "calorias_100g": 60},
    {"alimento": "sopa de tomate", "calorias_100g": 40},
    {"alimento": "tortitas de verduras", "calorias_100g": 150},
    {"alimento": "nachos con queso", "calorias_100g": 350},
    {"alimento": "queso mozzarella", "calorias_100g": 300},
    {"alimento": "queso cheddar", "calorias_100g": 403},
    {"alimento": "yogur natural", "calorias_100g": 59},
    {"alimento": "yogur con fruta", "calorias_100g": 95},
    {"alimento": "cereal azucarado", "calorias_100g": 388},
    {"alimento": "tamal mexicano", "calorias_100g": 225},
    {"alimento": "pozole", "calorias_100g": 110},
    {"alimento": "torta mexicana", "calorias_100g": 260},
    {"alimento": "birria", "calorias_100g": 170},
    {"alimento": "fajitas de pollo", "calorias_100g": 150},
    {"alimento": "fajitas de res", "calorias_100g": 180},
    {"alimento": "empanada argentina", "calorias_100g": 260},
    {"alimento": "choripan", "calorias_100g": 280},
    {"alimento": "chimichurri (salsa)", "calorias_100g": 180},
    {"alimento": "pancakes", "calorias_100g": 227},
    {"alimento": "waffles", "calorias_100g": 291},
    {"alimento": "miel", "calorias_100g": 304},
    {"alimento": "jalea (mermelada)", "calorias_100g": 250},
    {"alimento": "mantequilla", "calorias_100g": 717},
    {"alimento": "margarina", "calorias_100g": 720},
    {"alimento": "aceite vegetal", "calorias_100g": 884},
    {"alimento": "aguas frescas", "calorias_100g": 35},
    {"alimento": "té chai", "calorias_100g": 20},
    {"alimento": "capuchino", "calorias_100g": 38},
    {"alimento": "latte", "calorias_100g": 54},
    {"alimento": "mocha", "calorias_100g": 80},
    {"alimento": "pescado empanizado", "calorias_100g": 230},
    {"alimento": "pescado al ajillo", "calorias_100g": 160},
    {"alimento": "huevos revueltos", "calorias_100g": 140},
    {"alimento": "huevos estrellados", "calorias_100g": 180},
    {"alimento": "omelette", "calorias_100g": 150},
    {"alimento": "queso crema", "calorias_100g": 350},
    {"alimento": "crema batida", "calorias_100g": 257},
    {"alimento": "malt shake", "calorias_100g": 140},
    {"alimento": "granizado con sirope", "calorias_100g": 90},
    {"alimento": "pupusa de arroz", "calorias_100g": 240},
    {"alimento": "pupusa de queso y chicharrón", "calorias_100g": 280},
    {"alimento": "pupusa de ayote", "calorias_100g": 210},
    {"alimento": "pupusa de mora", "calorias_100g": 200},
    {"alimento": "pan con chumpe", "calorias_100g": 225},
    {"alimento": "pan con gallina india", "calorias_100g": 215},
    {"alimento": "chilate", "calorias_100g": 50},
    {"alimento": "nuégados", "calorias_100g": 290},
    {"alimento": "turrón", "calorias_100g": 310},
    {"alimento": "canelas", "calorias_100g": 330},
    {"alimento": "tostadas con huevo", "calorias_100g": 220},
    {"alimento": "pastelitos de papa", "calorias_100g": 190},
    {"alimento": "quesadilla de arroz", "calorias_100g": 400},
    {"alimento": "empanadas de plátano", "calorias_100g": 220},
    {"alimento": "pollo empanizado", "calorias_100g": 240},
    {"alimento": "carne en salsa", "calorias_100g": 210},
    {"alimento": "gallo en chicha", "calorias_100g": 200},
    {"alimento": "mariscada", "calorias_100g": 120},
    {"alimento": "cocido salvadoreño", "calorias_100g": 140},

    # Comidas genéricas más comunes
    {"alimento": "carne de res", "calorias_100g": 250},
    {"alimento": "carne de cerdo", "calorias_100g": 290},
    {"alimento": "carne de pollo", "calorias_100g": 165},
    {"alimento": "carne frita", "calorias_100g": 280},
    {"alimento": "carne al vapor", "calorias_100g": 180},
    {"alimento": "filete de pescado", "calorias_100g": 120},
    {"alimento": "pescado hervido", "calorias_100g": 110},
    {"alimento": "pescado a la plancha", "calorias_100g": 125},
    {"alimento": "pescado al vapor", "calorias_100g": 100},
    {"alimento": "huevo duro", "calorias_100g": 155},
    {"alimento": "huevo cocido", "calorias_100g": 150},
    {"alimento": "huevo frito", "calorias_100g": 196},
    {"alimento": "arroz con verduras", "calorias_100g": 130},
    {"alimento": "arroz frito simple", "calorias_100g": 170},
    {"alimento": "arroz integral", "calorias_100g": 111},
    {"alimento": "ensalada verde", "calorias_100g": 45},
    {"alimento": "vegetales cocidos", "calorias_100g": 55},
    {"alimento": "verduras al vapor", "calorias_100g": 40},
    {"alimento": "sopa de pollo", "calorias_100g": 80},
    {"alimento": "sopa de verduras casera", "calorias_100g": 60},
    {"alimento": "guisado de verduras", "calorias_100g": 70},
    {"alimento": "fruta mixta", "calorias_100g": 60},
    {"alimento": "ensalada de frutas", "calorias_100g": 70},
    {"alimento": "pollo desmenuzado", "calorias_100g": 150},
    {"alimento": "pollo en caldo", "calorias_100g": 120},
    {"alimento": "frijoles parados", "calorias_100g": 130},
    {"alimento": "frijoles con crema", "calorias_100g": 175}
    
]
#Funcion conectada al boton ENTER, todo lo que ejecuta cuando se da click el boton
def registrar_comidas(caja_comidas, texto_error, texto_calorias_resultado, dropdown_menu):
    
    global calorias_totales
    
    comida = caja_comidas.get().lower()
    cantidades = dropdown_menu.get()
    
    if comida == "" or cantidades == "":
        texto_error.config(text= "Llena todos los campos", foreground = "red")
        return
    
    if cantidades.isdigit():
        texto_error.config(text= "")
    else:
        texto_error.config(text= "Digite un numero", foreground = "red")
        return
    #Se hace int aqui para compararlo con numeros enteros (hasta aca para
    #evitar error al no recibir input)
    cantidades = int(cantidades)
    
    #El bucle que ve cada diccionario dentro de la lista y corrobora si la comida
    #pertenece a algun alimento de cada diccionario
    existe_la_comida = False
    for diccionario in calorias_por_comida:
        if comida == diccionario["alimento"]:
            texto_error.config(text= "")
            existe_la_comida = True
            if cantidades == 100:
                calorias_totales += diccionario["calorias_100g"]
            elif cantidades == 50:
                calorias_totales += round((diccionario["calorias_100g"]/ 100) * 50, 2)
            elif cantidades == 150:
                calorias_totales += round((diccionario["calorias_100g"]/100) * 150, 2)
            else:
                texto_error.config(text= "Digite una cantidad (gramos) válida (50, 100, 150)", foreground = "red")
                return
    if existe_la_comida == False:
        texto_error.config(text= f"La comida: {comida} no esta registrada", foreground = "red")
        caja_comidas.delete(0,"end")
        dropdown_menu.delete(0,"end")
        return
    
    comidas_registradas.append(comida)
    comidas_registradas.append(cantidades)
    texto_error.config(text= f"Comida: {comida} registrada!", foreground= "green")
    
    print(comidas_registradas)
    texto_calorias_resultado.config(text= str(calorias_totales))
    
    caja_comidas.delete(0,"end")
    dropdown_menu.delete(0,"end")

calorias_excedidas = 0
def calcular_exceder(texto_calorias_aldia):
    global calorias_excedidas
    if calorias_totales == 2000:
        calorias_excedidas = calorias_totales - 2000
    elif calorias_totales > 2000:
        calorias_excedidas = calorias_totales - 2000
    elif calorias_totales < 2000:
        calorias_excedidas = calorias_totales - 2000
    texto_calorias_aldia.config(text= f"Te excediste/faltan {calorias_excedidas} calorias de 2000")
        
        
