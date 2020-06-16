label murcia:
    $ murcia = True
    
    #personajes
    define quemacho = Character("J.A. Quemacho", color="#CE8684", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define acolito = Character("Testigo de ShenRon", color="#21F006", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define rana = Character("JUFTGH", color="#0D6302", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define naar = Character("Raan Zas", color="#0D6302", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define alter = Character("Álter Ego", color="#0D6302", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define panini = Character("Amparo, secretaria de Panini Co.", color="#0D6302", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define maga = Character("Maga Sara", color="#0D6302", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image gymmurcia = "images/gymmurcia.jpg"
    image murcia1 = "images/murcia1.jpg"
    image murcia2 = "images/murcia2.jpg"
    image murcia3 = "images/murcia3.jpg"
    image murcia4 = "images/murcia4.jpg"
    image standby = "images/standby.jpg"
        
    image cuñadomurcia = "images/camacho.png"
    image rana = "images/rana.png"
    image a18 = "images/a18.png"
    image maga = "images/maga.png"
    image naar = "images/naar.png"
    image alter = "images/alter.png"
    image panini = "images/panini.png"
    
    image gymtextmu1 = Text("{size=40}Gimnasio La Mancuerna Loca",color="#fff", text_align=0.3)
    image gymtextmu2 = Text("{size=40}Especialistas en Boxeo Colombiano y Greguerías",color="#fff", text_align=0.3)
    image textmur = Text("{size=40}La Asociación Europea de Videojuegos Cutres impide la continuación de esta novela visual ante el nivel de absurdez alcanzado.\n Rogamos esperen unos minutos hasta que podamos ofrecerles algo mínimamente coherente.",color="#fff", text_align=0.3)
    image textmur2 = Text("{size=40}Gracias por su paciencia.",color="#fff", text_align=0.3)

    
    scene travelmurcia at Pan((0, 0), (300,0), 20.0)
    play music "entradillamurcia.mp3"
    $ renpy.pause(16.5, hard=True)
    
    play music "cancionciudadmur.mp3"
    
    if mrajao == True:
      
        scene murcia1 with fade
        $ renpy.pause(0.5, hard=True)
        show a18 at center with moveintop
        acolito "Perdone, ¿le interesaría conocer la iglesia de nuestro señor Son Goku?"
        extend " Él murió para salvarnos de Célula."
        r "¡No me diga!"
        extend " ¿Y se encuentra bien ya?"
        acolito "Tiene sus momentos."
        pov "Lo siento, pero tenemos prisa."
        acolito "Tengan entonces el número 25 de la serie roja."
        montoto "No llevamos nada suelto."
        acolito "No se preocupen. Es gratis."
        acolito "Que el Duende Tortuga esté con vosotros."
        hide a18 with moveouttop
        r "¿Qué te ha dado, Montoto?"
        pov "Es un manga."
        r "¿Un qué?"
        montoto "Es una especie de tebeo."
        r "¿Como los de Deliranta Rococó?"
        pov "Sí, me extraña que la conozcas?"
        r "¿Está usted de broma? Estudiábamos sus historias en la universidad del partido. Era nuestro modelo de vida."
        montoto "Creo que allí a lo lejos se divisa la ciudad."
        scene murcia2 with fade
        $ renpy.pause(1,hard=True)
        r "Me la esperaba más..."
        extend " más..."
        pov "¿Anclada en el suelo?"
        r "No sea ridículo. Imagino que está construida así por la legislación antiterremotos."
        r "Es solo que no veo espacio para muchos coches. No me gusta andar."
        show rana at center with moveinleft
        r "¡Hombre! Pero si es JUFTGH."
        r "DRTGGI AHGOYJ JRROGHR JTHWT."
        rana "¡HFBNVB AHRTPÑVB SFUOW!"
        r "PLFOIE NVKZADF... "
        extend "PFOLDEQ"
        rana "¿DFYRUEODFH DHDUIQOE?"
        menu:
            "KFJFLKF":
                rana "¡ACHO JFIPLBV!"
            "DFNBMZAÑFLP":
                rana "¡ACHO FSDKGG!"
        r "¡Nos vemos en el próximo congreso del partido!"
        hide rana with moveoutright
        pov "¿Qué le ha dicho?"
        r "No me he enterado muy bien. Ya sabe el acento que tienen los murcianos."
        r "He creído entender que nos aconsejaba entrar a la ciudad por la puerta del este."
        scene murcia3 with fade
        $ renpy.pause(0.5, hard=True)
        show naar at center with moveinright
        $ renpy.pause(0.3, hard=True)
        naar "¡Alto! ¿Quién vive?"
        pov "¡Viva el GUA!"
        naar "..."
        pov "Siempre quise decirlo..."
        r "Somos una delegación del P.P.K. en busca de los votos del representante local."
        naar "¿Cómo?"
        montoto "Vamos al gimnasio."
        naar "Ah... ¡No podéis pasar! Esta ciudad está siendo sitiada por las fuerzas reptilianas bajo mi mando."
        r "Ah... en ese caso..."
        r "Psst, Montoto, otro loco... No me dijiste que España estaba llena de ellos."
        montoto "Presidente, usted ha nacido aquí, bien debería saberlo."
        r "¿A mí que me cuentas? Si yo nunca me entero de nada..."
        naar "Chacho, ¿me váis a hacer caso o qué?"
        naar "A ver, vuestros papeles reptilianos u os mando a la cazuela, que hoy no hemos decidido todavía qué comer."
        show naar at right with move
        $ renpy.pause(0.2, hard=True)
        show alter at left with moveinleft
        alter "¿Otra vez hablando con desconocidos, Raan?"
        naar "Han empezado ellos..."
        alter "Discúlpenla. De vez en cuando le da por contar su historia con los reptilianos... Se junta con el otro, que dice que es annunaki y venga a chupar sapos todas las tardes..."
        alter "Yo ya no sé qué hacer con ella."
        r "¿Podemos pasar entonces?"
        alter "Sí, claro."
        extend " Ah, y cuidado con el ojo reptante."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmu1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmu2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmurcia with fade
        show cuñadomurcia at center
        quemacho "Kikiri ririki kikiki."
        r "Montoto, creo que le entiendo."
        montoto "Pero eso es imposible, Presidente."
        r "Que sí, no me preguntes cómo pero sé lo que dice."
        pov "Igual en otra vida fue una gallina..."
        quemacho "Kiririki kikiki kiriki."
        menu:
            "Kikiriki ki kiri rikiri":
                quemacho "¡KIKIRI KIRI KIRIRIKI KIKIKI'"
                r "¡Corramos, creo qe le he dicho que anoche le comi las pechugas a su mujer."
                pov "sin ser usted nada de eso."
                scene murcia4 with fade
                r "Por un momento pensé que íbamos a ser devorados por un pollo gigante."
                pov "En todo caso se lo hubiera comido a usted."
                r "No te creas, ha dicho que tus lorzas le parecían muy apetitosas."
                montoto "Otra oportunidad perdida para conseguir los votos."
                jump mapa
            "Kiririri kikikiri kiri kiri":
                quemacho "De acuerdo, por deferencia hacia sus acompañantes humanos hablaré en español."
                quemacho "Por cierto, felicidades, habla gallino como un nativo, aunque tiene un ligero acento de Barbate."
                r "Me sale cuando me pongo nervioso."
                quemacho "Tranquilícese, que estamos entre amigos."
                quemacho "O no..."
                extend " ¿De qué equipo es usted?"
                r "¿Yo? Del mejor, y todo el mundo sabe quién es el mejor, aunque no todo el mundo coincida en quién es el mejor."
                quemacho "Chico, ese quiebro no se lo veias ni a Molowny. De todas formas se te ve de derechas, así que debes de ser del Real Madrid."
                r "Hombre..."
                quemacho "Lo que yo decía."
        quemacho "Yo sé que eres un tío preparao. Un tío con estudios. Diría que hasta inteligente."
        montoto "Qué bien le conoce..."
        quemacho "Te voy a someter a un cuestionario para medir si estás capacitado para un puesto de tan alta trascendencia."
        quemacho "Piensa que vas a tener el destino de millones de personas, qué digo de millones, de miles de españoles en tus manos."
        quemacho "Y eso es una cosa muy importante, porque españoles, lo que se dice españoles, somos muy pocos."
        quemacho "¿Estás preparado?"
        quemacho "Qué pregunta, un español siempre lo está."
        $ quemacho("En Black & Decker, ¿quién era el negro? Ojo que tiene trampa.", interact=False)
        menu:
            "Black":
                quemacho "Error."
                extend " Te dije que tenía trampa."
                quemacho "Ánimo que seguro que remontas."
            "Decker":
                quemacho "Ese es el que perseguía a El Equipo A."
                quemacho "Que por cierto, le echaron de la serie porque se gastaba la mitad del presupuesto en tinte para el pelo y lentillas de colores."
                quemacho "Ánimo que seguro que remontas."
            "Ninguno de los dos, eran chinos.":
                quemacho "¡Efectivamente! Hoy día todo viene de China, hasta los negros."
                $ puntosj += 0.5
        quemacho "Ahora una de las que me gustan a mí, de deporte."
        $ quemacho ("¿Qué sustancias tomó Lance Armstrong para ganar sus Tours de Francia?", interact=False)
        menu:
            "Clembuterol":
                pass
            "Patriotismo americano":
                quemacho "Correcto. Las malas lenguas dirán que se tomó mierda química de esas, pero nada hay que te dope más que levantarte cada mañana escuchando el himno de tu nación."
                $ puntosj += 0.5
                pass
            "Transfusiones de sangre de Indurain":
                quemacho "Entonces hubiera llegado a la Luna."
                quemacho "Ánimo que seguro que remontas."
            "Choco krispis":
                quemacho "Ojo, que también le encontraron en sangre restos, pero en una cantidad demasiado baja."
                quemacho "Ánimo que seguro que remontas."
        quemacho "Y con la siguiente entramos en el ecuador del cuestionario."
        $ quemacho ("¿Qué me recomiendas para evitar las molestas manchas de sudor?", interact=False)
        menu:
            "Que te laves":
                quemacho "Vamos a ver, ¿me estás llamando guarro? ¿No sabes que existe una enfermedad que hace que sudes más de lo normal?"
                quemacho "Se llama Sudoriparitis y es muy dura. Así que menos tonterías."
                quemacho "A ver si vamos a perder las amistades."
            "Usa camisetas negras":
                quemacho "Por contrato tengo que llevar camisas. En qué momento escucharía los consejos financieros del Buitre..."
                quemacho "Me hizo firmar un contrato con Tommy Eldelciber para llevar su ropa durante 15 años."
                quemacho "Y una mierda que me paga, no te creas."
            "No levantes los brazos":
                quemacho "Lo he pesando y no es práctico. Mi mujer a veces me dice que le alcance un bote en los estantes superiores de la cocina y no puedo decirle que lo coja ella, que el jardinero que hemos contratado hace pilates."
                r "¿Y eso qué tiene que ver?"
                pov "Qué poco sabes de la vida, M. Rajao."
            "Múdate al Metro de Madrid, línea 8, que allí no desentonas.":
                quemacho "Pues ahora que lo dices, recuerdo de mi época como muletilla en el club que siempre iba contento al estadio. Claro, era por eso. Allí no me veía juzgado por ser diferente. Estaba entre iguales."
                quemacho "Muchas gracias."
                $ puntosj += 0.5
        $ quemacho ("¿En qué post de El Expreso a Thule, Mr. Roboto declara su amor por las tetas?", interact=False)
        menu:
            "¿Estás de broma? Si tiene, literalmente, cientos de posts hablando de lo mismo":
                quemacho "Es cierto, pero hay uno que escribió para una amiga muy especial."
                pov "Pues todos ellos. Menudo pájaro, no escribía una sola letra sin tener una chica a la que quisiera trincarse en mente."
                quemacho "Tengo que dar por incorrecta la respuesta."
            "Venga ya, si seguro que ni siquiera él sabe de que está hablando. Y eso que ha escrito la pregunta.":
                quemacho "Pero para algo está el buscador de su blog."
            "Un post sobre la guerra civil que no va a gustar a nadie.":
                quemacho "Casi. Ese va sobre ligar. Le gusta mucho hablar de lo que no sabe."
            "¿Puedo preguntarte algo?":
                quemacho "¡Correcto! Gracias a ese post alguna lectora llegó a pensar en enviarle una fototetas. Por supuesto todas sus lectoras tenían sentido común y no le enviaron nada."
                quemacho "Estuvo llorando dos semanas pues pensaba que si con esa brillante oda a enseñar las tetas no había conseguido nada, ya nadie le enseñaría las suyas."
                quemacho "Dejó de pedir que se las enseñaran a todas las chicas con las que se cruzaba, lo que hizo que, por una vez, pudiera entablar cierta conversación con ellas."
                quemacho "Por desgracia, en cuanto abría la boca se daban cuenta de que era un gilipollas y le dejaban igual."
                quemacho "O peor, porque la duda de si le hubieran enseñado las tetas quedaba ahí."
                $ puntosj += 0.5
            
            
        quemacho "Por cierto, elexpresoathule.blogspot.com , el mejor blog que podrás encontrar si escribes esa dirección en tu navegador web favorito."
        quemacho "Eso ha sido todo. Vuestros aciertos habrán subido al marcador de votos. Ya lo dice el dicho: una pregunta, un voto."
        quemacho "Nos vemos."
        r "Hasta la vista, amigo."
        quemacho "¡A mandar!"
                                                                                                                                                        
                                  
    if ken == True:
  
        scene murcia1
        $ renpy.pause(1, hard=True)
        show a18 at center with moveintop
        acolito "Perdone, ¿le interesaría conocer la iglesia de nuestro señor Son Goku?"
        extend " Él murió para salvarnos de Célula."
        k "No tenía ni idea de tamaño sacrificio. Es un acto que llena de fe los corazones de los justos."
        extend " ¿Haces algo esta noche?"
        espejo "Mi picha brava estepario, vámonos antes de que pierdas la cabeza."
        pov "Lo siento, pero tenemos prisa."
        acolito "Tengan entonces el número 25 de la serie roja."
        espejo "No llevamos nada suelto."
        acolito "No se preocupen. Es gratis."
        acolito "Que el Duende Tortuga esté con vosotros."
        hide a18 with moveouttop
        k "¿Qué te ha dado, mi reflejo?"
        pov "Es un manga."
        k "¿Un qué?"
        espejo "Es una especie de tebeo."
        k "¿Está por alguna parte escrito su número de teléfono?"
        espejo "Déjame ver..."
        espejo "El único teléfono que he encontrado es de una tal Editorial Panini."
        k "Mmm, es un nombre raro para una mujer, aunque una vez estuve con un robot llamado Alejandra Olivas, así que..."
        k "Voy a llamar."
        pov "¿Es necesario?"
        k "Por supuesto. ¿Dónde has aprendido tú a ligar?"
        k "Tienes que llamar siempre en cuanto te despides de tu objetivo. De esa forma retiene tu imagen en el cerebro durante el tiempo necesario para que quede archivado en su neocórtex."
        k "Lo leí en un libro sobre seducción científica. A partir de ese momento, haga lo que haga, pensará en ti."
        pov "¿Incluso cuando esté en el baño?"
        k "..."
        k "¿Te imaginas?"
        k "Ahora silencio que voy a hablar."
        pov "Podemos continuar andando mientras."
        scene murcia4 with fade
        $ renpy.pause(0.4, hard=True)
        stop music
        play sound "comunicando.mp3"
        $ renpy.pause(4, hard=True)
        show panini at right with dissolve
        panini "Compañía de Serigrafía y Derivados Panini, ¿en qué puedo ayudarle?"
        k "Hola, guapa. Soy el atractivo joven con el que te has cruzado antes."
        panini "¿Ricardo?"
        k "Ricardo no, Ken."
        panini "Ay chico, perdona. Y yo todo este tiempo llamándote Ricardo. Eso la Marisleisis que me dijo que te llamabas así."
        k "No te preocupes. Es normal. Reconozco que hasta hace no mucho era un desconocido para las masas."
        panini "Es que tampoco ayuda que trabajes en ese cuchitril que te han asignado."
        k "Mujer, no llamaría así a las oficinas de Hierraz."
        panini "¿Qué oficinas? ¿Le has puesto nombre a ese sótano poblado por humedades y compañeros despreciables de departamento?"
        k "A más de uno sí que le enviaría de vuelta a su comunidad autónoma. En eso tienes razón..."
        panini "Bueno, ¿y qué querías? Como me pille el jefe hablando contigo me va a echar la bronca."
        k "Que si quieres follar."
        panini "Vale."
        extend " Dentro de una hora en la puerta."
        k "Nos vemos, bombón."
        hide panini
        play sound "cortar.mp3"
        $ renpy.pause(1, hard=True)
        k "Tenemos que terminar con esto rápido. Me están esperando."
        pov "¿Dónde habéis quedado exactamente?"
        k "Pues en la puerta..."
        extend " ... "
        k "¡Maldición! Estaba tan emocionado por mojar el churro que se me ha olvidado concretar. Voy a volver a llamarla."
        $ renpy.pause(2, hard=True)
        k "¡No hay línea!"
        espejo "Inténtalo más tarde. Ahora tenemos que continuar."
        extend " Creo que allí a lo lejos se divisa la ciudad."
        scene murcia2 with fade
        $ renpy.pause(1,hard=True)
        k "Me la esperaba más..."
        extend " más..."
        pov "¿Anclada en el suelo?"
        k "No seas ridículo. Imagino que está construida así por la legislación antiterremotos."
        k "Es solo que no veo espacio para muchos coches. No me gusta andar."
        show rana at center with moveinleft
        k "¡Hombre! Pero si es JUFTGH."
        k "DRTGGI AHGOYJ JRROGHR JTHWT."
        rana "¡HFBNVB AHRTPÑVB SFUOW!"
        k "PLFOIE NVKZADF... "
        extend "PFOLDEQ"
        rana "¿DFYRUEODFH DHDUIQOE?"
        menu:
            "KFJFLKF":
                rana "¡ACHO JFIPLBV!"
            "DFNBMZAÑFLP":
                rana "¡ACHO FSDKGG!"
        k "¡Nos vemos en el próximo congreso del partido!"
        hide rana with moveoutright
        pov "¿Qué le ha dicho?"
        k "No me he enterado muy bien. Ya sabes el acento que tienen los murcianos."
        k "He creído entender que nos aconsejaba entrar a la ciudad por la puerta del este."
        scene murcia3 with fade
        $ renpy.pause(0.5, hard=True)
        show naar at center with moveinright
        $ renpy.pause(0.3, hard=True)
        naar "¡Alto! ¿Quién vive?"
        pov "¡Viva el GUA!"
        naar "..."
        pov "Siempre quise decirlo..."
        k "Somos una delegación del PRESOE en busca de los votos del representante local."
        naar "¿Cómo?"
        espejo "Vamos al gimnasio."
        naar "Ah... ¡No podéis pasar! Esta ciudad está siendo sitiada por las fuerzas reptilianas bajo mi mando."
        k "Ah... en ese caso..."
        k "Psst, Espejo, otro loco... No me dijiste que España estaba llena de ellos."
        espejo "Si te mezclaras más con la gente, te hubieras dado cuenta."
        k "¡Si yo me mezclo mucho!"
        espejo "No solo con mujeres."
        k "¿Y por qué iba a relacionarme con hombres?"
        naar "Chacho, ¿me váis a hacer caso o qué?"
        naar "A ver, vuestros papeles reptilianos u os mando a la cazuela, que hoy no hemos decidido todavía qué comer."
        show naar at right with move
        $ renpy.pause(0.2, hard=True)
        show alter at left with moveinleft
        alter "¿Otra vez hablando con desconocidos, Raan?"
        naar "Han empezado ellos..."
        alter "Discúlpenla. De vez en cuando le da por contar su historia con los reptilianos... Se junta con el otro, que dice que es annunaki y venga a chupar sapos todas las tardes..."
        alter "Yo ya no sé qué hacer con ella."
        k "¿Podemos pasar entonces?"
        alter "Sí, claro."
        extend " Ah, y cuidado con el ojo reptante."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmu1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmu2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmurcia with fade
        show cuñadomurcia at center
        quemacho "Kikiri ririki kikiki."
        k "Mi doble luminoso, creo que le entiendo."
        espejo "Pero eso es imposible."
        k "Los años que estuve trabajando como oveja en la granja de mi abuelo sí que sirvieron de algo..."
        k "De alguna manera aprendí el lenguaje de las gallinas mientras pastaba junto al corral."
        quemacho "Kiririki kikiki kiriki."
        menu:
            "Kikiriki ki kiri rikiri":
                quemacho "¡KIKIRI KIRI KIRIRIKI KIKIKI'"
                k "¡Corramos, creo qe le he dicho que anoche le comi las pechugas a su mujer."
                pov "Para una vez que te da por ser sincero..."
                scene murcia3 with fade
                k "Por un momento pensé que íbamos a ser devorados por un pollo gigante."
                pov "En todo caso te hubiera comido a ti."
                k "No te creas, ha dicho que tus lorzas le parecían muy apetitosas."
                espejo "Otra oportunidad perdida para conseguir los votos."
                k "No temas. Allí donde fracasó Rodríguez de la Borpolla, yo triunfaré."
                jump mapa
            "Kiririri kikikiri kiri kiri":
                quemacho "De acuerdo, por deferencia hacia sus acompañantes humanos hablaré en español."
                quemacho "Por cierto, felicidades, habla gallino como un nativo, aunque tiene un ligero acento de Barbate."
                k "Me sale cuando me pongo nervioso."
                quemacho "Tranquilícese, que estamos entre amigos."
                quemacho "O no..."
                extend " ¿De qué equipo es usted?"
                k "¿Yo? Del mejor, y todo el mundo sabe quién es el mejor, aunque no todo el mundo coincida en quién es el mejor."
                quemacho "Chico, ese quiebro no se lo veias ni a Molowny. De todas formas se te ve de derechas, así que debes de ser del Real Madrid."
                k "Hombre..."
                quemacho "Lo que yo decía."
        quemacho "Yo sé que eres un tío preparao. Un tío con estudios. Diría que hasta inteligente."
        espejo "¡Qué bien le conoce!"
        quemacho "Te voy a someter a un cuestionario para medir si estás capacitado para un puesto de tan alta trascendencia."
        quemacho "Piensa que vas a tener el destino de millones de personas, qué digo de millones, de miles de españoles en tus manos."
        quemacho "Y eso es una cosa muy importante, porque españoles, lo que se dice españoles, somos muy pocos."
        quemacho "¿Estás preparado?"
        quemacho "Qué pregunta, un español siempre lo está."
        $ quemacho("En Black & Decker, ¿quién era el negro? Ojo que tiene trampa.", interact=False)
        menu:
            "Black":
                quemacho "Error."
                extend " Te dije que tenía trampa."
                quemacho "Ánimo que seguro que remontas."
            "Decker":
                quemacho "Ese es el que perseguía a El Equipo A."
                quemacho "Que por cierto, le echaron de la serie porque se gastaba la mitad del presupuesto en tinte para el pelo y lentillas de colores."
                quemacho "Ánimo que seguro que remontas."
            "Ninguno de los dos, eran chinos.":
                quemacho "¡Efectivamente! Hoy día todo viene de China, hasta los negros."
                $ puntosj += 0.5
        quemacho "Ahora una de las que me gustan a mí, de deporte."
        $ quemacho ("¿Qué sustancias tomó Lance Armstrong para ganar sus Tours de Francia?", interact=False)
        menu:
            "Clembuterol":
                pass
            "Patriotismo americano":
                quemacho "Correcto. Las malas lenguas dirán que se tomó mierda química de esas, pero nada hay que te dope más que levantarte cada mañana escuchando el himno de tu nación."
                $ puntosj += 0.5
                pass
            "Transfusiones de sangre de Indurain":
                quemacho "Entonces hubiera llegado a la Luna."
                quemacho "Ánimo que seguro que remontas."
            "Choco krispis":
                quemacho "Ojo, que también le encontraron en sangre restos, pero en una cantidad demasiado baja."
                quemacho "Ánimo que seguro que remontas."
        quemacho "Y con la siguiente entramos en el ecuador del cuestionario."
        $ quemacho ("¿Qué me recomiendas para evitar las molestas manchas de sudor?", interact=False)
        menu:
            "Que te laves":
                quemacho "Vamos a ver, ¿me estás llamando guarro? ¿No sabes que existe una enfermedad que hace que sudes más de lo normal?"
                quemacho "Se llama Sudoriparitis y es muy dura. Así que menos tonterías."
                quemacho "A ver si vamos a perder las amistades."
            "Usa camisetas negras":
                quemacho "Por contrato tengo que llevar camisas. En qué momento escucharía los consejos financieros del Buitre..."
                quemacho "Me hizo firmar un contrato con Tommy Eldelciber para llevar su ropa durante 15 años."
                quemacho "Y una mierda que me paga, no te creas."
            "No levantes los brazos":
                quemacho "Lo he pesando y no es práctico. Mi mujer a veces me dice que le alcance un bote en los estantes superiores de la cocina y no puedo decirle que lo coja ella, que el jardinero que hemos contratado hace pilates."
                k "¿Y eso qué tiene que ver?"
                pov "Qué poco sabes de la vida marital, Ken."
                k "Quita, quita. Prefiero que me hagan un Suresnes antes que casarme."
            "Múdate al Metro de Madrid, línea 8, que allí no desentonas.":
                quemacho "Pues ahora que lo dices, recuerdo de mi época como muletilla en el club que siempre iba contento al estadio. Claro, era por eso. Allí no me veía juzgado por ser diferente. Estaba entre iguales."
                quemacho "Muchas gracias."
                $ puntosj += 0.5
        $ quemacho ("¿En qué post de El Expreso a Thule, Mr. Roboto declara su amor por las tetas?", interact=False)
        menu:
            "¿Estás de broma? Si tiene, literalmente, cientos de posts hablando de lo mismo":
                quemacho "Es cierto, pero hay uno que escribió para una amiga muy especial."
                pov "Pues todos ellos. Menudo pájaro, no escribía una sola letra sin tener una chica a la que quisiera trincarse en mente."
                quemacho "Tengo que dar por incorrecta la respuesta."
            "Venga ya, si seguro que ni siquiera él sabe de que está hablando. Y eso que ha escrito la pregunta.":
                quemacho "Pero para algo está el buscador de su blog."
            "Un post sobre la guerra civil que no va a gustar a nadie.":
                quemacho "Casi. Ese va sobre ligar. Le gusta mucho hablar de lo que no sabe."
            "¿Puedo preguntarte algo?":
                quemacho "¡Correcto! Gracias a ese post alguna lectora llegó a pensar en enviarle una fototetas. Por supuesto todas sus lectoras tenían sentido común y no le enviaron nada."
                quemacho "Estuvo llorando dos semanas pues pensaba que si con esa brillante oda a enseñar las tetas no había conseguido nada, ya nadie le enseñaría las suyas."
                quemacho "Dejó de pedir que se las enseñaran a todas las chicas con las que se cruzaba, lo que hizo que, por una vez, pudiera entablar cierta conversación con ellas."
                quemacho "Por desgracia, en cuanto abría la boca se daban cuenta de que era un gilipollas y le dejaban igual."
                quemacho "O peor, porque la duda de si le hubieran enseñado las tetas quedaba ahí."
                $ puntosj += 0.5
            
            
        quemacho "Por cierto, elexpresoathule.blogspot.com , el mejor blog que podrás encontrar si escribes esa dirección en tu navegador web favorito."
        quemacho "Eso ha sido todo. Vuestros aciertos habrán subido al marcador de votos. Ya lo dice el dicho: una pregunta, un voto."
        quemacho "Nos vemos."
        k "Muchas gracias. Saludos a su primo de Kentucky."
        quemacho "De tu parte, hijo de..."
        
      
        
    if coletas == True:
 
        scene murcia1 with fade
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
        c "Ahora entiendo esas galas de \"Murcia, qué hermosa eres\". Bien que necesitaban la publicidad."
        show a18 at center with moveintop
        acolito "Perdone, ¿le interesaría conocer la iglesia de nuestro señor Son Goku?"
        extend " Él murió para salvarnos de Célula."
        c "Para lo que valió... Luego regresó y se tuvo que encargar Son Gohanda del engendro del Dr. Gero."
        acolito "Pero con la ayuda de Goku. ¿O es que no le vio usted detrás de su hijo dándole todo su apoyo y su cariño?"
        stalin "Marchémonos que no me gusta la deriva que está tomando esta conversación."
        acolito "Antes de marcharse, tengan el número 25 de la serie roja."
        stalin "No llevamos nada suelto."
        acolito "No se preocupen. Es gratis."
        acolito "Que el Duende Tortuga esté con vosotros."
        hide a18 with moveouttop
        c "¡Es justo el que me faltaba para completar la colección!"
        c "Solía comprarlos todos los jueves con el dinero que Errejota sacaba pidiendo junto a la Estatua del Ángel Caído, en El Retiro."
        c "La semana en que salía este número a la venta se puso enfermo y no pude comprarlo."
        pov "Parece una anécdota sacada de \"Aquellos maravillosos años\"."
        c "¿Verdad que sí?"
        c "Venga, [jugador]. ¡Canta conmigo!"
        c "Volando, volandooooo"
        $ letra = ""
        $ letra = renpy.input("")
        pov "[letra]"
        c "Imagina, tú y yo, lucharemos los doooooos"
        $ letra = renpy.input("")
        pov "[letra]"
        c "Imagina, nunca a un amigo abandonaremos."
        $ letra = renpy.input("")
        pov "[letra]"
        stalin "¡Basta!"
        stalin "Creo que allí a lo lejos se divisa la ciudad. Dejad las niñerías y pongámonos en marcha."
        c "Es que él era más de Ranma 1/2."
        scene murcia2 with fade
        $ renpy.pause(1,hard=True)
        c "Me la esperaba más..."
        extend " más..."
        pov "¿Anclada en el suelo?"
        stalin "Más paupérrima, atrasada, triste, gris, paleta... Aquí pocos votos vamos a arañar."
        c "Tus ideales se asientan en pilares de prejuicios."
        stalin "Como los de cualquier persona."
        show rana at center with moveinleft
        $ renpy.pause(0.4, hard=True)
        c "¡Hombre! Pero si es JUFTGH."
        c "DRTGGI AHGOYJ JRROGHR JTHWT."
        rana "¡HFBNVB AHRTPÑVB SFUOW!"
        c "PLFOIE NVKZADF... "
        extend "PFOLDEQ"
        rana "¿DFYRUEODFH DHDUIQOE?"
        menu:
            "KFJFLKF":
                rana "¡ACHO JFIPLBV!"
            "DFNBMZAÑFLP":
                rana "¡ACHO FSDKGG!"
        stalin "FSFTTET HRHR YURRIUR FSWRWRW WRWRW."
        pov "FBCNXXJKSETIY DANDQICCAKAOC."
        stalin "FFDFIWRJWRJNV AQQORTPLÑCM."
        c "¡¡AOQEMGKG FSFFIJW JHWJJ!!"
        scene black 
        stop music
        $ renpy.pause(1, hard=True)
        show textmur:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(10, hard=True)
        scene standby with fade
        play music "taxi.mp3"
        $ renpy.pause(30, hard=True)
        stop music
        scene black
        $ renpy.pause(1, hard=True)
        show textmur2:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene murcia3 with fade
        $ renpy.pause(0.5, hard=True)
        show naar at center with moveinright
        $ renpy.pause(0.3, hard=True)
        naar "¡Alto! ¿Quién vive?"
        c "¡Viva el GUA!"
        naar "..."
        c "Siempre quise decirlo..."
        stalin "Somos una delegación de la verdadera izqui..."
        c "De Queremos."
        stalin "... Eso. Vamos en busca de los votos del representante local."
        naar "¿Cómo?"
        pov "Vamos al gimnasio."
        naar "Ah... ¡No podéis pasar! Esta ciudad está siendo sitiada por las fuerzas reptilianas bajo mi mando."
        c "Ah... en ese caso..."
        c "Psst, Staline, otro loco... No me dijiste que España estaba llena de ellos."
        stalin "Pues ya tienes la entrepierna lo suficientemente oscura para conocer tu país."
        c "¿A mí que me cuentas? Si yo nunca me entero de nada..."
        naar "Chacho, ¿me váis a hacer caso o qué?"
        naar "A ver, vuestros papeles reptilianos u os mando a la cazuela, que hoy no hemos decidido todavía qué comer."
        show naar at right with move
        $ renpy.pause(0.2, hard=True)
        show maga at left with moveinleft
        maga "¿Otra vez hablando con desconocidos, Raan?"
        naar "Han empezado ellos..."
        maga "Discúlpenla. De vez en cuando le da por contar su historia con los reptilianos... Se junta con el otro, que dice que es annunaki y venga a chupar sapos todas las tardes..."
        maga "Yo ya no sé qué hacer con ella."
        c "¿Podemos pasar entonces?"
        maga "Sí, claro."
        extend " Ah, y cuidado con el ojo reptante."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmu1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmu2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmurcia with fade
        show cuñadomurcia at center
        quemacho "Kikiri ririki kikiki."
        c "No he entendido ni una palabra."
        stalin "Normal. Es un gallo."
        quemacho "Kiririki kiki ririki."
        c "¿Y ahora qué estará diciendo?"
        stalin "Ah, creo entenderle."
        stalin "Ha dicho: soy un gallo tierno y sabroso y quiero que me desplumen y me empalen con una barra de duro y recio acero."
        quemacho "¡Qué violento!"
        stalin "¿Ves cómo entiendo el lenguaje de las gallinas?"
        quemacho "Tampoco hacía falta ponerse así. Todos tenemos derecho a hablar en el idioma que queramos, ¿no? Vaya un demócrata estás hecho."
        c "Es lo que siempre le digo..."
        quemacho "Tú sí que me caes bien."
        extend " Yo sé que eres un tío preparao. Un tío con estudios. Diría que hasta inteligente."
        stalin "Qué bien le conoce..."
        quemacho "Te voy a someter a un cuestionario para medir si estás capacitado para un puesto de tan alta trascendencia como la presidencia del país."
        quemacho "Piensa que vas a tener el destino de millones de personas, qué digo de millones, de miles de españoles en tus manos."
        quemacho "Y eso es una cosa muy importante, porque españoles, lo que se dice españoles, somos muy pocos."
        quemacho "¿Estás preparado?"
        quemacho "Qué pregunta, un español siempre lo está."
        $ quemacho("En Black & Decker, ¿quién era el negro? Ojo que tiene trampa.", interact=False)
        menu:
            "Black":
                quemacho "Error."
                extend " Te dije que tenía trampa."
                quemacho "Ánimo que seguro que remontas."
            "Decker":
                quemacho "Ese es el que perseguía a El Equipo A."
                quemacho "Que por cierto, le echaron de la serie porque se gastaba la mitad del presupuesto en tinte para el pelo y lentillas de colores."
                quemacho "Ánimo que seguro que remontas."
            "Ninguno de los dos, eran chinos.":
                quemacho "¡Efectivamente! Hoy día todo viene de China, hasta los negros."
                $ puntosj += 0.5
        quemacho "Ahora una de las que me gustan a mí, de deporte."
        $ quemacho ("¿Qué sustancias tomó Lance Armstrong para ganar sus Tours de Francia?", interact=False)
        menu:
            "Clembuterol":
                pass
            "Patriotismo americano":
                quemacho "Correcto. Las malas lenguas dirán que se tomó mierda química de esas, pero nada hay que te dope más que levantarte cada mañana escuchando el himno de tu nación."
                $ puntosj += 0.5
                pass
            "Transfusiones de sangre de Indurain":
                quemacho "Entonces hubiera llegado a la Luna."
                quemacho "Ánimo que seguro que remontas."
            "Choco krispis":
                quemacho "Ojo, que también le encontraron en sangre restos, pero en una cantidad demasiado baja."
                quemacho "Ánimo que seguro que remontas."
        quemacho "Y con la siguiente entramos en el ecuador del cuestionario."
        $ quemacho ("¿Qué me recomiendas para evitar las molestas manchas de sudor?", interact=False)
        menu:
            "Que te laves":
                quemacho "Vamos a ver, ¿me estás llamando guarro? ¿No sabes que existe una enfermedad que hace que sudes más de lo normal?"
                quemacho "Se llama Sudoriparitis y es muy dura. Así que menos tonterías."
                quemacho "A ver si vamos a perder las amistades."
            "Usa camisetas negras":
                quemacho "Por contrato tengo que llevar camisas. En qué momento escucharía los consejos financieros del Buitre..."
                quemacho "Me hizo firmar un contrato con Tommy Eldelciber para llevar su ropa durante 15 años."
                quemacho "Y una mierda que me paga, no te creas."
            "No levantes los brazos":
                quemacho "Lo he pesando y no es práctico. Mi mujer a veces me dice que le alcance un bote en los estantes superiores de la cocina y no puedo decirle que lo coja ella, que el jardinero que hemos contratado hace pilates."
                c "¿Y eso qué tiene que ver?"
                stalin "Qué poco sabes de la vida, Coletas."
            "Múdate al Metro de Madrid, línea 8, que allí no desentonas.":
                quemacho "Pues ahora que lo dices, recuerdo de mi época como muletilla en el club que siempre iba contento al estadio. Claro, era por eso. Allí no me veía juzgado por ser diferente. Estaba entre iguales."
                quemacho "Muchas gracias."
                $ puntosj += 0.5
        $ quemacho ("¿En qué post de El Expreso a Thule, Mr. Roboto declara su amor por las tetas?", interact=False)
        menu:
            "¿Estás de broma? Si tiene, literalmente, cientos de posts hablando de lo mismo":
                quemacho "Es cierto, pero hay uno que escribió para una amiga muy especial."
                pov "Pues todos ellos. Menudo pájaro, no escribía una sola letra sin tener una chica a la que quisiera trincarse en mente."
                quemacho "Tengo que dar por incorrecta la respuesta."
            "Venga ya, si seguro que ni siquiera él sabe de qué está hablando. Y eso que ha escrito la pregunta.":
                quemacho "Pero para algo está el buscador de su blog."
            "Un post sobre la guerra civil que no va a gustar a nadie.":
                quemacho "Casi. Ese va sobre ligar. Le gusta mucho hablar de lo que no sabe."
            "¿Puedo preguntarte algo?":
                quemacho "¡Correcto! Gracias a ese post alguna lectora llegó a pensar en enviarle una fototetas. Por supuesto todas sus lectoras tenían sentido común y no le enviaron nada."
                quemacho "Estuvo llorando dos semanas pues pensaba que si con esa brillante oda a enseñar las tetas no había conseguido nada, ya nadie le enseñaría las suyas."
                quemacho "Dejó de pedir que se las enseñaran a todas las chicas con las que se cruzaba, lo que hizo que, por una vez, pudiera entablar cierta conversación con ellas."
                quemacho "Por desgracia, en cuanto abría la boca se daban cuenta de que era un gilipollas y le dejaban igual."
                quemacho "O peor, porque la duda de si le hubieran enseñado las tetas quedaba ahí."
                $ puntosj += 0.5
            
            
        quemacho "Por cierto, elexpresoathule.blogspot.com , el mejor blog que podrás encontrar si escribes esa dirección en tu navegador web favorito."
        quemacho "Eso ha sido todo. Vuestros aciertos habrán subido al marcador de votos. Ya lo dice el dicho: una pregunta, un voto."
        quemacho "Nos vemos."
        c "¡Abajo el Coronel Sunders!"
        quemacho "Dí que sí, compañero."
    
    jump mapa