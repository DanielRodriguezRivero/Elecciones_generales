init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("prueba.ogg", channel="sound", loop="True")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")



label madrid:
    $ madrid = True
    define vaquerizo = Character("Eulalio Vaquerizo", color="#2E64FE", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define seiya = Character("Caballero de Pegaso", color="#F57B96", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define ciego = Character("Anciano Ciego", color="#F8F8FA", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image gymmadrid = "images/gymmadrid.jpg"
    image madrid1 = "images/madrid1.jpg"
    image madrid2 = "images/madrid2.jpg"
    image panaderia = "images/panaderia.jpg"
    
    image cuñadomadrid = "images/mario2.png"
    image seiya1 = "images/seiya.png"
    image ciego = "images/ciego.png"
    
    image gymtextmad1 = Text("{size=40}Gimnasio La Posada del Fitness",color="#fff", text_align=0.3)
    image gymtextmad2 = Text("{size=40}Only beautiful people",color="#fff", text_align=0.3)
    scene travelmadrid at Pan((0, 0), (300,0), 20.0)
    play music "entradillamadrid.mp3"
    $ renpy.pause(15, hard=True)
    play music "cancionciudad.mp3"
    
    if mrajao == True:
        scene madrid1 with fade
        $ renpy.pause(0.5, hard=True)
        r "Estamos aquí al lado como quien dice y nunca había visto esta parte de la ciudad a pie."
        r "¿Por qué hemos tenido que dejar la limusina en el aparcamiento?"
        montoto "Recuerda, Presidente, que estamos de incógnito. No debemos llamar la atención."
        pov "Creo que es un poco tarde para eso."
        play sound "blow.ogg"
        $ renpy.pause(1, hard=True)
        show seiya1 at center with dissolve
        $ renpy.pause(1, hard=True)
        seiya "Ahora te llamo, Robledo."
        robledo "Vale, y lo siento ¿eh? Yo lo intenté pero es complicado ganar a Son Goku."
        seiya "Perdone usted, caballero."
        r "Joven, mire por donde camina, que parece usted un coche y por la acera van los viandantes."
        pov "Oye, yo te conozco de algo..."
        seiya "Me lo dicen mucho."
        extend " Soy Seiya, el caballero de Pegaso."
        r "Sus padres eran muy graciosos."
        seiya "Eso pensaba yo, pero al llegar a la universidad eramos cuatro Seiya. Nos distinguían por el pelo."
        montoto "¿Y qué estudiabas?"
        seiya "Filología griega. ¡Jajaja!"
        extend " Es broma, siempre digo lo mismo. Mi madre no me hubiera dejado. No quería que fuera un muerto de hambre."
        seiya "Soy licenciado en Veterinaria."
        pov "¿Y qué haces por aquí? Porque tú no eres de aquí."
        seiya "¿Cómo lo has sabido? Mi madre es de Kyoto y mi padre de Totana."
        seiya "Me tuve que mudar aquí porque Hokkaido es muy de provincias. Para ayudar a parir a las vacas y vacunar a los cerdos está bien, pero mi verdadero sueño es triunfar en la zarzuela."
        seiya "Y ya sabes que si quieres triunfar en el mundo de la cultura te tienes que venir a la capital."
        pov "Sí, no me imagino a Manolo García tocando en su pueblo."
        seiya "¿Quién?"
        pov "Nada."
        extend " Por casualidad no sabrás donde queda el gimnasio de la ciudad."
        seiya "Pues es largo de explicar y tengo que ir a comprar el pan. Si me acompañáis os digo cómo llegar."
        montoto "No sé yo si deberíamos perder el tiempo acompañando a este pelanas."
        r "¿Quién sabe? Igual nos enseña alguna parte interesante de la ciudad... El Prado, Chueca..."
        menu:
            "Acompañémosle":
                scene panaderia with fade
                $ renpy.pause(0.3, hard=True)
                show seiya at center with dissolve
                seiya "Jo, dos euros por un largo gordo cocido. Qué cara se está volviendo la vida."
                r "Qué manera más creativa de nombrar al pan."
                seiya "Os váis a reir, pero no tengo suelto."
                $ seiya("¿No tendréis unos duros sueltos?", interact=False)
                menu: 
                    "Ten":
                        seiya "Que el Patriarca te lo pague con una diosa."
                        seiya "Por cierto, se me olvidó comentaros que soy el adjunto al jefe del Gimnasio, que está a dos calles al girar a la derecha en la plaza de fuera."
                        seiya "Por vuestra buena acción, os habéis ganado mi voto."
                        r "Muchas gracias, joven punky."
                        extend " ¿Ves Montoto cómo hay que confiar en la juventud?"
                        $ puntosj +=1
                        scene madrid2 with fade
                        $ renpy.pause(0.3, hard=True)
                        show seiya at center with dissolve
                        seiya "Nuestros caminos se separan aquí. Tengo que rescatar a Saori, que se ha quedado encerrada en el wc por culpa de un pestillo traicionero."
                        hide seiya

                    "Me pillas más pelado que Kojack":
                        seiya "Pues a ver cómo arreglamos esto, porque yo sin pan no me voy..."
                        hide seiya at right with move
                        pov "Esto..."
                        play music "sirena.mp3"
                        show polibarna at center with dissolve
                        policia "Conque robando a un humilde panadero, ¿eh?"
                        policia "¡Venga al talego!"
                        scene carcel with dissolve
                        play sound "portazo.mp3"
                        $ renpy.pause(1, hard=True)
                        pov "Quién me mandaría a mi relacionarme con políticos..."
                        pov "En fin, al menos podré dedicarme a sacarme Derecho sin gastarme un solo duro."
                        jump credits
                
            "Pasemos entonces":
                pass

        
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmad1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmad2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmadrid with fade
        $ renpy.pause(1, hard=True)
        show cuñadomadrid at center with dissolve
        r "¡Hola!"
        vaquerizo "Hola, maricón."
        r "¿Qué me ha llamado?"
        extend " Montoto... ¡Lo sabe! ¡LO SABE!"
        pov "Siempre habla asi a todo el mundo."
        vaquerizo "Claro, corazón."
        extend " Tú no te preocupes que tu secreto está a salvo conmigo. Soy un tumbona."
        vaquerizo "Me ha dicho Nebraska que íbais a venir. El otro día me llegó una carta el Ministerio de Justicia y yo me extrañé porque yo estoy en contra de las injusticias, pero cuando la leí ya me enteré de menos."
        vaquerizo "Menos mal que tengo a mi Nebraska, que es la que me saca de todos los embrollos en los que me meten."
        vaquerizo "Que para ser sintéticos, esto del Gimnasio lo decidí yo aunque fue idea de la Nancy Apollardada, que quería estar rodeada de Testarragona y como a ella no le dejan al mando de nada porque no sabe donde tiene la cabeza..."
        vaquerizo "De ahí su nombre, claro. A ver si te vas a creer que nos ponemos los motes porque lo leemos en las galletas de los chinos. Jajajajaj"
        r "[jugador] hablar tú que yo no tengo ánimo ahora de nada."
        pov "Verás Eulalio..."
        vaquerizo "Llámame Lali."
        pov "Verás, Lali. Hemos venido en busca de tus tres votos para que M. Rajao pueda gobernar con mano de hierro España."
        r "Lo de gobernar es un decir."
        vaquerizo "Si ya lo sabía. ¡La policía no es tonta!"
        vaquerizo "En principio habia pensado en que os disfrazárais de mamarrachos y valorar vuestro atrevimiento estilístico, pero con las pintas que me traéis ya veo que tenéis de sobra."
        vaquerizo "Asi que mejor os voy a hacer un test de cultura pop que encontré en el Nuevo Vale el viernes pasado."
        vaquerizo "Os leo las tarjetas estas que me ha escrito la chica de producción. Pili, te adoro."
        vaquerizo "Por si está jugando a esto."
        vaquerizo "Veamos..."
        $ vaquerizo("¿Cual es el número atómico del Wolframio?", interact=False)
        menu:
            "76":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "74":
                vaquerizo "¡Muy bien!"
                vaquerizo "Como diría Fabio: ¡venga otra ralla!"
                $ puntosj += 0.5
            "72":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "78":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("¿Cuántos años estuvo activo el escrito Guy de Maupaussant?", interact=False)
        menu:
            "109809":
                vaquerizo "¡Correctísimo!"
                pov "¿Seguro?"
                vaquerizo "Lo puedes encontrar en la whiskypedia, chocho."
                $ puntosj += 0.5
            "Eso no se pregunta, ¡que no estamos en El tiempo es oro!":
                vaquerizo "Chico, si son preguntas facilitas que una adolescente con dudas sobre el Richi le pone podría resolver."
            "34":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "21":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
                
        $ vaquerizo("¿Quién planteó el Problema de los puentes de Konigsberg?", interact=False)
        menu:
            "Federico Barbarroja":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Fibonnacci":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Euler":
                vaquerizo "¡Y otro minipunto para el equipo superfachi!"
                r "Me gusta cómo suena."
                $ puntosj += 0.5
            "El cartero de Konigsberg":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("¿Cómo se llama la figura retórica de pensamiento que consiste en designar una cosa con el nombre de otra con la que existe una relación de inclusión?", interact=False) 
        menu:
            "Sinécdoque":
                vaquerizo "Lo que yo digo siempre: claro que he ido a la escuela, ¿sinocdequé voy a saber yo leer y escribir?"
                vaquerizo "¡Al rico minipunto para mis niños!"
                $ puntosj += 0.5
            "Metáfora":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Fábula":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Sandía":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
                
        $ vaquerizo("¿Qué es un spin?", interact=False)
        menu: 
            "Un giro":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Una propiedad física de las partículas subatómicas":
                vaquerizo "¡Coooooorrecto!"
                vaquerizo "Vamos que nos queda nada y menos."
                $ puntosj += 0.5
            "Como Don Pimpón llamaba a Espinete cariñosamente cuando volvía al barrio tras un viaje de meses por el ancho mundo":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Nada":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("Amigos de Nuevo Vale, mi Jonathan me ha pedido que le coma el rabo. ¿quiere que me haga canibal? Atentamente, Marifé Lación.", interact=False)
        menu: 
            "Tú abre la boca y cuando lo tengas a tiro, muerde":
                vaquerizo "Oh, no ha podido ser."
            "Coméntaselo a tu padre, preferiblemente justo cuando llegue de trabajar":
                vaquerizo "Oh, no ha podido ser."
            "Cierra los ojos, abre la boca y piensa que estas ante un polo de limón, esto es, escupe y pon cara de asco":
                vaquerizo "Oh, no ha podido ser."
            "Marifé, no me pagan lo suficiente para esto. Lee un libro y culturízate":
                vaquerizo "Esa respuesta me ha llegado al corazón. Me hubiera gustado que alguien me hubiera dicho..."
                vaquerizo "Pero vaya, que habéis ganado otro minipunto."
                $ puntosj += 0.5
        
        vaquerizo "Con preguntas así te das cuenta del poder que tiene el redactor de una revista sobre la vida de millones de adolescentes."
        vaquerizo "Son como modernos dictadores que, quién sabe, un día podrían incitar a la revolución, desde esas páginas cuché."
        vaquerizo "Da miedo. Imagina que les da por prohibir las hombreras. No había pensado en esto, fíjate tú."
        vaquerizo "Por eso es bueno hablar con otras personas, ver otros mundos, comer rabos incluso. Todo es saludable para mente y cuerpo."
        vaquerizo "Pues hasta aquí se ha vendido todo el pescado."
        extend " Has conseguido..."
        extend " No he llevado la cuenta, maricón, pero el ordenador sí, así que no te preocupes que todas las preguntas acertadas han subido a tu marcador de votos."
        r "Mucho gusto de haberle conocido. Nosotros nos vamos ya."
        vaquerizo "¿No me vas a dar dos besos antes?"
        r "..."
        extend " ¿En la boca?"
        vaquerizo "Donde tú quieras, corazón."
        montoto "Mejor un apretón de manos, ¿eh?"
        vaquerizo "Uy, qué manos más frías. ¿Dónde las has metido? ¿En poliespán?"
        pov "Muchas gracias por todo."
        
                
                
    if ken == True:
        scene madrid1 with fade
        $ renpy.pause(0.5, hard=True)
        k "Estamos aquí al lado como quien dice y nunca había visto esta parte de la ciudad a pie."
        k "¿Por qué he tenido que cubrir mis músculos marcados con este abrigo?"
        espejo "Recuerda, caramelito caliente, que estamos de incógnito. No debemos llamar la atención."
        pov "Creo que es un poco tarde para eso."
        play sound "blow.ogg"
        $ renpy.pause(1, hard=True)
        show seiya1 at center with dissolve
        $ renpy.pause(1, hard=True)
        seiya "Ahora te llamo, Robledo."
        robledo "Vale, y lo siento ¿eh? Yo lo intenté pero es complicado ganar a Son Goku."
        seiya "Perdone usted, caballero."
        k "Chico, mira por donde caminas, que pareces un coche y por la acera van los viandantes."
        pov "Oye, yo te conozco de algo..."
        seiya "Me lo dicen mucho."
        extend " Soy Seiya, el caballero de Pegaso."
        k "Tus padres eran unos cachondos."
        seiya "Eso pensaba yo, pero al llegar a la universidad eramos cuatro Seiya. Nos distinguían por el pelo."
        espejo "¿Y qué estudiabas?"
        seiya "Filología griega. ¡Jajaja!"
        extend " Es broma, siempre digo lo mismo. Mi madre no me hubiera dejado. No quería que fuera un muerto de hambre."
        seiya "Veterinaria."
        pov "¿Y qué haces por aquí? Porque tú no eres de aquí."
        seiya "Me tuve que mudar aquí porque Hokkaido es muy de provincias. Para curar vacas está bien, pero mi verdadero sueño es triunfar en la zarzuela."
        seiya "Y ya sabes que si quieres triunfar en el mundo de la cultura te tienes que venir a la capital."
        pov "Sí, no me imagino a Manolo García tocando en su pueblo."
        seiya "¿Quién?"
        pov "Nada."
        extend " Por casualidad no sabrás donde queda el gimnasio de la ciudad."
        seiya "Pues es largo de explicar y tengo que ir a comprar el pan. Si me acompañáis os digo cómo llegar."
        espejo "No sé yo si deberíamos perder el tiempo acompañando a este punky."
        k "¿Quién sabe? Igual nos enseña alguna parte interesante de la ciudad... El Prado, Carabanchel..."
        menu:
            "Acompañémosle":
                scene panaderia with fade
                $ renpy.pause(0.3, hard=True)
                show seiya at center with dissolve
                seiya "Jo, dos euros por un largo gordo cocido. Qué cara se está volviendo la vida."
                k "Qué manera más creativa de nombrar al pan."
                seiya "Os váis a reir, pero no tengo suelto."
                $ seiya("¿No tendréis unos duros sueltos?", interact=False)
                menu: 
                    "Ten":
                        seiya "Que el Patriarca te lo pague con una diosa."
                        seiya "Por cierto, se me olvidó comentaros que soy el adjunto al jefe del Gimnasio, que está a dos calles al girar a la derecha en la plaza de fuera."
                        seiya "Por vuestra buena acción, os habéis ganado mi voto."
                        k "Muchas gracias, joven anarquista."
                        extend " ¿Ves Reflejo mío cómo hay que confiar en la juventud?"
                        $ puntosj +=1
                        scene madrid2 with fade
                        $ renpy.pause(0.3, hard=True)
                        show seiya at center with dissolve
                        seiya "Nuestros caminos se separan aquí. Tengo que rescatar a Saori, que se ha quedado encerrada en el wc por culpa de un pestillo traicionero."
                        hide seiya
                    "Me pillas más pelado que Kojack":
                        seiya "Pues a ver cómo arreglamos esto, porque yo sin pan no me voy..."
                        hide seiya at right with move
                        pov "Esto..."
                        play music "sirena.mp3"
                        show polibarna at center with dissolve
                        policia "Conque robando a un humilde panadero, ¿eh?"
                        policia "¡Venga al talego!"
                        scene carcel
                        play sound "portazo.mp3"
                        $ renpy.pause(1, hard=True)
                        pov "Quién me mandaría a mi relacionarme con políticos..."
                        pov "En fin, al menos podré dedicarme a sacarme Derecho sin gastarme un solo duro."
                        jump credits
                
            "Pasemos entonces":
                pass
                

        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmad1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmad2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmadrid with fade
        show cuñadomadrid at center 
        k "¡Hola!"
        vaquerizo "Hola, maricón."
        vaquerizo "Me ha dicho Nebraska que íbais a venir. El otro día me llegó una carta el Ministerio de Justicia y yo me extrañé porque yo estoy en contra de las injusticias, pero cuando la leí ya me enteré de menos."
        vaquerizo "Menos mal que tengo a mi Nebraska, que es la que me saca de todos los embrollos en los que me meten."
        vaquerizo "Que para ser sintéticos, esto del Gimnasio lo decidí yo aunque fue idea de la Nancy Apollardada, que quería estar rodeada de Testarragona y como a ella no le dejan al mando de nada porque no sabe donde tiene la cabeza..."
        vaquerizo "De ahí su nombre, claro. A ver si te vas a creer que nos ponemos los motes porque lo leemos en las galletas de los chinos. Jajajajaj"
        k "[jugador] hablar tú que yo no tengo ánimo ahora de nada."
        pov "Verás Eulalio..."
        vaquerizo "Llámame Lali."
        pov "Verás, Lali. Hemos venido en busca de tus tres votos para que Ken Sánchez pueda gobernar con mano de hierro España."
        vaquerizo "Lo hará con la mano con la que se hace las autosatisfacciones, jajaja."
        vaquerizo "Si ya lo sabía. ¡La policía no es tonta!"
        vaquerizo "En principio habia pensado que os disfrazárais de mamarrachos y valorar vuestro atrevimiento estilístico, pero con las pintas que me traéis ya veo que tenéis de sobra."
        vaquerizo "Asi que mejor os voy a hacer un test de cultura pop que encontré en el Nuevo Vale el viernes pasado." 
        vaquerizo "Os leo las tarjetas estas que me ha escrito la chica de producción. Pili, te adoro."
        vaquerizo "Por si está jugando a esto."
        vaquerizo "Veamos..."
        $ vaquerizo("¿Cual es el número atómico del Wolframio?", interact=False)
        menu:
            "76":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "74":
                vaquerizo "¡Muy bien!"
                vaquerizo "Como diría Fabio: ¡venga otra ralla!"
                $ puntosj += 0.5
            "72":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "78":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("¿Cuántos años estuvo activo el escritor Guy de Maupaussant?", interact=False)
        menu:
            "109809":
                vaquerizo "¡Correctísimo!"
                pov "¿Seguro?"
                vaquerizo "Lo puedes encontrar en la whiskypedia, chocho."
                $ puntosj += 0.5
            "Eso no se pregunta, ¡que no estamos en El tiempo es oro!":
                vaquerizo "Chico, si son preguntas facilitas que una adolescente con dudas sobre el Richi le pone podría resolver."
            "34":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "21":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
                
        $ vaquerizo("¿Quién planteó el Problema de los puentes de Konigsberg?", interact=False)
        menu:
            "Federico Barbarroja":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Fibonnacci":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Euler":
                vaquerizo "¡Y otro minipunto para el equipo superfachi!"
                r "Me gusta cómo suena."
                $ puntosj += 0.5
            "El cartero de Konigsberg":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("¿Cómo se llama la figura retórica de pensamiento que consiste en designar una cosa con el nombre de otra con la que existe una relación de inclusión?", interact=False) 
        menu:
            "Sinécdoque":
                vaquerizo "Lo que yo digo siempre: claro que he ido a la escuela, sinocdequé voy a saber yo leer y escribir?"
                vaquerizo "¡Al rico minipunto para mis niños!"
                $ puntosj += 0.5
            "Metáfora":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Fábula":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Sandía":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
                
        $ vaquerizo("¿Qué es un spin?", interact=False)
        menu: 
            "Un giro":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Una propiedad física de las partículas subatómicas":
                vaquerizo "¡Coooooorrecto!"
                vaquerizo "Vamos que nos queda nada y menos."
                $ puntosj += 0.5
            "Como Don Pimpón llamaba a Espinete cariñosamente cuando volvía al barrio tras un viaje de meses por el ancho mundo":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Nada":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("Amigos de Nuevo Vale, mi Jonathan me ha pedido que le coma el rabo. ¿quiere que me haga canibal? Atentamente, Marifé Lación.", interact=False)
        menu: 
            "Tú abre la boca y cuando lo tengas a tiro, muerde":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Coméntaselo a tu padre, preferiblemente justo cuando vuelva de trabajar un lunes":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Cierra los ojos, abre la boca y piensa que estas ante un polo de limón, esto es, escupe y pon cara de asco":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Marifé, no me pagan lo suficiente para esto. Lee un libro y culturízate":
                vaquerizo "Esa respuesta me ha llegado al corazón. Me hubiera gustado que alguien me hubiera dicho..."
                vaquerizo "Pero vaya, que habéis ganado otro minipunto."
                $ puntosj += 0.5
        
        vaquerizo "Con preguntas así te das cuenta del poder que tiene el redactor de una revista sobre la vida de millones de adolescentes."
        vaquerizo "Son como modernos dictadores que, quién sabe, un día podrían incitar a la revolución, desde esas páginas cuché."
        vaquerizo "Da miedo. Imagina que les da por prohibir las hombreras. No había pensado en esto, fíjate tú."
        vaquerizo "Por eso es bueno hablar con otras personas, ver otros mundos, comer rabos incluso. Todo es saludable para mente y cuerpo."
        vaquerizo "Pues hasta aquí se ha vendido todo el pescado."
        extend " Has conseguido..."
        extend " No he llevado la cuenta, maricón, pero el ordenador sí, así que no te preocupes que todas las preguntas acertadas han subido a tu marcador de votos."
        k "Muchas gracias. Saluda a Alaska de mi parte."
        vaquerizo "¿A quién?"
        k "A tu mujer."
        vaquerizo "Ah, Laraska. Yo se los doy. No te preocupes."
        
                
        
        
    if coletas == True:
        scene madrid1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        
        
        c "La de veces que me habré pateado yo estas calles."
        stalin "Sí, casi puedo decir en qué rincón de esta ciudad hiciste de mimo, en que portal fumabas hierba con tus colegas o en qué plaza montaste tus granjas de piojos."
        pov "Es reconfortante estar en casa."
        play sound "blow.ogg"
        show seiya1 at center with dissolve
        $ renpy.pause(1, hard=True)
        seiya "Ahora te llamo, Robledo."
        robledo "Vale, y lo siento ¿eh? Yo lo intenté pero es complicado ganar a Son Goku."
        seiya "Perdone usted, caballero."
        c "¡Hostias! ¡Si eres Saint Seiya!"
        seiya "El mismo: Seiya, el caballero de Pegaso. Para servirles a dios y a ustedes."
        stalin "Sus padres eran muy graciosos."
        seiya "Eso pensaba yo, pero al llegar a la universidad eramos cuatro Seiya. Nos distinguían por el pelo."
        stalin "¿Y qué estudiabas?"
        seiya "Filología griega. ¡Jajaja!"
        extend " Es broma, siempre digo lo mismo. Mi madre no me hubiera dejado. No quería que fuera un muerto de hambre."
        seiya "Estoy en cuarto de Veterinaria."
        pov "¿Y qué haces en la ciudad? Porque tú no eres de aquí."
        seiya "Me tuve que mudar porque Hokkaido, mi ciudad natal, es muy de provincias. Para ayudar a las vacas a parir está bien, pero mi verdadero sueño es triunfar en la zarzuela."
        seiya "Y ya sabes que si quieres triunfar en el mundo de la cultura te tienes que venir a la capital."
        pov "Sí, no me imagino a Manolo García tocando en su pueblo."
        seiya "¿Quién?"
        pov "Nada."
        extend " Por casualidad no sabrás donde queda el gimnasio de la ciudad."
        seiya "Pues es largo de explicar y tengo que ir a comprar el pan. Si me acompañáis os digo cómo llegar."
        stalin "No sé yo si deberíamos perder el tiempo acompañando a este elemento contrarrevolucionario."
        c "¿Quién sabe? Igual nos enseña alguna parte interesante de la ciudad... La Casa de Campo, La Mazmorra del Android..."
        menu:
            "Acompañémosle":
                scene panaderia with fade
                $ renpy.pause(0.5, hard=True)
                show seiya at center with dissolve
                seiya "Jo, dos euros por un largo gordo cocido. Qué cara se está volviendo la vida."
                c "Qué manera más creativa de nombrar al pan."
                seiya "Os váis a reir, pero no tengo suelto."
                $ seiya("¿No tendréis unos duros sueltos?", interact=False)
                menu: 
                    "Ten":
                        seiya "Que el Patriarca te lo pague con una diosa."
                        seiya "Por cierto, se me olvidó comentaros que soy el adjunto al jefe del Gimnasio, que está a dos calles al girar a la derecha en la plaza de fuera."
                        seiya "Por vuestra buena acción, os habéis ganado mi voto."
                        c "Muchas gracias, hermano."
                        extend " ¿Ves Staline cómo hay que confiar en la juventud?"
                        $ puntosj +=1
                        scene madrid2 with fade
                        $ renpy.pause(0.3, hard=True)
                        show seiya at center with dissolve
                        seiya "Nuestros caminos se separan aquí. Tengo que rescatar a Saori, que se ha quedado encerrada en el wc por culpa de un pestillo traicionero."
                        hide seiya
                        c "En esta calle recuerdo que me di mi primer beso con una cofluencia."
                        pov "¿Estaba buena?"
                        c "¿Acaso importa cuando hay intención de pactar?"
                    "Me pillas más pelado que Kojack":
                        seiya "Pues a ver cómo arreglamos esto, porque yo sin pan no me voy..."
                        hide seiya at right with move
                        pov "Esto..."
                        play music "sirena.mp3"
                        show polibarna at center with dissolve
                        policia "Conque robando a un humilde panadero, ¿eh?"
                        policia "¡Venga al talego!"
                        scene carcel
                        play sound "portazo.mp3"
                        $ renpy.pause(1, hard=True)
                        pov "Quién me mandaría a mi relacionarme con políticos..."
                        pov "En fin, al menos podré dedicarme a sacarme Derecho sin gastarme un solo duro."
                        jump credits
                
            "Pasemos entonces":
                scene madrid2 with dissolve
                $ renpy.pause(1, hard=True)
                show seiya at center with fade
                seiya "Nuestros caminos se separan aquí. Tengo que rescatar a Saori, que se ha quedado encerrada en el wc por culpa de un pestillo traicionero."
                hide seiya
                c "En esta calle recuerdo que me di mi primer beso con una cofluencia."
                pov "¿Estaba buena?"
                c "¿Acaso importa cuando hay intención de pactar?"
                

        show ciego at center with dissolve
        $ renpy.pause(0.5, hard=True)
        ciego "Felipe, ¿eres tú?"
        c "Señor, creo que se confunde."
        extend " Soy El Coletas."
        ciego "A mi no me engañas: ¡tú eres Felipe!"
        stalin "Yo empecé a sospecharlo cuando empezó a utilizar acondicionador para el pelo, como si fuera la tapicería de un coche."
        c "Le aseguro que se equivoca. No soy ese señor del que usted me habla."
        ciego "Me vas a decir a mí... que te vi hace ya... buff la tira de años, ahí en la plaza del pueblo."
        ciego "Yo estaba sentado entre la Tomasa y mi señora, y por suerte tenía un sombrero en el regazo porque la Tomasa aquel día llevaba un vestido al que objetivamente le faltaba un botón en la pechera."
        ciego "Y aquello estaba que iba a rebosar. Y mi mujer venga a hablar de tus patillas, Felipe. Lo frondosas que eran las patillas y lo lustrosas... Yo me confié, me pasé un segundo de más mirando aquel escote y mi señora me pilló."
        ciego "De la hostia que me dio me quedé así."
        c "Vaya historia más triste, pero le aseguro que yo no soy Felipe."
        ciego "Al menos no le dio por aplastarme el sombrero."
        extend " Una cosa te iba a decir..."
        ciego "La pensión ni me la toques, ¿eh, Felipe?"
        ciego "Que veo lo suficiente todavía como para acertarte en la cabeza con la garrota."
        c "Vámonos de aquí antes de que alguien salga herido."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmad1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmad2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmadrid with fade
        $ renpy.pause(1, hard=True)
        show cuñadomadrid at center with moveinright
        c "¡Eulalio Vaquerizo! El icono glam de España."
        vaquerizo "Y cada día el de más gente."
        vaquerizo "Hola, maricón."
        vaquerizo "Me ha dicho Nebraska que íbais a venir. El otro día me llegó una carta el Ministerio de Justicia y yo me extrañé porque yo estoy en contra de las injusticias, pero cuando la leí ya me enteré de menos."
        vaquerizo "Menos mal que tengo a mi Nebraska, que es la que me saca de todos los embrollos en los que me meten."
        vaquerizo "Que para ser sintéticos, esto del Gimnasio lo decidí yo aunque fue idea de la Nancy Apollardada, que quería estar rodeada de Testarragona y como a ella no le dejan al mando de nada porque no sabe donde tiene la cabeza..."
        vaquerizo "De ahí su nombre, claro. A ver si te vas a creer que nos ponemos los motes porque lo leemos en las galletas de los chinos. Jajajajaj"
        c "[jugador], habla tú que la emoción me embarga."
        pov "Verás Eulalio..."
        vaquerizo "Llámame Lali."
        pov "Verás, Lali. Hemos venido en busca de tus tres votos para que El Coletas pueda gobernar con mano de hierro España."
        stalin "No sería capaz ni aunque le transplantaran el brazo de Mazinguer Z."
        vaquerizo "Si ya estaba al tanto de todo. ¡La policía no es tonta!"
        vaquerizo "En principio habia pensado en que os disfrazárais de mamarrachos y valorar vuestro atrevimiento estilístico, pero con las pintas que me traéis ya veo que tenéis de sobra."
        vaquerizo "Asi que mejor os voy a hacer un test de cultura pop que encontré en el Nuevo Vale el viernes pasado."
        vaquerizo "Os leo las tarjetas estas que me ha escrito la chica de producción. Pili, te adoro."
        vaquerizo "Por si está jugando a esto."
        vaquerizo "Veamos..."
        $ vaquerizo("¿Cual es el número atómico del Wolframio?", interact=False)
        menu:
            "76":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "74":
                vaquerizo "¡Muy bien!"
                vaquerizo "Como diría Fabio: ¡venga otra ralla!"
                $ puntosj += 0.5
            "72":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "78":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("¿Cuántos años estuvo activo el escrito Guy de Maupaussant?", interact=False)
        menu:
            "109809":
                vaquerizo "¡Correctísimo!"
                pov "¿Seguro?"
                vaquerizo "Lo puedes encontrar en la whiskypedia, chocho."
                $ puntosj += 0.5
            "Eso no se pregunta, ¡que no estamos en El tiempo es oro!":
                vaquerizo "Chico, si son preguntas facilitas que una adolescente con dudas sobre el Richi le pone podría resolver."
            "34":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "21":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
                
        $ vaquerizo("¿Quién planteó el Problema de los puentes de Konigsberg?", interact=False)
        menu:
            "Federico Barbarroja":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Fibonnacci":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Euler":
                vaquerizo "¡Y otro minipunto para el equipo superfachi!"
                r "Me gusta cómo suena."
                $ puntosj += 0.5
            "El cartero de Konigsberg":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("¿Cómo se llama la figura retórica de pensamiento que consiste en designar una cosa con el nombre de otra con la que existe una relación de inclusión?", interact=False) 
        menu:
            "Sinécdoque":
                vaquerizo "Lo que yo digo siempre: claro que he ido a la escuela, sinocdequé voy a saber yo leer y escribir?"
                vaquerizo "¡Al rico minipunto para mis niños!"
                $ puntosj += 0.5
            "Metáfora":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Fábula":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Sandía":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
                
        $ vaquerizo("¿Qué es un spin?", interact=False)
        menu: 
            "Un giro":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Una propiedad física de las partículas subatómicas":
                vaquerizo "¡Coooooorrecto!"
                vaquerizo "Vamos que nos queda nada y menos."
                $ puntosj += 0.5
            "Como Don Pimpón llamaba a Espinete cariñosamente cuando volvía al barrio tras un viaje de meses por el ancho mundo":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Nada":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
        
        $ vaquerizo("Amigos de Nuevo Vale, mi Jonathan me ha pedido que le coma el rabo. ¿quiere que me haga canibal? Atentamente, Marifé Lación.", interact=False)
        menu: 
            "Tú abre la boca y cuando lo tengas a tiro, muerde":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Coméntaselo a tu padre, preferiblemente justo cuando llegue de trabajar":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Cierra los ojos, abre la boca y piensa que estas ante un polo de limón, esto es, escupe y pon cara de asco":
                vaquerizo "Oh, no ha podido ser. A ver la siguiente vez."
            "Marifé, no me pagan lo suficiente para esto. Lee un libro y culturízate":
                vaquerizo "Esa respuesta me ha llegado al corazón. Me hubiera gustado que alguien me hubiera dicho..."
                vaquerizo "Pero vaya, que habéis ganado otro minipunto."
                $ puntosj += 0.5
        
        vaquerizo "Con preguntas así te das cuenta del poder que tiene el redactor de una revista sobre la vida de millones de adolescentes."
        vaquerizo "Son como modernos dictadores que, quién sabe, un día podrían incitar a la revolución, desde esas páginas cuché."
        vaquerizo "Da miedo. Imagina que les da por prohibir las hombreras. No había pensado en esto, fíjate tú."
        vaquerizo "Por eso es bueno hablar con otras personas, ver otros mundos, comer rabos incluso. Todo es saludable para mente y cuerpo."
        vaquerizo "Pues hasta aquí se ha vendido todo el pescado."
        extend " Has conseguido..."
        extend " No he llevado la cuenta, maricón, pero el ordenador sí, así que no te preocupes que todas las preguntas acertadas han subido a tu marcador de votos."
        c "¿Me puede firmar un autógrafo?"
        vaquerizo "¿En el pene?"
        stalin "¡Por el representante de Engels! ¡Cuánta degeneración!"
        vaquerizo "No te quejes, chocho, que también te firmo a ti siquieres."
        stalin "Vámonos, [jugador]"
                
    
    jump mapa