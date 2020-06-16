label bilbao:
    $ bilbao = True
    $ lluvia2 = renpy.random.randint(1,20)
    if barcelona == True:
        $ barna = True
    
    #personajes
    define churrasco = Character("Txurrasco", color="#222221", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define abertxale = Character("Iñaki", color="#70706A", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define reportera = Character("Periodista", color="#A43E82", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define misterioso = Character("Tristangudari", color="#3B4C64", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define misterioso2 = Character("Salfumán", color="#3B4C64", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)

    
    #imagenes
    image mordor1 = "images/bilbao/mordorintro.jpg"
    image mordor3 = "images/bilbao/mordor3.jpg"
    
    image abertxale  = "images/bilbao/abertxale.png"
    image txurrasco  = "images/bilbao/txurrasco.png"
    image misterioso  = "images/bilbao/misterioso.png"
    
    image periodista  = "images/periodista.png"
    image gymbilbo = "images/gymbilbo.jpg"
    image bilbao1 = "images/bilbao1.jpg"
    image bilbao2 = "images/bilbao2.jpg"
    
    image gymtextbi1 = Text("{size=40}Gimnasio Forja de Hombres",color="#fff", text_align=0.3)
    image gymtextbi2 = Text("{size=40}Zure pussy jan izan dut",color="#fff", text_align=0.3)
    
    
    if mrajao == True:
        scene travelmordor at Pan((0, 0), (300,0), 20.0)
        play music "entradillabilbo.mp3"
        $ renpy.pause(10, hard=True)
        stop music
        play music "cancionciudadani.mp3"
        scene mordor1 with fade
        $ renpy.pause(0.5, hard=True)
        show abertxale with moveinright
        r "Mira Montoto, ¡un abertxale!"
        montoto "Presidente, a mi me parece un muñeco."
        show abertxale at center with move
        r "No digas sandeces. Es la diversidad de los pueblos de España."
        r "Acérquese [jugador], y dígale buenos días a ese buen hombre."
        pov "¿Y por qué no se lo dice usted mismo?"
        r "Es que soy muy tímido."
        show abertxale at left with moveinright
        $ renpy.pause(0.4, hard=True)
        hide abertxale with moveoutleft
        r "Mira, ya se ha ido. Ahora no sabremos dónde tenemos que ir."
        montoto "¿Tú no tienes alguna idea, [jugador]?"
        pov "Qué va. Al único lugar que he ido fue a Uikokahonia con el viaje de fin de curso de la carrera."
        r "¿Y que tal está?"
        pov "Bah, no valió la pena tanto esfuerzo."
        
        scene mordor3 with fade
        $ renpy.pause(1, hard=True)
        show misterioso with dissolve
        misterioso2 "Pssst."
        r "Mira, Montoto. Es nuestro amigo, Salfumán, el blanco popular."
        misterioso2 "Cuánto bueno por aquí. ¿Qué tal va todo por la España Media?"
        r "No me puedo quejar. Estamos con el rollo este de a ver cómo se resuelven las elecciones, pero yo confío en que podamos mantener el dominio del Señor Oscuro sobre la península."
        misterioso2 "Le gustará escucharlo."
        misterioso2 "Oye, ¿cómo va el asunto ese de capturar a los medianos?"
        r "Los progresos son lentos pero vamos avanzando. Tenemos encerrado a Torbe. Esperamos hacerle cantar pronto."
        misterioso2 "¿Y eso qué tiene que ver?"
        r "Hombre, yo vi un vídeo suyo en el que..."
        pov "¿Qué es ese asunto de los medianos?"
        misterioso2 "Federico y Santiago, pareja sentimental y ladrones de guante blanco. Me entraron en la torre hace un mes y se llevaron unas joyas muy preciadas para mí."
        misterioso2 "En especial un anillo."
        extend " ¿No lo habrás visto por casualidad?"
        pov "He visto muchos anillos en mi vida. Si no especifica más..."
        montoto "A mi me gustaba \"Anillos de oro\"."
        misterioso2 "Gracias por el apunte que a nadie interesaba."
        r "No te preocupes, Salfumán. Daremos con ellos."
        misterioso2 "Más os vale. El jefe está que se sube por las paredes. En el techo está ya. No os digo más."
        misterioso2 "Tened los ojos bien abiertos."
        r "Nos vemos, amigo."
        hide misterioso with dissolve
        pov "Tenéis unos amigos muy raros."
        montoto "Vamos, que en tu pandilla no hay nadie que se haya follado a un orco y os haya llamado por la mañana pidiendo que alguien fuera a recogerle a Las Barranquillas o el típico con las orejas puntiagudas..."
        r "En mi cuadrilla había uno al que llamábamos \"Chino\" y eso que era de Mérida."
        pov "¿Y por qué lo llamábais así?"
        r "¡For the lol!"
        pov "..."
        r "Me lo enseñó el Chino."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextbi1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbi2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        stop music
        scene gymbilbo with wiperight
        r "Hola"
        show txurrasco at center with dissolve
        r "¡Montoto! ¡El señor oscuro!"
        churrasco "¡Zorionak a mi gimnasio!"
        r "Y el de todos los españoles."
        churrasco "No, este lo he pagado yo con mi dinero."
        r "Pues verá..."
        churrasco "No digas nada. Sé a lo que habéis venido. Soy negro. Lo sé todo."
        extend " Y lo del rabo también."
        r "Cielos, ¿cómo sabía...?"
        churrasco "Si queréis mis votos teneis que tirarme la basura."
        montoto "Eso es fácil."
        extend " Será una experiencia nueva para nosotros, pero creo que saldremos victoriosos."
        churrasco "No os confiéis, pues el contenedor está al final del temible..."
        extend "¡¡¡Laberinto vasco!!!"
        r "Qué exagerados sois los de Bilbao."
        churrasco "No lo olvidéis: necesitaréis de la ayuda del tiempo para poder encontrar la salida."
        r "¿El tiempo? ¿Alguien tiene hora?"
        montoto "Yo solo puedo decir cuándo es de noche y como extra adicional, cuándo se inicia la temporada fiscal."
        montoto "Huelo a sangre, la fecha se acerca..."
        pov "Me dejé el móvil cargando."
        r "¿Pero no tienes reloj?"
        pov "¿Quién lo tiene hoy día?"
        r "Pues la gente decente que tiene un trabajo y lo consulta para saber cuándo llega tarde a fichar."
        pov "¿Y tú por qué no tienes uno?"
        r "Porque para eso estoy rodeado de gente que hace todo lo que digo y responde a todo lo que pregunto. Mira."
        extend " Montoto, ¿a qué sabe la carne humana?"
        montoto "A tofu."
        r "¿Ves?"
        pov "Eso lo sabe cualquiera."
        r "Pues ahora más difícil..."
        extend "Montoto, ¿cómo se llama la madre del jugador?"
        montoto "..."
        extend "¡¡María!!"
        r "¿Ha acertado?"
        menu: 
            "Con cierta perplejidad, lo corroboro":
                r "Si te lo dije. Tiene poderes."
            "Ni una letra ha acertado":
                montoto "¿Estás seguro de que no eres adoptado?"
                montoto "Lo veo claramente en las estrellas."
        pov "Espero que adivines dónde está la salida."
        montoto "Ahí ya no te puedo ayudar, le quitaria la gracia al juego."
        pov "Ah, ¿pero la tiene?"
        montoto "Hombre, dale una oportunidad. Lo ha hecho gratis y sin el objetivo de follar en mente. Eso tiene mérito."
        churrasco "¿Os váis ya? que tengo que cerrar esto y mi madre me está esperando para cenar."
        r "¿A qué misionero os váis a comer hoy?"
        churrasco "Ni me voy a molestar."
        jump lab1
        
        
    if ken == True:
        scene travelbilbao at Pan((0, 0), (300,0), 20.0)
        play music "entradillabilbo2.mp3"
        $ renpy.pause(10, hard=True)
        stop music
        play music "cancionciudad.mp3"
        scene bilbao1 with dissolve
        $ renpy.pause(0.5, hard=True)
        k "Qué me gusta el bacalado de Bilbado."
        espejo "Rapsoda apolíneo, no hables así que te puede escuchar alguien."
        k "No te enfades. Es que siempre quise decirlo."
        show periodista at center with moveinright
        reportera "Perdone que le moleste, señor Sánchez."
        k "Tú nunca molestas, guapa."
        reportera "Me llamo Blanca Maceta y trabajo para un periódico."
        espejo "¿Cuál?"
        reportera "Preferiría no decirlo."
        espejo "Seguro que es La Gaceta o el Pulgarcito."
        k "¿Acaso importa?"
        k "Deja que la muchacha hable tranquilamente."
        reportera "¿Puedo hacerle una entrevista?"
        k "Siempre que no me preguntes nada comprometido..."
        reportera "Por favor, soy periodista."
        k "Tienes razónn. Perdóname. Adelante."
        $ reportera ("Bien, ¿considera que el Burguer King es mejor que McDonalds?", interact=False)
        menu:
            "Un republicano como yo solo puede escoger McDonalds.":
                pass
            "Burguer ¿qué? McDonalds ¿qué?":
                pass
            "A mi dame un pepito de ternera y soy feliz.":
                pass
        $ reportera ("¿Dónde hay más gilipollas?", interact=False)
        menu:
            "Twitter":
                pass
            "Instagram":
                pass
            "El partido de la oposición, que es como decir en Twitter":
                pass
        $ reportera ("¿Qué color es el más bonito del mundo?", interact=False)
        menu:
            "Amarillo huevo de pato.":
                pass
            "Negro culo de grillo.":
                pass
            "Rojo socialdemócrata.":
                pass
            "Azul.":
                pass
        $ reportera ("¿Cómo se conquista a Ken Sánchez?", interact=False)
        menu:
            "Una noche romántica en Suresnes.":
                pass
            "Discutiendo la viabilidad de una comisión para el estudio de la reforma de la ley de partidos en la propiedad vertical.":
                pass
            "Una mamada ya me viene bien.":
                k "Y no estoy insinuando nada, ¿eh?"
                reportera "Me imagino."
        reportera "Creo que eso es todo. Mis lectores encontrarán sus respuestas muy interesantes."
        k "Perdone, señorita."
        extend " ¿Puedo hacerle yo una pregunta?"
        reportera "Es algo inusual, pero adelante."
        menu:
            "¿Cómo es que la luna en sus ojos brilla y mi corazón obnubila?":
                reportera "Oigh, sabe usted llegar al interior de una dama."
                k "Aunque sin ropa lo tengo más fácil."
                espejo "Debemos irnos ya."
                k "Hasta luego, guapa."
                hide periodista
            "¿Cómo es que su sonrisa, a mi bragueta mete prisa?":
                reportera "¡Qué descarado!"
                espejo "Disculpe al candidato, está muy estresado."
                espejo "Nos marchamos."
                hide periodista
            "¿Follamos o jugamos al baloncesto?":
                reportera "¡Por favor, soy periodista!"
                k "Le ruego me disculpe."
                extend " ¿En su casa o en la mía?"
                reportera "Mejor en la tuya que mi compañera de piso no se depila desde hace una semana y hay que abrirse paso a machetazos."
                espejo "Tendrá que ser en otra ocasión. Tenemos un país que conquistar. ¿Lo has olvidado, capullo de rosa mío?"
                k "Es verdad. Te dejo mi teléfono en la contraportada del programa del partido."
                hide periodista
        
        scene bilbao2 with fade
        $ renpy.pause(1, hard=True)
        show misterioso with dissolve
        misterioso "Pssst."
        pov "Oye, Ken. Creo que te llama ese señor."
        k "¿A mí? Imposible."
        k "Se habrá confundido con otro hombre de izquierdas."
        misterioso "Psst. Psst. El señor guapo y acompañantes."
        pov "¿Ves cómo te llamaba?"
        misterioso "¡Arratsaldeón!"
        k "¡Ay ese Salmerón!"
        misterioso "¿Le interesaría conocer el secreto que guardo?"
        espejo "No me diga más. Debajo de esa capa, ¿verdad?"
        espejo "Así conocí a mi primer ex-marido."
        misterioso "Se trata de un secreto que le permitirá asegurar la victoria en el juego."
        k "¿Qué juego? Yo lo que quiero ganar son las elecciones."
        pov "Quizá se refiere a que el proceso electoral es un juego en sí mismo."
        espejo "En ese caso, que nos diga todo lo que sabe. Bien sabe Dios que nos hace falta toda la ayuda del mundo para conseguir la victoria. Y eso que los socialistas no creemos más que en Felipe y El País de los ye-yés."
        k "Hable usted, señor siniestro."
        misterioso "Sabed pues, que si visitáis ciertas ciudades con un vínculo común durante vuestro periplo, conseguiréis un número de votos extra que os alzará a lo más alto del Olimpo de la Moncloa."
        k "¿Qué ciudades son esas? ¿Cuales sus vínculos? ¿Está calvo debajo de esa chistera? ¿Me ama?"
        misterioso "No lo puedo decir. Tampoco. No, solo tengo entradas. De 8 a 12, por un bocadillo de Mortadela."
        k "No trabajo los embutidos."
        misterioso "En ese caso... Mi labor aquí ha concluido. Adiós."
        hide misterioso with blinds
        espejo "Qué personaje más misterioso."
        k "Y que lo digas. Esa melena me confundía mucho."
        
        scene black with wipeleft
        $ renpy.pause(0.5, hard=True)
        show gymtextbi1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbi2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymbilbo with fade
        show txurrasco at center with dissolve
        churrasco "¡Bienvenidos, amigos!"
        k "Hol..."
        churrasco "No digáis nada. Sé a lo que habéis venido. Soy negro. Lo sé todo."
        extend " Y lo del rabo también."
        k "Cuando quieras echamos una pelea de sables láser."
        churrasco "Si queréis mis votos teneis que tirarme la basura."
        espejo "Eso es fácil."
        extend " Será una experiencia nueva para nosotros, pero creo que saldremos victoriosos."
        churrasco "No os confiéis, pues el contenedor está al final del temible..."
        extend "¡¡¡Laberinto vasco!!!"
        k "Qué exagerados sois los de Bilbao."
        churrasco "No lo olvidéis: necesitaréis de la ayuda del tiempo para poder encontrar la salida."
        k "¿El tiempo? ¿Alguien tiene hora?"
        espejo "Yo solo puedo decir quién es el hombre más guapo de toda España."
        k "¿Y quién es?"
        espejo "Tú bien lo sabes, ¡tiburón!"
        pov "Yo me dejé el móvil cargando y no sé qué hora es."
        k "¿Pero no tienes reloj?"
        pov "¿Quién lo tiene hoy día?"
        k "Pues la gente decente que tiene un trabajo y lo consulta para saber cuándo llega tarde a fichar."
        pov "¿Y tú por qué no tienes uno?"
        k "Porque para eso estoy rodeado de gente que hace todo lo que digo y responde a todo lo que pregunto."
        k "Por ejemplo, Espejito, espejito, ¿quién es la máxima autoridad en el partido?"
        espejo "Estoooo... ¿quieres la verdad o lo que te haría feliz?"
        churrasco "¿Os váis ya? que tengo que cerrar esto y mi madre me está esperando para cenar."
        k "Vámonos. Sé muy bien cuándo no me quieren en un sitio."
        churrasco "La entrada está ahí a la izquierda, junto al lavabo para blancos."
        jump lab1ken
        
    if coletas == True:
        scene travelbilbao at Pan((0, 0), (300,0), 20.0)
        play music "entradillabilbo2.mp3"
        $ renpy.pause(10, hard=True)
        stop music
        play music "cancionciudad.mp3"
        scene bilbao1 with dissolve
        if barcelona == True:
            if yausado == False:
                stalin "Propicios días, compañeros... ¿Puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        show periodista at center with moveinleft
        reportera "Perdone, ¿es usted el famoso líder de izquierdas..."
        stalin "En efecto."
        c "Creo que se refiere a mí."
        stalin "Crii qui si rifiiri i mí."
        stalin "Vaya con el egocéntrico..."
        reportera "¿Me permitiría hacerle una entrevista, señor Coletas?"
        c "Siempre que no me preguntes nada comprometido..."
        reportera "Por favor, soy periodista."
        c "Tienes razón. Perdóname. Adelante."
        c "Y llámame Coletis."
        $ reportera ("Bien, ¿considera que el Burguer King es mejor que McDonalds?", interact=False)
        menu:
            "Un republicano como yo solo puede escoger McDonalds.":
                pass
            "La app del McDonalds tiene buenas ofertas. Me quedo con ellos.":
                pass
            "A mi dame un pepito de ternera y soy feliz.":
                pass
        $ reportera ("¿Qué color es el más bonito del mundo?", interact=False)
        menu:
            "Amarillo huevo de pato.":
                pass
            "Morado vestido de Rizos.":
                pass
            "Púrpura Whoopie Goldberg.":
                pass
            "Azul.":
                pass
        $ reportera ("¿Dónde hay más gilipollas?", interact=False)
        menu:
            "Twitter":
                pass
            "Instagram":
                pass
            "El partido de la oposición, que es como decir en Twitter":
                pass
        $ reportera ("¿Cómo se conquista al Coletas?", interact=False)
        menu:
            "Una partida a Magic The Gathering.":
                pass
            "Discutiendo la viabilidad de una comisión para el estudio de la reforma de la ley de partidos en la propiedad vertical.":
                pass
            "Cazando Pokémons en el parque a la luz de los led.":
                c "Y no estoy insinuando nada, ¿eh?"
                reportera "Me imagino."
        reportera "Creo que eso es todo. Mis lectores encontrarán sus respuestas muy interesantes."
        c "Perdona, compañera."
        extend " ¿Puedo hacerte yo una pregunta?"
        reportera "Es algo inusual, pero adelante."
        menu:
            "¿Crees que fue una pérdida para el partido que se marchara El Carteras?":
                stalin "¡Disidente!"
                reportera "¿Quién?"
                c "Me lo imaginaba..."
                stalin "Debemos irnos ya."
                c "Hasta luego, compañera."
                stalin "¿Esto cuándo sale?"
                reportera "La semana que viene en el blog que tiene mi prima Queca. Les enviaré la dirección a su correo."
                hide periodista
            "¿Me aconsejas una buena máscara para el pelo?":
                reportera "Lo siento, yo no uso esas cosas."
                stalin "Hasta una mujer es más masculina que tú. Debería darte verguenza."
                extend " Anda, vámonos ya."
                c "Hasta luego, compañera."
                stalin "¿Esto cuándo sale?"
                reportera "La semana que viene en el blog que tiene mi prima Queca. Les enviaré la dirección a su correo."
                hide periodista
            "¿Alguna vez has estado en tu casa programando un juego y ha entrado por tu ventana un profundo olor a porro?":
                reportera "Me pasa muy a menudo. Vivo cerca de una de vuestras sedes."
                stalin "Debemos irnos ya."
                c "Hasta luego, compañera."
                stalin "¿Esto cuándo sale?"
                reportera "La semana que viene en el blog que tiene mi prima Queca. Les enviaré la dirección a su correo."
                hide periodista                
                
        scene bilbao2 with wiperight
        if lluvia > 10:
            show rain
        $ renpy.pause(1, hard=True)
        show misterioso with dissolve
        misterioso "Pssst."
        pov "Oye, Coletas. Creo que te llama ese señor."
        c "¿A mí? Será el líder de izquierdas de la región que querrá llegar a un pacto por la futura gobernabilidad."
        misterioso "Psst. Psst. El señor guapo y acompañantes."
        pov "Igual lo que quiere es otra cosa."
        misterioso "¡Arratsaldeón!"
        c "Arratsaldeón, adineko."
        misterioso "¿Le interesaría conocer el secreto que guardo?"
        stalin "En la URSS teníamos personas como usted. Se acercaban a uno en los parques del pueblo y cuando la policía pasaba de largo se abrían la gabardina y ¡zasca!"
        stalin "Un torpedo del Octubre Rojo encimando a su objetivo."
        misterioso "Se trata de un secreto que le permitirá asegurar la victoria en el juego."
        c "¿La victoria? En unas elecciones nadie gana ni pierde. Es la representación de las distintas ideas que profesa el pueblo la que se decide."
        pov "Quizá se refiere a que el proceso electoral es un juego en sí mismo."
        stalin "En ese caso, que nos diga todo lo que sabe. Bien sabe Dios que nos hace falta toda la ayuda del mundo para conseguir vencer. Y eso que los marxistas no creemos más que en Marx y Don Santiago Bernabéu."
        stalin "Los marxistas del Real Madrid, al menos."
        c "Hable usted, señor siniestro."
        misterioso "Sabed pues, que si visitáis ciertas ciudades con un vínculo común durante vuestro periplo, conseguiréis un número de votos extra que os alzará a lo más alto del Olimpo de la Moncloa."
        c "¿Qué ciudades son esas? ¿Cuales sus vínculos? ¿Está calvo debajo de esa chistera? ¿Se aliaría su confluencia con la mía?"
        misterioso "No lo puedo decir. Tampoco. No, solo tengo entradas. Solo si me da un bocadillo de Mortadela."
        c "No trabajo los embutidos."
        misterioso "En ese caso... Mi labor aquí ha concluido. Adiós."
        hide misterioso with blinds
        c "Qué personaje más misterioso."
        stalin "¿Ahora se le llama \"misterioso\" a no lavarse?" 
        scene black with wipeleft
        $ renpy.pause(0.5, hard=True)
        show gymtextbi1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbi2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymbilbo with fade
        show txurrasco at center with dissolve
        churrasco "¡Bienvenidos, amigos!"
        c "Hol..."
        churrasco "No digáis nada. Sé a lo que habéis venido. Soy negro. Lo sé todo."
        stalin "Y seguro que lo del rabo también."
        churrasco "Si queréis mis votos teneis que tirarme la basura."
        stalin "Eso es fácil."
        extend " Será una experiencia nueva para nosotros, pero creo que saldremos victoriosos."
        churrasco "No os confiéis, pues el contenedor está al final del temible..."
        extend "¡¡¡Laberinto vasco!!!"
        c "Qué exagerados sois los de Bilbao."
        churrasco "No lo olvidéis: necesitaréis de la ayuda del tiempo para poder encontrar la salida."
        c "¿El tiempo? ¿Alguien tiene hora?"
        c "Sabía que tendría que haberme traido el móvil."
        pov "¿No tienes reloj?"
        stalin "Los comunistas debemos vivir ajenos a la tecnología porque ha sido fabricada con mano de obra esclava. Los capitalistas, por contra, no tienen ningún inconveniente en que los niños trabajen catorce horas al día para fabricar sus juguetes."
        pov "¿Y entonces lo del móvil del Coletas?"
        stalin "¿Qué parte de \"los comunistas\" no has entendido?"
        churrasco "¿Os váis ya? que tengo que cerrar esto y mi madre me está esperando para cenar."
        stalin "Ahora que me fijo... ¿tú no estudiarías Teleco en la Patrice Lumumba, verdad?"
        churrasco "No sé de qué me habla. La entrada al laberinto está a mano derecha, junto al baño de los blancos."
        jump lab1col
    jump mapa