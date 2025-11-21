#logica.py

comidas_registradas = []
calorias_totales = 0


calorias_por_comida =  [
    {"alimento": "aceite vegetal", "calorias_100g": 884},
    {"alimento": "aguacate", "calorias_100g": 160},
    {"alimento": "aguas frescas", "calorias_100g": 35},
    {"alimento": "alitas de pollo", "calorias_100g": 290},
    {"alimento": "arepas", "calorias_100g": 218},
    {"alimento": "arroz blanco", "calorias_100g": 130},
    {"alimento": "arroz con leche", "calorias_100g": 160},
    {"alimento": "arroz con verduras", "calorias_100g": 130},
    {"alimento": "arroz frito", "calorias_100g": 190},
    {"alimento": "arroz frito simple", "calorias_100g": 170},
    {"alimento": "arroz integral", "calorias_100g": 111},
    {"alimento": "atol chuco", "calorias_100g": 80},
    {"alimento": "atol de arroz", "calorias_100g": 110},
    {"alimento": "atol de elote", "calorias_100g": 90},
    {"alimento": "atun en aceite", "calorias_100g": 198},
    {"alimento": "atun en agua", "calorias_100g": 116},
    {"alimento": "baguette", "calorias_100g": 270},
    {"alimento": "banana", "calorias_100g": 89},
    {"alimento": "bebida energética", "calorias_100g": 45},
    {"alimento": "berenjena frita", "calorias_100g": 250},
    {"alimento": "birria", "calorias_100g": 170},
    {"alimento": "brocoli", "calorias_100g": 34},
    {"alimento": "brownie", "calorias_100g": 466},
    {"alimento": "budín", "calorias_100g": 250},
    {"alimento": "burrito", "calorias_100g": 240},
    {"alimento": "café con azúcar", "calorias_100g": 20},
    {"alimento": "café negro", "calorias_100g": 2},
    {"alimento": "camarones al ajillo", "calorias_100g": 160},
    {"alimento": "camarones empanizados", "calorias_100g": 240},
    {"alimento": "canelas", "calorias_100g": 330},
    {"alimento": "capuchino", "calorias_100g": 38},
    {"alimento": "carne adobada", "calorias_100g": 240},
    {"alimento": "carne al vapor", "calorias_100g": 180},
    {"alimento": "carne asada", "calorias_100g": 250},
    {"alimento": "carne de cerdo", "calorias_100g": 290},
    {"alimento": "carne de pollo", "calorias_100g": 165},
    {"alimento": "carne de res", "calorias_100g": 250},
    {"alimento": "carne en salsa", "calorias_100g": 210},
    {"alimento": "carne frita", "calorias_100g": 280},
    {"alimento": "carne guisada", "calorias_100g": 200},
    {"alimento": "carne molida de cerdo", "calorias_100g": 290},
    {"alimento": "carne molida de res", "calorias_100g": 250},
    {"alimento": "casamiento", "calorias_100g": 150},
    {"alimento": "cereal azucarado", "calorias_100g": 388},
    {"alimento": "cereza", "calorias_100g": 63},
    {"alimento": "ceviche", "calorias_100g": 90},
    {"alimento": "cheetos", "calorias_100g": 512},
    {"alimento": "chilaquiles", "calorias_100g": 220},
    {"alimento": "chilate", "calorias_100g": 50},
    {"alimento": "chimichurri (salsa)", "calorias_100g": 180},
    {"alimento": "chocolate", "calorias_100g": 546},
    {"alimento": "chocolate caliente", "calorias_100g": 90},
    {"alimento": "chocobanano", "calorias_100g": 220},
    {"alimento": "choripan", "calorias_100g": 280},
    {"alimento": "chorizo salvadoreño", "calorias_100g": 310},
    {"alimento": "chow mein", "calorias_100g": 138},
    {"alimento": "chuleta de cerdo", "calorias_100g": 260},
    {"alimento": "churritos", "calorias_100g": 480},
    {"alimento": "coco", "calorias_100g": 354},
    {"alimento": "cocido salvadoreño", "calorias_100g": 140},
    {"alimento": "cola", "calorias_100g": 42},
    {"alimento": "coliflor", "calorias_100g": 25},
    {"alimento": "costilla de cerdo", "calorias_100g": 290},
    {"alimento": "crema batida", "calorias_100g": 257},
    {"alimento": "crema salvadoreña", "calorias_100g": 210},
    {"alimento": "croissant", "calorias_100g": 406},
    {"alimento": "curtido", "calorias_100g": 22},
    {"alimento": "doritos", "calorias_100g": 490},
    {"alimento": "donas", "calorias_100g": 420},
    {"alimento": "durazno", "calorias_100g": 39},
    {"alimento": "elote cocido", "calorias_100g": 96},
    {"alimento": "empanada argentina", "calorias_100g": 260},
    {"alimento": "empanadas de frijol", "calorias_100g": 240},
    {"alimento": "empanadas de leche", "calorias_100g": 250},
    {"alimento": "empanadas de plátano", "calorias_100g": 220},
    {"alimento": "enchiladas", "calorias_100g": 260},
    {"alimento": "ensalada de frutas", "calorias_100g": 70},
    {"alimento": "ensalada de repollo", "calorias_100g": 22},
    {"alimento": "ensalada rusa", "calorias_100g": 120},
    {"alimento": "ensalada verde", "calorias_100g": 45},
    {"alimento": "espaguetis a la boloñesa", "calorias_100g": 175},
    {"alimento": "espaguetis con carne", "calorias_100g": 150},
    {"alimento": "fajitas de pollo", "calorias_100g": 150},
    {"alimento": "fajitas de res", "calorias_100g": 180},
    {"alimento": "filete de pescado", "calorias_100g": 120},
    {"alimento": "flan", "calorias_100g": 140},
    {"alimento": "fresa", "calorias_100g": 32},
    {"alimento": "frijoles cocidos", "calorias_100g": 140},
    {"alimento": "frijoles con crema", "calorias_100g": 175},
    {"alimento": "frijoles parados", "calorias_100g": 130},
    {"alimento": "frijoles refritos", "calorias_100g": 180},
    {"alimento": "fruta mixta", "calorias_100g": 60},
    {"alimento": "gallo en chicha", "calorias_100g": 200},
    {"alimento": "galletas", "calorias_100g": 450},
    {"alimento": "garbanzos cocidos", "calorias_100g": 164},
    {"alimento": "garnachas", "calorias_100g": 240},
    {"alimento": "granizado con sirope", "calorias_100g": 90},
    {"alimento": "granola", "calorias_100g": 471},
    {"alimento": "guacamole", "calorias_100g": 152},
    {"alimento": "guisado de verduras", "calorias_100g": 70},
    {"alimento": "guayaba", "calorias_100g": 68},
    {"alimento": "hamburguesa", "calorias_100g": 260},
    {"alimento": "hamburguesa con queso", "calorias_100g": 280},
    {"alimento": "helado", "calorias_100g": 200},
    {"alimento": "horchata", "calorias_100g": 90},
    {"alimento": "hot dog", "calorias_100g": 290},
    {"alimento": "huevo", "calorias_100g": 155},
    {"alimento": "huevo cocido", "calorias_100g": 150},
    {"alimento": "huevo duro", "calorias_100g": 155},
    {"alimento": "huevo frito", "calorias_100g": 196},
    {"alimento": "huevos estrellados", "calorias_100g": 180},
    {"alimento": "huevos revueltos", "calorias_100g": 140},
    {"alimento": "hummus", "calorias_100g": 166},
    {"alimento": "jamón", "calorias_100g": 145},
    {"alimento": "jalea (mermelada)", "calorias_100g": 250},
    {"alimento": "jugos naturales", "calorias_100g": 45},
    {"alimento": "kiwi", "calorias_100g": 61},
    {"alimento": "lasagna", "calorias_100g": 150},
    {"alimento": "latte", "calorias_100g": 54},
    {"alimento": "lechuga", "calorias_100g": 14},
    {"alimento": "leche descremada", "calorias_100g": 35},
    {"alimento": "leche entera", "calorias_100g": 61},
    {"alimento": "lentejas cocidas", "calorias_100g": 116},
    {"alimento": "limonada", "calorias_100g": 42},
    {"alimento": "macarrones con queso", "calorias_100g": 164},
    {"alimento": "malt shake", "calorias_100g": 140},
    {"alimento": "mandarina", "calorias_100g": 53},
    {"alimento": "mango", "calorias_100g": 60},
    {"alimento": "maní salado", "calorias_100g": 585},
    {"alimento": "mantequilla", "calorias_100g": 717},
    {"alimento": "manzana", "calorias_100g": 52},
    {"alimento": "mariscada", "calorias_100g": 120},
    {"alimento": "margarina", "calorias_100g": 720},
    {"alimento": "melon", "calorias_100g": 34},
    {"alimento": "miel", "calorias_100g": 304},
    {"alimento": "mocha", "calorias_100g": 80},
    {"alimento": "mojarra frita", "calorias_100g": 210},
    {"alimento": "nachos con queso", "calorias_100g": 350},
    {"alimento": "naranjada", "calorias_100g": 45},
    {"alimento": "nuggets", "calorias_100g": 290},
    {"alimento": "nuégados", "calorias_100g": 290},
    {"alimento": "omelette", "calorias_100g": 150},
    {"alimento": "onion rings", "calorias_100g": 411},
    {"alimento": "pan blanco", "calorias_100g": 265},
    {"alimento": "pan con chumpe", "calorias_100g": 225},
    {"alimento": "pan con gallina india", "calorias_100g": 215},
    {"alimento": "pan dulce", "calorias_100g": 330},
    {"alimento": "pan francés", "calorias_100g": 285},
    {"alimento": "pan integral", "calorias_100g": 247},
    {"alimento": "pan de ajo", "calorias_100g": 350},
    {"alimento": "panes con gallina", "calorias_100g": 205},
    {"alimento": "panes con pollo", "calorias_100g": 190},
    {"alimento": "pancakes", "calorias_100g": 227},
    {"alimento": "papas al horno", "calorias_100g": 93},
    {"alimento": "papas cocidas", "calorias_100g": 87},
    {"alimento": "papas fritas", "calorias_100g": 312},
    {"alimento": "papaya", "calorias_100g": 43},
    {"alimento": "pastel de chocolate", "calorias_100g": 360},
    {"alimento": "pastel de pollo", "calorias_100g": 260},
    {"alimento": "pastelitos de carne", "calorias_100g": 280},
    {"alimento": "pastelitos de papa", "calorias_100g": 190},
    {"alimento": "pechuga de pollo a la plancha", "calorias_100g": 165},
    {"alimento": "pepino", "calorias_100g": 15},
    {"alimento": "pera", "calorias_100g": 57},
    {"alimento": "pescado a la plancha", "calorias_100g": 125},
    {"alimento": "pescado al ajillo", "calorias_100g": 160},
    {"alimento": "pescado al vapor", "calorias_100g": 100},
    {"alimento": "pescado empanizado", "calorias_100g": 230},
    {"alimento": "pescado frito", "calorias_100g": 220},
    {"alimento": "pescado hervido", "calorias_100g": 110},
    {"alimento": "piña", "calorias_100g": 50},
    {"alimento": "pizza", "calorias_100g": 266},
    {"alimento": "pizza hawaiana", "calorias_100g": 270},
    {"alimento": "pizza pepperoni", "calorias_100g": 298},
    {"alimento": "platanos al horno", "calorias_100g": 158},
    {"alimento": "platanos con crema", "calorias_100g": 240},
    {"alimento": "platanos fritos", "calorias_100g": 200},
    {"alimento": "pollo agridulce", "calorias_100g": 190},
    {"alimento": "pollo asado", "calorias_100g": 180},
    {"alimento": "pollo desmenuzado", "calorias_100g": 150},
    {"alimento": "pollo en caldo", "calorias_100g": 120},
    {"alimento": "pollo empanizado", "calorias_100g": 240},
    {"alimento": "pollo frito", "calorias_100g": 260},
    {"alimento": "pollo guisado", "calorias_100g": 150},
    {"alimento": "pollo teriyaki", "calorias_100g": 150},
    {"alimento": "palomitas de maíz", "calorias_100g": 375},
    {"alimento": "pozole", "calorias_100g": 110},
    {"alimento": "pringles", "calorias_100g": 520},
    {"alimento": "pupusa de arroz", "calorias_100g": 240},
    {"alimento": "pupusa de ayote", "calorias_100g": 210},
    {"alimento": "pupusa de chicharrón", "calorias_100g": 270},
    {"alimento": "pupusa de frijol", "calorias_100g": 210},
    {"alimento": "pupusa de mora", "calorias_100g": 200},
    {"alimento": "pupusa de queso", "calorias_100g": 230},
    {"alimento": "pupusa de queso y chicharrón", "calorias_100g": 280},
    {"alimento": "pupusa loca", "calorias_100g": 300},
    {"alimento": "pupusa revuelta", "calorias_100g": 260},
    {"alimento": "puré de papa", "calorias_100g": 88},
    {"alimento": "quesadilla", "calorias_100g": 260},
    {"alimento": "quesadilla salvadoreña", "calorias_100g": 380},
    {"alimento": "quesadilla de arroz", "calorias_100g": 400},
    {"alimento": "queso cheddar", "calorias_100g": 403},
    {"alimento": "queso crema", "calorias_100g": 350},
    {"alimento": "queso duro blando", "calorias_100g": 320},
    {"alimento": "queso mozzarella", "calorias_100g": 300},
    {"alimento": "ramen instantáneo", "calorias_100g": 440},
    {"alimento": "ruffles", "calorias_100g": 520},
    {"alimento": "salchichas", "calorias_100g": 300},
    {"alimento": "sandia", "calorias_100g": 30},
    {"alimento": "sándwich de jamón", "calorias_100g": 230},
    {"alimento": "sándwich de pollo", "calorias_100g": 210},
    {"alimento": "shawarma", "calorias_100g": 230},
    {"alimento": "sopa de gallina", "calorias_100g": 95},
    {"alimento": "sopa de pata", "calorias_100g": 140},
    {"alimento": "sopa de pescado", "calorias_100g": 100},
    {"alimento": "sopa de pollo", "calorias_100g": 80},
    {"alimento": "sopa de res", "calorias_100g": 85},
    {"alimento": "sopa de tomate", "calorias_100g": 40},
    {"alimento": "sopa de verduras", "calorias_100g": 45},
    {"alimento": "sopa de verduras casera", "calorias_100g": 60},
    {"alimento": "sopa minestrone", "calorias_100g": 60},
    {"alimento": "sushi (promedio)", "calorias_100g": 130},
    {"alimento": "tacos", "calorias_100g": 240},
    {"alimento": "tamal de chipilín", "calorias_100g": 180},
    {"alimento": "tamal de gallina", "calorias_100g": 215},
    {"alimento": "tamal mexicano", "calorias_100g": 225},
    {"alimento": "tamales de elote", "calorias_100g": 190},
    {"alimento": "té chai", "calorias_100g": 20},
    {"alimento": "té helado azucarado", "calorias_100g": 27},
    {"alimento": "tocino", "calorias_100g": 540},
    {"alimento": "tomate", "calorias_100g": 18},
    {"alimento": "torta mexicana", "calorias_100g": 260},
    {"alimento": "tortilla de harina", "calorias_100g": 300},
    {"alimento": "tortilla de maíz", "calorias_100g": 218},
    {"alimento": "tortilla española", "calorias_100g": 154},
    {"alimento": "tortitas de verduras", "calorias_100g": 150},
    {"alimento": "tostadas con huevo", "calorias_100g": 220},
    {"alimento": "tres leches", "calorias_100g": 240},
    {"alimento": "turrón", "calorias_100g": 310},
    {"alimento": "uva", "calorias_100g": 69},
    {"alimento": "vegetales cocidos", "calorias_100g": 55},
    {"alimento": "verduras al vapor", "calorias_100g": 40},
    {"alimento": "waffles", "calorias_100g": 291},
    {"alimento": "wrap de pollo", "calorias_100g": 190},
    {"alimento": "yuca frita", "calorias_100g": 170},
    {"alimento": "yuca sancochada", "calorias_100g": 120},
    {"alimento": "yogur con fruta", "calorias_100g": 95},
    {"alimento": "yogur natural", "calorias_100g": 59},
    {"alimento": "zanahoria", "calorias_100g": 41}
]


