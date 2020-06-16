# Puedes colocar el 'script' de tu juego en este archivo.

# Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

#Declaración de la animación del gráfico de esperar a hacer click.
init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("prueba.ogg", channel="sound", loop="True")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


image ctc_blink:
    xpos 0.98 ypos 0.95
    xanchor 1.0 yanchor 1.0
    "sobre1.png"
    linear 0.5 alpha 1.0
    "sobre2.png"
    linear 0.5 alpha 1.0
    repeat
    
#graficos de la animacion de lluvia
image rain:
    "rain1.png"
    0.2
    "rain3.png"
    0.2
    "rain2.png"
    0.2
    repeat

#variable que le dirá al juego qué hace cada posición del imagemap del menu inicio
$ config.main_menu = [
    (u"Start Game", "start", "True"),
    (u"Load Game", _intra_jumps("load_screen", "main_game_transition"), "True"),
    (u"Preferences", _intra_jumps("instructions", "main_game_transition"), "True"),
    (u"Quit", ui.jumps("_quit"), "True")
    ]



# Declara los personajes usados en el juego como en el 
#   ejemplo.
define r = Character('M. Rajao', color="#0026FF",window_left_padding=160, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("rajao.png", xalign=0.0, yalign=1.0),callback=callback) #M. Rajao
define montoto = Character('Montoto', color="#23B9B1",window_left_padding=160, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("montoto.png", xalign=0.0, yalign=1.0),callback=callback) #M. Rajao
define c = Character('Coletas', color="#770A5C", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("elcoletas.png", xalign=0.0, yalign=1.0),callback=callback)  #El coletas
define stalin = Character('Staline', color="#FE0019", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("stanli.png", xalign=0.0, yalign=1.0),callback=callback) 
define k = Character('Ken Sánchez', color="#912C3E", window_left_padding=160, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("ken.png", xalign=0.0, yalign=1.0),callback=callback)  #Ken Sanchez
define espejo = Character('El reflejo de un líder', color="#A9A8A8", window_left_padding=160, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("espejo.png", xalign=0.0, yalign=1.0),callback=callback)  #Ken Sanchez
define pov = Character("[jugador]", color="#F5F4F4", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback) #el personaje jugador
define churri = Character("Tu churri", color="#8678c7", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback) #la pareja

