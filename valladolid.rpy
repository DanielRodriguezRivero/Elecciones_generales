label valladolid:
    $ valladolid = True
    
    #personajes
    define cascabeles = Character("El Toro Cascabeles", color="#000000", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define vega = Character("Manolo de Vega", color="#A18154", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define tortlon = Character("Tortlon", color="#2CC97A", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    #imagenes
    image gymvalladolid = "images/gymvalladolid.jpg"
    image valladolid1 = "images/valladolid1.jpg"
    image valladolid2 = "images/valladolid2.jpg"
    image valladolid3 = "images/valladolid3.jpg"
    image valladolid4 = "images/valladolid4.jpg"
    
    image toro = "images/toro.jpg"
    image cuñadovalladolid = "images/bull.png"
    image vigilante = "images/vigilante.png"
    image vega = "images/vega.png"
    image tortlon = "images/tortlon.png"
    
    image gymtextva1 = Text("{size=40}Gimnasio Shapes",color="#fff", text_align=0.3)
    image gymtextva2 = Text("{size=40}Prohibidos los zurdos",color="#fff", text_align=0.3)
    
    scene travelvalladolid at Pan((0, 0), (300,0), 20.0)
    play music "entradillavalladolid.mp3"
    $ renpy.pause(14, hard=True)
    
    play music "cancionciudad.mp3"
    
    if mrajao == True:
       
        scene valladolid1 with fade
        $ renpy.pause(1, hard=True)
        show tortlon at center with dissolve
        tortlon "Buenas tardes, manguarrianes."
        extend " ¿Queréis comprar alguno de mis cuadros?"
        pov "Yo a ti te conozco..."
        tortlon "Me lo dicen mucho. Quizá de algún salón de cómic, del blog de Mr. Roboto..."
        pov "No, no. Tú salías en la novela visual \"Jim del Espacio Exterior 2\""
        tortlon "En efecto. Acción, misterio, humor... si eso es lo que buscas, no te la recomiendo, pero si quieres maravillarte con lo que la mente humana puede crear a partir de una sobredosis de Panteras Rosa, es tu juego."
        pov "Lo probaré en cuanto termine con este."
        tortlon "No te defraudará."
        tortlon "¿Me compráis algo entonces?"
        pov "Tenemos algo de prisa. Vamos al gimnasio."
        tortlon "Que os vaya bien, majos."
        scene valladolid2 with wiperight
        $ renpy.pause(0.5, hard=True)
        r "Ahora teníamos que tomar esa calle a la derecha, ¿no?"
        pov "..."
        pov "Ah, que me preguntas a mí."
        r "Tú eres nuestro guía."
        pov "¡Si yo en esta ciudad no he estado nunca!"
        r "Como te he visto caminar tan decidido..."
        pov "Es que estaba siguiendo a la rubia esa de los vaqueros-tanga."
        extend " Y si nos quedamos mucho tiempo de charla voy a perder de vista su trasero cincelado en tela vaquera."
        vega "Pssst."
        r "¿Qué ha sido eso?"
        vega "Psst, psst."
        montoto "Parece que viene de esa callejuela."
        r "Vayamos a mirar."
        pov "Sí, claro. Vamos a meternos en un callejón oscuro por el que no camina nadie desde la muerte de Fernando el Católico. ¿Qué puede salir mal?"
        scene valladolid3 with dissolve
        $ renpy.pause(1, hard=True)
        show vega at center with moveintop
        r "¡Jesús, qué susto!"
        vega "Perdonen ustedes, pero la discreción es necesaria."
        r "¿Se oculta de algo?"
        extend " ¿No será un criminal?"
        vega "Así me han llamado muchos, pero nada más lejos de la realidad."
        vega "Me llamo Manolo de Vega y soy el último torero sobre la Tierra."
        montoto "Eso es imposible. Espartaco torea mañana en Teruel."
        vega "¡Eso es mentira! Teruel no existe y Espartaco murió hace siglos. Además, no era torero por mucho que tuviera un buen estoque."
        vega "Los toreros hemos sido exterminados. Desde que se prohibieron las corridas en toda España, nos hemos convertido en una especie en vías de extinción."
        vega "Languidecimos. Vimos el brillo de un decreto ley cruzar la península a toda velocidad, inconscientes de lo que significaría su impacto sobre el código civil."
        vega "Dos días después de la prohibición, las calles se llenaron de toreros que no sabían qué hacer con sus vidas. Muchos se escudaron en la bebida, pero Bertín cerró sus bodegas horas después."
        vega "Era el único que nos hacía precio."
        vega "Muchos otros decidieron montar un negocio. Las tiendas de souvenirs de toreo proliferaron como otrora lo hicieran los que compraban oro. El resultado fue el mismo: la quiebra."
        vega "Ya fue mala suerte que a los japoneses se los comiera Godzilla. Eran los únicos turistas interesados en nuestros productos."
        vega "Por si no fuera suficiente, cuando íbamos por la calle la gente no nos reconocía. Ni siquiera se dignaban a insultarnos. Habíamos pasado a un plano irrelevante de la existencia."
        vega "Poco a poco fuimos desapareciendo sin dejar rastro."
        vega "Yo logré sobrevivir como extra en el mundo del espectáculo. Intenté enchufar a El Fandi, pero estaba demasiado gordo y además, no había tanta demanda en la industria del entretenimiento para tanto torero."
        vega "Con uno sobraba."
        vega "¡Cuidado! ¡Un toro de vigilancia!"
        hide vega with moveouttop
        show vigilante at left with moveinright
        $ renpy.pause(0.5, hard=True)
        hide vigilante
        $ renpy.pause(0.5, hard=True)
        show vega with moveintop
        r "¿Qué fue eso?"
        vega "Esa es la segunda parte de la historia."
        vega "Cuando nuestro número no suponía ya ninguna amenaza para su especie, Esponjoso, el rey de los toros, dio la orden 69: cazad a todos los toreros."
        vega "Se crearon escuadrones de la muerte de toros que recorrieron las calles imponiendo su reinado de terror y de sangre."
        vega "A Luís Mejías le tiraron dentro de un contenedor de reciclaje de papel. El Peteneras fue devorado vivo y El niño de la llana y Pepinito fueron esclavizados en la factoría de CDs pirata que los toros tienen en Villablino y con la que ayudan a financiar al terrorismo y Al Qaeda."
        r "¡Cielos! Desconocía por completo su problemática."
        vega "Nadie pensó nunca en los toreros. Yo logré escapar gracias a mis conocimientos de ocultación, los cuales adquirí al mirar fijamente el cráneo de Peter O´toole durante el rodaje de \"Misión Imposible 4\"."
        vega "La mejor de la saga. Y no porque salga yo."
        montoto "¿Cómo es Tom Cruise?"
        vega "Más alto de lo que pensaba."
        montoto "¿Y paga sus impuestos?"
        vega "A tanto no llegué."
        pov "Nos disculpa un momento, señor De Vega."
        vega "Disculpados están."
        hide vega with moveouttop
        pov "Vaya chiflado el hombre este."
        r "¿Pero qué dices, [jugador]?"
        pov "Está claro que se ha montado una película en su cabeza, y de las malas."
        r "¿Cómo va a inventarse alguien una historia tan dramática?"
        show vega with moveintop
        vega "Creo que están hablando de mí."
        pov "¡Qué va!"
        vega "No me gusta que me mientan..."
        extend "Ni que me llamen loco."
        vega "¿Acaso haría un loco esto?"
        hide vega
        show vega:
            zoom 1.0
            linear 1.0 zoom 1.5
            linear 1.0 zoom 1.0
            repeat
        vega "¿O esto?"
        hide vega
        show vega:
            xzoom .75 yzoom .75
            linear 1.0 xzoom 1.25 yzoom .75
            linear 1.0 xzoom .75 yzoom 1.25
            repeat
        vega "¿O incluso esto?"
        hide vega
        show vega:
            xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
            rotate 0
            linear 4.0 rotate 360
            repeat
        vega "¿Hola?"
        vega "¡Maldición! Se han ido. Tendría que haberles pedido el euro directamente."
        scene valladolid4 with wipeleft
        pov "Como la próxima vez no me hagáis caso y os pongáis a hablar con desconocidos, os dejo solos y me vuelvo a mi casa."
        r "Pobre hombre. Sigo diciendo que es una víctima de la sociedad."
        pov "Vamos directo al gimnasio. Allí hay un cartel que nos indica su ubicación."
        
        scene black with dissolve
        show gymtextva1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextva2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene black
        montoto "Esto está muy negro."
        r "Como Drácula..."
        montoto "Tantead las paredes a ver si encontramos el interruptor de la luz."
        $ renpy.pause(2,hard=True)
        play sound "click0.wav"
        scene gymvalladolid with fade
        show cuñadovalladolid at center
        r "Montoto, ¡un toro! ¡No le mires a los ojos!"
        montoto "Es al color rojo a lo que responden."
        pov "Yo juraría que es por el movimiento por lo que embisten."
        r "pues deja de moverte como si quisieras morir hoy mismo."
        pov "¡Si solo me estoy rascando!"
        r "eso es lo que digo yo a mi mujer cuando me pilla con..."
        cascabeles "¿Váis a estar mucho rato así? Tengo cosas que hacer, ¿sabéis?"
        r "Disculpe usted, señor Toro."
        cascabeles "Típico de los humanos, cosificando a los animales. No soy solo un toro, que también. Soy un ciudadano animal y Cascabeles me llaman."
        r "Disculpe usted, Señor Cascabeles."
        cascabeles "Llámeme Cas, como el whisky." 
        extend " ¿Vienen a buscar mi cabeza? Que no les engañen mis modales, les advierto que cara pagarán su osadía."
        montoto "Descuide, solo queremos pedirle que nos dé sus tres votos para las elecciones al gobierno del país."
        cascabeles "Mmmmuuuu ¿Y piensan que se los dará así de primeras? ¿Que el apoyo de un toro vale tan poco que lo va regalando al primero que lo reclama?" 
        montoto "Desde luego que no, por eso queremos saber qué podemos hacer para complacerle."
        cascabeles "Han de saber vuecencias que solo, por convicción y naturaleza, a un tipo de persona le puedo dar mi voto."
        extend " Por eso he aquí mi prueba: ¿dónde banderillearían a este congénere de quien les habla para ahorrarle sufrimiento?"
        $ result = renpy.imagemap("images/toro.jpg", "images/toro.jpg", [
            (357, 202, 1155, 682, "toro2"),  
            (0, 0, 1269, 209, "torolibre"),
            (1139, 0, 1366, 768, "torolibre"),
            (0, 0, 260, 768, "torolibre"),
            (0, 412, 497, 768, "torolibre"),
            (0, 690, 1366, 768, "torolibre"),
            ], focus="imagemap")
        
        if result == "toro2":
            cascabeles "Ya veo. Para usted banderillear a un toro es necesario."
            pov "La hemos cagado."
            cascabeles "Les doy tres segundos para que salgan de aquí. Den gracias a que me enceré los cuernos justo antes de que entraran."
            scene valladolid4 with fade
            pov "Nada, unos votos que se diluyen en la bruma."
            r "Pues como los que votan a Tox."
            jump mapa
            
        if result == "torolibre":
            cascabeles "Son ustedes hombres de bien. Que no se diga que Cascabeles no cumple su palabra."
            cascabeles "Suyos son los votos."
            r "Muchas gracias, señor toro."
            $ puntosj +=3
            jump mapa
        
        

        

        
    if ken == True:
     
        scene valladolid1 with fade
        $ renpy.pause(1, hard=True)
        show tortlon at center with dissolve
        tortlon "Buenas tardes, manguarrianes."
        extend " ¿Queréis comprar alguno de mis cuadros?"
        pov "Yo a ti te conozco..."
        tortlon "Me lo dicen mucho. Quizá de algún salón de cómic, del blog de Mr. Roboto..."
        pov "No, no. Tú salías en la novela visual \"Jim del Espacio Exterior 2\""
        tortlon "En efecto. Acción, misterio, humor... si eso es lo que buscas, no te la recomiendo, pero si quieres maravillarte con lo que la mente humana puede crear a partir de una sobredosis de Panteras Rosa, es tu juego."
        pov "Lo probaré en cuanto termine con este."
        tortlon "No te defraudará."
        tortlon "¿Me compráis algo entonces?"
        pov "Tenemos algo de prisa. Vamos al gimnasio."
        tortlon "Que os vaya bien, majos."
        scene valladolid2 with dissolve
        $ renpy.pause(0.5, hard=True)
        r "Ahora teníamos que tomar esa calle a la derecha, ¿no?"
        pov "..."
        pov "Ah, que me preguntas a mí."
        r "Tú eres nuestro guía."
        pov "Si yo en esta ciudad no he estado nunca."
        r "Como te he visto caminar tan decidido..."
        pov "Es que estaba siguiendo a la rubia esa de los vaqueros-tanga."
        extend " Y si nos quedamos mucho tiempo de charla voy a perder de vista su trasero cincelado en tela vaquera."
        enigma "Pssst."
        r "¿Qué ha sido eso?"
        enigma "Psst, psst."
        montoto "Parece que viene de ese callejón."
        r "Vayamos a mirar."
        pov "Sí, claro. Vamos a meternos en un callejón oscuro por el que no pasa nadie. ¿Qué puede salir mal?"
        scene valladolid3 with dissolve
        $ renpy.pause(1, hard=True)
        show vega at center with moveintop
        
        scene valladolid2 with wiperight
        $ renpy.pause(0.5, hard=True)
        k "Ahora teníamos que tomar esa calle a la izquierda, ¿no?"
        pov "..."
        pov "Ah, que me preguntas a mí."
        k "Tú eres el que está en cabeza de la expedición."
        pov "¡Si yo en esta ciudad no he estado nunca!"
        k "Como te he visto caminar tan decidido..."
        pov "Es que estaba siguiendo a la rubia esa de los vaqueros-tanga."
        extend " Y si nos quedamos mucho tiempo de charla voy a perder de vista su trasero cincelado en tela vaquera."
        enigma "Pssst."
        k "¿Qué ha sido eso?"
        enigma "Psst, psst."
        espejo "Parece que viene de esa callejuela."
        k "Vayamos a mirar."
        pov "Sí, claro. Vamos a meternos en un callejón oscuro por el que no camina nadie desde la muerte de Fernando el Católico. ¿Qué puede salir mal?"
        scene valladolid3 with dissolve
        $ renpy.pause(1, hard=True)
        show vega at center with moveintop
        k "¡Jesús, qué susto!"
        vega "Perdonen ustedes, pero la discreción es necesaria."
        k "¿Se oculta de algo?"
        extend " ¿También cree que Susana va tras su cabeza?"
        vega "Muchas mujeres han yacido en mi cama, mas ninguna se llamaba Susana."
        vega "Me llamo Manolo de Vega y soy el último torero sobre la Tierra."
        espejo "Eso es imposible. Espartaco torea mañana en Teruel."
        vega "¡Eso es mentira! Teruel no existe y Espartaco murió hace siglos. Además, no era torero por mucho que tuviera un buen estoque."
        vega "Los toreros hemos sido exterminados. Desde que se prohibieron las corridas en toda España, nos hemos convertido en una especie en vías de extinción."
        vega "Languidecimos. Vimos el brillo de un decreto ley cruzar la península a toda velocidad, inconscientes de lo que significaría su impacto sobre el código civil."
        vega "Dos días después de la prohibición, las calles se llenaron de toreros que no sabían qué hacer con sus vidas. Muchos se escudaron en la bebida, pero Bertín cerró sus bodegas horas después."
        vega "Era el único que nos hacía precio."
        vega "Muchos otros decidieron montar un negocio. Las tiendas de souvenirs de toreo proliferaron como otrora lo hicieran los que compraban oro. El resultado fue el mismo: la quiebra."
        vega "Ya fue mala suerte que a los japoneses se los comiera Godzilla. Eran los únicos turistas interesados en nuestros productos."
        vega "Por si no fuera suficiente, cuando íbamos por la calle la gente no nos reconocía. Ni siquiera se dignaban a insultarnos. Habíamos pasado a un plano irrelevante de la existencia."
        vega "Poco a poco fuimos desapareciendo sin dejar rastro."
        vega "Yo logré sobrevivir como extra en el mundo del espectáculo. Intenté enchufar a El Fandi, pero estaba demasiado gordo y además, no había tanta demanda en la industria del entretenimiento para tanto torero."
        vega "Con uno sobraba."
        vega "¡Cuidado! ¡Un toro de vigilancia!"
        hide vega with moveouttop
        show vigilante at left with moveinright
        $ renpy.pause(0.5, hard=True)
        hide vigilante
        $ renpy.pause(0.5, hard=True)
        show vega with moveintop
        k "¿Qué ha sido eso?"
        vega "Esa es la segunda parte de la historia."
        vega "Cuando nuestro número no suponía ya ninguna amenaza para su especie, Esponjoso, el rey de los toros, dio la orden 69: cazad a todos los toreros."
        vega "Se crearon escuadrones de la muerte de toros que recorrieron las calles imponiendo su reinado de terror y de sangre."
        vega "A Luís Mejías le tiraron dentro de un contenedor de reciclaje de papel. El Peteneras fue devorado vivo y El niño de la llana y Pepinito fueron esclavizados en la factoría de CDs pirata que los toros tienen en Villablino y con la que ayudan a financiar al terrorismo y Al Qaeda."
        k "¡Caray! Desconocía por completo su problemática."
        vega "Nadie pensó nunca en los toreros. Yo logré escapar gracias a mis conocimientos de ocultación, los cuales adquirí al mirar fijamente el cráneo de Peter O´toole durante el rodaje de \"Misión Imposible 4\"."
        vega "La mejor de la saga. Y no porque salga yo."
        espejo "¿Cómo es Tom Cruise?"
        vega "Más bajito de lo que pensaba."
        k "¿Es verdad lo que dicen de los enanos?"
        vega "A tanto no llegué."
        pov "Nos disculpa un momento, señor De Vega."
        vega "Disculpados están."
        hide vega with moveouttop
        pov "Vaya chiflado el hombre este."
        k "¿Pero qué dices, [jugador]?"
        pov "Está claro que se ha montado una película en su cabeza, y de las malas."
        k "¿Cómo va a inventarse alguien una historia tan dramática?"
        show vega with moveintop
        vega "Creo que están hablando de mí."
        pov "¡Qué va!"
        vega "No me gusta que me mientan..."
        extend "Ni que me llamen loco."
        vega "¿Acaso haría un loco esto?"
        hide vega
        show vega:
            zoom 1.0
            linear 1.0 zoom 1.5
            linear 1.0 zoom 1.0
            repeat
        vega "¿O esto?"
        hide vega
        show vega:
            xzoom .75 yzoom .75
            linear 1.0 xzoom 1.25 yzoom .75
            linear 1.0 xzoom .75 yzoom 1.25
            repeat
        vega "¿O incluso esto?"
        hide vega
        show vega:
            xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
            rotate 0
            linear 4.0 rotate 360
            repeat
        vega "¿Hola?"
        vega "¡Maldición! Se han ido. Tendría que haberles pedido el euro directamente."
        scene valladolid4 with wipeleft
        pov "Como la próxima vez no me hagáis caso y os pongáis a hablar con desconocidos, os dejo solos y me vuelvo a mi casa."
        k "Pobre hombre. Como socialista, me comprometo a crear una comisión que estudie su situación en busca de una solución."
        pov "Vamos directo al gimnasio. Allí hay un cartel que nos indica su ubicación."
        scene black with dissolve
        show gymtextva1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextva2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene black
        espejo "Esto está muy negro."
        k "Como Drácula..."
        espejo "Tantead las paredes a ver si encontramos el interruptor de la luz."
        $ renpy.pause(2,hard=True)
        play sound "click0.wav"
        scene gymvalladolid with fade
        show cuñadovalladolid at center
        k "¡¡Ondiá, un torero!!"
        cascabeles "Oiga, sin insultar. Soy un toro y Cascabeles me llaman."
        k "Disculpe usted, Señor Cascabeles."
        cascabeles "Llámeme Cas, como el whisky." 
        extend " ¿Vienen a buscar mi cabeza? Que no les engañen mis modales, les advierto que cara pagarán su osadía."
        espejo "Descuide, solo queremos pedirle que nos dé sus tres votos para las elecciones al gobierno del país."
        cascabeles "Mmmmuuuu ¿Y piensan que se los dará así de primeras? ¿Que el apoyo de un toro vale tan poco que lo va regalando al primero que lo reclama?" 
        espejo "Desde luego que no, por eso queremos saber qué podemos hacer para complacerle."
        cascabeles "Han de saber vuecencias que solo, por convicción y naturaleza, a un tipo de persona le puedo dar mi voto."
        extend " Por eso he aquí mi prueba: ¿dónde banderillearían a este congénere de quien les habla para ahorrarle sufrimiento?"
        $ result = renpy.imagemap("images/toro.jpg", "images/toro.jpg", [
            (357, 202, 1155, 682, "toro2"),  
            (0, 0, 1269, 209, "torolibre"),
            (1139, 0, 1366, 768, "torolibre"),
            (0, 0, 260, 768, "torolibre"),
            (0, 412, 497, 768, "torolibre"),
            (0, 690, 1366, 768, "torolibre"),
            ], focus="imagemap")
        
        if result == "toro2":
            cascabeles "Ya veo. Para usted banderillear a un toro es necesario."
            pov "La hemos cagado."
            cascabeles "Les doy tres segundos para que salgan de aquí. Den gracias a que me enceré los cuernos justo antes de que entraran."
            scene valladolid4 with fade
            pov "Nada, unos votos que se diluyen en la bruma."
            k "Pues como los que votan a los demás."
            jump mapa
            
        if result == "torolibre":
            cascabeles "Son ustedes hombres de bien. Que no se diga que Cascabeles no cumple su palabra."
            cascabeles "Suyos son los votos."
            k "Muchas gracias, señor toro."
            $ puntosj +=3
            jump mapa
        
    if coletas == True:
  
        scene valladolid1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Salud, camaradas... ¿Puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolución."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        $ renpy.pause(1, hard=True)
        show tortlon at center with dissolve
        tortlon "Buenas tardes, manguarrianes."
        extend " ¿Queréis comprar alguno de mis cuadros?"
        pov "Yo a ti te conozco..."
        tortlon "Me lo dicen mucho. Quizá de algún salón de cómic, del blog de Mr. Roboto..."
        pov "No, no. Tú salías en la novela visual \"Jim del Espacio Exterior 2\""
        tortlon "En efecto. Acción, misterio, humor... si eso es lo que buscas, no te la recomiendo, pero si quieres maravillarte con lo que la mente humana puede crear a partir de una sobredosis de Panteras Rosa, es tu juego."
        pov "Lo probaré en cuanto termine con este."
        tortlon "No te defraudará."
        tortlon "¿Me compráis algo entonces?"
        pov "Tenemos algo de prisa. Vamos al gimnasio."
        tortlon "Que os vaya bien, majos."
        scene valladolid2 with wiperight
        $ renpy.pause(0.5, hard=True)
        k "Ahora teníamos que girar en esa plaza, ¿no?"
        pov "..."
        pov "Ah, que me preguntas a mí."
        c "Tú eres el primus inter pares de este viaje."
        pov "¡Si yo en esta ciudad no he estado nunca!"
        c "Como te he visto caminar tan decidido..."
        pov "Es que estaba siguiendo a la rubia esa de los vaqueros-tanga."
        extend " Y si nos quedamos mucho tiempo de charla voy a perder de vista su trasero cincelado en tela vaquera."
        enigma "Pssst."
        c "¿Qué ha sido eso?"
        enigma "Psst, psst."
        stalin "Parece que viene de esa callejuela."
        c "Vayamos a mirar."
        pov "Sí, claro. Vamos a meternos en un callejón oscuro por el que no camina nadie desde la muerte de Fernando el Católico. ¿Qué puede salir mal?"
        scene valladolid3 with dissolve
        $ renpy.pause(1, hard=True)
        show vega at center with moveintop
        c "¡Hostia, qué susto! Ni que fueras Spiderman, macho."
        vega "Perdonen ustedes, pero la discreción es necesaria."
        c "¿De qué te estás escondiendo?"
        extend " ¿Te oprime el patriarcado rancio por vestir como un transexual?"
        vega "¿Qué tiene de malo mi aspecto?"
        c "¡Esa es la actitud!"
        vega "Me llamo Manolo de Vega y soy el último torero sobre la Tierra."
        stalin "¿Torero? ¿No los prohibió la cheka de Barcelona?"
        vega "En efecto, así ocurrió. Fue la primera en tomar la mortal decisión."
        vega "Los toreros hemos sido exterminados. Desde que se prohibieron las corridas en toda España, nos hemos convertido en una especie en vías de extinción."
        vega "Languidecimos. Vimos el brillo de un decreto ley cruzar la península a toda velocidad, inconscientes de lo que significaría su impacto sobre el código civil."
        vega "Dos días después de la prohibición, las calles se llenaron de toreros que no sabían qué hacer con sus vidas. Muchos se escudaron en la bebida, pero Bertín cerró sus bodegas horas después."
        vega "Era el único que nos hacía precio."
        vega "Muchos otros decidieron montar un negocio. Las tiendas de souvenirs de toreo proliferaron como otrora lo hicieran los que compraban oro. El resultado fue el mismo: la quiebra."
        vega "Ya fue mala suerte que a los japoneses se los comiera Godzilla. Eran los únicos turistas interesados en nuestros productos."
        vega "Por si no fuera suficiente, cuando íbamos por la calle la gente no nos reconocía. Ni siquiera se dignaban a insultarnos. Habíamos pasado a un plano irrelevante de la existencia."
        vega "Poco a poco fuimos desapareciendo sin dejar rastro."
        vega "Yo logré sobrevivir como extra en el mundo del espectáculo. Intenté enchufar a El Fandi, pero estaba demasiado gordo y además, no había tanta demanda en la industria del entretenimiento para tanto torero."
        vega "Con uno sobraba."
        vega "¡Cuidado! ¡Un toro de vigilancia!"
        hide vega with moveouttop
        show vigilante at left with moveinright
        $ renpy.pause(0.5, hard=True)
        hide vigilante
        $ renpy.pause(0.5, hard=True)
        show vega with moveintop
        pov "¿Qué hace un toro corriendo libre por las calles?"
        vega "Esa es la segunda parte de la historia."
        vega "Cuando nuestro número no suponía ya ninguna amenaza para su especie, Esponjoso, el rey de los toros, dio la orden 69: cazad a todos los toreros."
        vega "Se crearon escuadrones de la muerte de toros que recorrieron las calles imponiendo su reinado de terror y de sangre."
        vega "A Luís Mejías le tiraron dentro de un contenedor de reciclaje de papel. El Peteneras fue devorado vivo y El niño de la llana y Pepinito fueron esclavizados en la factoría de CDs pirata que los toros tienen en Villablino y con la que ayudan a financiar al terrorismo y Al Qaeda."
        c "¡Señor Toro, aquí hay un opositor!"
        vega "¡Maldito, me has traicionado!"
        show vega at left with move
        $ renpy.pause(0.5, hard=True)
        show vigilante at right with moveinright
        vega "¡Asesino! Cara venderé mi vida."
        vega "Que nadie diga que Manolo de Vega nunca enfrentó a la muerte con valor."
        show vega at center with move
        show vigilante at center with move
        scene valladolid4 with fade
        pov "Como la próxima vez no me hagáis caso y os pongáis a hablar con desconocidos, os dejo solos y me vuelvo a mi casa."
        c "Al menos hemos realizado una buena acción y hemos librado al mundo de un sanguinario asesino."
        stalin "Di que sí."
        pov "Vamos directo al gimnasio. Allí hay un cartel que nos indica su ubicación."
        scene black with dissolve
        show gymtextva1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextva2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene black
        c "Esto está muy negro."
        stalin "Como Drácula..."
        c "Tantead las paredes a ver si encontramos el interruptor de la luz."
        $ renpy.pause(2,hard=True)
        play sound "click0.wav"
        scene gymvalladolid with fade
        show cuñadovalladolid at center
        c "¡¡Ondiá, un torero!!"
        cascabeles "Oiga, sin insultar. Soy un toro y Cascabeles me llaman."
        c "Disculpe usted, Señor Cascabeles."
        cascabeles "Llámeme..." 
        stalin "¿Cas?"
        cascabeles "¿Eres tú, Tango? No me lo puedo creer."
        extend " ¿Vienen a buscar mi cabeza? Que no les engañen mis modales, les advierto que cara pagarán su osadía."
        stalin "Descuide, solo queremos pedirle que nos dé sus tres votos para las elecciones al gobierno del país."
        cascabeles "Mmmmuuuu ¿Y piensan que se los dará así de primeras? ¿Que el apoyo de un toro vale tan poco que lo va regalando al primero que lo reclama?" 
        pov "Desde luego que no, por eso queremos saber qué podemos hacer para complacerle."
        cascabeles "Han de saber vuecencias que solo, por convicción y naturaleza, a un tipo de persona le puedo dar mi voto."
        extend " Por eso he aquí mi prueba: ¿dónde banderillearían a este congénere de quien les habla para ahorrarle sufrimiento?"
        $ result = renpy.imagemap("images/toro.jpg", "images/toro.jpg", [
            (357, 202, 1155, 682, "toro2"),  
            (0, 0, 1269, 209, "torolibre"),
            (1139, 0, 1366, 768, "torolibre"),
            (0, 0, 260, 768, "torolibre"),
            (0, 412, 497, 768, "torolibre"),
            (0, 690, 1366, 768, "torolibre"),
            ], focus="imagemap")
        
        if result == "toro2":
            cascabeles "Ya veo. Para usted banderillear a un toro es necesario."
            pov "La hemos cagado."
            cascabeles "Les doy tres segundos para que salgan de aquí. Den gracias a que me enceré los cuernos justo antes de que entraran."
            scene valladolid4 with fade
            pov "Nada, unos votos que se diluyen en la bruma."
            c "Pues como los que votan a OE."
            jump mapa
            
        if result == "torolibre":
            cascabeles "Son ustedes hombres de bien. Que no se diga que Cascabeles no cumple su palabra."
            cascabeles "Suyos son los votos."
            c "Muchas gracias, Cas."
            $ puntosj +=3
            jump mapa
    
    jump mapa