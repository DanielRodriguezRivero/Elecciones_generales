label cuenca:
    $ cuenca = True
    #personajes
    define bertin = Character("Norberto O.", color="#F5ECE1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define parcuenca = Character("Pareja Libertina", color="#B64153", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define pedro = Character("Pedro Diosdado", color="#B64153", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define ana = Character("Ana Masó", color="#B64153", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define asterix = Character("Libertinos Franceses", color="#48AADC", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    #background
    image gymcuenca = "images/gymcuenca.jpg"
    image cuenca1 = "images/cuenca1.jpg"
    image cuenca5 = "images/cuenca5.jpg"
    image cuenca4 = "images/cuenca4.jpg"
    image cuenca2 = "images/cuenca2.jpg"
    image cuenca3 = "images/cuenca3.jpg"


    image jamones = "images/jamones.jpg"
    
    #imagenes personajes
    image cuñadocuenca = "images/bertin.png"
    image parejac = "images/parejac.png"
    image parejad = "images/parejad.png"
    image asterix = "images/asterix.gif"
    
    image gymtextcu1 = Text("{size=40}Gimnasio Asses on Fire",color="#fff", text_align=0.3)
    image gymtextcu2 = Text("{size=40}Campeones del mundo de Sentadillas",color="#fff", text_align=0.3)
    scene travelcuenca at Pan((0, 0), (300,0), 20.0)
    play music "entradillacuenca.mp3"
    $ renpy.pause(15.3, hard=True)
    
    play music "cancionciudad.mp3"
    
    if mrajao == True:

        scene cuenca1 with dissolve
        $ renpy.pause(0.5, hard=True)
        show parejac at center with moveinleft
        parcuenca "¡Hola! ¿Qué tal?"
        extend " ¿Folláis?"
        r "Juntos nunca. A veces uno mira cómo lo hace el otro, pero solo cuando hay algo que celebrar."
        montoto "Presidente, no me gusta que airees nuestras actividades."
        parcuenca "Jajaja qué graciosos. ¿No habéis venido por lo del encuentro entonces?"
        pov "¿Qué encuentro?"
        parcuenca "¿Cuál va a ser? El IIIer Encuentro Internacional \"Miremos a Cuenca\" de Jóvenes Swingers."
        r "Psst, Montoto, ¿qué es un swinger?"
        montoto "Imagino que debe de estar relacionado con el golf."
        pov "Sí, la cosa va de meter pelotas en un hoyo usando un palo."
        parcuenca "Eso si eres muy experimentado."
        montoto "Pues lo que yo decía."
        parcuenca "¿Entonces qué? ¿Os hace un trío?"
        r "Quite, quite, que a Razna el último no le salió bien."
        parcuenca "Vosotros os lo perdéis."
        hide parejac with moveoutright
        r "¿Por qué nadie me propone cosas interesantes como una capea o el robo de un servicio público?"
        montoto "Lo de los servicios públicos ya me parece que..."
        r "Es cierto. A veces olvido lo eficiente que soy."
        montoto "Que somos."
        r "Porque os dejo."
        scene cuenca2 with dissolve
        $ renpy.pause(1, hard=True)
        r "No me lo puedo creer. Ahí viene otra pareja. Rápido, Montoto, haz como que me besas."
        show asterix with moveinright
        asterix "Oh, la, lá. ¿Ves, Gordelix? Los hispanos se dan oscúlos en público y tú no quiegues ni que te de la mano."
        asterix "¿No te pica la bagba, Casper?"
        montoto "No soy un fantasma. Soy un..."
        asterix "Sí, si, si, si, si. Pero hablemos de lo impogtante:  "
        extend " ¿Queguéis gollo?"
        pov "Si me disculpáis, yo me voy a mirar escaparates por allí."
        asterix "Tú puedes migag si quiegues. Al bagbitas con migada de satigo segugo que le gusta."
        r "Mire, yo he venido aquí a otra cosa. No puedo perder el tiempo."
        asterix "Hasta que puedas entonces. Au revoir, moreno."
        r "¿Ves, Montoto? Y tú empeñado en que no gastara el dinero en tinte."
        pov "¿Podemos ir al gimnasio de una vez?"
        r "Si yo estaba haciendo tiempo hasta que se hiciera de noche."
        pov "¿Para qué?"
        scene cuenca3 with dissolve
        $ renpy.pause(1, hard=True)
        r "Para esto."
        montoto "Qué bonito, Presidente. Me recuerda a la boda de la hija del jefe con Aggggg."
        r "Cuando Aullalobos subió al escenario y se tiró encima del público y aplastó al camarero, ¿verdad?"
        r "Ya no se hacen fiestas como esas..."
        r "Podemos irnos."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextcu1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextcu2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymcuenca with fade
        $ renpy.pause(0.5, hard=True)
        show cuñadocuenca at center
        r "¡Hombre, Norberto! ¿Cómo tú por aquí tan lejos de tu Jerez natal?"
        bertin "Ya ves, campeón, las vueltas que da la vida."
        r "Pues han debido de girarla mucho para encontrarte en este lugar en mitad de ninguna parte."
        bertin "Muchacho, no digas eso, que esto es mú bonito."
        bertin "Mis huevos colganderos han hecho más por este pueblo que las casas colgantes."
        extend " Gracias a mí, 4786 mujeres y algún que otro hombre confuso saben dónde queda en el mapa."
        bertin "Y luego está el boca a boca. No culo a boca. Eso nunca, chiquillo."
        bertin "Las autoridades locales, conocedoras de este hecho, me ofrecieron la dirección de este gimnasio y aquí estoy, echando las vacaciones más bien que ná."        
        r "¿Está Arevalo también? Me gustaría saludarle."
        bertin "Le he mandado a comprar el pan hace una hora y todavía no ha vuelto."
        bertin "Estará en la Plaza Mayor pidiendo limosna. Ahora que no puede contar chistes de gangosos tiene que sacar provecho de su arte. Dice que así se siente útil."
        r "Es que este país ya no es lo que era."
        bertin "Pues tú tienes mucha mano, gachón. A ver si haces algo cuando seas presidente."
        pov "Ya lo ha sido y no ha..."
        r "Será la primera medida que tome, Norberto. Los chistes de gangosos recuperarán el status que nunca debieron perder."
        r "Dicho lo cual, para que se apruebe dicha medida tendría que presidir el ejecutivo y ya sabes que estoy aquí para pedirte tus votos."
        bertin "No se hable más, aquí mismo los tenía guardados esperando que vinieras."
        r "¿Te ha molestado alguno de mis rivales?"
        bertin "Vino El Coletas, pero le di un manguerazo y salió huyendo como los gatos. ¡Jajajaja!"
        bertin "Vamos a mi bodega. Te invito a un vinito."
        pov "Disculpe, siento ser la voz discordante pero por algo me estoy perdiendo la final de Fútbol Australiano."
        extend " Según la ley usted debe someter al candidato, aquí presente, a una prueba con la que ganarse su apoyo. De lo contrario, incurriría en flagrante delito, blablabla, blablabla."
        bertin "Caray con el abogado del estado..."
        r "Uy, ya me gustaría que lo fuera. Sería más manejable. Es un don nadie o una doña nadie, no lo tengo muy claro."
        bertin "Oye, pues eso a mí me interesa. ¿Te apetece tomarte una copita en mi buhardilla? Está mal iluminada pero es muy cómoda."
        menu:
            "Tengo más rabo que espalda":
                bertin "Estuve en Tailandia hace diez años. No me voy a asustar."
                r "¿Y qué fuiste a hacer allí?"
                bertin "Digamos que aprendí a jugar al golf sin palo."
                r "¿También eres un swinger de esos?"
                bertin "Porque mi mujer no quiere, que si no..."
                $sexohombre=True
            "Paso de tu culo":
                $ sexomujer = True
                bertin "Chiquilla, vaya modales. Me recuerdas a la Pipi esta..."
                r "¿Estrada?"
                bertin "No, la otra, la del caballo y el mono que caga de memoria."
                r "Pipi Calzashlargash."
                bertin "Esa misma."
                
        pov "Estábamos hablando de la prueba..."
        bertin "Bufff, ¿y ahora que te pongo yo?"
        r "Muy bruto, Norberto."
        montoto "Ay, dios..."
        bertin "¡Ah, ya sé! Tanto que se me conoce por el chistecito del plato de jamón, venid al almacén y os cuento."
        scene jamones with fade
        $ renpy.pause(0.5, hard=True)
        bertin "¿Veis todas estas patas de guarro?"
        r "Se me hace la boca agua."
        bertin "Como a cualquier buen español. Pues hay uno, solo uno, que es un 5J, el resto son jamones buenos pero muy correosos. Los tengo aquí para las fiestas ibicencas que doy todos los jueves."
        bertin "Si quieres mis votos, tendrás que adivinar cual es el jamón de alta calidad."
        r "Eso está chupado."
        
        $ result = renpy.imagemap("images/jamones.jpg", "images/jamones.jpg", [
            (778, 0, 825, 193, "cierto"),  
            (0, 0, 777, 193, "fals1"),
            (836, 0, 1366, 193, "fals2"),
            (0, 194, 1366, 768, "fals3"),
            ], focus="imagemap")
        
        if result == "cierto":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Pleno al quince, ¡crack!"
            bertin "Tienes mis votos. ¿Queréis que os saque una tapita?"
            pov "Tenemos que irnos ya."
            bertin "Pues casi que mejor, porque el que me corta el jamón no sé dónde se ha metido. Seguro que está vagueando. Como es venezolano..."
            $ puntosj +=3
            jump mapa
            
        if result == "fals1":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "Pero ¿sabes qué? Que me da igual. Te voy a dar los votos porque te los mereces. Y como salgan los otros este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            r "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            pov "Lo que va usted a hacer es ilegal. Ha perdido y no debería recibir recompensa por ello."
            bertin "El límite de la legalidad lo marca la moral de los dirigentes y las tragaderas del pueblo."
            r "Y cada día que pasa doy gracias a dios de haber nacido en España."
            r "¿Nos vemos en la montería del próximo domingo?"
            bertin "Allí estaré, campeón."
            $ puntosj +=3
            jump mapa
            
        if result == "fals2":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "Pero ¿sabes qué? Que me da igual. Te voy a dar los votos porque te los mereces. Y como salgan los otros este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            r "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            pov "Lo que va usted a hacer es ilegal. Ha perdido y no debería recibir recompensa por ello."
            bertin "El límite de la legalidad lo marca la moral de los dirigentes y las tragaderas del pueblo."
            r "Y cada día que pasa doy gracias a dios de haber nacido en España."
            r "¿Nos vemos en la montería del próximo domingo?"
            bertin "Allí estaré, campeón."
            $ puntosj +=3
            jump mapa
            
        if result == "fals3":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "Pero ¿sabes qué? Que me da igual. Te voy a dar los votos porque te los mereces. Y como salgan los otros este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            r "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            pov "Lo que va usted a hacer es ilegal. Ha perdido y no debería recibir recompensa por ello."
            bertin "El límite de la legalidad lo marca la moral de los dirigentes y las tragaderas del pueblo."
            r "Y cada día que pasa doy gracias a dios de haber nacido en España."
            r "¿Nos vemos en la montería del próximo domingo?"
            bertin "Allí estaré, campeón."
            $ puntosj +=3
            jump mapa
        
        
        
        
    if ken == True:

        scene cuenca1 with dissolve
        $ renpy.pause(1, hard=True)
        show parejac at center with dissolve
        parcuenca "¡Hola! ¿Qué tal?"
        extend " ¿Folláis?"
        k "Por favor, ese es mi estado natural."
        parcuenca "¡Genial! Aunque solo lo hacemos con parejas heterosexuales."
        k "¿No os vale con Espejo?"
        parcuenca "¿Pero qué clase de depravado eres tú?"
        espejo "Oye, sin faltar."
        k "Esperad, dadme un minuto."
        hide parejac
        k "Oye, [jugador]... Esto va a resultar muy violento pero..."
        $ k("¿Tú qué eres?", interact=False)
        menu:
            "¿En serio?":
                k "Sí, ¿qué pasa?"
                pov "Llevamos un buen rato y no te has dado cuenta de algo tan básico, algo que hasta los mosquitos saben en cuanto entran en una habitación."
                k "Hija o hijo, si no te vistieras con ropa del Primark y llevaras un corte de pelo como dios manda..."
                k "La naturaleza lo dejó bien claro: pelo corto para los chicos, para las chicas pelo largo o media melena si quieres dar a entender que estás receptiva."
                k "Y por tu pelo diría que lo estás pero con ese jersey no puedo ver los montes frutales."
                extend " Y no es plan de lanzarse a lo loco, que hay mucho fan de Europe por ahí suelto a estas alturas de la vida."
                k "Que por cierto, creo que tocarán en las fiestas de Sarón 2017."
                pov "Mira, lo que quieras, pero yo paso."
                pass
            "Soy un tío":
                k "¡Maldición! Nos quedamos sin follar."
                if novalencia == True:
                    pov "Pero si te tiraste a la señora de piedra esa antes. Vaya estómago, por cierto."
                    k "Aquello fueron negocios. Esto lo hubiera hecho por placer."
                    pov "¿No crees que te hubiera ido mejor haciendo carrera en otro trabajo?"
                    k "Lo intenté. Siempre quise ser registrador de la propiedad pero la nota no me llegaba... y tengo un ojo vago."
                pass
            "Vale, voy a hacer como que no me ha ofendido que no te hayas dado cuenta de que soy una mujer":
                k "¡Genial!"
                extend " ¿Follamos?"
                pov "..."
                k "No entre nosotros. Eso, si quieres, al final. Digo con esta pareja."
                pov "Voy a hacer como que no he oído nada."
                
        k "Así no hay manera de aliviar tensiones."
        espejo "Tómate un Tranquimazín."
        k "Ya me tomé un bol entero para desayunar."
        espejo "Eso eran Chocokrispies."
        k "Pues el mismo efecto hacen, además, estamos hablando de follar."
        pov "Será mejor que continuemos nuestro camino."
        k "Lo que no sé es por qué nos han entrado esa pareja de chicos. Quiero decir, para mí es normal porque soy un macho alfa pero con [jugador] y Espejo, que es como mi doble malvado, nunca pensé que pudiera atraer a alguien."
        espejo "Maldita sea, Ken, es ver unas tetas y perder la cabeza."
        pov "Pues lo disimula muy bien cuando sale en televisión."
        espejo "Es que junto a los cereales le suelo poner bromuro. Hoy se me ha olvidado."
        extend " A ver si te crees que el PRESOE pondría al frente de la organización a alguien con un discurso tan vacío."
        scene cuenca4 with fade
        $ renpy.pause(0.5, hard=True)
        k "Cuanto bullicio, ¿no?"
        pov "Pues aquí no hay nadie."
        k "Y sin embargo está ahí. Escucha, escucha."
        stop music 
        play sound "bullicio.ogg"
        $ renpy.pause(4, hard=True)
        stop sound
        show parejad with moveinleft
        $ renpy.pause(0.5, hard=True)
        ana "Perdone, ¿es usted Ken Sánchez?"
        k "Sexy, sexy, lover. En persona."
        pedro "Te hemos reconocido desde el otro lado de la calle y..."
        espejo "No puede follar. Tiene gonorrea."
        k "¡Oye!"
        espejo "Es la única manera de deshacernos de ellos rápidamente."
        ana "No, no es eso lo que íbamos a preguntarle."
        k "¿Entonces?"
        pedro "Tú te presentas a la presidencia del gobierno, ¿verdad?"
        k "Aunque algunos \"críticos\" digan lo contrario, así es."
        ana "Y tienes poder para que se hagan las cosas, ¿no?"
        k "No soy el ratón Pérez, pero algo podré hacer si salgo elegido."
        pedro "Pues mira, ¿podrías arreglarlo para que los condones tuvieran abrefácil? No sé, un tapón, una cremallera o una pestaña. Es que la otra noche comenzamos una caja de 24 y los tuve que tirar todos porque no se podían abrir."
        pedro "Ella quería usar los dientes pero con los piños que tiene, que parece la hija de Drácula, seguro que los rompía o algo y yo soy muy joven para tener un baby que me llame papá y se cague en mis Micromanía."
        k "En cuanto pise el despacho de la Moncloa, crearé una comisión para intentar solucionar el problema."
        ana "Mucha gente te estará agradecida. Mucha."
        k "¿Algo más?"
        pedro "Nada. Nos vamos que va a abrir el pub ya. Suerte con la gonorrea. Eso te echas pólvora en el matojo, una chispa y adiós problemas."
        espejo "Creo que voy a vomitar."
    
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextcu1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextcu2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymcuenca with fade
        show cuñadocuenca at center
        k "¡Hombre, Norberto! Mi Don Luís Mejía particular. ¿Cómo tú por aquí tan lejos de tu fábrica de chochetes?"
        bertin "Ya ves, campeón, las vueltas que da la vida."
        k "Pues han debido de girarla mucho para encontrarte en este lugar en mitad de ninguna parte."
        bertin "Muchacho, no digas eso, que esto es mú bonito."
        bertin "Mis huevos colganderos han hecho más por este pueblo que las casas colgantes."
        extend " Gracias a mí, 4786 mujeres y algún que otro hombre confuso saben dónde queda en el mapa."
        bertin "Y luego está el boca a boca. No culo a boca. Eso nunca, chiquillo."
        bertin "Las autoridades locales, conocedoras de este hecho, me ofrecieron la dirección de este gimnasio y aquí estoy, echando las vacaciones más bien que ná."        
        k "¿Está Arevalo también? Me gustaría saludarle."
        bertin "Le he mandado a comprar el pan hace una hora y todavía no ha vuelto."
        bertin "Estará en la Plaza Mayor pidiendo limosna. Ahora que no puede contar chistes de gangosos tiene que sacar provecho de su arte. Dice que así se siente útil."
        k "Es que este país ya no es lo que era."
        bertin "Pues tú tienes mucha mano, gachón. A ver si haces algo cuando seas presidente."
        k "Será la primera medida que tome, Norberto. Los chistes de gangosos recuperarán el status que nunca debieron perder."
        k "Dicho lo cual, para que se apruebe dicha medida tendría que presidir el ejecutivo y ya sabes que estoy aquí para pedirte tus votos."
        bertin "No se hable más, aquí mismo los tenía guardados esperando que vinieras."
        k "¿Te ha molestado alguno de mis rivales?"
        bertin "Vino El Coletas, pero le di un manguerazo y salió huyendo como los gatos. ¡Jajajaja!"
        bertin "Y a M. Rajao no le he visto. No te voy a engañar, le hubiera dado los votos a él."
        bertin "Vamos a mi bodega. Te invito a un vinito."
        pov "Disculpe, siento ser la voz discordante pero por algo me estoy perdiendo la final de Fútbol Australiano."
        extend " Según la ley usted debe someter al candidato, aquí presente, a una prueba con la que ganarse su apoyo. De lo contrario, incurriría en flagrante delito, blablabla, blablabla."
        bertin "Caray con el abogado del estado..."
        extend " Bufff, ¿y ahora que te pongo yo?"
        espejo "Muy bruto, Norberto."
        bertin "¡Ah, ya sé! Tanto que se me conoce por el chistecito del plato de jamón, venid al almacén y os cuento."
        scene jamones with fade
        $ renpy.pause(0.5, hard=True)
        bertin "¿Veis todas estas patas de guarro?"
        k "Se me hace la boca agua."
        bertin "Como a cualquier buen español. Pues hay uno, solo uno, que es un 5J, el resto son jamones buenos pero muy correosos. Los tengo aquí para las fiestas ibicencas que doy todos los jueves."
        bertin "Si quieres mis votos, tendrás que adivinar cual es el jamón de alta calidad."
        k "Eso está chupado."        
        
        $ result = renpy.imagemap("images/jamones.jpg", "images/jamones.jpg", [
            (778, 0, 825, 193, "cierto"),  
            (0, 0, 777, 193, "fals1"),
            (836, 0, 1366, 193, "fals2"),
            (0, 194, 1366, 768, "fals3"),
            ], focus="imagemap")
        
        if result == "cierto":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Pleno al quince... Ya se ve que los bolivarianos seréis unos sinverguenzas y unos criminales, pero el buen gusto por el jamón lo tenéis fino, ¿eh, bribones?"
            bertin "No me queda otra que darte mis votos. Eso sí te digo, como ganes me voy a México, que allí sí que se vive bien."
            $ puntosj +=3
            jump mapa
            
        if result == "fals1":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "Pero ¿sabes qué? Que me da igual. Te voy a dar los votos porque te los mereces. Y como salgan los otros este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            k "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            pov "Lo que va usted a hacer es ilegal. Ha perdido y no debería recibir recompensa por ello."
            bertin "El límite de la legalidad lo marca la moral de los dirigentes y las tragaderas del pueblo."
            k "Y cada día que pasa doy gracias a dios de haber nacido en España."
            k "¿Nos vemos en la montería del próximo domingo?"
            bertin "Allí estaré, campeón."
            $ puntosj += 3
            jump mapa
            
        if result == "fals2":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "Pero ¿sabes qué? Que me da igual. Te voy a dar los votos porque te los mereces. Y como salgan los otros este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            k "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            pov "Lo que va usted a hacer es ilegal. Ha perdido y no debería recibir recompensa por ello."
            bertin "El límite de la legalidad lo marca la moral de los dirigentes y las tragaderas del pueblo."
            k "Y cada día que pasa doy gracias a dios de haber nacido en España."
            k "¿Nos vemos en la montería del próximo domingo?"
            bertin "Allí estaré, campeón."
            $ puntosj += 3
            jump mapa
            
        if result == "fals3":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "Pero ¿sabes qué? Que me da igual. Te voy a dar los votos porque te los mereces. Y como salgan los otros este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            k "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            pov "Lo que va usted a hacer es ilegal. Ha perdido y no debería recibir recompensa por ello."
            bertin "El límite de la legalidad lo marca la moral de los dirigentes y las tragaderas del pueblo."
            k "Y cada día que pasa doy gracias a dios de haber nacido en España."
            k "¿Nos vemos en la montería del próximo domingo?"
            bertin "Allí estaré, campeón."
            $ puntosj += 3
            jump mapa
        
    if coletas == True:

        scene cuenca5 with dissolve
        $ renpy.pause(1, hard=True)
        if barcelona == True:
            if yausado == False:
                stalin "Salud, camaradas... ¿Puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        show parejad at center with dissolve
        pedro "¡Hola! ¿Qué tal?"
        extend " ¿Folláis?"
        c "¿Con uno mismo cuenta?"
        stalin "Metafóricamente, mucho."
        pov "Ahora ya entiendo lo de \"poliamor\"..."
        ana "¿No estáis aquí por lo del congreso?"
        stalin "Primera noticia que tengo de que se celebre algo significativo en este monumento a la piedra."
        pedro "Pues hace nada que comenzó el IIIer encuentro \"Miremos a Cuenca\" de Jóvenes Swingers."
        c "¿Y cómo no me he enterado de su existencia antes?"
        stalin "Imagino que los que tengan pareja estarán mejor informados de estos acontecimientos."
        c "Qué te gusta hacer sangre..."
        stalin "Te dije que la dejaras, que te la iba a jugar. Y al final, mira, te termina dejando ella a ti y por ello perdemos el voto de los aspirantes al trono de MYHYV."
        pov "¿Y cómo os conocísteis? Siempre me ha llamado la atención el mundo swinger, pero las chicas que conozco son muy reacias."
        ana "En una cafetería de un pueblecito del interior. Yo estaba mojando un trozo de bizcocho en un chocolate riquísimo cuando se me acercó con el portátil y se me sentó al lado."
        ana "Me conquistó enseñándome vídeos de la Eurocopa durante cuatro horas. En una mesa cercana una pareja no dejaba de criticarnos pero me dio igual. Le vi el Rólex en la muñeca y me dije: \"Mari, con este tienes futuro, pero tendrás que buscarte la forma de tirarte a otros que sean más normales porque tu cuerpo pide mucha marcha.\""
        pedro "Y aquí estamos."
        stalin "Una historia muy conmovedora. Si Shakespeare estuviera vivo hubiera desechado esa pastelada de Romeo y Julieta y hubiera inmortalizado vuestro romance."
        ana "¿Verdad que sí?"
        stalin "..."
        stalin "No sé ni para qué me molesto en abrir la boca en este país."
        c "Tenemos que irnos. Mucha suerte y... "
        extend " No sé qué se dice en estos casos... ¿Follad bien?"
        pedro "¡Gracias! Se intentará. Normalmente la que folla es ella. Yo mientras estoy en la habitación de al lado seleccionando las mejores jugadas de la Liga para enseñárselas después."
        scene cuenca4 with wipeleft
        $ renpy.pause(0.5, hard=True)
        stalin "Luego la gente se extrañará de la baja natalidad del país. Sois todos unos desviados."
        pov "¿Tú no tienes hijos?"
        stalin "Tenía... Un desastre. Para que luego digan que la genética es una ciencia. Es una lotería. Me salió una capitalista y un pacifista."
        stalin "Con lo guapo que era yo de joven. ¿Tú has visto fotos mías de la época? Las tenía que tirar al Volga para que me dejaran en paz."
        pov "Algo me han comentado, sí."
        c "¿Qué decís? "
        extend "No os oigo."
        c "Cuanto bullicio, ¿no?"
        pov "Pues aquí no hay nadie."
        c "Y sin embargo el ambiente es ensordecedor. Escucha, escucha."
        stop music 
        play sound "bullicio.ogg"
        $ renpy.pause(4, hard=True)
        stop sound
        pov "Un poco exagerado sí que eres."
        show parejac with moveinleft
        $ renpy.pause(0.5, hard=True)
        parcuenca "Perdona, ¿tú eres el Coletas?"
        c "El auténtico líder de la izquierda. Que no os diga lo contrario gente sin pelo."
        parcuenca "Te hemos reconocido desde el otro lado de la calle y..."
        stalin "No puede follar. Tiene gonorrea."
        c "¡Oye!"
        stalin "Es la única manera de deshacernos de ellos rápidamente."
        parcuenca "No, no es eso lo que íbamos a preguntarle."
        c "¿Entonces?"
        parcuenca "Tú te presentas a la presidencia del gobierno, ¿verdad?"
        c "Aunque algunos críticos digan lo contrario, así es."
        parcuenca "Y tienes poder para que se hagan las cosas, ¿no?"
        c "No soy un Máster del Universo pero algo podré hacer si salgo elegido."
        parcuenca "Pues mira, ¿podrías arreglarlo para que los condones tuvieran abrefácil? No sé, un tapón, una cremallera o una pestaña. Es que la otra noche comenzamos una caja de 24 y los tuve que tirar todos porque no se podían abrir."
        parcuenca "Ella quería usar los dientes pero con los piños que tiene, que parece la hija de Drácula, seguro que los rompía o algo y yo soy muy joven para tener un baby que me llame papá y se cague en mis Micromanía."
        c "En cuanto pise el despacho de la Moncloa, crearé una comisión para intentar solucionar el problema."
        parcuenca "Mucha gente te estará agradecida. Mucha."
        c "¿Algo más?"
        parcuenca "Nada. Nos vamos que va a abrir el pub ya. Suerte con la gonorrea. Eso te echas pólvora en el matojo, una chispa y adiós problemas."
        stalin "Creo que voy a vomitar."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextcu1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextcu2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymcuenca with fade
        $ renpy.pause(0.5, hard=True)
        show cuñadocuenca at center
        $ renpy.pause(0.5, hard=True)
        c "Buenas noches, señor."
        bertin "¡Oh, El Coletas! Qué asco, qué pestilencia, qué desagrado. Vete antes de que me de un vahido y pierda la facultad de uso de la pituitaria."
        pov "Disculpe, siento ser la voz discordante pero por algo me estoy perdiendo la final de Fútbol Australiano."
        extend " Según la ley usted debe someter al candidato, aquí presente, a una prueba con la que ganarse su apoyo o perderlo. De lo contrario, incurriría en flagrante delito, blablabla, blablabla."        
        bertin "Caray con el abogado del estado..."
        stalin "Ya me gustaría que lo fuera. Sería más manejable. Es un don nadie o una doña nadie, no lo tengo muy claro."
        bertin "Oye, pues eso a mí me interesa. ¿Te apetece tomarte una copita en mi buhardilla? Está mal iluminada pero es muy cómoda."
        menu:
            "Tengo más rabo que espalda":
                bertin "Estuve en Tailandia hace diez años. No me voy a asustar."
                c "¿Y qué fuiste a hacer allí?"
                bertin "Digamos que aprendí a jugar al golf sin palo."
                stalin "¿También eres un swinger de esos?"
                bertin "Porque mi mujer no quiere, que si no..."
                $sexohombre=True
            "Paso de tu culo":
                $ sexomujer = True
                bertin "Chiquilla, vaya modales. Me recuerdas a la Pipi esta..."
                c "¿Estrada?"
                bertin "No, la otra, la del caballo y el mono que caga de memoria."
                c "Pipi Calzaslargas."
                bertin "Esa misma."
        pov "Estábamos hablando de la prueba..."
        bertin "Bufff, ¿y ahora qué te pongo yo?"
        bertin "¡Ah, ya sé! Tanto que se me conoce por el chistecito del plato de jamón, venid al almacén y os cuento."
        scene jamones with fade
        $ renpy.pause(0.5, hard=True)
        bertin "¿Veis todas estas patas de guarro?"
        c "Se me hace la boca agua."
        bertin "Como a cualquier buen español. Mmmm, qué raro... En fin..."
        bertin "Pues hay uno, solo uno, que es un 5J, el resto son jamones buenos pero muy correosos. Los tengo aquí para las fiestas ibicencas que doy todos los jueves."
        bertin "Si quieres mis votos, tendrás que adivinar cuál es el jamón de alta calidad."
        c "Eso está chupado."
        
        $ result = renpy.imagemap("images/jamones.jpg", "images/jamones.jpg", [
            (778, 0, 825, 193, "cierto"),  
            (0, 0, 777, 193, "fals1"),
            (836, 0, 1366, 193, "fals2"),
            (0, 194, 1366, 768, "fals3"),
            ], focus="imagemap")
        
        if result == "cierto":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Pleno al quince... Ya se ve que los bolivarianos seréis unos sinverguenzas y unos criminales, pero el buen gusto por el jamón lo tenéis fino, ¿eh, bribones?"
            bertin "No me queda otra que darte mis votos. Eso sí te digo, como ganes me voy a México, que allí sí que se vive bien."
            $ puntosj +=3
            jump mapa
            
        if result == "fals1":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "No te mereces mis votos porque como salgas elegido, este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            stalin "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            bertin "Ahora idos de aquí antes de que suelte a los perros con rayos láser en la cabeza."
            jump mapa
            
        if result == "fals2":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "No te mereces mis votos porque como salgas elegido, este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            stalin "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            bertin "Ahora idos de aquí antes de que libere los globos con espermicida picante."
            jump mapa
            
        if result == "fals3":
            scene gymcuenca with fade
            $ renpy.pause(0.5, hard=True)
            show cuñadocuenca at center
            bertin "Chiquillo, si se ve a legua que ese es un sencillo 4J..."
            bertin "No te mereces mis votos porque como salgas elegido, este país se va a la mierda."
            bertin "Si vieras la de cosas que me contaba la regidora de \"Contacto con tacto\" mientras nos fumábamos el cigarro de después..."
            stalin "¿De dónde era?"
            bertin "De Mónaco, como los colchones."
            extend " Pero Venezuela, un infierno en la tierra. Lo peor."
            bertin "Ahora idos de aquí antes de que convoque al Demogorgon y os coma la cabeza, aunque tú con ese pelo igual le haces vomitar."
            c "Envidia, lo llaman."
            jump mapa

    
    jump mapa