#Funcion conectada al boton ENTER, todo lo que ejecuta cuando se da click el boton
def obtener_nombres_comidas():
    nombres_alimentos = []
    for c in calorias_por_comida:
        nombres_alimentos.append(c["alimento"])
    return nombres_alimentos

def registrar_comidas(combo_alimentos, texto_error, texto_calorias_resultado, entrada_gramos, historial):
    global calorias_totales
    
    alimento = combo_alimentos.get().strip().lower() #Lista despegable
    cantidades = entrada_gramos.get().strip()
    

    if alimento == "" or cantidades == "":
        texto_error.config(text= "Llena todos los campos", foreground = "red")
        return
    

    if cantidades.isdigit(): #Es un digito
        gramos = int(cantidades)
        texto_error.config(text="")
    else:
        texto_error.config(text= "Digite un numero valido para gramos", foreground = "red")
        return
    
    


    for diccionario in calorias_por_comida:
        if alimento == diccionario["alimento"]:
            calorias_a_sumar = round((diccionario["calorias_100g"] * gramos)/100 , 2)
            calorias_totales += calorias_a_sumar




            


            comidas_registradas.append({
                "alimento": alimento,
                "gramos": gramos,
                "calorias": calorias_a_sumar
            }) #Para historial de pedidos



            historial.insert("end", f"{alimento.capitalize()} - {gramos} g - {calorias_a_sumar} kcal")
            
            texto_calorias_resultado.config(text=calorias_totales)
            texto_error.config(text=f"{alimento} registrado :D", foreground="green")

            
            if calorias_totales > 2000:
                texto_error.config(text= "HAS SUPERO LAS 2000 kcal !!!", foreground="red")
            break

    

def calcular_exceder(texto_calorias_aldia):
    global calorias_excedidas
    calorias_meta = (2000)
    calorias_excedidas = calorias_totales - calorias_meta
    if calorias_totales > calorias_meta:
        texto_calorias_aldia.config(text= f"Te excediste por: {round(calorias_excedidas)} calorias de 2000 kcal.", foreground="red")
    elif calorias_totales < calorias_meta:
        texto_calorias_aldia.config(text= f"Te faltan {round(abs(calorias_excedidas))} calorias de 2000 kcal.", foreground="blue")
    else:
        texto_calorias_aldia.config(text= f"Perfecto! Llegaste a las {round(calorias_meta)} calorias de 2000 kcal.", foreground="green")

