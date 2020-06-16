label tenerife:
    $ tenerife = True
    $ ingredientes = 0
    $ flash = Fade(.25, 0, .75, color="#fff")
    
    #personajes
    define caco = Character("Caco Chanante", color="#306E35", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define fangirl = Character("Señora Cachonda", color="#58D3F7", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define bounty = Character("Gold Digger", color="#E0E70C", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define it = Character("Romualda, It Girl", color="#F06E23", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define esceptico = Character("Quim Destort", color="#758F45", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image gymtenerife = "images/gymtenerife.jpg"
    image mercado = "images/mercado.jpg"
    image tenerife1 = "images/tenerife1.jpg"
    image tenerife2 = "images/tenerife2.jpg"
    image bardecarretera = "images/bardecarretera.jpg"
    
    image cuñadotenerife = "images/caco.png"
    image chicacaco = "images/chicacaco.png"
    image esceptico = "images/esceptico.png"
    image itgirl = "images/itgirl.png"
    
    image gymtextte1 = Text("{size=40}Gimnasio All Stars",color="#fff", text_align=0.3)
    image gymtextte2 = Text("{size=40}A la excelencia por la vigorexia",color="#fff", text_align=0.3)
    
    scene traveltenerife at Pan((0, 0), (300,0), 20.0)
    play music "entradillatenerife.mp3"
    $ renpy.pause(14, hard=True)
    
    play music "cancionciudad.mp3"
    if mrajao == True:
        
        scene tenerife1 with fade
        $ renpy.pause(0.5, hard=True)
        show itgirl at center with moveinleft
        it "Disculpe, ¿podrían hacerme una foto?"
        r "Faltaba más, señorita. Colóquese donde guste."
        it "No, no, que sea un selfie, sosteniendo el móvil en contrapicado, pero que no se les vea, claro está."
        pov "¿Por qué no lo haces tú? Ese es el significado de selfie, ¿no?"
        r "Corroboro lo que apunta [jugador]- Aprendi esa palabra en el Marca, cuando el lanzador de peso kazajo Anatoli Khaznatov se hizo una al lograr la medalla de oro en los mundiales de atletismo de Ulan Bator."
        r "Uno de los mejores mundiales de los últimos 30 años, he de decir."
        it "Es que..."
        it "... sniff..."
        r "¿Qué te ocurre?"
        it "Tengo los brazos demasiado cortos y me salen los selfies pegados a la nariz. Normalmente uso un palo para suplir mi carencia pero me lo dejé en el hotel y necesito esta foto."
        montoto "Tus amigas no se van a enfadar porque les enseñes una de cuerpo entero. Si estás muy bien."
        it "Es que es para el trabajo."
        r "Que deberes más extraños envían en clase."
        extend " Yo pensaba que destrozaría la educación pública, pero no tanto..."
        montoto "¿Pagas tus impuestos?"
        extend " ¿A qué te dedicas?"
        it "Me pongo ropa de grandes marcas y estas me pagan para que me haga fotos con ella y las suba a las redes sociales con la esperanza de que mis seguidoras, con escasos o nulos ingresos, se gasten decenas de euros en una diadema."
        r "¿Y yo perdiendo el tiempo aquí con Montoto y esta otra persona?"
        pov "Oye, que tengo nombre."
        r "Seguro que uno horroroso, como Lobo o Pocahontas."
        pov "Ya veo que ni te has molestado en aprendértelo."
        montoto "Tranquilo, yo lo tengo aquí apuntado en su declaración de la renta del año pasado."
        pov "¿Y qué haces tú con eso?"
        montoto "Soy Montoto, yo lo puedo todo en este país."
        pov "Menos conseguir que Mariano pague por sus crímenes..."
        it "Perdonen, ¿me hacen la foto? Todavía tengo que cambiarme de ropa 34 veces y antes tengo que pasar por el hotel."
        r "Faltaría más. Cuando usted mande."
        it "Aaaaa..."
        extend " hora."
        scene tenerife1 with flash
        r "¡Sapristi!"
        r " ¡Ha desaparecido!"
        montoto "Marchémonos de aquí."
        scene bardecarretera with wipeup
        $ renpy.pause(0.5, hard=True)
        show esceptico
        r "Y entonces la chica se desvaneció."
        esceptico "Amigos, creo que se han topado con la mítica \"Chica de la guagua\""
        esceptico "Dicen que saltó de una guagua en marcha para hacerle una foto a una cabra que estaba pastando, con tan mala suerte de que cayó por un acantilado."
        esceptico "Imagínense cómo acabó."
        r "¿Una guagua?"
        montoto "Es como llaman a los autobuses."
        r "¿Y los perros qué dicen, autobús?"
        hide esceptico 
        r "Montoto, ¿estás seguro de que esto es España?"
        montoto "Por supuesto, Presidente, tan español como el pan con tomate."
        r "¿Y por qué hablan todos tan raro?"
        montoto "Prque están lejos de Madrid, Presidente."
        pov "Creo que es hora de que nos pongamos en marcha."
        scene black with dissolve
        show gymtextte1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextte2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymtenerife with fade
        show cuñadotenerife at center
        caco "Hi, I´m Caco Chanante. And you are?"
        r "Hello my amigo. How estas? Me ser M. Rajao. Spanish, muy Spanish."
        caco "Oh my goodness. I should have moved to puerto rico."
        r "You vote for me?"
        caco "I don´t know exactly what the hell you want but in any case: no."
        r "Porfa, please!"
        pov "Hi Mr. Caco, sorry to interrupt but he will stay here until you give him the opportunity to get your votes for the presidential election."
        caco "Mmm, I have a little problem. If you help me with it, I´ll give him my votes."
        pov "Great! Just tell me."
        caco "Do you know the recipe for mojo picon? I moved to this island two weeks ago and all the people I talk to, ask me if I have tasted it. Must be a five stars dish."
        pov "Kind of..."
        r "¿Qué está diciendo, [jugador]. Yo lo estoy entendiendo pero para asegurarme..."
        pov "Votará por usted si le ayudamos."
        r "Mr. Wonderful!"
        caco "What?"
        pov "Don´t pay attention to him. He´s the Walter Mondale of Spain."
        caco "Oh, I´m sorry."
        pov "Do you have pen and paper?"
        caco "Sure. Let´s begin."
        caco "To be honest, I only need to know the ingredients to buy them in the market."
        caco "I invited a horny girl I met this morning in the Pub Escándalo and I want to impress her."
        caco "She told me that she will cook mojo picon and..."
        pov "Don´t worry."
        caco "You know what? Let´s go to the market so we´ll save some time. My hottie will arrive soon."
        scene mercado with dissolve
        show cuñadotenerife at center
        caco "Tell me, what should I purchase?"
        menu:
            "1 Pimiento Rojo":
                $ ingredientes +=1
                pass
            " Medio Pepino":
                pass
            "1 Pimiento verde":
                pass
            "2 Papayas":
                pass
        caco "Ok, great! Next ingredient!"
        menu:
            "Un ramo de perejil":
                pass
            "Un cuarto de cebolla":
                pass
            "Seis ajos":
                $ ingredientes +=1
                pass
            "Cuarto y mitad de achicoria":
                pass
        caco "Here it is. Next!"
        menu:
            "1 cucharadita de chumino":
                caco "Mmm, I like chumino."
                pov "Yes, it´s very... tasteful."
                pass
            "1 cucharada de comino":
                $ ingredientes +=1
                pass
            "1 pizca de azafran":
                pass
            "Media cucharada de curry":
                pass
        caco "Good. And the last one..."
        menu:
            "2 guindillas secas":
                pass
            "3 chiles guajillos":
                pass
            "5 gramos de pimentón":
                pass
            "2 guindillas piconas":
                $ ingredientes +=1
                pass
        caco "Time to go home, boys!"
        scene gymtenerife with fade
        show caco at center
        caco "Please, sit while my girl comes. And don´t put your feet on the table. I watched on the TV that Spanish use to do that a lot."
        pov "Don´t you trust us?"
        caco "The short answer is No. The long one is No with a long \"but\""
        play sound "timbre.mp3"
        $ renpy.pause(1, hard=True)
        caco "Oh, she´s here."
        show caco at left with move
        show chicacaco at right
        bounty "¡Hello sweetheart!"
        bounty "Uy, ¿qué hacéis vosotros aquí?"
        bounty "No es gay, ¿eh?"
        bounty "Además, ¡yo le vi primero!"
        caco "What are you talking about?"
        pov "We are talking about the mojo picón."
        caco "Oh, ok."
        pov "Perdone señorita, no es lo que parece."
        bounty "Aunque no te lo creas, esa excusa no funciona nunca. Y no será por la de veces que he intentado colarla."
        pov "Hemos ayudado al señor Chanante al mercado para comprar los ingredientes para la rica salsa canaria y estábamos esperando a su llegada para que nos confirmara si hemos acertado."
        bounty "Uff menos mal. Pensaba que le iban los tríos aquí a Mr. Guiri."
        bounty "Dejadme ver..."
        r "A todo esto, ¿podría mentir un poco si resulta que no hemos dado una?"
        bounty "¿Y arriesgarme a perder la confianza del señor huevos de oro? Ni hablar."
        if ingredientes == 4:
            $ puntosj += 3
            bounty "Oye, pues lo habeís acertado todo. Podríais pasar por guanches y todo."
            r "Yo tengo experiencia. De niño siempre hacía de apache cuando jugábamos a indios y vaqueros."
            caco "Well, my sexy sexy lover tells me that all is correct. Here are my 3 votes."
            #animación de votos
            r "Uff, pensaba que no lo conseguiríamos."
            r "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        if ingredientes == 3:
            $ puntosj += 2
            bounty "Oye, pues lo habeís acertado casi todo. Os ha fallado un ingrediente."
            pov "Lo más cerca que he estado nunca de Canarias fue una compañera de piso que se lió con todos menos conmigo, así que no nos podemos quejar."
            caco "Well, my sexy sexy lover tells me that all is almost correct. Here are my 2 votes."
            #animación de votos
            r "Uff, pensaba que no conseguiríamos ni un voto."
            r "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        if ingredientes == 2:
            $ puntosj += 1
            bounty "Habéis acertado la mitad. Os han fallado un par de ingredientes."
            montoto "Gracias, sabemos contar."
            bounty "Pero de salsa poco."
            pov "Lo más cerca que he estado nunca de Canarias fue una compañera de piso que se lió con todos menos conmigo, así que no nos podemos quejar."
            caco "Well, my sexy sexy lover tells me that all is almost correct. Here is 1 vote."
            #animación de votos
            r "Uff, mejor eso que irse de vacío."
            r "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        else:
            bounty "No habéis acertado ni una. Bueno, quizá una sí pero tanto da."
            pov "¿No nos va a dar un voto por lástima?"
            bounty "No."
            caco "So thanks to you I´m not going to have picky picky picky picky picky with her... Get out my gym!"
            #animación de votos
            r "¡Qué desastre! La suerte no nos acompaña."
            pov "Ni el desodorante."
            r "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
    if ken == True:
        scene tenerife1 with fade
        $ renpy.pause(0.5, hard=True)
        show itgirl at center with moveinleft
        it "Disculpe, ¿podrían hacerme una foto?"
        k "¿Y no te gustaría hacerte una instantánea conmigo?"
        it "Quizá luego..."
        k "Colócate donde quieras."
        it "No, no, que sea un selfie, sosteniendo el móvil en contrapicado, pero que no se les vea, claro está."
        pov "¿Por qué no lo haces tú? Ese es el significado de selfie, ¿no?"
        k "Yo es que soy más de fotopollas."
        it "No, por favor, ¡que me siguen muchas menores de edad!"
        it "Es que..."
        it "... sniff..."
        k "Si vas a llorar, aquí tienes mi hombro para apollarte."
        pov "No te molestes que la palabra suena igual."
        k "Que no se diga que Ken Sánchez no lo intenta hasta el hartazgo."
        it "Tengo los brazos demasiado cortos y me salen los selfies pegados a la nariz. Normalmente uso un palo para suplir mi carencia pero me lo dejé en el hotel y necesito esta foto."
        espejo "Tus amigas no se van a enfadar porque les enseñes una de cuerpo entero. Si estás muy bien."
        it "Es que es para el trabajo."
        k "Que deberes más extraños envían en clase."
        extend " Yo pensaba que M. Rajao destrozaría la educación pública, pero no tanto..."
        espejo " ¿A qué te dedicas?"
        it "Me pongo ropa de grandes marcas y estas me pagan para que me haga fotos con ella y las suba a las redes sociales con la esperanza de que mis seguidoras, con escasos o nulos ingresos, se gasten decenas de euros en una diadema."
        k "¿Y yo perdiendo el tiempo aquí intentando gobernar una nación de gente estéticamente mediocre."
        pov "Por no llamarla fea."
        k "El calificativo \"feo\" se queda corto ante la horripilancia de sus rostros."
        k "A veces me hubiera gustado nacer letón o sueco. Qué buenos que están todos..."
        pov "Pero si son más sosos que un capítulo audiodescrito de Médico de Familia."
        it "Perdonen, ¿me hacen la foto? Todavía tengo que cambiarme de ropa 34 veces y antes tengo que pasar por el hotel."
        k "Faltaría más. Cuando usted mande."
        it "Aaaaa..."
        extend " hora."
        scene tenerife1 with flash
        k "¡Zapateta!"
        extend " ¡Ha desaparecido!"
        espejo "Marchémonos de aquí."
        scene bardecarretera with wipeup
        $ renpy.pause(0.5, hard=True)
        show esceptico
        k "Y entonces, la chica desapareció."
        esceptico "Amigos, creo que se han topado con la mítica \"Chica de la guagua\""
        esceptico "Dicen que saltó de una guagua en marcha para hacerle una foto a una cabra que estaba pastando, con tan mala suerte de que cayó por un acantilado."
        esceptico "Imagínense cómo acabó."
        k "Pues no muy mal. Vamos, yo me la hubiera fol..."
        espejo "Los fantasmas no existen, mi Tristanbaker metrosexual."
        extend " Y mucho menos las fantasmas guarras robanovios."
        pov "Pues en Cazafantasmas..."
        espejo "Eso era una película."
        espejo "Además, no entiendo qué hacemos hablando de esto si no sabemos cómo ir al gimnasio."
        k "Por eso paramos aquí. ¿No lo recuerdas?"
        espejo "Estábamos en elipsis, ¿cómo quieres que lo supiera?"
        k "Espejos..."
        esceptico "Qué me va a decir a mí. Pasé los mejores años de mi vida viviendo en concubinato con un espejo rococó. La arranqué de un armario durante una visita a Versalles."
        esceptico "Lo nuestro era un amor prohibido. Pero cuando se aprobó la ley de unión entre objetos inanimados y personas, ella me dejó. Lo único que veía en mí era el riesgo. La ponía como una moto."
        esceptico "Todas las noches le pasaba un trapo embadurnado con Pronto. Primero lentamente, y cuando veía que..."
        pov "Es más información de la que quiero procesar. ¿Sabe dónde queda el gimnasio de la ciudad?"
        esceptico "No, pero podría encontrar con los ojos cerrados el clít..."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextte1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextte2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymtenerife with fade
        k "¿Dónde estamos?"
        espejo "Creo que en el gimnasio."
        pov "Tiene toda la pinta. Lo que no sé es cómo hemos venido."
        k "La magia del clítoris..."
        show cuñadotenerife at center
        caco "Hi, I´m Caco Chanante. And you are?"
        k "Yes, my friend."
        caco "Oh, god. Does anyone in your group speak English?"
        k "Yes, we can!"
        pov "I speak just a little."
        caco "Good. That will be enough. Do you understand fuck off?"
        k "Otan, de entrada, no."
        espejo "Te has liado, émulo de Shakespeare."
        pov "Come on, we only want your votes for the presidential election."
        caco "Mmm, I have a little problem. If you help me with it, I´ll give him my votes."
        pov "Great! Just tell me."
        caco "Do you know the recipe for mojo picon? I moved to this island two weeks ago and all the people I talk to, ask me if I have tasted it. Must be a five stars dish."
        pov "Kind of..."
        k "¿Qué está diciendo, [jugador]. Yo lo estoy entendiendo pero para asegurarme..."
        pov "Votará por usted si le ayudamos."
        k "Vote for Pedro!"
        caco "What?"
        pov "Don´t pay attention to him. He´s the Gerald Ford of Spain."
        caco "Oh, I´m sorry."
        pov "Do you have pen and paper?"
        caco "Sure. Let´s begin."
        caco "To be honest, I only need to know the ingredients to buy them in the market."
        caco "I invited a horny girl I met this morning in the Pub Escándalo and I want to impress her."
        caco "She told me that she will cook mojo picon and..."
        pov "Don´t worry."
        caco "You know what? Let´s go to the market so we´ll save some time. My hottie will arrive soon."
        scene mercado with dissolve
        show cuñadotenerife at center
        caco "Tell me, what should I purchase?"
        menu:
            "1 Pimiento Rojo":
                $ ingredientes +=1
                pass
            " Medio Pepino":
                pass
            "1 Pimiento verde":
                pass
            "2 Papayas":
                pass
        caco "Ok, great! Next ingredient!"
        menu:
            "Un ramo de perejil":
                pass
            "Un cuarto de cebolla":
                pass
            "Seis ajos":
                $ ingredientes +=1
                pass
            "Cuarto y mitad de achicoria":
                pass
        caco "Here it is. Next!"
        menu:
            "1 cucharadita de chumino":
                caco "Mmm, I like chumino."
                pov "Yes, it´s very... tasteful."
                pass
            "1 cucharada de comino":
                $ ingredientes +=1
                pass
            "1 pizca de azafran":
                pass
            "Media cucharada de curry":
                pass
        caco "Good. And the last one..."
        menu:
            "2 guindillas secas":
                pass
            "3 chiles guajillos":
                pass
            "5 gramos de pimentón":
                pass
            "2 guindillas piconas":
                $ ingredientes +=1
                pass
        caco "Time to go home, boys!"
        scene gymtenerife with fade
        show caco at center
        caco "Please, sit while my girl comes. And don´t put your feet on the table. I watched on the TV that Spanish use to do that a lot."
        pov "Don´t you trust us?"
        caco "The short answer is No. The long one is No with a long \"but\""
        play sound "timbre.mp3"
        $ renpy.pause(1, hard=True)
        caco "Oh, she´s here."
        show caco at left with move
        show chicacaco at right
        bounty "¡Hello sweetheart!"
        bounty "Uy, ¿qué hacéis vosotros aquí?"
        bounty "No es gay, ¿eh?"
        bounty "Además, ¡yo le vi primero!"
        caco "What are you talking about?"
        pov "We are talking about the mojo picón."
        caco "Oh, ok."
        pov "Perdone señorita, no es lo que parece."
        bounty "Aunque no te lo creas, esa excusa no funciona nunca. Y no será por la de veces que he intentado colarla."
        pov "Hemos ayudado al señor Chanante al mercado para comprar los ingredientes para la rica salsa canaria y estábamos esperando a su llegada para que nos confirmara si hemos acertado."
        bounty "Uff menos mal. Pensaba que le iban los tríos aquí a Mr. Guiri."
        bounty "Dejadme ver..."
        k "A todo esto, ¿podría mentir un poco si resulta que no hemos dado una?"
        bounty "¿Y arriesgarme a perder la confianza del señor huevos de oro? Ni hablar."
        if ingredientes == 4:
            $ puntosj += 3
            bounty "Oye, pues lo habeís acertado todo. Podríais pasar por guanches y todo."
            k "Yo tengo experiencia. De niño siempre hacía de apache cuando jugábamos a indios y vaqueros."
            caco "Well, my sexy sexy lover tells me that all is correct. Here are my 3 votes."
            #animación de votos
            k "Uff, pensaba que no lo conseguiríamos."
            k "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        if ingredientes == 3:
            $ puntosj += 2
            bounty "Oye, pues lo habeís acertado casi todo. Os ha fallado un ingrediente."
            pov "Lo más cerca que he estado nunca de Canarias fue una compañera de piso que se lió con todos menos conmigo, así que no nos podemos quejar."
            caco "Well, my sexy sexy lover tells me that all is almost correct. Here are my 2 votes."
            k "Uff, pensaba que no conseguiríamos ni un voto."
            k "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        if ingredientes == 2:
            $ puntosj += 1
            bounty "Habéis acertado la mitad. Os han fallado un par de ingredientes."
            espejo "Gracias, sabemos contar."
            bounty "Pero de salsa poco."
            pov "Lo más cerca que he estado nunca de Canarias fue una compañera de piso que se lió con todos menos conmigo, así que no nos podemos quejar."
            caco "Well, my sexy sexy lover tells me that all is almost correct. Here is 1 vote."
            k "Uff, mejor eso que irse de vacío."
            k "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        else:
            bounty "No habéis acertado ni una. Bueno, quizá una sí pero tanto da."
            pov "¿No nos va a dar un voto por lástima?"
            bounty "No."
            caco "So thanks to you I´m not going to have picky picky picky picky picky with her... Get out my gym!"
            k "¡Qué desastre! La suerte no nos acompaña."
            pov "Ni el desodorante."
            k "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        
    if coletas == True:
   
        scene tenerife1 with fade
        $ renpy.pause(0.5, hard=True)
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        show itgirl at center with moveinleft
        it "Disculpe, ¿podrían hacerme una foto?"
        c "Faltaría más, compañera. Colócate donde quieras."
        it "No, no, que sea un selfie, sosteniendo el móvil en contrapicado, pero que no se les vea, claro está."
        pov "¿Por qué no lo haces tú? Ese es el significado de selfie, ¿no?"
        it "Es que..."
        it "... sniff..."
        r "¿Qué te ocurre?"
        it "Tengo los brazos demasiado cortos y me salen los selfies pegados a la nariz. Normalmente uso un palo para suplir mi carencia pero me lo dejé en el hotel y necesito esta foto."
        stalin "Tus amigas no se van a enfadar porque les enseñes una de cuerpo entero. Cumples con los estándares estéticos de la buena mujer socialista."
        it "Es que es para el trabajo."
        stalin "En Kizelovski hacían lo mismo. Durante 12 horas picaban piedra hasta alcanzar el rico permafrost siberiano y después se dedicaban a pintarse las uñas y retratarse con las vetustas cámaraas de entonces."
        stalin "Tiempos divertidos en Kizelovski que ya nunca volverán."
        c " ¿A qué te dedicas?"
        it "Me pongo ropa de grandes marcas y estas me pagan para que me haga fotos con ella y las suba a las redes sociales con la esperanza de que mis seguidoras, con escasos o nulos ingresos, se gasten decenas de euros en una diadema."
        stalin "¿Y para esto saltaba la gente el Muro de Berlín?"
        extend " ¡Gilipollas! Luego se sorprenderán de que estallen las burbujas financieras y de la dureza de las crisis."
        pov "En el comunismo la crisis es constante..."
        stalin "Exacto, y he ahí su ventaja."
        extend " El pueblo soviético no conoció nunca la opulencia y no se vio frustrado por no poder disfrutar de lujos que desconocía." 
        stalin "Por eso, la tasa de criminalidad era tan baja en nuestro país y por eso no puedes caminar por Central Park cuando se pone el sol sin que te dejen en ropa interior."
        it "Perdonen, ¿me hacen la foto? Todavía tengo que cambiarme de ropa 34 veces y antes tengo que pasar por el hotel."
        c "Claro que sí. Di "
        extend "¡pa"
        extend " ta"
        extend " ta!"
        scene tenerife1 with flash
        stalin "¡Por los huevos peludos de Lenin!"
        extend " ¿Dónde se ha metido?"
        pov "Marchémonos de aquí."
   
        scene bardecarretera with wipeup
        $ renpy.pause(0.5, hard=True)
        show esceptico
        c "Y entonces la chica se desvaneció."
        esceptico "Amigos, creo que se han topado con la mítica \"Chica de la guagua\""
        esceptico "Dicen que saltó de una guagua en marcha para hacerle una foto a una cabra que estaba pastando, con tan mala suerte de que cayó por un acantilado."
        esceptico "Imagínense cómo acabó."
        stalin "Aplastada como una pasa. Por eso es imposible que fuera ella."
        stalin "Además, los comunistas no creemos en fantasmas."
        pov "Tendrían mucho de lo que temer."
        stalin "Lo único que temo es el fin de los estados y la llegada del verdadero comunismo. En ese preciso instante, la lucha carecería de sentido y tendría que ganarme la vida de gigoló o cantando en el parque."
        c "No te preocupes, ese momento nunca llegará."
        pov "Camarero, hace media hora que pedí un café y todavía estoy esperando."
        esceptico "¿Y a mí que me cuenta? Esto es una mercería, pero como entraron tan excitados por ese encuentro en la carretera, me daba cosa cortarles."
        stalin "¿Sabe al menos dónde encontrar un bar decente o una tienda de licores?"
        esceptico "No, pero sí que podría indicarles la ubicación del gimnasio."
        c "¿Cómo ha sabido...?"
        esceptico "¿Está de broma? Hoy en día poca gente entra en una mercería porque no tienen ni idea de qué es, así que veo mucho la tele y estoy informado de la situación del país."
        esceptico "Además, reconocí de inmediato al señor Staline. Soy un gran admirador de sus películas: Trosky, de la 1 a la 6, sin contar la quinta. Esa es muy mala; Aquella en la que tenía que desbaratar los planes de unos ladrones capitalistas que habían caído en una montaña..."
        esceptico "Esa otra en la que se liaba con una rubia tonta, la de Los Correligionarios, en la que se juntaba con Beria, Kamenev y Zinoviev, entre otros, para instaurar el comunismo en pequeñas comunidades caribeñas dirigidas con mano de hierro por dictadores burgueses..."
        stalin "¡Un fan! Haberlo dicho antes, no le hubiera robado 15 euros de la caja."
        esceptico "¿Me podría firmar un autógrafo?"
        stalin "No."
        pov "Nos tenemos que ir. Gracias por su ayuda."
        scene black with dissolve
        show gymtextte1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextte2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymtenerife with fade
        show cuñadotenerife at center
        caco "Hi, I´m Caco Chanante. And you are?"
        c "Hi! I´m El Coletas. Nice to meet you. I have travel a lot to London: Camdem Town, Picadilly, Whitechapel..."
        caco "Congrats. Do you want a prize?"
        c "Well..."
        caco "Sorry, it´s not usual to find someone in this island who speaks my language. They barely speaks Spanish. It´s really annoying."
        c "You know, the education under Franco´s..."
        stalin "¡Enano de carnaval!"
        c "Sorry for muy friend. He´s a bit over the top."
        stalin "¡No me he drogado!"
        c "Nadie está diciendo eso."
        c "Anyway, Would you be so kind to vote for me in the next presidential elections?"
        c "I don´t know if you know what I´m talking about."
        caco "I received the flyer a couple of hours before."
        caco "Mmm, I have a little problem. If you help me with it, I´ll give him my votes."
        c "Great! Just tell me."
        caco "Do you know the recipe for mojo picon? I moved to this island two weeks ago and all the people I talk to, ask me if I have tasted it. Must be a five stars dish."
        c "Kind of..."
        c "Do you have pen and paper?"
        caco "Sure. Let´s begin."
        caco "To be honest, I only need to know the ingredients to buy them in the market."
        caco "I invited a horny girl I met this morning in the Pub Escándalo and I want to impress her."
        caco "She told me that she will cook mojo picon and..."
        c "Don´t worry."
        caco "You know what? Let´s go to the market so we´ll save some time. My hottie will arrive soon."
        scene mercado with dissolve
        show cuñadotenerife at center
        caco "Tell me, what should I purchase?"
        menu:
            "1 Pimiento Rojo":
                $ ingredientes +=1
                pass
            " Medio Pepino":
                pass
            "1 Pimiento verde":
                pass
            "2 Papayas":
                pass
        caco "Ok, great! Next ingredient!"
        menu:
            "Un ramo de perejil":
                pass
            "Un cuarto de cebolla":
                pass
            "Seis ajos":
                $ ingredientes +=1
                pass
            "Cuarto y mitad de achicoria":
                pass
        caco "Here it is. Next!"
        menu:
            "1 cucharadita de chumino":
                caco "Mmm, I like chumino."
                pov "Yes, it´s very... tasteful."
                pass
            "1 cucharada de comino":
                $ ingredientes +=1
                pass
            "1 pizca de azafran":
                pass
            "Media cucharada de curry":
                pass
        caco "Good. And the last one..."
        menu:
            "2 guindillas secas":
                pass
            "3 chiles guajillos":
                pass
            "5 gramos de pimentón":
                pass
            "2 guindillas piconas":
                $ ingredientes +=1
                pass
        caco "Time to go home, boys!"
        scene gymtenerife with fade
        show caco at center
        caco "Please, sit while my girl comes. And don´t put your feet on the table. I watched on the TV that Spanish use to do that a lot."
        pov "Don´t you trust us?"
        caco "The short answer is No. The long one is No with a long \"but\""
        play sound "timbre.mp3"
        $ renpy.pause(1, hard=True)
        caco "Oh, she´s here."
        show caco at left with move
        show chicacaco at right
        bounty "¡Hello sweetheart!"
        bounty "Uy, ¿qué hacéis vosotros aquí?"
        bounty "No es gay, ¿eh?"
        bounty "Además, ¡yo le vi primero!"
        caco "What are you talking about?"
        pov "We are talking about the mojo picón."
        caco "Oh, ok."
        pov "Perdone señorita, no es lo que parece."
        bounty "Aunque no te lo creas, esa excusa no funciona nunca. Y no será por la de veces que he intentado colarla."
        pov "Hemos ayudado al señor Chanante al mercado para comprar los ingredientes para la rica salsa canaria y estábamos esperando a su llegada para que nos confirmara si hemos acertado."
        bounty "Uff menos mal. Pensaba que le iban los tríos aquí a Mr. Guiri."
        bounty "Dejadme ver..."
        c "A todo esto, ¿podría mentir un poco si resulta que no hemos dado una?"
        bounty "¿Y arriesgarme a perder la confianza del señor huevos de oro? Ni hablar."
        if ingredientes == 4:
            $ puntosj += 3
            bounty "Oye, pues lo habeís acertado todo. Podríais pasar por guanches y todo."
            c "Yo tengo experiencia. De niño siempre hacía de apache cuando jugábamos a indios y vaqueros."
            caco "Well, my sexy sexy lover tells me that all is correct. Here are my 3 votes."
            #animación de votos
            c "Uff, pensaba que no lo conseguiríamos."
            c "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        if ingredientes == 3:
            $ puntosj += 2
            bounty "Oye, pues lo habeís acertado casi todo. Os ha fallado un ingrediente."
            pov "Lo más cerca que he estado nunca de Canarias fue una compañera de piso que se lió con todos menos conmigo, así que no nos podemos quejar."
            caco "Well, my sexy sexy lover tells me that all is almost correct. Here are my 2 votes."
            #animación de votos
            c "Uff, pensaba que no conseguiríamos ni un voto."
            c "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
        if ingredientes == 2:
            $ puntosj += 1
            bounty "Habéis acertado la mitad. Os han fallado un par de ingredientes."
            stalin "Gracias, sabemos contar."
            bounty "Pero de salsa poco."
            pov "Lo más cerca que he estado nunca de Canarias fue una compañera de piso que se lió con todos menos conmigo, así que no nos podemos quejar."
            caco "Well, my sexy sexy lover tells me that all is almost correct. Here is 1 vote."
            #animación de votos
            c "Uff, mejor eso que irse de vacío."
            c "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        else:
            bounty "No habéis acertado ni una. Bueno, quizá una sí pero tanto da."
            pov "¿No nos va a dar un voto por lástima?"
            bounty "No."
            caco "So thanks to you I´m not going to have picky picky picky picky picky with her... Get out my gym!"
            #animación de votos
            c "¡Qué desastre! La suerte no nos acompaña."
            pov "Ni el desodorante."
            c "¡Vayámonos de aquí antes de que la isla desaparezca en la bruma."
            jump mapa
        
    jump mapa   
