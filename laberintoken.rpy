label lab1ken:
    $ lab3var = False
    scene black with fade
    play music "laberinto.mp3"
    $ renpy.pause(5, hard=True)
    scene lab1 with dissolve
    $ renpy.pause(0.5, hard=True)
    narrador "Ante tus ojos está la salida de la cueva lúgubre a la que daba la puerta del gimnasio. A lo lejos las olas rompen furiosas contra las rocas de la orilla de una playa que, ingenuamente, confundes con La Concha."
    pov "Está en San Sebastián, por cierto."
    k "Ya lo sabía. ¿Te piensas que estás con M. Rajao?"
    $ narrador("¿Hacia dónde dirigirás tus pasos? Recuerda, el tiempo es tu aliado.", interact=False)
    menu:
        "Norte":
            pass
        "Sur":
            pass #por definir
        "Este":
            jump lab2ken
        "Oeste":
            pass

label lab2ken:
    scene lab2 with dissolve
    narrador "Dejas atrás la playa. Por el rabillo del ojo crees observar cómo una bandada de cangrejos sale del mar en tu persecución, pero tienen las patas tan cortas que tardarían un siglo en alcanzarte."
    narrador "Llegas al inicio de un camino que atraviesa un bosque negro como un defensa central del Congo Belga. Todo es tétrico en esta tierra dejada de la mano de dios, en la que la tristeza y la soledad cabalgan y azotan a partes iguales a todas las almas atormentadas que se atreven a hoyar la tierra."
    k "Un par de constructores y en un año lo tienes convertido en la periferia de Burgos."
    narrador "El camino se bifurca en todas direcciones. Recuerda el dicho: el viajero sabio usa GPS."
    k "Esto es ridículo. Vamos a tirar la basura, no al Anapurna."
    narrador "¿Y quién dice que el contenedor no esté allí? Que estás en Bilbao, hostias."
    $ narrador("¿Qué dirección eliges?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            pass
        "Sur":
            jump lab3ken
        "Oeste":
            jump lab1ken

label lab3ken:
    if lab3var == False:
        scene lab3alt with dissolve
        narrador "Un florido campo de amapolas se despliega ante tus ojos. El rojo brillante que emanan los pétalos te hace recordar una antigua amante, un nunca olvidado amor y a tu profesora de Matemáticas, que te tenía manía."
        k "No era manía lo que me tenía. No puedo decir lo que le pasaba a esa mujer porque en estos tiempos me denunciarían en el cuartelillo."
        narrador "Pero en el prado no estáis solos. Entre dos encinas se alza, amenazante, fibroso, feroz..."
        espejo "Dios mío, ¡un dragón!"
        extend " ¿Qué hacemos ahora? No podemos pasar mientras esté ahí."
        k "¿Y si nos lo follamos?"
        narrador "El dragón te mira con los ojos como platos. Un par de amenazadoras nubes negras surgen de sus sobredimensionados orificios nasales." 
        narrador "Por un instante parece que una llamarada de fuego vaya a convertir hasta la última célula de vuestro cuerpo en ceniza, pero en cuanto Ken da un paso hacia él con una amplia sonrisa, la bestia alza el vuelo sin darle la espalda hasta no verse fuera del alcance de su..." 
        narrador "Vamos, que se va."
        pov "Al fin has encontrado alguien que se te resiste."
        k "No te creas. Al sur de aquí hay una chica de orígenes humildes, sonrisa franca y pelo en permanente permanente que no cae rendida ante mis encantos como debería."
        espejo "Yo siempre he dicho que Susana es un tío. ¿Le has mirado la nuez? Si poco le falta para saltarte a la cabeza y darte de puñetazos."
        $ lab3var = True
        $ narrador("¿Qué dirección tomas?", interact=False)
        menu:
            "Norte":
                pass
            "Este":
                jump lab2ken
            "Sur":
                jump lab1ken
            "Oeste":
                jump lab4ken   
        
        
    else:
        scene lab3 with dissolve
    k "¿Otra vez aquí?"
    k "Espero que tengas mejor ojo ahora."
    $ narrador("¿Hacia dónde te diriges?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            jump lab2ken
        "Sur":
            jump lab1ken
        "Oeste":
            jump lab4ken
            
label lab4ken:
    scene lab4 with dissolve
    narrador "Has ido a parar a las puertas de una fortaleza de amarillos muros que se pierden en la inmensidad del cielo. No alcanzas a ver las almenas. Sin embargo, las puertas de entrada son del tamaño de un ser humano."
    k "De uno no muy alto, todo hay que decirlo."
    espejo "Igual estamos en Ecuador."
    pov "¿Esto ha pasado la censura?"
    narrador "Te parece escuchar un susurro que proviene del interior. Cuando te acercas a la puerta norte, tropiezas con una roca."
    k "¿¿Y si cogemos la roca?"
    $ narrador("¿Hacia dónde te diriges?", interact=False)
    menu:
        "Norte":
            jump lab5ken
        "Este":
            jump lab1ken
        "Sur":
            pass
        "Oeste":
            jump lab2ken


label lab5ken:
    scene lab5 with dissolve
    $ renpy.pause(0.5, hard=True)
    narrador "Has aparecido en lo alto de un acantilado que da al mar. Un camino transitado lo atraviesa de parte a parte. Examinas la senda con detenimiento en busca de algún rastro, pero sin éxito."
    narrador "Las palmeras se mecen con la suave brisa nocturna que proviene de la costa; y el mar, como el rostro de una pelirroja, refleja la luz de innumerables puntos luminosos que arden con la fuerza de mil soles en lo profundo del cosmos."
    $ narrador("¿Hacia dónde te llevarán tus pasos?", interact=False)
    menu:
        "Norte":
            pass
        "Este":
            jump lab6ken
        "Sur":
            jump lab3ken
        "Oeste":
            jump lab2ken
            
label lab6ken:
    scene lab6 with dissolve
    $ renpy.pause(0.5, hard=True)
    narrador "La salida al fin. Junto a un muro de piedra similar al de la fortaleza que atravesaste anteriormente, se encuentra el contenedor de residuos solidos urbanos. Echas en falta los contenedores de reciclaje, pero no estás aquí para salvar al mundo."
    espejo "Solo para salvarse a sí mismo."
    k "Pues ya está. Echamos la basura y esa puerta de ahí imagino que será la salida."
    $ puntosj += 3
    churrasco "Os habéis ganado los votos."
    k "Así me gusta."
    jump mapa
