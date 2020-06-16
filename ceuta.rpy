label ceuta:
    $ ceuta = True
    #personajes
    define binladen = Character("Pin Laden", color="#8B591C", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define moro = Character("Máquina de Amar", color="#755A39", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image btext2 = anim.Blink(Text("¡Tres votos!", color="#ff0", size=76))
    
    image gymceuta = "images/gymceuta.jpg"
    image ceuta1 = "images/ceuta1.jpg"
    image ceuta2 = "images/ceuta2.jpg"
    
    
    image cuñadoceuta = "images/pinladen.png"
    image moro = "images/moro.gif"
    
    image bomba = "images/bomba.jpg"
    image gymtextta1 = Text("{size=40}Gimnasio World Class",color="#fff", text_align=0.3)
    image gymtextta2 = Text("{size=40}Recientemente adquirido por King Africa",color="#fff", text_align=0.3)
    scene travelceuta at Pan((0, 0), (300,0), 20.0)
    play music "entradillaceuta.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "zulu.mp3"
    
    if mrajao == True:
        scene ceuta1 with fade
        $ renpy.pause(0.6,hard=True)
        r "África... el continente madre."
        pov "Técnicamente es Europa."
        r "Pero está en el continente africano, ¿no? Luego es África."
        r "¿Acaso es la Guyana Francesa, Europa?"
        pov "Técnicamente..."
        r "Ticniciminti, ticniciminti..."
        extend " Técnicamente yo podría ser el jefe de tu padre."
        $ nacimiento = renpy.input("¿Dónde naciste?")
        r "Pues por [nacimiento] estuve en aquella época como ayudante de campaña de Arias Navarro. Igual tu padre me traía el carajillo de las mañanas."
        pov "..."
        r "No me mires así. Pudo pasar."
        pov "Que yo sepa no le he dicho en qué año nací."
        r "Ni me importa. Dejémonos de tonterías y vayamos al gimnasio que tengo demasiado dinero encima como para estar en estas calles de infieles mahomet..."
        show roboto at right with moveinright
        roboto "Perdona pero no quiero que me corten la cabeza por un juego al que apenas van a jugar cuatro gatos. Nada de referencias al islam. ¿Está claro?"
        r "No dire nada."
        hide roboto with moveoutbottom
        r "Qué, ¿vamos al bar a tomarnos una tapa de jamón?"
        scene ceuta2 with wipedown
        $ renpy.pause(1, hard=True)
        r "Esto es increible."
        r "No hay una sola indicación en español. Montoto, ¿aquí no se obliga a los niños a hablar en español?"
        montoto "Por obligarse, se obliga."
        r "¿Y entonces por qué no hablan el idioma?"
        montoto "Se ve que el lenguaje de las armas está más extendido."
        pov "Eso es de Tu Pac, ¿no?"
        r "Y nosotros aquí sin un tirachinas con el que defendernos."
        montoto "Tranquilo, Presidente. En cuanto caiga la noche no tendrá que preocuparse."
        r "Pues ya me dirás qué hacemos mientras tanto. Mira, ¡ahí viene un moro!"
        show moro at center with moveinleft
        montoto "Saludos, señor moro."
        moro "Jau! Yo no ser moro, ser \"Máquina de amar\", de la tribu de los Pies Negros."
        pov "¿Qué hace un nativo americano tan lejos de su hogar?"
        moro "Como tú saber por película de Kevin Costner, el hombre blanco nos encerró en nuestras reservas donde hemos languidecido, sumergidos en alcohol y juegos de azar. Yo querer algo más para mi familia, así que venir a Europa, la tierra de las oportunidades."
        moro "Saltar la valla ayer junto con el campeón olímpico de salto con pértiga de Gabón. Buena gente. Le huele el aliento."
        moro "Yo esperar obtener puesto en un ayuntamiento. Concejal de turismo, ser mi mayor sueño."
        r "¿Te lo quieres comer?"
        montoto "Si acabas de llegar no sabrás entonces dónde queda el gimnasio."
        moro "Claro que saber. Cuando estar fuera de tu zona de confort, tener que dominar el entorno o sufrir en el intento."
        moro "No gustar sufrir."
        moro "Girar a la derecha en la mezquita, luego a la izquierda en tiroteo de narcotraficantes y todo recto. Llegar fácilmente."
        pov "Agradecido."
        moro "Emocionado por haberles podido ayudar. ¿Creer que dar puntos para solicitud de trabajo?"
        pov "No tengo ni idea."
        moro "No importar, yo camelarme a funcionaria con graves carencias sentimentales."
        scene black with fade
        $ renpy.pause(0.5, hard=True)
        stop music
        creador "¡Hola! Perdona que te interrumpa. Soy el creador."
        creador "No el creador de todo, solo de este juego. Te he estado observando un rato y..."
        extend " mira, que tu cara lo dice todo y no quiero que lo pases mal, así a lo tonto..."
        creador "Te doy la oportunidad de poner fin a la experiencia y salir con las mismas neuronas con las que comenzaste a jugar, aunque con menos tiempo para descargarte videos de Xhamster, o de continuar jugando..."
        creador "Tuya es la decisión."
        menu:
            "¡Quiero salir de aquí":
                $ renpy.play("error.wav")
                scene pantalla
                $ renpy.pause(2.5)
                creador "JAJAJAJA. Es todo mentira."
                creador "¡De aquí no se va nadie!"
                creador "Vuelve a la historia..."
                creador "¡AHORA!"
        
            "¿Bromeas? Llevo años esperando este juego. Quiero seguir hasta el final.":
                creador "Oh... ¡Muchas gracias! No esperaba que te fuera a gustar esto..."
                creador "Oye, ya que te gusta el juego, infiero que yo también te molo."
                extend " ¿Me enviarías una fototetas?"
                menu:
                    "¡No!":
                        creador "Lo esperaba, no te creas. Yo siempre lo digo: put your fototetas where your mouth is (or will be tomorrow night after an expensive dinner and a couple of bottles of wine) pero ya no hay ética entre los jugadores así que..."
                        creador "Puedes seguir jugando, pero piensa que mientras disfrutas con mi creación, estoy llorando en un rincón mientras intento excitarme viendo antiguas fotos de Terelu."
                        creador "¡Por tu culpa!"
                    "Solo porque eres tú":
                        creador "Jo, no puedo ser más afortunado. Me la enviarás de verdad, ¿no? Mi dirección de correo es: veranodeldescontento@gmail.com"
                        creador "Si no me la envías, que sepas que el karma puede que te la devuelva, que una mañana te despiertes y entre los mensajes privados de WA lleno de fotopollas no socilitadas."
                        creador "¡Disfruta del juego!"

        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextta1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextta2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymceuta with fade
        show cuñadoceuta at center
        r "¡Hola!"
        binladen "Salam Aleikum."
        r "Aleikum Salam."
        binladen "¿Qué te trae por estos lugares?"
        extend " No se suelen ver muchos cristianos por estas tierras."
        r "Claro, sois más del Barça, ¿no? Venimos a pedir tu voto para gobernar con buen orden este país."
        binladen "Ah, mi voto. Pena no querer mi bota. Yo hacer buen precio. Solo 40 euros. Ser auténtica piel de demócrata."
        binladen "Tú tener mi voto si hacerme un favor."
        r "Claro, lo que sea."
        binladen "Tú dar a mi primo Omar, residente en Barcelona este paquete, no bomba ¿eh? Paquete inofensivo. Solo ingredientes para shawarma. Ya saber: leche, cacao, avellana y harina."
        if barcelona ==True:
            r "Lo sentimos, amigo, pero ya hemos estado allí y no nos da tiempo de volver."
            binladen "Oh, gran pena sentir Laden..."
        else:
            montoto "Presidente, piénsalo. No sabemos cómo se tomarán nuestros rivales el que ayudemos a un..."
            $ r ("¿Tú que dices [jugador]", interact=False)
            menu:
                "Ayudemos a este pobre hombre":
                    $ enta = True
                    $ puntosj +=3
                    binladen "Oh, yo estar tremendamente agradecido."
                    binladen "Que Alá te bendiga con un Toyota repleto de libios."
                    montoto "Por lo pronto con tus votos nos conformamos."
                    binladen "Delo por hecho."
                    r "Hasta la vista, Señor Laden."
                    jump mapa
                "Ni de coña llevo yo ese paquete":
                    binladen "En fin, yo entender. Ser difícil encontrar buenos mensajeros hoy día."
                    r "Aun así nos gustaría que nos diera su voto."
            
        binladen "Oye, una última cosa antes de marchar... que si me puedes echar una mano desarmando una bomba."
        pov "¿Pero no decía que...?"
        binladen "¿Qué esperar? Yo vender alfombra de pelo de rata a precio de platino. Culpa tuya por ser tonto."
        scene bomba
        r "Por lo que se ve en el contador, tenemos tiempo ¿no?"
        binladen "No fiar, yo comprar en Aliexpress."
        montoto "Tendremos que cortar un cable para que no estalle."
        pov "A ver cuál elegimos..."
        $ result = renpy.imagemap("images/bomba.jpg", "images/bomba2.jpg", [
            (194, 395, 241, 580, "psoe"),  
            (439, 392, 509, 581, "pp"),
            (837, 390, 952, 577, "ciudadanos"),
            (1086, 392, 1225, 577, "podemos"),
            ], focus="imagemap")
        
        if result == "pp":
            scene gymceuta with fade  
            show cuñadoceuta at center
            binladen "¡Lo has logrado!"
            extend " Loado sea el altísimo."
            binladen "Puedes marchar en paz. Tendrás mi voto llegado el momento."
            r "Muchas gracias, caballero. Es un placer cooperar con gente como usted."
            pov "En marcha pues."
            $ puntosj += 3
            hide cuñadoceuta
            show btext2:
                ypos 0.3
                xpos 0.3
            $ renpy.pause(2,hard=True)
        if result == "psoe":
            binladen "Eso no ha servido de nada. La bomba estallará por tu culpa."
            scene gymceuta with fade
            show cuñadoceuta at center
            r "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            montoto "Será mejor que nos alejemos de aquí a no mucho tardar, Presidente."
            pov "Nos vamos de vacío, entonces."
            r "No diga eso. Hemos hecho un amigo. Eso ya es mucho."

        if result == "ciudadanos":
            binladen "Es como si hubieras cortado una relación con tu ex. Irrelevante."
            scene gymceuta with fade
            show cuñadoceuta at center
            r "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            montoto "Será mejor que nos alejemos de aquí a no mucho tardar, presidente."
            pov "Nos vamos de vacío, entonces."
            r "No diga eso. Hemos hecho un amigo. Eso ya es mucho."
            
        if result == "podemos":
            binladen "Eso no ha servido de nada. La bomba estallará por tu culpa."
            scene gymceuta with fade
            show cuñadoceuta at center
            r "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            montoto "Será mejor que nos alejemos de aquí a no mucho tardar, presidente."
            pov "Nos vamos de vacío, entonces."
            r "No diga eso. Hemos hecho un amigo. Eso ya es mucho."
        
    if ken == True:
        
        scene ceuta1 with fade
        $ renpy.pause(0.5, hard=True)
        k "África... el continente madre."
        pov "Técnicamente es Europa."
        k "Pero está en el continente africano, ¿no? Luego es África."
        k "¿Acaso es la Guyana Francesa, Europa?"
        pov "Técnicamente..."
        k "Ticniciminti, ticniciminti..."
        extend " Técnicamente yo podría ser tu padre."
        $ nacimiento = renpy.input("¿Dónde naciste?")
        k "Pues por [nacimiento] estuve hace unos años como ayudante de campaña de Calvo Sotelo. Igual me trinqué a tu madre."
        pov "..."
        k "No me mires así. Pudo pasar. ¿Por qué crees que Sánchez es un apellido tan común?"
        espejo "Creo que aquí no encontrarás a nadie con ese apellido."
        k "Nunca se sabe. Estuve pegando carteles de Suarez en Marbella durante el verano. El rey de Arabia Saudí tenía una sirvienta llamada Aisha. Por las noches nos escapábamos y mientras ella me leía el Corán yo le com..."
        show roboto at right with moveinright
        roboto "Perdona pero no quiero que me corten la cabeza por un juego al que apenas van a jugar cuatro gatos. Nada de referencias al islam. ¿Está claro?"
        k "No dire nada."
        hide roboto with moveoutbottom
        k "Qué, ¿vamos al bar a tomarnos una tapa de jamón?"
        scene ceuta2 with wipedown
        $ renpy.pause(1, hard=True)
        k "Esto es increible."
        k "No hay una sola indicación... Esto me recuerda a aquella vez en que me perdí en los USA yendo a aquella universidad. Menos mal que apareció Obama en moto y me indicó el camino."
        k "El dios socialista nos sonríe. Por ahí viene un señor moro, los Obama de España. Viene a pie, pero seguro que es de ayuda."
        show moro at center with moveinleft
        k "Saludos, señor moro."
        moro "Jau! Yo no ser moro, ser \"Máquina de amar\", de la tribu de los Pies Negros."
        pov "¿Qué hace un nativo americano tan lejos de su hogar?"
        moro "Como tú saber por película de Kevin Costner, el hombre blanco nos encerró en nuestras reservas donde hemos languidecido, sumergidos en alcohol y juegos de azar. Yo querer algo más para mi familia, así que venir a Europa, la tierra de las oportunidades."
        moro "Saltar la valla ayer junto con el campeón olímpico de salto con pértiga de Gabón. Buena gente. Le huele el aliento."
        moro "Yo esperar obtener puesto en un ayuntamiento. Concejal de turismo, ser mi mayor sueño."
        k "¿Te lo quieres comer?"
        espejo "Si acabas de llegar no sabrás entonces dónde queda el gimnasio."
        moro "Claro que saber. Cuando estar fuera de tu zona de confort, tener que dominar el entorno o sufrir en el intento."
        moro "No gustar sufrir."
        moro "Girar a la derecha en la mezquita, luego a la izquierda en tiroteo de narcotraficantes y todo recto. Llegar fácilmente."
        pov "Agradecido."
        moro "Emocionado por haberles podido ayudar. ¿Creer que dar puntos para solicitud de trabajo?"
        pov "No tengo ni idea."
        moro "No importar, yo camelarme a funcionaria con graves carencias sentimentales."
        scene black with wipeleft
        $ renpy.pause(0.5, hard=True)
        show gymtextta1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextta2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymceuta with fade
        show cuñadoceuta at center
        k "Hola"
        binladen "Salam Aleikum."
        k "Aleikum Salam."
        k "¿Nos hemos visto antes?"
        binladen "Mmm, ¿tú estar en comunión de mi sobrina Tatiana?"
        k "Siento decir que no."
        binladen "¿En la graduación de mi nieta Carlota?"
        k "Tampoco."
        binladen "Pues entonces ser coincidencia."
        k "Si, supongo que es eso."
        binladen "¿Qué te trae por estos lugares?"
        extend " No se suelen ver muchos cristianos por estas tierras."
        k "Claro, sois más del Barça, ¿no? Venimos a pedir tu voto para gobernar con buen orden este país."
        binladen "Ah, mi voto. Pena no querer mi bota. Yo hacer buen precio. Solo 40 euros. Ser auténtica piel de demócrata."
        binladen "Tú tener mi voto si hacerme un favor."
        k "Claro, lo que sea."
        binladen "Tú dar a mi primo Omar, residente en Barcelona este paquete, no bomba ¿eh? Paquete inofensivo. Solo ingredientes para shawarma. Ya saber: leche, cacao, avellana y harina."
        if barcelona ==True:
            k "Lo sentimos, amigo, pero ya hemos estado allí y no nos da tiempo de volver."
            binladen "Oh, gran pena sentir Laden..."
        else:
            espejo "Regalo de los cielos, piénsalo. No sabemos cómo se tomarán nuestros rivales el que ayudemos a un..."
            $ k ("¿Tú que dices [jugador]", interact=False)
            menu:
                "Ayudemos a este pobre hombre":
                    $ enta = True
                    $ puntosj +=3
                    binladen "Oh, yo estar tremendamente agradecido."
                    binladen "Que Alá te bendiga con un Toyota repleto de libios."
                    espejo "Por lo pronto con tus votos nos conformamos."
                    binladen "Delo por hecho."
                    k "Hasta la vista, Señor Laden."
                    jump mapa
                "Ni de coña llevo yo ese paquete":
                    binladen "En fin, yo entender. Ser difícil encontrar buenos mensajeros hoy día."
                    k "Aun así nos gustaría que nos diera su voto."
            
        binladen "Oye, una última cosa antes de marchar... que si me puedes echar una mano desarmando una bomba."
        pov "¿Pero no decía que...?"
        binladen "¿Qué esperar? Yo vender alfombra de pelo de rata a precio de platino. Culpa tuya por ser tonto."
        scene bomba
        k "Por lo que se ve en el contador, tenemos tiempo ¿no?"
        binladen "No fiar, yo comprar en Aliexpress."
        espejo "Tendremos que cortar un cable para que no estalle."
        pov "Pues a ver cual elegimos..."
        $ result = renpy.imagemap("images/bomba.jpg", "images/bomba2.jpg", [
            (194, 395, 241, 580, "psoe"),  #coordenadas para los boliches, etc
            (439, 392, 509, 581, "pp"),
            (837, 390, 952, 577, "ciudadanos"),
            (1086, 392, 1225, 577, "podemos"),
            ], focus="imagemap")
        
        if result == "pp":
            binladen "Eso no ha servido de nada. La bomba estallará por tu culpa."
            scene gymceuta with fade
            show cuñadoceuta at center
            k "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            espejo "Será mejor que nos alejemos de aquí a no mucho tardar, mi bombero."
            pov "Nos vamos de vacío, entonces."
            k "No digas eso. Hemos hecho un amigo. Eso ya es mucho."
        if result == "psoe":
            scene gymceuta with fade  
            show cuñadoceuta at center
            binladen "¡Lo has logrado!"
            extend " Loado sea el altísimo."
            binladen "Puedes marchar en paz. Tendrás mi voto llegado el momento."
            k "Muchas gracias, caballero. Es un placer cooperar con gente como usted."
            pov "En marcha pues."
            $ puntosj += 3
            hide cuñadoceuta
            show btext2:
                ypos 0.3
                xpos 0.3
            $ renpy.pause(2,hard=True)
        if result == "ciudadanos":
            binladen "Es como si hubieras cortado una relación con tu ex. Irrelevante."
            scene gymceuta with fade
            show cuñadoceuta at center
            k "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            espejo "Será mejor que nos alejemos de aquí a no mucho tardar, mi bombero."
            pov "Nos vamos de vacío, entonces."
            k "No digas eso. Hemos hecho un amigo. Eso ya es mucho."
        if result == "podemos":
            binladen "Eso no ha servido de nada. La bomba estallará por tu culpa."
            scene gymceuta with fade
            show cuñadoceuta at center
            k "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            espejo "Será mejor que nos alejemos de aquí a no mucho tardar, mi bombero."
            pov "Nos vamos de vacío, entonces."
            k "No digas eso. Hemos hecho un amigo. Eso ya es mucho."
        
    if coletas == True:
 
        scene ceuta1 with fade
        $ renpy.pause(1, hard=True)
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
                
        c "África... el continente madre."
        stalin "Qué recuerdos de mis alumnos de la Universidad Patrice Lumumba..."
        stalin "No me escriben ni nada. Les di la mejor educación marxista posible y cuando regresaron a sus paises se encerraron en sus mansiones, rodeados de oro y se olvidaron del pobre Staline."
        pov "Creo que voy a llorar."
        c "Me siento como Juan Echanove en \"Bajarse al moro\"."
        pov "¿Por algo en especial?"
        c "No, era por hacer la referencia cultureta. Tengo una imagen que mantener."
        scene ceuta2 with wipedown
        $ renpy.pause(0.6, hard=True)
        show moro at center with moveinleft
        c "Salam Aleikum, hermano."
        moro "Jau! Yo ser Máquina de amar, de la tribu de los Pies Negros."
        pov "¿Qué hace un nativo americano tan lejos de su hogar?"
        moro "Como tú saber por película de Kevin Costner, el hombre blanco nos encerró en nuestras reservas donde hemos languidecido, sumergidos en alcohol y juegos de azar. Yo querer algo más para mi familia, así que venir a Europa, la tierra de las oportunidades."
        moro "Saltar la valla ayer junto con el campeón olímpico de salto con pértiga de Gabón. Buena gente. Le huele el aliento."
        moro "Yo esperar obtener puesto en un ayuntamiento. Concejal de turismo, ser mi mayor sueño."
        stalin "Si acabas de llegar no sabrás entonces dónde queda el gimnasio."
        moro "Claro que saber. Cuando estar fuera de tu zona de confort, tener que dominar el entorno o sufrir en el intento."
        moro "No gustar sufrir."
        moro "Girar a la derecha en la mezquita, luego a la izquierda en tiroteo de narcotraficantes y todo recto. Llegar fácilmente."
        
        scene black with fade
        stop music
        creador "¡Hola! Perdona que te interrumpa. Soy el creador."
        creador "No el creador de todo, solo de este juego. Te he estado observando un rato y..."
        extend " mira, que tu cara lo dice todo y no quiero que lo pases mal, así a lo tonto..."
        creador "Te doy la oportunidad de poner fin a la experiencia y salir con las mismas neuronas con las que comenzaste a jugar, aunque con menos tiempo para descargarte videos de Xhamster, o de continuar jugando..."
        creador "Tuya es la decisión."
        menu:
            "¡Quiero salir de aquí":
                $ renpy.play("error.wav")
                scene pantalla
                $ renpy.pause(2.5)
                creador "JAJAJAJA. Es todo mentira."
                creador "¡De aquí no se va nadie!"
                creador "Vuelve a la historia..."
                creador "¡AHORA!"
        
            "¿Bromeas? Llevo años esperando este juego. Quiero seguir hasta el final.":
                creador "Oh... ¡Muchas gracias! No esperaba que te fuera a gustar esto..."
                creador "Oye, ya que te gusta el juego, infiero que yo también te molo."
                extend " ¿Me enviarías una fototetas?"
                menu:
                    "¡No!":
                        creador "Lo esperaba, no te creas. Yo siempre lo digo: put your fototetas where your mouth is (or will be tomorrow night after an expensive dinner and a couple of bottles of wine) pero ya no hay ética entre los jugadores así que..."
                        creador "Puedes seguir jugando, pero piensa que mientras disfrutas con mi creación, estoy llorando en un rincón mientras intento excitarme viendo antiguas fotos de Terelu."
                        creador "¡Por tu culpa!"
                    "Solo porque eres tú":
                        creador "Jo, no puedo ser más afortunado. Me la enviarás de verdad, ¿no? Mi dirección de correo es: veranodeldescontento@gmail.com"
                        creador "Si no me la envías, que sepas que el karma puede que te la devuelva, que una mañana te despiertes y entre los mensajes privados de WA lleno de fotopollas no socilitadas."
                        creador "¡Disfruta del juego!"
        

        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextta1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextta2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymceuta with fade  
        $ renpy.pause(0.4, hard=True)
        show cuñadoceuta at center
        c "Salam Aleikum"
        binladen "Aleikum Salam."
        extend " ¿Qué te trae por estos lugares?"
        extend " No se suelen ver muchos cristianos en estas tierras."
        c "Claro, sois más del Barça, ¿no? Venimos a pedir tu voto para gobernar con buen orden este país."
        binladen "Ah, mi voto. Pena no querer mi bota. Yo hacer buen precio. Solo 40 euros. Ser auténtica piel de demócrata."
        binladen "Tú tener mi voto si hacerme un favor."
        c "Claro, lo que sea."
        binladen "Tú dar a mi primo Omar, residente en Barcelona este paquete, no bomba ¿eh? Paquete inofensivo. Solo ingredientes para shawarma. Ya saber: leche, cacao, avellana y harina."
        if barcelona ==True:
            c "Lo sentimos, amigo, pero ya hemos estado allí y no nos da tiempo de volver."
            binladen "Oh, gran pena sentir Laden..."
        else:
            stalin "Camarada, piénsalo. No sabemos cómo se tomarán nuestros rivales el que ayudemos a un..."
            $ c ("¿Tú que dices [jugador]", interact=False)
            menu:
                "Ayudemos a este pobre hombre":
                    $ enta = True
                    $ puntosj +=3
                    binladen "Oh, yo estar tremendamente agradecido."
                    binladen "Que Alá te bendiga con un Toyota repleto de libios."
                    stalin "Por lo pronto con tus votos nos conformamos."
                    binladen "Delo por hecho."
                    c "Hasta la vista, Señor Laden."
                    jump mapa
                "Ni de coña llevo yo ese paquete":
                    binladen "En fin, yo entender. Ser difícil encontrar buenos mensajeros hoy día."
                    c "Aun así nos gustaría que nos diera su voto."
            
        binladen "Oye, una última cosa antes de marchar... que si me puedes echar una mano desarmando una bomba."
        pov "¿Pero no decía que...?"
        binladen "¿Qué esperar? Yo vender alfombra de pelo de rata a precio de platino. Culpa tuya por ser tonto."
        scene bomba
        c "Por lo que se ve en el contador, tenemos tiempo ¿no?"
        binladen "No fiar, yo comprar en Aliexpress."
        stalin "Tendremos que cortar un cable para que no estalle."
        pov "Pues a ver cuál elegimos..."
        $ result = renpy.imagemap("images/bomba.jpg", "images/bomba2.jpg", [
            (194, 395, 241, 580, "psoe"),  #coordenadas para los boliches, etc
            (439, 392, 509, 581, "pp"),
            (837, 390, 952, 577, "ciudadanos"),
            (1086, 392, 1225, 577, "podemos"),
            ], focus="imagemap")
        
        if result == "pp":
            binladen "Eso no ha servido de nada. La bomba estallará por tu culpa."
            scene gymceuta with fade
            show cuñadoceuta at center
            c "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            stalin "Será mejor que nos alejemos de aquí a no mucho tardar."
            pov "Nos vamos de vacío, entonces."
            c "No digas eso. Hemos hecho un amigo. Eso ya es mucho."
        if result == "psoe":
            binladen "Eso no ha servido de nada. La bomba estallará por tu culpa."
            scene gymceuta with fade
            show cuñadoceuta at center
            c "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            stalin "Será mejor que nos alejemos de aquí a no mucho tardar."
            pov "Nos vamos de vacío, entonces."
            c "No digas eso. Hemos hecho un amigo. Eso ya es mucho."
        if result == "ciudadanos":
            binladen "Es como si hubieras cortado una relación con tu ex. Irrelevante."
            scene gymceuta with fade
            show cuñadoceuta at center
            c "¿Y ahora qué hacemos?"
            binladen "No sé ustedes pero yo correr a la frontera antes de que esto estalle."
            stalin "Será mejor que nos alejemos de aquí a no mucho tardar."
            pov "Nos vamos de vacío, entonces."
            c "No digas eso. Hemos hecho un amigo. Eso ya es mucho."
        if result == "podemos":
            scene gymceuta with fade  
            show cuñadoceuta at center
            binladen "¡Lo has logrado!"
            extend " Loado sea el altísimo."
            binladen "Puedes marchar en paz. Tendrás mi voto llegado el momento."
            c "Muchas gracias, caballero. Es un placer cooperar con gente como usted."
            pov "En marcha pues."
            $ puntosj += 3
            hide cuñadoceuta
            show btext2:
                ypos 0.3
                xpos 0.3
            $ renpy.pause(2,hard=True)
    jump mapa