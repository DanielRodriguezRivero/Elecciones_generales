init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("prueba.ogg", channel="sound", loop="True")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")



label extrarradio:
    $ extrarradio = True
    #personajes
    define naranjito = Character("Nar-an-jito", color="#DB8309", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define pujol = Character("Yoda Pujol", color="#166B1F", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define gabi = Character("Gabriel", color="#5C516B", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image gymextra = "images/gymextra.jpg"
    image extra1 = "images/extra1.png"
    image clara = "images/clara.png"
    image gabi = "images/gabi.png"
    image rivera = "images/rivera.png"
    image extra0 = "images/extra0.jpg"
    image extra2 = "images/extra2.jpg"
    
    image gymtextex1 = Text("{size=40}Gimnasio Pirámides",color="#fff", text_align=0.3)
    image gymtextex2 = Text("{size=40}El primer año solo te cobramos un 3% de la mensualidad",color="#fff", text_align=0.3)
    image gymtextex3 = Text("{size=40}40 años han pasado desde que aquel al que llamaban El Masías llegó a estas tierras para liberarlas de las garras del malvado faraón.\n Desde entonces el pueblo catalan trabaja sin descanso para la creación de su nación, oprimidos por la clase dirigente,\n que en sus discursos hace referencia una y otra vez a esa tierra prometida que parece no llegar nunca\n y que muchos piensas, no es de este mundo.",color="#fff", text_align=0.3)
    
    scene travelextrarradio at Pan((0, 0), (270,0), 20.0)
    play music "entradilla.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "cancionciudadeg.mp3"
    
    if mrajao == True:
        scene black with dissolve
        $ renpy.pause(1, hard=True)
        show extra0 at Pan((0, -600), (0,898), 25.0)
        $ renpy.pause(20, hard=True)
        stop music
        scene extra1 with dissolve
        $ renpy.pause(0.5, hard=True)
        r "No recordaba que el extrarradio fuera así..."
        extend " ¿Qué habrá pasado?"
        montoto "Preguntemos a ese apuesto joven que se remueve inquieto bajo la palmera cuajada de dátiles."
        show rivera at center with dissolve
        naranjito "¡Hola, amigos!"
        naranjito "Un momento..."
        extend " ¡Eres tú! ¡La salvación de la Cataluña Hispana!"
        naranjito "Gracias a los patronos que has venido. La desesperación estaba a punto de llevarme al exprimidor."
        r "Tranquilo, muchacho. Cuéntame. ¿Qué ha pasado aquí?"
        naranjito "Verás, todo iba bien con el Faraón Frankmamón, de la tierra manaba leche y miel y el sol bañaba el delta del Llobregat al llegar la primavera."
        naranjito "Pero la vida de un faraón no es eterna en este mundo y más pronto que tarde tuvo que cruzar el umbral hacia la tierra de los muertos."
        naranjito "Entonces, con el pueblo confuso y sin liderazgo, llegaron ellos... Vinieron en sus naves desde el planeta Zuisa y esclavizaron a los buenos españoles que nos levantábamos todas las mañanas a loar al gobierno central de Madriz."
        naranjito "La vida antes era mucho mejor. Aún recuerdo las canciones alegres que cantábamos en el patio: Boyer, no te arrime a la pared que te va a llená de cal, de cal, del cal... En aquellos tiempos se le tenia poco aprecio a la arena, ¿verdad?"
        naranjito "Lo peor es que estos nuevos dirigentes amenazan con separar Cataluña del resto del imperio. Lo que traerá terribles consecuencias."
        naranjito "Nos echarán de la UEFA, de la FIFA y el Barça tendrá que jugar en la liga de solteros contra casados, y los casados este año vienen fuertes con la incorporacion de Rocha, que al final lo pesco la puri, la hija del pintor." 
        naranjito "El penalty mejor tirado de la historia de Sabadell. Eso me han contado."
        montoto "¿Y la gente no se rebela?"
        naranjito "Están anestesiados con una vieja profecía. El Masias, líder de la tercera vía, les dijo que algún día regresaría, pero me dijo un amigo, que casualmente trabaja en el CESID, que está haciendo chorizos en Berna."
        pov "Un sitio muy extraño para hacer embutido..."
        r "Cada uno lo hace donde puede. No vamos a juzgar a nadie por eso."
        naranjito "Y no tiene intención de venir. Personalmente, creo que todo es un bulo."
        r "No temas. La integridad de la mejor liga del mundo no se verá en peligro mientras yo sea presidente. Dime, ¿dónde se encuentra el líder de esos malvados?"
        naranjito "En la Nave-Pirámide que se ve ahí en el horizonte."
        naranjito "Iría con vosotros, pero va a salir la Plomadas de la piscina y no pienso perdérmelo por nada."
        r "No te preocupes. Llegaremos."
        scene extra2 with wipeleft
        $ renpy.pause(0.5, hard=True)
        show clara at center with moveinright
        show gabi at right with moveinright
        gabi "Perdonen..."
        r "¿Sí?"
        gabi "¿Ha visto a un bote de Lacasitos preocupado por aquí?"
        r "Hemos visto varios, pero estaban todos contentos..."
        gabi "Entonces nos hemos desviado demasiado del camino."
        gabi "Hagan el favor de decirle, si lo ven, que estamos en el parque de la avenida."
        r "Descuide, amigo."
        hide clara with moveoutleft
        $ renpy.pause(0.3, hard=True)
        hide gabi with moveoutleft
        scene black with fade
        show btext2:
            ypos 0.3
            xpos 0.3
        $ renpy.pause(3,hard=True)
        show gymtextex1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextex2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymextra with fade
        r "¡Hola!"
        pujol "Días buenos, visitante."
        r "Usted es... ¿Yoda Pujol?"
        pujol "Cierto ser. Sorprendido te veo."
        r "Me esperaba a alguien más... "
        extend "alto."
        pujol "La enfermedad de Azuisa padecer. Reducido mi tamaño un tres por ciento cada años es."
        r "Lo lamento... pero no piense que dándome pena logrará salirse con la suya."
        extend " He venido aquí a liberar a mi pueblo y acabar con tu régimen de tiranía independentista."
        pujol "A conseguir la poltrona tus pasos te han dirigido. Engañarme no puedes."
        pujol "Además, el estado actual de las cosas cosa mía no es. Mi responsabilidad tuve pero ya no. Si el responsable buscáis, al Masías prended."
        r "¿Dónde podemos encontrarle?"
        pujol "En los Alpes cultivando champiñones, creo."
        montoto "Nar-an-jito tenía razón."
        pujol "¿Ese joven por ahí suelto sigue? Hubo un momento en que una brillante carrera como vendedor de seguros pensé que llevaría."
        pujol "Seguir con la política emperrado está."
        r "¿Acaso no tiene derecho?"
        pujol "Como el que Mas."
        r "En cualquier caso, no está bien que explotes a tu gente."
        pujol "Libres ellos son."
        pujol "Al principio, cómo se colocaban las cadenas con la promesa de ser libres, me sorprendía."
        pov "¿Libertad en base a qué?"
        pujol "Al dinero que les pagamos."
        extend " Con viajes a países exóticos, televisiones de plasma enormes y coches de gran cilindrada sueñan. La libertad para ellos eso es."
        pujol "Y lo consiguen. Algunos de ellos, no todos. Para mantener viva la esperanza de prosperidad, el número justo. Como para igualarlos a todos, no los suficientes."
        pujol "En su miseria a gusto están si su vecino en el fango se ahoga. Y ahí están, creyéndose ricos mientras siervos de gleba ser."
        pov "Y alguien se aprovecha..."
        r "En cuanto a los votos..."
        pujol "¿Estando donde estás piensas que alguna oportunidad de que te los de tienes?"
        r "Yo pensaba..."
        pujol "Yo pensaba, yo creía, yo me equivocaba."
        montoto "¿Y ahora qué hacemos?"
        r "Pues no sé. Podrías transformarte y dejarlo inconsciente de un mordisco."
        montoto "¿Tú le has visto? No quiero coger la hepatitis o vete a saber qué."
        pov "Mejor será que nos marchemos."
        pujol "Cerrar la puerta al salir, tenéis."

        
        
    if ken == True:
        scene black with dissolve
        $ renpy.pause(1, hard=True)
        show extra0 at Pan((0, -600), (0,898), 25.0)
        $ renpy.pause(20, hard=True)
        stop music
        scene extra1 with dissolve
        $ renpy.pause(0.5, hard=True)
        k "Vaya... siento la necesidad de mi pueblo en estas tierras soleadas... Cualquiera diría que estamos en Andalucía."
        k "Quiero hacer algo diferente. Quiero empaparme de necesidad, de sufrimiento, de anhelos. Llévame allí donde está la gente más necesitada de la presencia de Ken Sánchez."
        pov "Pues hay un pub..."
        espejo "Adalid de los pobres de mis entrereflejos, preguntemos a este... joven... apoyado tras esa palmera."
        show rivera at center with moveinright
        $ renpy.pause(0.5, hard=True)
        naranjito "¡Hola, amigos!"
        naranjito "Un momento..."
        extend " ¡Eres tú! ¡La salvación de la Cataluña Hispana!"
        naranjito "Gracias a los patronos que has venido. La desesperación estaba a punto de llevarme al exprimidor."
        k "Tranquilo, muchacho. Cuéntame. ¿Qué ha pasado aquí?"
        naranjito "Verás, todo iba bien con el Faraón Frankmamón, de la tierra manaba leche y miel y el sol bañaba el delta del Llobregat al llegar la primavera."
        naranjito "Pero la vida de un faraón no es eterna en este mundo y más pronto que tarde tuvo que cruzar el umbral hacia la tierra de los muertos."
        naranjito "Entonces, con el pueblo confuso y sin liderazgo, llegaron ellos... Vinieron en sus naves desde el planeta Zuisa y esclavizaron a los buenos españoles que nos levantábamos todas las mañanas a loar al gobierno central de Madriz."
        naranjito "La vida antes era mucho mejor. Aún recuerdo las canciones alegres que cantábamos en el patio: Boyer, no te arrime a la pared que te va a llená de cal, de cal, del cal... En aquellos tiempos se le tenia poco aprecio a la arena, ¿verdad?"
        naranjito "Lo peor es que estos nuevos dirigentes amenazan con separar Cataluña del resto del imperio. Lo que traerá terribles consecuencias."
        naranjito "Nos echarán de la UEFA, de la FIFA y el Barça tendrá que jugar en la liga de solteros contra casados, y los casados este año vienen fuertes con la incorporacion de Rocha, que al final lo pesco la puri, la hija del pintor." 
        naranjito "El penalty mejor tirado de la historia de Sabadell. Eso me han contado."
        espejo "¿Y la gente no se rebela?"
        naranjito "Están anestesiados con una vieja profecía. El Masías, líder de la tercera vía, les dijo que algún día regresaría, pero me dijo un amigo, que casualmente trabaja en el CESID, que está haciendo chorizos en Berna."
        pov "Un sitio muy extraño para hacer embutido..."
        k "Cada uno lo hace donde puede. No vamos a juzgar a nadie por eso."
        naranjito "Y no tiene intención de venir. Personalmente, creo que todo es un bulo."
        k "No temas. La integridad de la mejor liga del mundo no se verá en peligro mientras yo sea presidente. Dime, ¿dónde se encuentra el líder de esos malvados?"
        naranjito "En la Nave-Pirámide que se ve ahí en el horizonte."
        naranjito "Iría con vosotros, pero va a salir la Plomadas de la piscina y no pienso perdérmelo por nada."
        k "No te preocupes. Llegaremos."
        scene extra2 with fade
        $ renpy.pause(0.5, hard=True)
        show clara at center with moveinright
        show gabi at right with moveinright
        gabi "Perdonen..."
        k "¿Sí?"
        gabi "¿Ha visto a un bote de Lacasitos preocupado por aquí?"
        k "Hemos visto varios, pero estaban todos contentos..."
        gabi "Entonces nos hemos desviado demasiado del camino."
        gabi "Hagan el favor de decirle, si lo ven, que estamos en el parque de la avenida."
        k "Descuide, amigo."
        hide clara with moveoutleft
        $ renpy.pause(0.3, hard=True)
        hide gabi with moveoutleft
        scene black with dissolve
        show gymtextex1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextex2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymextra with fade        
        k "¡Hola!"
        pujol "Días buenos, visitante."
        k "Usted es... ¿Yoda Pujol?"
        pujol "Cierto ser. Sorprendido te veo."
        k "Me esperaba a alguien más... "
        extend "alto."
        pujol "La enfermedad de Azuisa padecer. Reducido mi tamaño un tres por ciento cada años es."
        k "Lo lamento... pero no piense que dándome pena logrará salirse con la suya."
        extend " He venido aquí a liberar a mi pueblo y acabar con tu régimen de tiranía independentista."
        pujol "A conseguir la poltrona tus pasos te han dirigido. Engañarme no puedes."
        pujol "Además, el estado actual de las cosas cosa mía no es. Mi responsabilidad tuve pero ya no. Si el responsable buscáis, al Masías prended."
        k "¿Dónde podemos encontrarle?"
        pujol "En los Alpes cultivando champiñones, creo."
        espejo "Nar-an-jito tenía razón."
        pujol "¿Ese joven por ahí suelto sigue? Hubo un momento en que una brillante carrera como vendedor de seguros pensé que llevaría."
        pujol "Seguir con la política emperrado está."
        k "¿Acaso no tiene derecho?"
        pujol "Como el que Mas."
        k "En cualquier caso, no está bien que explotes a tu gente."
        pujol "Libres ellos son."
        pujol "Al principio, cómo se colocaban las cadenas con la promesa de ser libres, me sorprendía."
        pov "¿Libertad en base a qué?"
        pujol "Al dinero que les pagamos."
        extend " Con viajes a países exóticos, televisiones de plasma enormes y coches de gran cilindrada sueñan. La libertad para ellos eso es."
        pujol "Y lo consiguen. Algunos de ellos, no todos. Para mantener viva la esperanza de prosperidad, el número justo. Como para igualarlos a todos, no los suficientes."
        pujol "En su miseria a gusto están si su vecino en el fango se ahoga. Y ahí están, creyéndose ricos mientras siervos de gleba ser."
        pov "Y alguien se aprovecha..."
        k "En cuanto a los votos..."
        pujol "¿Estando donde estás piensas que alguna oportunidad de que te los de tienes?"
        k "Yo pensaba..."
        pujol "Yo pensaba, yo creía, yo me equivocaba."
        k "¿Y ahora qué hacemos?"
        espejo "Pues no sé. Podrías intentar ligártelo..."
        k "¿Tú le has visto? No quiero coger la hepatitis o vete a saber qué."
        pov "Mejor será que nos marchemos."
        pujol "Cerrar la puerta al salir, tenéis."
        
    if coletas == True:
      
        scene extra1 with dissolve
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolución."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
                
        c "No recordaba que el extrarradio fuera así..."
        extend " ¿Qué habrá pasado?"
        stalin "Creo que se acerca... alguien extremadamente gordo..."
        pov "A ellos les gusta que les llamen obesos sin causa."
        stalin "Prisioneros de guerra invertidos les voy a llamar, no te jode."
        stalin "Cuando venga le voy a decir cuatro cosas sobre su dieta."
        show rivera at center with dissolve
        naranjito "¡Hola, amigos!"
        pov "Has tenido suerte de que se tratara de una fruta antropomorfa. No hubiera podido aguantar un solo insulto contra la gente rellenita."
        naranjito "¿A quién estás llamando relleno?"
        naranjito "Un momento..."
        extend " ¡Eres tú! ¡La salvación de...!"
        naranjito "¡NOOOOOO! ¡Eres el anticristo!"
        naranjito "¡Vade retro, Satanás!"
        naranjito "Esta equipación de fútbol vintage es lo único que tengo. No voy a permitir que tus discípulos impíos me lo arrebaten."
        stalin "A ver, obeso sin causa, por mucho que comparta tu opinión sobre aquí el camarada, cálmate y explícanos qué ha pasado en esta tierra. No recordaba tanto atraso desde el 39."
        naranjito "Verás, todo iba bien con el Faraón Frankmamón, de la tierra manaba leche y miel y el sol bañaba el delta del bajo Llobregat al llegar la primavera."
        naranjito "Pero la vida de un faraón no es eterna en este mundo y más pronto que tarde tuvo que cruzar el umbral hacia la tierra de los muertos."
        naranjito "Entonces, con el pueblo confuso y sin liderazgo, llegaron ellos... Vinieron en sus naves desde el planeta Zuisa y esclavizaron a los buenos españoles que nos levantábamos todas las mañanas a loar al gobierno central de Madriz."
        naranjito "La vida antes era mucho mejor. Aún recuerdo las canciones alegres que cantábamos en el patio: Boyer, no te arrime a la pared que te va a llená de cal, de cal, del cal... En aquellos tiempos se le tenia poco aprecio a la arena, ¿verdad?"
        naranjito "Lo peor es que estos nuevos dirigentes amenazan con separar Cataluña del resto del imperio. Lo que traerá terribles consecuencias."
        naranjito "Nos echarán de la UEFA, de la FIFA y el Barça tendrá que jugar en la liga de solteros contra casados, y los casados este año vienen fuertes con la incorporacion de Rocha, que al final lo pesco la puri, la hija del pintor." 
        naranjito "El penalty mejor tirado de la historia de Sabadell. Eso me han contado."
        naranjito "Además, no pagan las horas extra y la conciliación familiar es deplorable. Si eres un hombre no puedes pedirte baja y si eres una mujer, te miran las tetas."
        stalin "¿Y la gente no se rebela?"
        naranjito "Están anestesiados con una vieja profecía. El Masías, líder de la tercera vía, les dijo que algún día regresaría, pero me dijo un amigo, que casualmente trabaja en el CESID, que está haciendo chorizos en Berna."
        c "Pues deberían levantarse y clamar por sus derechos."
        naranjito "No lo harán. Su fe en un líder que vendrá a sacarlos de su apatía los hunde más en ella."
        stalin "Anda, mira, como pasa cont..."
        naranjito "Lo peor es que creo que El Masías no tiene intención de venir. Personalmente, creo que todo es un bulo."
        c "Dime, ¿dónde se encuentra el líder de la patronal?"
        naranjito "En la Nave-Pirámide que se ve ahí en el horizonte."
        naranjito "Iría con vosotros, pero va a salir la Plomadas de la piscina y no pienso perdérmelo por nada."
        c "No te preocupes. Llegaremos."
        scene extra2 with fade
        $ renpy.pause(0.5, hard=True)
        show clara at center with moveinright
        show gabi at right with moveinright
        gabi "Perdonen..."
        c "¿Sí?"
        gabi "¿Ha visto a un bote de Lacasitos preocupado por aquí?"
        c "Hemos visto varios, pero estaban todos contentos..."
        gabi "Entonces nos hemos desviado demasiado del camino."
        gabi "Hagan el favor de decirle, si lo ven, que estamos en el parque de la avenida."
        c "Descuide, amigo."
        hide clara with moveoutleft
        $ renpy.pause(0.3, hard=True)
        hide gabi with moveoutleft
        scene black with dissolve
        show gymtextex1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextex2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymextra with fade        
        c "¡Hola!"
        pujol "Días buenos, visitante."
        c "Usted es... ¿Yoda Pujol?"
        pujol "Cierto ser. Sorprendido te veo."
        c "Me esperaba a alguien más... "
        extend "alto."
        pujol "La enfermedad de Azuisa padecer. Reducido mi tamaño un tres por ciento cada años es."
        c "Lo lamento... pero no piense que dándome pena logrará salirse con la suya."
        extend " He venido aquí a acabar con tu régimen corrupto y la explotación laboral del pueblo."
        pujol "A conseguir la poltrona tus pasos te han dirigido. Engañarme no puedes."
        pujol "Además, el estado actual de las cosas culpa mía no es. Mi responsabilidad tuve pero ya no. Si el responsable buscáis, al Masías prended."
        c "¿Dónde podemos encontrarle?"
        pujol "En los Alpes cultivando champiñones, creo."
        stalin "Nar-an-jito tenía razón."
        pujol "¿Ese joven por ahí suelto sigue? Hubo un momento en que una brillante carrera como vendedor de seguros pensé que llevaría."
        pujol "Seguir con la política emperrado está."
        stalin "Cuando un tonto coge una linde..."
        pujol "Las frases terminar nunca hace."
        c "En cualquier caso, no está bien que explotes a tu gente."
        pujol "Suya es la decisión de serlo o no."
        pujol "Al principio, cómo se colocaban las cadenas con la promesa de ser libres, me sorprendía."
        pov "¿Libertad en base a qué?"
        pujol "Al dinero que les pagamos."
        extend " Con viajes a países exóticos, televisiones de plasma enormes y coches de gran cilindrada sueñan. La libertad para ellos eso es."
        pujol "Y lo consiguen. Algunos de ellos, no todos. Para mantener viva la esperanza de prosperidad, el número justo. Como para igualarlos a todos, no los suficientes."
        pujol "En su miseria a gusto están si su vecino en el fango se ahoga. Y ahí están, creyéndose ricos mientras siervos de gleba ser."
        pov "Y alguien se aprovecha..."
        stalin "Se hace un poco tarde y tengo que recoger mi uniforme de gala de la tintorería."
        c "En cuanto a los votos..."
        pujol "¿Estando donde estás piensas que alguna oportunidad de que te los de tienes?"
        c "Yo pensaba..."
        pujol "Yo pensaba, yo creía, yo me equivocaba."
        c "¿Y ahora qué hacemos?"
        stalin "Si de mi dependiera, avisaría a la cheka de Barcelona y antes de que pudiera decir: \"Tres tristes triges, pastraban...\""
        stalin "Vamos, que me lo llevaba preso al gulag de Las Rozas."
        c "¿Tú le has visto? Nadie querría tocarlo por miedo a coger la hepatitis o vete a saber qué."
        pov "Mejor será que nos marchemos."
        pujol "Cerrar la puerta al salir, tenéis."
    
    jump mapa