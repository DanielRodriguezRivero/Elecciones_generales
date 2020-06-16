label lab1col:
    $ lab3var = False
    $ orden = ""
    scene black with fade
    play music "laberinto.mp3"
    $ renpy.pause(5, hard=True)
    scene lab1 with dissolve
    narrador "Ante tus ojos está la salida de la cueva lúgubre a la que daba la puerta del gimnasio. A lo lejos las olas rompen furiosas contra las rocas de la orilla de una playa que, ingenuamente, confundes con La Concha."
    c "Recuerdo esto de mis tiempos con el Spectrum."
    c "Escribe \"jódete\" a ver qué pasa. Yo siempre lo hacía."
    $ orden = renpy.input(">") 
    if orden == "jódete" or orden == "jodete":
        narrador "Jódete tú, enano coñón."
        c "Era lo que esperaba."
    else:
        c "Oye, ya te vale no hacerme caso. Soy tu líder de izquierdas."
    $ narrador("¿Hacia dónde continuarás?", interact=False)
    menu:
        "Norte":
            pass
        "Sur":
            pass #por definir
        "Este":
            jump lab2col
        "Oeste":
            pass

label lab2col:
    scene lab2 with dissolve
    narrador "Dejas atrás la playa. Por el rabillo del ojo crees observar cómo una bandada de cangrejos sale del mar en tu persecución, pero tienen las patas tan cortas que tardarían un siglo en alcanzarte."
    narrador "Llegas al inicio de un camino que atraviesa un bosque negro como un defensa central del Congo Belga. Todo es tétrico en esta tierra dejada de la mano de dios, en la que la tristeza y la soledad cabalgan y azotan a partes iguales a todas las almas atormentadas que se atreven a hoyar la tierra."
    $ narrador("¿Hacia dónde te diriges?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            pass
        "Sur":
            jump lab3col
        "Oeste":
            jump lab1col

label lab3col:
    if lab3var == False:
        scene lab3alt with dissolve
        $ lab3var = True
        $ renpy.pause(0.5, hard=True)
        narrador "Un florido campo de amapolas se despliega ante tus ojos. El rojo brillante que emanan los pétalos te hace recordar una antigua amante, un nunca olvidado amor y a tu profesora de Matemáticas, que te tenía manía."
        narrador "Pero en el prado no estáis solos. Entre dos encinas se alza, amenazante, fibroso, feroz..."
        stalin "Salud, camarada dragón. ¿Qué haces por estos lares?"
        stalin "Ajá, ya veo. Eres un miembro más de la clase proletaria explotado por el cerdo capitalista poseedor de este laberinto."
        stalin "Sí, sí. Él te envía comida fresca y tú no protestas mucho, pero ¿no mereces algo más? ¿Acaso viene él a ensuciarse el pellejo manteniendo inexpugnable el lugar?"
        stalin "¿Son sus manos las que recogen los restos humeantes de los intrusos que se cruzan en tu camino?"
        stalin "No, ¿verdad? ¿Entonces por qué no vas a su lujosa mansión, levantada con los tesoros que consigues para él y le demuestras quién es el que manda?"
        narrador "El dragón alza el vuelo mientras tararea la Internacional. No os molestará más."
        $ narrador("¿Cuál será tu siguiente destino?", interact=False)
        menu:
            "Norte":
                pass
            "Este":
                jump lab2col
            "Sur":
                jump lab1col
            "Oeste":
                jump lab4col 
    else:
        scene lab3 with dissolve
    c "¿Otra vez aquí?"
    c "Espero que tengas mejor ojo ahora."
    $ narrador("¿Hacia dónde te diriges?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            jump lab2col
        "Sur":
            jump lab1col
        "Oeste":
            jump lab4col
            
label lab4col:
    scene lab4 with dissolve
    narrador "Has ido a parar a las puertas de una fortaleza de amarillos muros que se pierden en la inmensidad del cielo. No alcanzas a ver las almenas. Sin embargo, las puertas de entrada son del tamaño de un ser humano."
    $ narrador("¿Hacia dónde te diriges?", interact=False)
    menu:
        "Norte":
            jump lab5col
        "Este":
            jump lab1col
        "Sur":
            pass
        "Oeste":
            jump lab2col


label lab5col:
    scene lab5 with dissolve
    narrador "Has aparecido en lo alto de un acantilado que da al mar. Un camino transitado lo atraviesa de parte a parte. Examinas la senda con detenimiento en busca de algún rastro, pero sin éxito."
    narrador "Las palmeras se mecen con la suave brisa nocturna que proviene de la costa; y el mar, como el rostro de una pelirroja, refleja la luz de innumerables puntos luminosos que arden con la fuerza de mil soles en lo profundo del cosmos."
    $ narrador("¿Hacia dónde te llevarán tus pasos?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            jump lab6col
        "Sur":
            jump lab3col
        "Oeste":
            jump lab2col
            
label lab6col:
    scene lab6 with dissolve
    narrador "La salida al fin. Junto a un muro de piedra similar al de la fortaleza que atravesaste anteriormente, se encuentra el contenedor de residuos solidos urbanos. Echas en falta los contenedores de reciclaje, pero no estás aquí para salvar al mundo."
    c "Pues ya está. Echamos la basura y esa puerta de ahí imagino que será la salida."
    $ puntosj += 3
    churrasco "Os habéis ganado los votos."
    c "Así me gusta."
    jump mapa
