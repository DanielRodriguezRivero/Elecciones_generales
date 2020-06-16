label novalencia:
    $ novalencia = True
    
    #personajes
    define falton = Character("Sr. Faltón #45", color="#19C973", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define rita = Character("Rita Repulsa", color="#BCC6BA", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define fuerzas = Character("Fuerzas Vivas de lo que no es Valencia", color="#7A7365", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define petula = Character("Pétula", color="#9E3F5D", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define guia = Character("Gaizka Mendieta", color="#8BEA3C", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define viejo = Character("Arnaldo Lopetegui", color="#142FF9", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image gymnovalencia = "images/gymnovalencia.jpg"
    image hotel = "images/hotel.jpg"
    image novalencia1 = "images/novalencia1.jpg"
    image novalencia2 = "images/novalencia2.jpg"
    image novalencia3 = "images/novalencia3.jpg"
    
    image cuñadonovalencia = "images/rita.png"
    image fuerzas2 = "images/fuerzas.png"
    image petula = "images/petula.png"
    image guia = "images/guia.png"
    image noval1 = "images/noval1.jpg"
    
    image gymtextno1 = Text("{size=40}Gimnasio PowerStrong",color="#fff", text_align=0.3)
    image gymtextno2 = Text("{size=40}Nuestra es la voluntad",color="#fff", text_align=0.3)
    image gymtexthotel = Text("{size=40}Cinco minutos después...",color="#fff", text_align=0.3)
    image gymtexthotel2 = Text("{size=40}Hotel para Amantes \"Maldita Lisiada\"",color="#fff", text_align=0.3)
    
    scene travelnovalencia at Pan((0, 0), (300,0), 20.0)
    play music "entradillanovalencia.mp3"
    $ renpy.pause(16, hard=True)
    
    if valencia == True:
        scene noval1 with dissolve
        $ renpy.pause(0.5, hard=True)
        show fuerzas2 with dissolve
        fuerzas "¿Cómo? ¿Se atreve usted a venir a nuestra insigne ciudad solo después de haber visitado a esos necios valencianos?"
        pov "¿Acaso está prohibido? ¿Qué tiene de malo?"
        fuerzas "Y se atreve a preguntar que qué tiene de malo..."
        fuerzas "¡LARGO DE AQUÍ O LLAMAMOS AL ANSELMO Y SU ESCOPETA!"
        pov "Jo, qué cerrados son en este pueblo."
        fuerzas "¿Pueblo? ¡ANSELMO TRAE A SARA JUANA QUE HAY FORASTEROS CACHONDEÁNDOSE DE NOSOTROS!"
        jump mapa
    
    play music "cancionciudad2.mp3"
    
    if mrajao == True:
    
        scene novalencia1 with dissolve
        $ renpy.pause(1, hard=True)
        r "Qué largo se ha hecho el viaje a..."
        show guia at center
        guia "Buenos días, caballero. Sabrá usted que no se encuentra en Valencia, ¿verdad?"
        r "Por supuesto..."
        extend " ¿Y dónde estoy exactamente?"
        guia "Tiene usted el placer de hallarse en una ciudad milenaria, con una historia singular, arte e idiosincrasia propia."
        r "Lo tienen todo muy verde."
        guia "¡Bienvenido!"
        hide guia with moveoutbottom
        montoto "Se ha marchado antes de que pudieramos preguntarle por la ubicación del gimnasio."
        pov "Tendremos que caminar un poco hasta que nos crucemos con otra persona."
        scene novalencia2 with wipedown
        montoto "Por ahí viene alguien."
        show petula at center with moveinleft
        r "Disculpe usted."
        petula "¿Querían algo?"
        r "¿Sabe donde se encuentra el gimnasio local?"
        petula "¿Te estás cachondeando de mí?"
        petula "Catorce años de piloto de combate, luchando para que el suministro de chuches permanezca constante y no suban de precio, me retiran del servicio activo por un problema con las articulaciones y venga el cachondeo."
        petula "¿Tengo pinta de ir al gimnasio? No puedo doblar las rodillas, tengo 14 tornillos sujetando el menisco y dos remos de aluminio en los brazos."
        petula "Lo bueno es que llevo sobria desde el 97. Cada vez que voy a tomar una copa, derramo el contenido en mi espalda."
        r "Disculpe, no pretendía ofenderla."
        petula "Los civiles son muy desagradecidos con todo lo castrense."
        petula "Cuando en algún desierto lejano alguien decida que los occidentales no merecemos comer regalíz rojo, ya vendréis a pedirnos que os saquemos las castañas del fuego."
        hide petula with moveoutright
        r "En este pueblo hay gente muy rara."
        falton "¡Hijo de una hiena!"
        r "¡Qué original! Ese nunca me lo habían dicho."
        montoto "No le hagas caso, Presidente. Los mediocres se esconden en el anonimato."
        r "No te preocupes. Si tampoco he entendido muy bien qué ha querido decir."
        pov "Vayamos por esa avenida, algo me dice que nuestro objetivo se encuentra allí."
        scene novalencia3 with wiperight
        $ renpy.pause(1, hard=True)
        show viejo at center with moveinleft
        viejo "Un momento, M. Rajao. Te he reconocido desde lejos."
        viejo "Ahora me vas a escuchar."
        r "Dígame, buen hombre."
        viejo "Cuando Franco, venían los grises a llevarse mis gallinas. Luego vinieron los socialistas y se las llevaron también. Más tarde, llegaron los independentistas y me dijeron que al fin las gallinas serían mías, pero que mientras tanto, tenían que llevárselas también..." 
        viejo "El caso es que siempre me quedo sin gallinas..."
        r "¿Y ha probado a comprarse vacas?"
        viejo "No... ahora que lo dice, no."
        r "Pues ahí tiene la respuesta."
        r "Enhorabuena, ha sido usted ayudado por M. Rajao."
        montoto "Cuando tenga las vacas, avíseme."
        scene black with dissolve
        show gymtextno1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextno2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymnovalencia with fade
        show rita at center
        r "¡Qué bien te veo, Rita! ¿Has adelgazado?"
        rita "No, pero mantengo mi peso. Mi trabajo me cuesta, no creas, pero ya sabes que no soy muy de vicios."
        r "Jejejej"
        montoto "Jejeje"
        rita "Jejej"
        pov "¿Van a dejar de reírse o qué? Esto está empezando a ser muy siniestro."
        rita "Cómo se nota que este no ha estado nunca por aquí."
        r "Es un pringado que nos han endilgado por la historia esta de las elecciones."
        rita "Sí, he leído algo sobre el tema."
        r "Entonces, qué, ¿me das tus tres votos?"
        rita "Según la circular tengo que ponerte una prueba."
        r "Y tú no eres de saltarte la legalidad vigente."
        rita "Jejejeje"
        montoto "Jejeje"
        r "Jejej"
        rita "Uy, se me ha caíd este sobre. No sé qué habrá dentro pero no me puedo agachar a cogerlo. De todas formas, no tengo manos."
        pov "Ya lo recojo yo."
        r "Quita hombre, no te molestes. Además, tú no tienes experiencia en estas cosas."
        r "A ver qué tenemos por aquí..."
        r "Puedo abrirlo, ¿no?"
        rita "El que lo coge se lo queda, ¿no? Eso dice la normativa."
        pov "¿Cual? ¿La del patio del colegio?"
        rita "Si queréis puedo llamar a alguien para que tire a vuestro amigo al Pisuerga."
        montoto "¿No queda un poco lejos de aquí?"
        rita "Ah, ¿no es el que desemboca en Murcia?"
        pov "Ese es el Segura."
        rita "Primera vez que lo escucho."
        r "Bueno, Rita, nos marchamos ya."
        rita "No has mirado lo que había en el sobre."
        r "Cielos, es cierto. A ver..."
        show btext2:
            ypos 0.3
            xpos 0.3
        $ renpy.pause(3,hard=True)
        $ puntosj += 3
        r "¡No me lo esperaba! Hoy es nuestro día de suerte."
        pov "Yupi, ahora podéis ir al bingo que seguro que toca."
        montoto "Mejor a la Lotería Nacional, que tenemos más... mano."
        r "Hasta luego, Rita. Cuídate."
        rita "Adiós, Presidente. Ve por la sombra que aquí con el calor no se puede estar mucho tiempo en la calle."

        
    if ken == True:
     
        scene novalencia1 with dissolve
        $ renpy.pause(1, hard=True)
        k "Qué largo se ha hecho el viaje a..."
        show guia at center
        guia "Buenos días, caballero. Sabrá usted que no se encuentra en Valencia, ¿verdad?"
        k "Por supuesto..."
        extend " ¿Y dónde estoy exactamente?"
        guia "Tiene usted el placer de encontrarse en una ciudad milenaria, con una historia singular, arte e idiosincrasia propia."
        k "..."
        guia "¡Bienvenido!"
        hide guia with moveoutbottom
        espejo "Se ha marchado antes de que pudieramos preguntarle por la ubicación del gimnasio."
        pov "Tendremos que caminar un poco hasta que nos crucemos con otra persona."
        scene novalencia2 with dissolve
        espejo "Por ahí viene alguien."
        show petula at center with moveinleft
        k "Disculpe usted."
        petula "¿Querían algo?"
        k "¿Sabe donde se encuentra el gimnasio local?"
        petula "¿Te estás cachondeando de mí?"
        petula "Catorce años de piloto de combate, luchando para que el suministro de chuche permanezca constante y no suban de precio, y me retiran del servicio activo por un problema con las articulaciones y venga el cachondeo."
        petula "¿Tengo pinta de ir al gimnasio? No puedo doblar las rodillas, tengo 14 tornillos sujetando el menisco."
        petula "Lo bueno es que llevo sobria desde el 97, cada vez que voy a tomar una copa, derramo el contenido en mi espalda."
        k "Disculpe, no pretendía ofenderla."
        petula "Los civiles son muy desagradecidos con todo lo castrense."
        petula "Cuando en algún desierto lejano alguien decida que los occidentales no merecemos comer regalíz rojo, ya vendréis a pedirnos que os saquemos las castañas del fuego."
        hide petula with moveoutright
        k "¡Espere! ¿Quiere venir a tomar algo al pub esta noche?"
        k "..."
        k "No me ha debido de escuchar."
        k "En este pueblo hay gente muy rara."
        falton "¡Hijo de una hiena!"
        espejo "¿Quién ha sido?"
        pov "Vayamos por esa avenida, algo me dice que nuestro objetivo se encuentra allí."
        scene novalencia3 with wiperight
        $ renpy.pause(1, hard=True)
        show viejo at center with moveinleft
        viejo "Un momento, Ken Sánchez. Te he reconocido desde lejos."
        viejo "Ahora me vas a escuchar."
        k "Dígame, buen hombre."
        viejo "Cuando Franco, venían los grises a llevarse mis gallinas. Luego vinieron los socialistas y se las llevaron también. Más tarde, llegaron los independentistas y me dijeron que al fin las gallinas serían mías, pero que mientras tanto, tenían que llevárselas también..." 
        viejo "El caso es que siempre me quedo sin gallinas..."
        k "Desgarrador testimonio, amigo."
        k "Como presidente del partido, me comprometo a preguntar a alguien por el tema."
        viejo "Pero..."
        k "Adiós."
        scene black with dissolve
        show gymtextno1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextno2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymnovalencia with fade
        $ renpy.pause(0.5, hard=True)
        show rita at center
        k "¿Qué ven mis desgastados ojos?"
        k "¿Acaso no es el rostro de un ángel esculpido en piedra el que se muestra ante este impío pecador?"
        pov "Psst, espejo. ¿Qué está haciendo?"
        espejo "Lo que mejor se le da: seducir a las masas."
        pov "No era esa la imagen que tenía de él. Si hasta los negros se limpian la mano cuando se la dan."
        espejo "Ese niño estaba comiendo Nutella pero no se dio cuenta de que estaba pringado hasta que no le saludó mi Kunta Kinte."
        k "Ante su belleza, me he quedado obnubilado. Lo que venía a hacer, se me ha olvidado."
        k "Señorita, si sus pechos son tan duros como su cara, me hospedo en el Hotel Roquefort, habitación Cheddar."
        rita "Caballero, si su polla se mueve como su lengua, voy en cinco minutos."
        espejo "Pero, Ken..."
        scene black with dissolve
        show gymtexthotel:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(1, hard=True)
        show gymtexthotel2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(1, hard=True)
        scene hotel with dissolve
        $ renpy.pause(1,hard=True)
        show rita at center
        k "Lo que no he traido es protección."
        rita "Mientras tus espermatozoides no lleven taladro, no hay problema."
        k "Aquí el único que percute, soy yo."
        rita "Qué me ponen los hombres vulgares."
        rita "Apaga la luz que no me gusta que me vean sin los rulos."
        scene black with dissolve
        play sound "taladro.mp3"
        $ renpy.pause(5, hard=True)
        play sound "piedras.mp3"
        $ renpy.pause(3, hard=True)
        play sound "muelle.mp3"
        scene black with Shake((0, 0, 0, 0), 4.0, dist=10)
        show btext2:
            ypos 0.3
            xpos 0.3
        $ renpy.pause(3,hard=True)
        $ puntosj +=3
        scene hotel with dissolve
        $ renpy.pause(1, hard=True)
        show rita at center
        rita "Ahora no podrás tener relaciones sexuales hasta dentro de una semana."
        espejo "Tranquila, con suerte estará jodiendo a todo el país dentro de poco."
        k "¿Qué haces tú aquí?"
        espejo "Lo he visto todo."
        k "¿Y lo has grabado?"
        espejo "¿Por qué clase de perturbada me tomas?"
        k "Tendré que conformarme con lo que grabé en el móvil, aunque sin luz no se verá nada."
        espejo "Debería haberte dejado hace mucho. No sé cómo es que sigo contigo."
        k "En una palabras:"
        k " cunnilingus."
        rita "Eso a mí no me lo has hecho."
        k "Una vez chupé sin querer una piedra pómez. Nunca más. Gracias."
        espejo "¿Podemos irnos ya?"
        k "Podemos y debemos. Cinco minutos más en esta habitación y tendré una nueva pretendienta."
        rita "Tranquilo chulito. Lo que hemos hecho ha sido por vicio. En cuestión de amores busco otras cosas."
        k "En cualquier caso, ha sido un placer."
        rita "Lo sé."
        scene novalencia3 with dissolve
        espejo "Te las llevas de calle, Peter."
        k "Es lo que me dice mi mujer siempre."
        espejo "Pues que sepas que conmigo has terminado."
        k "No te pongas así. Lo hice por los votos. Ya estamos tres más cerca de la victoria."
        $ puntosj += 3
        jump mapa
        
    if coletas == True:
   
        scene novalencia1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        c "Qué largo se ha hecho el viaje a..."
        show guia at center
        guia "Buenos días, caballero. Sabrá usted que no se encuentra en Valencia, ¿verdad?"
        c "Por supuesto..."
        extend " ¿Y dónde estoy exactamente?"
        guia "Tiene usted el placer de encontrarse en una ciudad milenaria, con una historia singular, arte e idiosincrasia propia."
        c "¿Habita aquí algún grupo de izquierdas?"
        guia "¡Bienvenido!"
        hide guia with moveoutbottom
        stalin "Se ha marchado antes de que pudieramos preguntarle por la ubicación del gimnasio."
        c "Y no me ha respondido."
        stalin "De eso no le culpo."
        pov "Tendremos que caminar un poco hasta que nos crucemos con otra persona."
        scene novalencia2 with dissolve
        stalin "Por ahí viene alguien."
        show petula at center with moveinleft
        c "Disculpa, compañera."
        petula "¿Querían algo?"
        c "¿Sabes donde se encuentra el gimnasio local?"
        petula "¿Te estás cachondeando de mí?"
        petula "Catorce años de piloto de combate, luchando para que el suministro de chuche permanezca constante y no suban de precio, y me retiran del servicio activo por un problema con las articulaciones y venga el cachondeo."
        petula "¿Tengo pinta de ir al gimnasio? No puedo doblar las rodillas, tengo 14 tornillos sujetando el menisco."
        petula "Lo bueno es que llevo sobria desde el 97, cada vez que voy a tomar una copa, derramo el contenido en mi espalda."
        c "Disculpa, no pretendía ofenderte."
        petula "Los civiles son muy desagradecidos con todo lo castrense."
        petula "Cuando en algún desierto lejano alguien decida que los occidentales no merecemos comer regalíz rojo, ya vendréis a pedirnos que os saquemos las castañas del fuego."
        hide petula with moveoutright
        c "En este pueblo hay gente muy rara."
        falton "¡Hijo de una hiena!"
        stalin "Ahí tienes tu respuesta a la existencia de un grupo de izquierdas."
        pov "Vayamos por esa avenida, algo me dice que nuestro objetivo se encuentra allí."
        scene novalencia3 with wiperight
        $ renpy.pause(1, hard=True)
        show viejo at center with moveinleft
        viejo "Un momento, Coletas. Te he reconocido desde lejos."
        viejo "Ahora me vas a escuchar."
        c "Dígame, buen hombre."
        viejo "Cuando Franco, venían los grises a llevarse mis gallinas. Luego vinieron los socialistas y se las llevaron también. Más tarde, llegaron los independentistas y me dijeron que al fin las gallinas serían mías, pero que mientras tanto, tenían que llevárselas también..." 
        viejo "El caso es que siempre me quedo sin gallinas..."
        c "¿Eso no es de El joven Indiana Jones?"
        viejo "No sé de qué me habla."
        c "Concretamente, el episodio en el que Indiana se unía al ejército de Pancho Villa..."
        stalin "Camarada Coletas, creo que el grupo terrorista \"Los de la ceja\" ha enviado a un agente para socavar tu liderazgo."
        c "Pensaba que la subida del IVA les había obligado a abandonar las armas."
        stalin "Nunca mientras sigan con la subvención..."
        hide viejo with moveoutright
        c "Vaya, se ha ido."
        stalin "El mundo está en decadencia. Ni agitadores profesionales es posible encontrar ya."
        scene black with dissolve
        show gymtextno1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextno2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymnovalencia with fade
        $ renpy.pause(1, hard=True)
        show rita at center
        c "Hola, ¿cómo va eso?"
        rita "Como me cuentes la historia de aquella vez que fuiste de mochilero a España te doy una patada en el culo y te mando de vuelta a la peluquería de la que nunca debiste haber salido así."
        c "Eh, tranquila que no me van las puretas."
        rita "¿Me estás llamando vieja?"
        pov "Calmémonos un poco."
        pov "Antes de nada, buenas tardes, señora Repulsa."
        rita "¿Tú también me quieres follar?"
        pov "¡Pero qué manía tiene todo el mundo con follar! Ni que fuera lo único en el mundo."
        pov "Hay otras cosas más importantes como: la sonrisa de un niño, la paz entre comunidades, el vuelo de una paloma, el color del cielo al amanecer..."
        stalin "El materialismo dialéctico."
        c "El último capítulo de la sexta temporada de Juego de Tronos."
        stalin "Las Tesis de abril."
        c "El primer disco de Yes."
        stalin "Un gulag recién construido."
        pov "Yo me salgo fuera. Cuando terminéis, me avisáis."
        rita "Caray, cómo se ha puesto, ¿no?"
        c "Y que lo digas. ¿Hemos hecho algo malo?"
        stalin "Nyet. Es que no nos entiende, seguramente por su débil cerebro pseudoburgués."
        rita "Mi Lourdes es igual. En cuanto empezamos a hablar de política se enfurruña y se encierra en su habitación."
        rita "Os voy a denunciar a la físcalia anticorrupción, nos grita. Pobre. Es joven e inocente. No sé a quién habrá salido."
        c "Seguro que en el fondo os quiere."
        rita "Lo sé, pero se hace duro. Sobre todo cuando voy con ella por la calle y me dicen que tengo la cara muy dura."
        rita "Ella no dice nada pero noto cómo se averguenza de mí. Y yo no tengo la culpa de ser así."
        c "Claro que no."
        rita "Perdonad que os moleste con mis problemas."
        extend " Ahora marchaos u os pego un tiro."
        c "¿Y los votos?"
        rita "¿De verdad creías tener alguna posibilidad de que te los diera?"
        rita "¿Y vosotros sois la alternativa?"
        c "La de este país y cada día la de más gente."
        rita "No según las encuestas."
        stalin "Están todas manipuladas."
        rita "Seguid soñando."
        rita "Fuera de aquí."
        stalin "Nyet. Tiene que proponernos una prueba. O eso o llamamos a la policía local."
        rita "¿La que me quita las multas cuando aparco en las plazas destinadas a los niños con cáncer?"
        stalin "Pues llamaremos al de las gafas de sol y le diremos que ha roto l´omertá."
        rita "..."
        rita "Está bien. Nos lo jugaremos a los dados. Tres veces lanzaré dos dados. El que saque la puntuación más alta, gana."
        rita "Por cada tirada nos jugamos un voto."
        stalin "Me parece correcto. Así fue como mi padre conoció a mi madre. Me iban a poner \"Ojos de serpiente\" cuando nací, pero les gustó más Staline."
        c "Pero, ¿dónde están los dados?"
        rita "Es que cuesta tiempo implementarlos. Tranquilos, el ordenador lo calcula."
        c "..."
        rita "¿No os fiáis de mí?"
        extend " No respondáis. Empiezo."
        $ contador = 0
        while contador <3:
            $ tiradaj = renpy.random.randint(1, 12)
            $ tiradarita = renpy.random.randint(1, 12)
            rita "Has sacado [tiradaj] y yo [tiradarita]"
            $ contador += 1
            if tiradaj > tiradarita:
                rita "¡Maldición! Esos dados están trucados."
                rita "Un voto para ti."
                $ puntosj += 1
            if tiradaj < tiradarita:
                rita "Jajajaj, ¡pringado!"
            if tiradaj == tiradarita:
                rita "Ni pa ti, ni pa mí."
                rita "Se siente."
        rita "No voy a dedicarte un minuto más de mi preciado tiempo. Tengo que ir a comprar naranjas."
        rita "Espero que pierdas las elecciones."
        scene novalencia3 with fade
        $ renpy.pause(0.5, hard=True)
        pov "¿Qué tal ha ido?"
        stalin "Dice que entres, que quiere ver tu rabo."
        c "No te rías de [jugador]. Venga, en marcha."
    
    jump mapa