label lab1:
    image lab1 = "images/laberinto/lab1.png"
    image lab2 = "images/laberinto/lab2.png"
    image lab3 = "images/laberinto/lab3.png"
    image lab3alt = "images/laberinto/lab3alt.jpg"
    image lab4 = "images/laberinto/lab4.png"
    image lab5 = "images/laberinto/lab5.png"
    image lab6 = "images/laberinto/lab6.png"
    $ lab3var = False
    
    scene black with fade
    play music "laberinto.mp3"
    $ renpy.pause(5, hard=True)
    
    scene lab1 with dissolve
    narrador "Ante tus ojos está la salida de la cueva lúgubre a la que daba la puerta del gimnasio. A lo lejos las olas rompen furiosas contra las rocas de la orilla de una playa que, ingenuamente, confundes con La Concha."
    pov "Está en San Sebastián, por cierto."
    r "Ya lo sabía. ¿Te piensas que estás con M. Rajao?"
    pov "..."
    r "Bueno, ¿qué? ¿Vamos a seguir?"
    $ narrador("¿Hacia dónde dirigirás tus pasos? Recuerda, el tiempo es tu aliado.", interact=False)
    menu:
        "Norte":
            pass
        "Sur":
            pass #por definir
        "Este":
            jump lab2
        "Oeste":
            pass

label lab2:
    scene lab2 with dissolve
    narrador "Dejas atrás la playa. Por el rabillo del ojo crees observar cómo una bandada de cangrejos sale del mar en tu persecución, pero tienen las patas tan cortas que tardarían un siglo en alcanzarte."
    narrador "Llegas al inicio de un camino que atraviesa un bosque negro como un defensa central del Congo Belga. Todo es tétrico en esta tierra dejada de la mano de dios, en la que la tristeza y la soledad cabalgan y azotan a partes iguales a todas las almas atormentadas que se atreven a hoyar la tierra."
    r "Un par de constructores y en un año lo tienes convertido en la periferia de Burgos."
    narrador "El camino se bifurca en todas direcciones. Recuerda el dicho: el viajero sabio usa GPS."
    r "Esto es ridículo. Vamos a tirar la basura, no al Anapurna."
    narrador "¿Y quién dice que el contenedor no esté allí? Que estás en Bilbao, hostias."
    $ narrador("¿Qué dirección eliges?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            pass
        "Sur":
            jump lab3
        "Oeste":
            jump lab1

label lab3:
    if lab3var == False:
        scene lab3alt with dissolve
        $ renpy.pause(0.5, hard=True)
        $ lab3var = True
        narrador "Un florido campo de amapolas se despliega ante tus ojos. El rojo brillante que emanan los pétalos te hace recordar una antigua amante, un nunca olvidado amor y a tu profesora de Matemáticas, que te tenía manía."
        narrador "Pero en el prado no estáis solos. Entre dos encinas se alza, amenazante, fibroso, feroz..."
        narrador "El dragón os mira fijamente. Pasa de un rostro a otro y del otro al anterior. Finalmente, se acerca a vosotros y abraza inesperadamente a M. Rajao."
        narrador "Habéis tenido suerte, es socio del P.P.K."
        narrador "Tras daros indicaciones de por dónde continuar, alza el vuelo a contarle a su madre que ha conocido al líder del partido. Es una historia mejor que cuando ella se dio un baño con Fraga en Benidorm."
        menu:
            "Norte":
                pass
            "Este":
                jump lab2
            "Sur":
                jump lab1
            "Oeste":
                jump lab4
        
        
    else:
        scene lab3 with dissolve
    r "¿Otra vez aquí?"
    r "Espero que tengas mejor ojo ahora."
    menu:
        "Norte":
            pass
        "Este":
            jump lab2
        "Sur":
            jump lab1
        "Oeste":
            jump lab4
            
label lab4:
    scene lab4 with dissolve
    $ renpy.pause(0.5, hard=True)
    narrador "Has ido a parar a las puertas de una fortaleza de amarillos muros que se pierden en la inmensidad del cielo. No alcanzas a ver las almenas. Sin embargo, las puertas de entrada son del tamaño de un ser humano."
    r "De uno no muy alto, todo hay que decirlo."
    montoto "Igual estamos en Ecuador."
    pov "¿Esto ha pasado la censura?"
    narrador "Te parece escuchar un susurro que proviene del interior. Cuando te acercas a la puerta norte, tropiezas con una roca."
    $ narrador("¿Hacia dónde te diriges?", interact=False)
    menu:
        "Norte":
            jump lab5
        "Este":
            jump lab1
        "Sur":
            pass
        "Oeste":
            jump lab2


label lab5:
    scene lab5 with dissolve
    $ renpy.pause(0.5, hard=True)
    narrador "Has aparecido en lo alto de un acantilado que da al mar. Un camino transitado lo atraviesa de parte a parte. Examinas la senda con detenimiento en busca de algún rastro, pero sin éxito."
    narrador "Las palmeras se mecen con la suave brisa nocturna que proviene de la costa; y el mar, como el rostro de una pelirroja, refleja la luz de innumerables puntos luminosos que arden con la fuerza de mil soles en lo profundo del cosmos."
    $ narrador("¿Hacia dónde te llevarán tus pasos?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            jump lab6
        "Sur":
            jump lab3
        "Oeste":
            jump lab2
            
label lab6:
    scene lab6 with dissolve
    $ renpy.pause(0.5, hard=True)
    narrador "La salida al fin. Junto a un muro de piedra similar al de la fortaleza que atravesaste anteriormente, se encuentra el contenedor de residuos solidos urbanos. Echas en falta los contenedores de reciclaje, pero no estás aquí para salvar al mundo."
    r "Pues ya está. Echamos la basura y esa puerta de ahí imagino que será la salida."
    $ puntosj += 3
    churrasco "Os habéis ganado los votos."
    r "Así me gusta."
    jump mapa
