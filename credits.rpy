init python:
    #si se escribe 'graficos', 'marujita), ('graficos', 'pepe')... apareceran juntos los dos bajo el epigrafe graficos
    credits = ('Guión', 'Dani "The Man" Johnson'), ('Sprites y CG', 'Muchos autores'), ('Script Girl', 'Luisa Lanas'), ('Catering', 'Croquetas para desayunar'), ('Catering', 'Croquetas para almorzar'), ('Catering', 'Croquetas para cenar'), ('Catering', 'Y una noche hubo pollo frito'), ('Programación', 'Yo'), ('Música', 'Todos los cortes son propiedad de sus autores'), ('Sexo sin compromiso', 'Eso aquí no se puede contar'), ('Villareal - Español', 'X'), ('Masajes', 'Lady Tailandia'), ('Testers', 'Hatseput Ramírez'), ('Testers', 'Cholo Simeone'), ('Testers', 'Dimitri Petrescu'), ('Testers', 'Ilona Iordanescu'), ('Testers', 'Aleksei Stajánov'), ('Testers', 'Paco el del kiosko'), ('Distribuidor', 'BitTorrent'), ('Ilustración de Portada', 'Sabrina Salerno'), ('Gracias especialmente a', 'Durex'), ('Gracias especialmente a', 'Pub Sensations'), ('Gracias especialmente a', 'Benedicto XVI'), ('Gracias especialmente a', 'Hugo Chaves'), ('Gracias especialmente a', 'La tiburona del cantábrico')
    credits_s = "{size=80}Elecciones Generales\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    #credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()

label credits:
    play music "cancioncreditos.mp3"
    image españacredito = "images/españacredito.jpg"
    image pagina = Text("{size=60}No nos hacemos responsables de las opiniones aquí vertidas. Cualquier parecido con la realidad es pura coincidencia.", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
    image splash = "images/logo.jpg" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
    image cred = Text(credits_s, font="creditos.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("", text_align=0.5)
    image thanks = Text("{size=80}¡Gracias por jugar!", text_align=0.5)
    image descargo = Text("{size=40}El material usado ha sido sacado de webs que decían ofrecer material libre de derechos. Si esto no fuera así porque en Internet hay mucho estafador, no duden en escribirme y borraré el material sin demora. No me demanden. Es inútil. Soy insolvente.", text_align=0.5)
    image descargo2 = Text("{size=40}Además, esto está hecho en Sichuan. A ver si hay cojones de ir a reclamarle algo a los chinos.", text_align=0.5)
    image descargo3 = Text("{size=40}Ningún animal fue maltratado durante la realización de esta novela visual.", text_align=0.5)
    image descargo4 = Text("{size=40}Pedro Sánchez, sí. Le molieron a palos (pero yo no tengo la culpa de eso).", text_align=0.5)
    image vota = "images/vota.jpg"
    $ credits_speed = 30 #scrolling speed in seconds
    #scene black #replace this with a fancy background
    scene españacredito
    r "¡Montoto, corre! Va a empezar el Madrid - Atleti ya."
    
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    show pagina  #splash es la imagen que hemos usado asi que aqui tendriamos que poner otra o lo que fuera
    with dissolve
    with Pause(5)
    hide pagina
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    scene black
    show descargo:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(8)
    hide descargo
    show descargo2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(6)
    hide descargo2
    show descargo3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(6)
    hide descargo3
    show descargo4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(6)
    hide descargo4
    show vota
    with dissolve
    with Pause (4)
    hide vota 
    with dissolve
    return