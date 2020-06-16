label mapa:
    stop music
    play music "mapa.mp3"
    #mientras hayamos visitado menos de 5 ciudades, seguir visitando.
    if contadorciudades < 5:
        scene mapa1
        pov "¿Qué ciudad quieres visitar?"
        $ result = renpy.imagemap("images/mapadefinitivo1.jpg", "images/mapadefinitivo2.jpg", [
            (402, 647, 605, 686, "boliches"),  #coordenadas para los boliches, etc
            (620, 606, 773, 644, "malaga"),
            (378, 516, 545, 563, "sevilla"),
            (926, 368, 1148, 419, "valencia"),
            (964, 460, 1139, 523, "novalencia"),
            (699, 386, 856, 431, "cuenca"),
            (704, 521, 870, 564, "murcia"),
            (530, 328, 708, 376, "madrid"),
            (633, 263, 852, 309, "pocerogrado"),
            (884, 203, 1107, 237, "extrarradio"),
            (1157, 202, 1357, 245, "barcelona"),
            (1186, 360, 1351, 396, "mallorca"),
            (572, 726, 863, 767, "ceuta"),
            (164, 608, 316, 727, "tenerife"),
            (691, 128, 884, 169, "larioja"),
            (449, 163, 666, 201, "valladolid"),
            (477, 39, 665, 77, "torrelavega"),
            (788, 29, 935, 70, "bilbao"),
            (222, 39, 405, 147, "vigo"),
            ], focus="imagemap")
        
        if result == "boliches":
            if boliches == False:
                $ contadorciudades += 1
                $ boliches = True
                jump boliches
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
        
        if result == "malaga":
            if malaga == False:
                $ contadorciudades += 1
                $ malaga = True
                jump malaga
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "sevilla":
            if sevilla == False:
                $ contadorciudades += 1
                $ sevilla = True
                jump sevilla
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "murcia":
            if murcia == False:
                $ contadorciudades += 1
                $ murcia = True
                jump murcia
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "ceuta":
            if ceuta == False:
                $ contadorciudades += 1
                $ ceuta = True
                jump ceuta
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "tenerife":
            if tenerife == False:
                $ contadorciudades += 1
                $ tenerife = True
                jump tenerife
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "larioja":
            if larioja == False:
                $ contadorciudades += 1
                $ larioja = True
                jump larioja
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "madrid":
            if madrid == False:
                $ contadorciudades += 1
                $ madrid = True
                jump madrid
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "pocerogrado":
            if pocerogrado == False:
                $ contadorciudades += 1
                $ pocerogrado = True
                jump pocerogrado
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "barcelona":
            if barcelona == False:
                $ contadorciudades += 1
                $ barcelona = True
                jump barcelona
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "extrarradio":
            if extrarradio == False:
                $ contadorciudades += 1
                $ extrarradio = True
                jump extrarradio
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "bilbao":
            if bilbao == False:
                $ contadorciudades += 1
                $ bilbao = True
                jump bilbao
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "torrelavega":
            if torrelavega == False:
                $ contadorciudades += 1
                $ torrelavega = True
                jump torrelavega
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "valladolid":
            if valladolid == False:
                $ contadorciudades += 1
                $ valladolid = True
                jump valladolid
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "mallorca":
            if mallorca == False:
                $ contadorciudades += 1
                $ mallorca = True
                jump mallorca
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "valencia":
            if valencia == False:
                $ contadorciudades += 1
                $ valencia = True
                jump valencia
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "novalencia":
            if novalencia == False:
                $ contadorciudades += 1
                $ novalencia = True
                jump novalencia
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "vigo":
            if vigo == False:
                $ contadorciudades += 1
                $ vigo = True
                jump vigo
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
            
        if result == "cuenca":
            if cuenca == False:
                $ contadorciudades += 1
                $ cuenca = True
                jump cuenca
            else:
                pov "¿Para qué quieres volver aquí?"
                jump mapa
                
    #si se han visitado cinco ciudades, se salta al final, mejor dicho, al recuento de votos y secuencias finales, creditos, etc.        
    else:
        scene mapa1
        pov "Nuestro viaje ha llegado a su fin. Es la hora de la verdad. Cruza los dedos."
        jump fin
            
            
             
    show introcuatro
    if coletas == True:
        c "Hola"
        jump fin    #para poner créditos como los de las pelis
    if ken == True:
        k "Hola soy ken"
        jump fin    #para poner créditos como los de las pelis
    if mrajao == True:
        r "Hola, me mariano"
        jump fin    #para poner créditos como los de las pelis
    