#jueces
define nabo = Character("El Honorable Juez Nabo", color="#58D3F7", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
define bedel = Character("Bedel #2", color="#B58929", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
define robledo = Character("El Malhablado Juez Robledo", color="#2740D1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback) 
define martinez = Character("El Homófobo Juez Martínez", color="#27D190", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback) 
define aleli = Character("La Elegante Jueza Alelí", color="#D127C3", window_left_padding=150, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("aleli.gif", xalign=0.0, yalign=1.0), callback=callback) 
define enigma = Character("???", color="#27D190", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback) 
define chapero = Character("El Sofisticado Juez Chapero", color="#27D146", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("chapero.png", xalign=0.0, yalign=1.0), callback=callback) 
define alcantara = Character("El Observador Juez Alcántara", color="#8D5B22", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("alcantara.png", xalign=0.0, yalign=1.0), callback=callback) 
define cifuentes = Character("El Inflexible Juez Cifuentes", color="#2587A7", window_left_padding=150, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("cifuentes.png", xalign=0.0, yalign=1.0), callback=callback) 
define conrado = Character("El Honesto Juez Conrado", color="#1151DA", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("conrado.png", xalign=0.0, yalign=1.0), callback=callback) 
define heredia = Character("El Pusilánime Juez Heredia", color="#DE5F3F", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("heredia.png", xalign=0.0, yalign=1.0), callback=callback) 
define martinez2 = Character("El Recién Salido del Armario Juez Martinez", color="#27D190", window_left_padding=170, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("martinez2.png", xalign=0.0, yalign=1.0), callback=callback)
define robledo2 = Character("El Malhablado Juez Robledo", color="#2740D1", window_left_padding=150, ctc="ctc_blink", ctc_position="fixed", show_side_image=Image("robledo2.png", xalign=0.0, yalign=1.0), callback=callback) 

#personajes varios
define presentador = Character("Bob Jennings", color="#CCA049", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
define narrador = Character("El viejo archivero", color="#CCA049", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)

#Imagenes del cuartel general de los politicos
image presoehq = "images/presoe.jpg"
image queremoshq = "images/queremos.jpg"
image ppkhq = "images/ppkhq.jpg"




#imágenes de la splash screen
image splash = "inicio.jpg"
image uno = "uno.jpg"
image dos = "dos.jpg"
image tres = "tres.jpg"
image introuno = "introuno.jpg"
image introdos = "introdos.jpg"
image introtres = "introtres.jpg"
image introcuatro = "introcuatro.jpg"
image introcinco = "introcinco.jpg"
image introseis = "introseis.jpg"
image introsiete = "introsiete.jpg"
image introocho = "introocho.jpg"
image portada = "portada.jpg"

#imágenes del final
image fin1 = "fin1.jpg"
image fin2 = "fin2.jpg"
image fin3 = "fin3.jpg"

#imágenes del mapa de España
image mapa1 = "images/mapadefinitivo1.jpg"
image mapa2 = "images/mapadefinitivo2.jpg"

#definición de las flechas
image derecha = "images/derecha.png"
image izquierda = "images/izquierda.png"
image arriba = "images/arriba.png"
image abajo = "images/abajo.png"

#imagenes varias
image noticias = "images/noticias.jpg"
image pantalla = "images/pantalla.jpg"

#texto como imágenes
image texto = Text("{size=40}Tribunal Constitucional",color="#000000", text_align=0.3)
image texto2 = Text("{size=40}23 de diciembre",color="#000000", text_align=0.3)
image texto3 = Text("{size=40}Al día siguiente...",color="#ffffff", text_align=0.3)
image texto4 = Text("{size=40}27 de junio, 2016",color="#ffffff", text_align=0.3)
image texto5 = Text("{size=40}Media hora después...",color="#ffffff", text_align=0.3)
image textomoncloa1 = Text("{size=40}Palacio de La Moncloa",color="#ffffff", text_align=0.3)
image textomoncloa2 = Text("{size=40}Cuartel General del P.P.K.",color="#ffffff", text_align=0.3)
image textoqueremos1 = Text("{size=40}Palacio de Invierno",color="#ffffff", text_align=0.3)
image textoqueremos2 = Text("{size=40}Cuartel General de Queremos",color="#ffffff", text_align=0.3)
image textopresoe1 = Text("{size=40}Peluquería Manoli",color="#ffffff", text_align=0.3)
image textopresoe2 = Text("{size=40}Cuartel General del Presoe",color="#ffffff", text_align=0.3)


#imagenes del inicio
image robledo2 = im.Flip("robledo.png", horizontal=True)
image tribunal = "tribunal.jpg"
image interior = "interior.jpg"
image martinez = "images/martinez.png"
image nabo = "images/nabo.png"
image robledo = "images/robledo.png"
image bedel = "images/bedel.png"
image cifuentes = "images/cifuentes.png"
image aleli = "images/aleli.gif"
image heredia = "images/heredia.png"
image alcantara = "images/alcantara.png"
image conrado = "images/conrado.png"
image chapero = "images/chapero.png"
image diasiguiente = "images/diasiguiente.jpg"

#imagenes de travelling
image travelbarna = "images/travelbarna.jpg"
image travelextrarradio = "images/travelextrarradio.jpg"
image travelceuta = "images/travelceuta.jpg"
image traveltenerife = "images/traveltenerife.jpg"
image travelboliches = "images/travelboliches.jpg"
image travelmalaga = "images/travelmalaga.jpg"
image travelsevilla = "images/travelsevilla.jpg"
image travelmurcia = "images/travelmurcia.jpg"
image travelpocerogrado = "images/travelpocerogrado.jpg"
image travelmadrid = "images/travelmadrid.jpg"
image travelvalencia = "images/travelvalencia.jpg"
image travelnovalencia = "images/travelnovalencia.jpg"
image travelrioja = "images/travelrioja.jpg"
image travelcuenca = "images/travelcuenca.jpg"
image travelbilbao = "images/travelbilbo.jpg"
image travelmordor = "images/travelbilbo2.PNG"
image travelvega = "images/travelvega.jpg"
image travelvigo = "images/travelvigo.jpg"
image travelmallorca = "images/travelmallorca.jpg"
image travelvalladolid ="images/travelvalladolid.jpg"





#imágenes de la intro y seleccion de personajes
image pantallaseleccion = "pantallaseleccion.jpg"
image pantallaseleccion2= "pantallaseleccion2.jpg"

#Color blanco para usar en la intro o donde sea
image white = Solid((255, 255, 255, 255))

#esto para cambiar el menu principal
init -2 python:
    layout.imagemap_main_menu(
        "portada2.jpg",
        "portada1.jpg",
        [ (120, 588, 281, 633, "Start Game"),
            (92, 659, 323, 707, "Load Game"), 
            (396, 583, 549, 635, "Preferences"),
            (395, 662, 552, 710, "Quit") ],
        )

#intro antes del menu principal
label splashscreen:
    scene white
    play music "inicio.mp3"
    with Pause(4)

    show splash with dissolve
    with Pause(4)
    
    scene white
    with Pause(3)
    
    show uno with dissolve
    with Pause(1.5)    
    show dos with dissolve
    with Pause (1)
    show tres with dissolve
    with Pause (4)
    
    show introuno with dissolve
    with Pause (3)
    show introdos with dissolve
    with Pause (3)
    show introtres with dissolve
    with Pause (3)
    show introcuatro with dissolve
    with Pause (3)
    show introcinco with dissolve
    with Pause (3)
    show introseis with dissolve
    with Pause (3)
    show introsiete with dissolve
    with Pause (3)
    show introocho with dissolve
    with Pause (3)
    return


# - El juego comienza aquí.
label start:
    #variables varias
    $ enta = False #si hemos ayudado a pin laden
    $ yausado = False #para ver si se ya volvio Stalin de estar con pikachu
    $ sexohombre = False  #para guardar el sexo del jugador
    $ sexomujer = False
    
    #variables de ciudades visitadas
    $ tenerife = False
    $ ceuta = False
    $ boliches = False
    $ malaga = False
    $ sevilla = False
    $ murcia = False
    $ novalencia = False
    $ valencia = False
    $ extrarradio = False
    $ barcelona = False
    $ mallorca = False
    $ cuenca = False
    $ madrid = False
    $ pocerogrado = False
    $ valladolid = False
    $ larioja = False
    $ vigo = False
    $ torrelavega = False
    $ bilbao = False
    
    #variables de puntuación. Se actualizarán según el jugador escoja personaje. Si escoge coletas pues solo se actualiza puntosrajao y puntosken
    $ puntosj = 0 #puntos del jugador
    $ puntoscoletas = 0 #puntos del coletas
    $ puntosrajao = 0 #puntos de rajao
    $ puntosken = 0 #puntos de Ken
    
    #variables para ver qué personaje escoge el jugador
    $ mrajao = False
    $ ken = False
    $ coletas = False

    #variable de cuantas veces se ha visitado una ciudad
    $ contadorciudades = 0
    
    #asi se hace un travelling. El primer 0,0 es las coordenadas desde las que se parte, 300,0 es hacia donde va y el 14 ni idea, velocida?
    stop music
    play music "tribunal.ogg"
    scene tribunal at Pan((0, 200), (0,800), 20.0)
    show texto:
        yanchor 0.5 ypos 0.8
        xpos 0.1
    $ renpy.pause(0.4, hard=True)
    show texto2:
        yanchor 0.5 ypos 0.85
        xpos 0.1
    with dissolve
    $ renpy.pause(7, hard=True)   #así no se puede quitar la animación haciendo clic
    scene black
    play sound "mazo.mp3"
    $ renpy.pause(1.2, hard=True)    
    scene interior with fade
    $ renpy.pause(0.4, hard=True)
    nabo "¡Orden!"
    extend " ¡Orden!"
    show nabo at center:
        ypos 0.7
    with dissolve
    $ renpy.pause(0.4, hard=True)
    nabo "Estamos de acuerdo entonces, salvo alguna discrepancia..."
    show nabo at right:
        ypos 0.7
    with move
    show robledo at left:
        ypos 0.7
    with dissolve
    robledo "¡Mis cojones discrepancias!"
    extend " Me niego a apoyar semejante sinvergonzonería."
    nabo "Dirás lo que quieras, Robledo, pero Bola de Dragón ha tenido una mayor influencia en la sociedad española que Saint Seiya y por eso pasa a ser declarado manga oficial del estado."
    robledo "¡Mis pelotas me va a chupar el dragón! Los caballeros del zodiaco posee una historia más madura y proporciona elementos educativos a los jóvenes que..."
    enigma "¡Maricón!"
    robledo "¿Quién ha sido?"
    extend " ¿Has sido tú, Inocencio?"
    chapero "¿Yo? No, no..."
    robledo "Entonces, ¿has sido tú, Elena?"
    aleli "¿Qué te voy a llamar yo eso?"
    play sound "mazo.mp3"
    $ renpy.pause(1, hard=True)
    nabo "Basta ya."
    extend " No hay más que discutir. Pasemos al siguiente punto del día..."
    nabo "Ah, sí."
    extend " Resulta que en las elecciones generales ha habido un triple empate entre los siguientes candidatos:"
    nabo "M. Rajao, cabeza de lista del Partido Presidiario de Kanguelo: P.P.K."
    nabo "Ken Sanchez, líder del PRESOE."
    nabo "Y finalmente, El Coletas, que según pone en su ficha se representa a sí mismo, aunque como eso no es posible creó la marca: Queremos."
    enigma "¡Maricón!"
    nabo "A ver, Martínez, ¡cállate de una vez!"
    hide robledo
    show martinez at left:
        ypos 0.7
    martinez "Gracias por descubrirme, macho."
    hide nabo
    show robledo2 at right:
        ypos 0.7
    robledo "¡Me vas a comer el rabo, Martínez!"
    martinez "Pues lo que yo decía."
    robledo "Me voy a cagar en tu pu..."
    hide robledo2
    show nabo at right:
        ypos 0.7
    play sound "mazo.mp3"
    $ renpy.pause(1, hard=True)
    hide martinez with move
    #hide robledo 
    #show nabo at right:
    #    ypos 0.7
    nabo "Alguacil, acompañe a los jueces a la salida, haga el favor."
    show robledo at left:
        ypos 0.7
    robledo "Pero, ¿por qué?"
    nabo "¿Te parece poco el tiempo que me estás haciendo perder?"
    hide robledo
    show martinez at left:
        ypos 0.7
    martinez "Yo no he hecho nada."
    extend " ¿Me vas a echar tú de aquí?"
    martinez "¿Tú y cuántos maricones más?"
    nabo "..."
    hide martinez
    show robledo at left:
        ypos 0.7
    robledo "Va, prometo no abrir más la boca."
    hide robledo
    show martinez at left:
        ypos 0.7
    martinez "Yo tampoco pienso hacerlo."
    nabo "Está bien..."
    hide martinez
    show nabo at center:
        ypos 0.7
    with move
    nabo "Dios, ahora recuerdo por qué no nos reunimos más a menudo..."
    alcantara "Y porque no hay bar."
    nabo "También, es verdad."
    nabo "A lo que íbamos: triple empate, bla, bla, bla. ¿Alguien sabe lo que dice la Constitución al respecto?"
    cifuentes "¿Nada?"
    nabo "Hombre, algo dirá, digo yo. Por algo es nuestra magna carta, la base de nuestra democracia escrita del puño y letra de los padres de la patria libre y una."
    nabo "¿No hay ningún artículo que nos pueda servir de guía?"
    show nabo at right:
        ypos 0.7
    with move
    show bedel at left
    bedel "Su café, señor."
    nabo "Gracias."
    conrado "Yo es que me la leí hace mucho tiempo..."
    extend " Mi cabeza ya no es la de antes."
    heredia "Yo también tengo recuerdos difusos."
    nabo "A ver, ¿es que nadie se ha leído el peñazo ese?"
    martinez2 "Yo solo recuerdo el artículo que establece el derecho de disfrutar de las prostitutas gratis..."
    nabo "No te esfuerces, Martínez. Deja de disimular que aquí todos sabemos lo tuyo con el bedel desde que le diste con la maza hace seis años."
    hide bedel
    show nabo at center:
        ypos 0.7
    with move
    martinez2 "Eh... Yo..."
    nabo "Si te queremos igual. No te preocupes."
    cifuentes "Una vez expuesta la sexualidad de Martínez, ¿Nos podemos ir ya a casa?"
    nabo "No, hay que resolver el asunto este de las elecciones."
    nabo "En vista de que la Constitución no nos sirve de nada, quién lo iba a decir, tenemos que proponer otras soluciones."
    nabo "¿Sugerencias?"
    aleli "¿Y si hacemos un concurso de cupcakes?"
    robledo "¿Y quién sería el jurado?"
    aleli "Precisamente tengo un primo que tiene un buen paladar para estas cosas."
    robledo2 "¿Quién?"
    extend " ¿Tu primo Andresito?"
    extend " ¿Andresito el fanegas?"
    heredia "Por mí, de acuerdo."
    aleli "Ya le diré cómo le vas llamando por ahí. En la próxima barbacoa a ver si eres capaz de decírselo a la cara."
    nabo "No, eso no sería serio. ¿Con qué cara iban a mirarnos fuera?"
    heredia "Con mala cara, es cierto."
    nabo "Más sugerencias."
    conrado "A mí no se me ocurre nada."
    alcantara "¿Y si los llevamos a que canten en un programa de esos en los que un jurado expone sus defectos y los humilla en público para que estén mejor preparados a la hora de enfrentarse al mundo exterior?"
    aleli "En lugar de cantar podrían hacer cupcakes."
    robledo2 "Elena, hija, parece que estés preñada. Qué fijación con las magdalenas."
    aleli "¡Micromachista!"
    robledo2 "¿Qué?"
    nabo "A ver, que se hace tarde y quiero echarme la siesta."
    chapero "Podríamos echarlo a suertes. Que tiren una moneda al aire y listo."
    nabo "Imposible, son tres. Yo no pienso romperme la cabeza intentando emparejarlos para que ninguno se queje de que no le ganó el otro."
    nabo "A ver, tormenta de ideas. Id diciendo lo primero que se os pase por la cabeza."
    heredia "Ay, dios."
    aleli "Una guerra de cupcakes."
    alcantara "Un examen de conducción por la M-30."
    robledo2 "Concurso de eructos."
    martinez2 "Que se midan la chorra."
    conrado "Que lo hablen entre ellos."
    aleli "A ver quién es capaz de esnifar más cupcakes."
    martinez2 "Que se besen y el primero que despegue los labios pierde."
    heredia "Que se tiren por un puente y el que sobreviva gana."
    nabo "¡No!"
    extend " ¡No!"
    extend " ¡No!"
    nabo "¡Sois la verguenza de la profesión!"
    alcantara "Pues tú no has dicho ni mú."
    show nabo at right:
        ypos 0.7
    with move
    show bedel at left
    bedel "Si me permiten..."
    extend " Creo que tengo la solución."
    nabo "Adelante, ¿qué propones?"
    bedel "Si no he entendido mal, los candidatos sacaron el mismo número de votos."
    robledo2 "Eso ya se dijo antes. ¿Te metió Martínez la maza en el oído?"
    nabo "Robledo, a la próxima te quito el coche oficial."
    robledo2 "¡No, por favor! Si no cualquiera escucha a mi suegra."
    nabo "Continúa, chaval."
    bedel "La cuestión es: ¿Por qué no hacer una segunda vuelta?"
    nabo "Eso sería muy caro. Además, no tenemos tiempo. Dentro de nada es Navidad. Imagina las cenas de nochebuena sin las discusiones entre cuñados sobre los resultados."
    bedel "Sería una segunda vuelta especial. Solo durante un día, los candidatos tendrán que recorrer cinco ciudades españolas, solo cinco."
    bedel "Una vez allí deberán conseguir el mayor número de votos de los ciudadanos que se vayan encontrando."
    bedel "El que tenga más votos al final del día, será el ganador."
    nabo "Oye Martínez, muy bien tu chico, ¿eh?"
    martinez2 "Estoy muy orgulloso de tí, Gustavo."
    nabo "Queda un lazo suelto, ¿cómo controlar los votos que irán consiguiendo los candidatos?"
    nabo "Líbreme dios de dudar de la honorabilidad de los candidatos, pero hay que asegurarse de que se cumple la ley."
    bedel "Sería tan fácil como que les acompañe un ciudadano normal y corriente y certifique el resultado."
    martinez2 "¡Ole, tú!"
    martinez2 "¡Guapo!"
    nabo "A ver, Roberto, guarda la compostura."
    nabo "Muchas gracias Gustavo, has servido bien a la patria."
    bedel "Pues ya que lo dice, me vendría bien un aumento..."
    nabo "Eso háblalo con Martínez."
    hide bedel
    show nabo at center:
        ypos 0.7
    with move
    nabo "Bien, haremos lo que sugiere el ligue de Roberto."
    nabo "Se levanta la sesión."
    conrado "Menos mal, me estaba cagando y no podía aguantar más."
    play sound "mazo2.mp3"
    scene black with fade
    show texto3:
         ypos 0.5
         xpos 0.1
    $ renpy.pause(3, hard=True)
    
    #al día siguiente
    #se te ha convocado por medio de un sorteo
    scene diasiguiente with fade
    show nabo at center:
        ypos 0.7
    nabo "Se le ha convocado, Señor o Señora..."
    nabo "A todo esto,"
    $ jugador = renpy.input("¿Cómo se llama?")
    $ jugador = jugador.strip()  #elimina los espacios
    if not jugador:
        $jugador = "Payasete"   #Si el jugador no ingresa ningún nombre, se le asigna el de "Payasete"
        nabo "En vista de que es reacio a compartir con la plebe su nombre, le llamaré Payasete."
        $ nabo("¿Le parece bien?", interact=False)
        menu:
            "Por mi vale":
                nabo "Prosigamos."
            "No tiene usted verguenza":
                nabo "Se jode."
    #pov "Me llamo [jugador]"  Así se usa la variable del nombre
    pov "Pero, oiga, ¿no podía haber escogido un lugar mejor para reunirnos?"
    nabo "¿Qué tiene de malo este?"
    pov "Hombre, no sé si me ha convocado para ayudar al estado o para meterme un billete de 50 euros en el tanga para que le haga..."
    extend " cosas."
    nabo "Qué imaginación tiene usted, [jugador]."
    nabo "Deduzco que leyó la misiva que le entregaron esta mañana."
    pov "Deduce usted bien."
    nabo "¿Y bien? ¿Tiene algo que decir?"
    pov "Pues que no entiendo todo este rollo. " 
    extend "¿Por qué no repiten las elecciones dentro de unos meses y ya está?"
    nabo "..."
    pov "Al fin y al cabo, no hay prisa, ¿no?"
    pov "Quiero decir, si la economía está teledirigida desde Europa, hasta un mono podría tomar las riendas del país mientras tanto."
    pov "Nadie va a darse cuenta de que no hay nadie a los mandos."
    nabo "¿Cómo no se nos ocurrió antes?"
    pov "Creo que conozco la razón pero no quiero ir a la cárcel."
    nabo "No se hable más. Habrá nuevos comicios; antes de que comience el verano, que si no luego la gente con el calor se olvida de su deber democrático."
    nabo "Con suerte esta vez conseguiremos la mayoría absoluta."
    pov "¿?"
    nabo "Es que mi primo es del PACMA."
    pov "Venga, nos vemos."
    scene black with fade
    show texto4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with fade
    $ renpy.pause(3, hard=True)
    scene interior with fade
    show nabo at right:
        ypos 0.7
    nabo "¿Quién lo iba a decir?"
    extend " Otra vez en las mismas."
    nabo "Triple empate y sin posibilidad de pactos viables."
    nabo "Qué cansancio. Le tendría que haber hecho caso a mi madre y haber estudiado para registrador de la propiedad."
    martinez2 "¡Pero si eso es un nido de enchufados!"
    nabo "También es verdad."
    cifuentes "¿Y si volvemos al plan inicial? Porque otras elecciones no podemos permitirnos, estamos deforestando el país con tanta papeleta."
    chapero "No pasa nada, las revendemos a Venezuela y ya está. Allí creo que necesitan papel higiénico."
    conrado "Vale, pero estamos ya en unas fechas... Yo me voy pasado mañana a L´ampurdá."
    chapero "No me esperaba esto de ti, Neferio. Pudiendo disfrutar de tu asueto en la muy española Rioseco eliges dispensar tu dinero a los independentistas."
    conrado "Oye, que mi madre es de allí."
    nabo "¡Ya está bien! Siempre acabamos hablando de cualquier cosa menos de lo que toca."
    aleli "Yo sí que sé lo que le gusta que le toquen a Martinez."
    play sound "mazo.mp3"
    $ renpy.pause(2, hard=True)
    nabo "¡Ya basta! No habrá nuevas elecciones porque caerían en Navidad, y al pueblo le puedes robar el dinero de sus impuestos, negar el futuro a sus hijos y tomarlo por imbécil, pero jamás prohibas La Liga ni le prives de una fiesta. Se nos echarían al cuello."
    heredia "¿Qué se van a cabrear? ¿Tú has visto los resultados de las elecciones?"
    nabo "En cualquier caso no nos podemos arriesgar."
    nabo "Encima el plan del bedel no es factible porque no tenemos tanto tiempo para llevarlo a cabo. Los del Club Bilderberg se están impacientando. Dadme una solución inmediatamente o nos quedamos aquí todo el verano."
    chapero "Eso no te lo crees ni tú."
    nabo "¡Joder! Qué difícil me lo ponéis siempre..."
    robledo2 "¿Y por qué no llamamos al lumbreras al que se le ocurrió lo de repetir las elecciones?"
    nabo "¡Al fín alguien tiene una buena idea!"
    scene black with pixellate
    show texto5:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)
    scene interior with fade
    show nabo at center:
        ypos 0.7
    nabo "Me alegro de volverle a ver, [jugador]. Ya le habrán informado de los detalles mientras venía hacia acá. Iré al grano: "
    extend "¿qué hacemos?"
    nabo "Mientras le esperábamos hemos hecho un pequeño brainstorming. A ver si alguna de las siguientes le parece idónea."
    pov "¿Incluye alguna de ellas la posibilidad de que le den por saco a otro ciudadano?"
    nabo "No." 
    pov "Y si ya han tenido varias ideas, ¿para qué me llaman?"
    nabo "Para que escoja una."
    pov "¿Y por qué no hacen un sorteo y ejecutan la que salga?"
    nabo "Porque de lo contrario no habría novela visual."
    pov "Nadie lo lamentaría."
    nabo "Déjese de zarandajas y elija."
    hide nabo
    menu:
        "Concurso de Breakdance":
            show nabo at center:
                ypos 0.7
            nabo "Tendrían que montar los plenos del congreso en la UCI. Tienen todos un cuerpo-escombro..."
            pov "Entonces la Gymkana nacional."
        "Los metemos en Gran hermano":
            show nabo at center:
                ypos 0.7
            nabo "No lo veo."
            pov "Entonces la Gymkana nacional."
        "Gymkana nacional":
            show nabo at center:
                ypos 0.7
            nabo "Me gusta el nombre, pero no lo entiendo. Creo que lo propuso el Juez Chapero. Tendría que haberle preguntado."
            nabo "¿En qué consistiría?"
        "Concurso Mister Camiseta Mojada":
            show nabo at center:
                ypos 0.7
            nabo "Sería la única opción en la que no solo no habría un ganador, sino que perderíamos todos."
            pov "Entonces la Gymkana nacional."
    nabo "Veamos a quién se le ocurrió esto..."
    nabo "El juez... Pacheco... Supondré que es el juez Chapero. Durante la sesión estuvimos bebiendo un poco y creo que Chapero se pasó un poco con el Gintonic."
    pov "Seguro que ha sido un exceso de cardamomo."
    nabo "Será eso."
    nabo "A ver, ujier, ¡manden llamar al Juez Chapero!"
    nabo "..."
    chapero "Perdón por el retraso. No encontraba los pantalones."
    nabo "Aquí, [jugador] ha elegido tu propuesta de gymkana."
    extend " ¿En qué consiste?"
    chapero "No tengo ni la más remota idea. Escuché esa palabra en el Grand Prix hace algunos años y desde entonces he querido usarla en una conversación."
    nabo "De lo más profesional, Inocencio."
    chapero "Lo que tú quieras, pero acabo de tacharlo de mi lista de cosas que hacer antes de jubilarme a costa de los españoles."
    nabo "[jugador], ¿se te ocurre en qué podría consistir esa... gymkana?"
    pov "Mientras disertaban sobre la infabilidad de la autoridad civil, he estado repasando el plan anterior..."
    martinez2 "¡El bedel es mío! ¡Ni se te ocurra echarle el ojo!"
    pov "¡Para nada! Pero se puede aprovechar parte de lo que planteó."
    martinez2 "Y no es lo único aprovechable..."
    pov "Es muy sencillo: En lugar de que los candidatos vayan por la ciudad mendigando el voto de los ciudadanos, hacemos que recorran los gimnasios de distintas ciudades españolas en busca del voto de los dueños de los mismos." 
    pov "Solo tendrían que convencer a una persona por ciudad. Sería más rápido."
    pov "Cada jefe de gimnasio dará tres votos al candidato si este supera la prueba que le plantée. Una vez visitados los distintos gimnasios, se contarán los votos acumulados y el que tenga más, gana."
    robledo2 "Pero, ¿por qué los gimnasios?"
    pov "Porque son los ágoras del siglo XXI. El gimnasio es el lugar donde los prohombres del mañana acuden a cincelar sus músculos con complejos proteínicos de alta tecnología."
    pov "Todos miran hacia ellos con admiración. Sus dueños han ocupado el lugar antaño reservado a los héroes troyanos o los jugadores del Real Madrid."
    pov "Si los candidatos aseguran sus votos, podremos colegir que sus seguidores, que se cuentan por millones, también les votarían."
    pov "Para aprovechar algo del plan anterior, pongamos que solo haya que visitar 5 gimnasios."
    aleli "Mejor 6."
    nabo "¿Y por qué 6?"
    aleli "Porque es mi número de la suerte."
    martinez2 "Sí, el número de cupcakes que te desayunas todas las mañanas."
    aleli "Cierra el pico, julandrón."
    nabo "¡A callar todos! Esto no es la consulta de Rappel. Serán cinco ciudades. [jugador], tú serás responsable de acompañar a uno de los candidatos."
    pov "¿Yo? No sé para qué digo nada..."
    nabo "¿No te enseñó tu padre que en la mili no abras la boca ni para comer natillas?"
    pov "En mi época ya estaba instaurado el ejército profesional."
    cifuentes "Así estáis, confiando en un sistema amañado para que se resuelvan vuestros problemas mientras los de siempre disfrutan de una extraordinaria placidez para hipotecar vuestras vidas."
    nabo "¡Cifuentes! Te he dicho mil veces que no escuches a Amaral."
    cifuentes "¡Somos demasiados y no podrán parar...!"
    nabo "Borrachos están insoportables."
    play sound "mazo.mp3"
    $ renpy.pause(2, hard=True)
    nabo "No se hable más. Soy magnánimo y por eso solo tendás que acompañar a uno, [jugador]. De los demás se encargarán el juez Chapero y el juez Conrado."
    conrado "Pero... ¡L´ampurdá!"
    nabo "Venga, que no estamos en temporada. Alli hay que ir en invierno. Además, tu madre no soporta a tu mujer, eso que le quitas de encima."
    nabo "¡Que entre la pantalla de selección del candidato!"
    
    
    
    #Selección de jugadores
    play music "pantallaseleccion.mp3" 
    $ result = renpy.imagemap("pantallaseleccion.jpg", "pantallaseleccion2.jpg", [
        (60, 124, 414, 766, "coletas"),  #coordenadas para los boliches, etc
        (486, 131, 871, 766, "ken"), 
        (962, 142, 1317, 766, "mariano"),
        ], focus="imagemap")
    
    if result == "coletas":
        scene pantallaseleccion
        $ coletas = True
        stop music
        play sound "elcoletas.mp3"
        $ renpy.pause(8, hard=True) 
        #presentacion del coletas
        scene black with dissolve
        show textoqueremos1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show textoqueremos2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene queremoshq with fade
        stalin "Saludos, Camarada [jugador]."
        pov "Propicios días, camarada."
        stalin "No desperdiciemos el tiempo en conveniencias burguesas. Voy a buscar al Coletas. Espere aquí."
        stalin "Ah, y no mire al cuadro que tiene a su derecha."
        stalin "Y si por un casual lo hace, recuerde que es normal que los ojos del jinete parezca que le siguen."
        pov "Me pasa mucho en casa de mi abuela."
        stalin "Su abuela debe de ser una excelente miembro del partido."
        stalin "CAMARADA COLETAS, EL PUEBLO LE RECLAMA."
        pov "Creía que iba a ir a buscarle."
        stalin "Es que la ciatica me está matando."
        c "Hombre, si es [jugador]. ¿Cómo estás?"
        c "Oye, que bonito está tu gato. ¿Qué le das de comer?"
        pov "¿Cómo sabe que tengo gato?"
        stalin "Lo hemos mirado en el Facebook. Ay si se hubiera inventado antes..."
        c "Perdona el retraso. Estaba terminando una partida de Colonos de Catán con Errejota y Menchenique. No dejaban que me marchara. Si llego a ir ganando yo seguro que se hubieran negado a seguir."
        pov "No pasa nada, pero creo que deberíamos ir yéndonos ya. Se hace tarde."
        c "Tienes razón, como buen comunista que eres."
        pov "Oye, que yo..."
        c "A ver si El Rulas nos puede llevar en su buga."
        pov "¿Se sigue diciendo buga a estas alturas de la película?"
        c "Si salgo de presidente, sí."
        c "¿Te vienes, Staline?"
        stalin "Por nada del mundo me perdería la posibilidad de un viaje gratis."
        jump mapa  
        
    if result == "mariano":
        scene pantallaseleccion
        $ mrajao = True
        stop music
        play sound "mrajao.mp3"
        $ renpy.pause(5, hard=True) 
        #presentacion de rajao
        scene black with dissolve
        show textomoncloa1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show textomoncloa2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene ppkhq with fade
        montoto "Buenas tardes. Tú debes de ser [jugador], ¿verdad?"
        pov "El mismo. ¿Qué tal todo por aquí?"
        montoto "Bien, bien. Soy Montoto, asistente personal de M. Rajao. Os acompañaré durante el viaje para darle consejo y paz espiritual."
        extend " Permítame presentarle a nuestro presidente."
        r "Hombre, un repartidor nuevo. ¿Me trae el pelapuros que compré en el Internet ayer?"
        montoto "Se equivoca, jefe. Es nuestro acompañante en el asunto de la Gymkana Nacional."
        r "¡Acabáramos! "
        extend "Perdóneme, joven. Es que no estoy acostumbrado a tratar con pobres. "
        r "Ya decía yo que muy poco habían tardado..."
        extend "Pero permítame que me presente: "
        r "Me llamo M. Rajao, líder de la organización criminal Sobreloo y del P.P.K."
        r "..."
        r "Lo he vuelto a decir, ¿verdad?"
        montoto "Eso me temo."
        pov "¿El qué?"
        r "Lo de la organización criminal. No me hagas caso, son tonterías. De pequeño jugaba a rol y me gustaba interpretar el papel de capo de la mafia."
        montoto "Gracias a dios que la gente de este país no lee."
        pov "En fin, Mucho gusto."
        pov "Oiga, una pregunta le quería hacer: ¿usar este edificio es legal?"
        r "Ah, pues no sé. ¿Importa acaso?"
        montoto "Si se me permite interrumpir, creo que sería mejor ponernos en camino. Tenemos que visitar muchas ciudades."
        r "De acuerdo. Usaré la litera portada por esclavos."
        montoto "Eso es muy lento, no llegariamos nunca al primer gimnasio."
        r "¿Y el Rolls Royce de Hitler?"
        montoto "En el taller."
        r "Pues nada, tendremos que apañarnos con la limusina de la organización."
        jump mapa
        
    if result == "ken":
        scene pantallaseleccion
        $ ken = True
        stop music
        play sound "kensanchez.mp3"
        $ renpy.pause(6, hard=True) 
        scene black with dissolve
        show textopresoe1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(0.5, hard=True)
        show textopresoe2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene presoehq with fade
        espejo "Hola compañero/a [jugador]. "
        extend "¿Te fue sencillo encontrar el camino hasta nuestra sede?"
        pov "Sí, le pregunté a mi portera y me dijo cómo llegar. Es clienta asidua."
        espejo "Siempre nos recomiendan."
        espejo "Sé lo que estás pensando: ¿Cuándo voy a conocer al faro del socialismo en Europa?"
        pov "Justo eso."
        espejo "No te voy a hacer sufrir más. Helo aquí: "
        k "Ken Sánchez is in da house, bitch!"
        espejo "Mi caramelín, te dije que el rollo Snoop Dogg era solo con los consumidores de drogas derivadas de la botánica que se reunen en el parque de enfrente."
        k "Lo siento, yo. Es que este señor/a parece muy joven."
        pov "¿Gracias?"
        k "Las que tú tienes. Pero no estamos aquí para flirtear. Permíteme que me presente: "
        k "Ken Sánchez, socialista, estilista de las estrellas, alternativa responsable. "
        k "Hubiera sido Mister España si no fuera porque Pablo Iglesias votó en contra."
        pov "¿Quién?"
        espejo "Nada, no le hagas caso. Creo que es mejor que nos pongamos en marcha."
        k "Creo bien. Es hora de partir. Iré a lomos de la ilusion y la esperanza de los españoles y las españolas."
        espejo "Pero necesitamos algo más práctico, hermoso mío. Además, no cabríamos todos. Recuerda: "
        extend "What would Felipe do?"
        k "¿Te refieres a lo del Gal?"
        espejo "¿De qué estás hablando, bellezón? " 
        extend "No, él alquilaría un coche, a cuenta del partido, claro."
        k "Eso haremos, sí. No sé qué haría sin mi."
        espejo "Languidecer en la oposición."
        jump mapa
        
    
    return
