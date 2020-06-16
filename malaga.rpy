label malaga:
    $ malaga = True
    #personajes
    define banderas = Character("Tony Banderolas", color="#DBA901", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define zorra = Character("Señora del Zorro", color="#FF00FF", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define enrique = Character("Enrique, el de Vicente", color="#8D8B8E", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define iker = Character("Íker Jiménez", color="#BA87C1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define nieves = Character("Jose Manuel Nieves", color="#EAAD9F", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define santi = Character("Santiago Vázquez", color="#74C164", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    #graficos de los autografos
    image autostallone = "images/stallonegraf.jpg"
    image autoclooney = "images/clooneygraf.jpg"
    image autogibson = "images/gibsongraf.jpg"
    image autosandler = "images/sandlergraf.jpg"
    image autospielberg = "images/spielbergraf.jpg"
    
    #lugares
    image gymmalaga = "images/gymmalaga.jpg"
    image malaga1 = "images/malaga1.jpg"
    image malaga2 = "images/malaga2.jpg"
    image malaga3 = "images/malaga3.jpg"
    image ikerfinal = "images/ikerfinal.jpg"
    image enriquefin1 = "images/enriquefin1.jpg"
    image enriquefin2 = "images/enriquefin2.jpg"
    image nievesfin = "images/nievesfin.jpg"
    
    #personajes imagenes
    image cuñadomalaga = "images/zorro.png"
    image zorraimg = "images/zorra.png"
    image gymtextmalaga1 = Text("{size=40}Gimnasio Bíceps de Oro",color="#fff", text_align=0.3)
    image gymtextmalaga2 = Text("{size=40}Convertimos tu cuerpo de plomo en una figura de plata",color="#fff", text_align=0.3)
    scene travelmalaga at Pan((0, 0), (300,0), 20.0)
    play music "entradillamalaga.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "cancionciudad.mp3"
    
    if mrajao == True:
       
        scene malaga1 with dissolve
        $ renpy.pause(0.5, hard=True)
        montoto "Ya estamos en la capital de la Costa del Sol."
        extend " Cuidado con la cartera. Esta es la única ciudad en la que los ciudadanos recaudan más que el estado."
        r "Así me gusta, gente con iniciativa."
        extend " ¿Y dices que aquí mandamos nosotros?"
        montoto "No podía ser de otra manera."
        r "Desde luego que no..."
        r "En fin, ¿nos vamos a la playa un rato antes de ir al gimnasio?"
        pov "Qué tópico, ¿no? Málaga ha hecho en los ultimos años un esfuerzo por ofrecer al visitante ocasional una amplia oferta cultural y de ocio más allá del sol y playa que tan bien ha definido esta localidad durante décadas pasadas."
        pov "En este movimiento se engloba la creacion de los museos dedicados a Picasso, el Museo de Arte Ruso y el Pompidou, junto al renovado puerto deportivo (cuña publicitaria pendiente de remuneración)"
        r "Yo solo quiero ponerme moreno. Luego, en el club, los muchachos se fijan en mis partes blandas..."
        montoto "Blancas, Presidente. Partes blancas."
        r "Sí, sí. Eso quería decir."
        r "Pues eso, que se fijan y queda muy feo en comparación."
        scene malaga2 with wiperight
        r "Esto no está como lo recuerdo. Era todo más provinciano, más rústico, improvisado, más acogedor, más seco..."
        r "Montoto, me estoy dando cuenta de que hace mucho que estoy encerrado en mi burbuja de confort."
        montoto "Dirá su zona."
        r "No, burbuja. Yo la llamo Pepita, como a mi abuela."
        r "¿Y bien, [jugador], ¿dónde vamos?"
        menu:
            "El Palo Street":
                pass
            "Mr. Roboto Avenue":
                pass
            "Marmalade Road":
                pass
            "Mollete Square":
                pass
        scene malaga3 with wipeleft
        $ renpy.pause(1, hard=True)
        stop music
        r "Hay algo que no me gusta de este lugar..."
        play sound "llamada.ogg"
        $ renpy.pause(2, hard=True)
        play sound "llamada.ogg"
        $ renpy.pause(2, hard=True)
        montoto "¿Lo cogemos?"
        r "No veo por qué no."
        scene black with fade
        iker "Y ahora pasemos a las llamadas de nuestros televidentes."
        scene ikerfinal with blinds
        r "¿Hola?"
        iker "Buenas noches, amigo del misterio. ¿Cual es la cuestión que querría exponer a nuestros expertos?"
        scene malaga3 
        r "¿Qué le digo?"
        montoto "Se te tiene que ocurrir algo, Presidente. Estamos en directo para toda España."
        montoto "Y por el amor de dios, ¡que no sea ninguna obviedad!"
        scene ikerfinal
        r "Verás, Íker, me gustaría saber si los reptilianos existen."
        iker "Inquietante tema."
        extend " Reptilianos. ¿Extras de la serie V que no lograron reinsertarse en el mercado laboral?"
        extend " ¿Leyenda urbana?"
        extend " ¿Los verdaderos amos de la Tierra?"
        scene enriquefin1
        enrique "Si me permites, Íker, me gustaría responder a nuestro espectador."
        enrique "Querido amigo, los reptilianos no solo existen, sino que además uno de ellos me debe 5.000 pesetas de las de antes."
        extend " Es un reptiliano muy famoso, no uno de esos de segunda fila que trabajan en los parques temáticos."
        scene ikerfinal
        iker "¿No nos puedes decir su nombre?"
        scene enriquefin1
        enrique "En fín... levantaría muchas ampollas, y más en la situación actual del país, pero si hay algo que me caracteriza es la búsqueda de la verdad sin importar el precio."
        scene nievesfin
        nieves "Eso, y la barba de chivo que gastas."
        scene enriquefin2
        enrique "Nieves, me aburres."
        enrique "Que lo sepa toda España, el nombre del reptiliano es M. Rajao."
        r "¡Pero si soy yo!"
        r "Y no te debo nada."
        enrique "¿Cómo que no, Rajao?"
        extend " Te presté cinco berenjenas para pagar los pelotazos en el Pub Roma durante la Alerta Ovni que hicimos en la Sierra de Guadarrama."
        r "Pero hombre, Enrique, yo pensaba que entre amigos..."
        enrique "En temas de dinero, no hay amistad que valga. Tú mejor que nadie debería saberlo."
        enrique "Si es que todos los reptilianos son iguales."
        enrique "Otro caso, Íker. En los 70, en una de las primeras ediciones del Festival de Benicasim, por aquel entonces llamado \"Festival del Caudillo Redentor\", recibí una llamada de la Reina de Inglaterra."
        enrique "Quería asistir al evento y como yo vivía al lado... Total, que le digo: vente y te dejo mi sofá. Así te ahorras el alojamiento. Y allá estuvo varios días. Lo pasamos muy bien, las cosas como son."
        enrique "Lo normal, vaya."
        extend " Hace cinco años, fui a Londres para un congreso de druidas progresistas y me dije: voy a visitar a Elizabeth a Buckingham Palace."
        enrique "Pues, oye, ¡que los guardias me impidieron la entrada!"
        enrique "Me puse a gritarle por la ventana: Elizabeth, no puedo creer que después de dejarme el baño lleno de compresas usadas ahora no me dejes ni entrar a decirte hola."
        scene ikerfinal
        iker "Aterrador..."
        scene enriquefin1
        enrique "Claro, aquello tiene muchas ventanas y no sé si me escucharía, pero desde ese día, reniego de los reptilianos."
        enrique "Antes me afeito la barba que hacerles otro favor."
        enrique "A partir de ahora, soy #TeamAnnunaki."
        enrique "Así que, sí, los reptilianos existen y como te pille uno cerca te va a joder la vida."
        scene ikerfinal
        iker "Creo que el telespectador ha colgado."
        enrique "Con tal de no pagar, hace lo que sea."
        iker "Me dicen que hay otra llamada."
        iker "Buenas noches, amigo."
        santi "Hola, Íker. ¿Te acuerdas de mí? Creo que no, porque si lo hicieras me hubieras llamado y ahora estaría ahí junto a Enrique tirándonos de la barba durante las pausas."
        iker "Sí, me dicen que se ha cortado la conexión."
        iker "Volvemos tras unos anuncios."
        scene malaga3 with wiperight
        pov "¿Le debes dinero al señor de Vicente?"
        r "¿Qué le voy a deber?"
        r "No digas tonterías, [jugador]."
        pov "Tontería ninguna, que te he dejado antes cinco euros para un paquete de Marlboro."
        r "Ya Montoto te lo reembolsará luego."
        montoto "Primero vayamos al gimnasio."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmalaga1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmalaga2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmalaga with fade
        show zorro at center
        r "¡Eres Tony Banderolas, el equilibrista que triunfó en las Américas y cumplió el sueño español de dar un braguetazo y tener la vida resulta."
        banderas "El mismo, y aquí está mi mujer."
        show zorro at left with move
        show zorraimg at right with moveinright
        zorra "Como me llames Zorra te parto la cara."
        r "No se preocupe, señorita."
        hide zorraimg with moveoutright
        show zorro at center with move
        banderas "¿Qué se os ofrece?"
        extend " ¿Venís a por una muestra de mi nueva colonia: Priapo, y que todos se enteren de que estas siempre a punto?"
        montoto "Nos preguntábamos si nos querría votar para ser presidente del país."
        banderas "A mi plim, yo solo vengo de vacaciones. Mientras no me tiréis abajo la casa..."
        r "Prometido."
        banderas "Una cosa os quería pedir ya que estamos. ¿Me podéis echar una mano con unos autógrafos?"
        r "¿Quiere que le firme uno?"
        banderas "No, verás, resulta que aquí la..."
        show zorro at left with move
        show zorraimg at right
        zorra "Como me llames zorra pido el divorcio."
        banderas "Pero qué perra te ha dado con el tema. No eres el centro del universo. Nadie te va a llamar zorra."
        banderas "¿Acaso te dice alguien que eres la Desperada?"
        zorra "¿Con estas tetas? Hay que estar loco."
        hide zorraimg
        show zorro at center with move
        banderas "Como iba diciendo, mi mujer ha sufrido varios reveses en la bolsa. Invirtió en Gowex, FCC y el Deutsche Bank."
        r "Ssshh, no diga nada malo de los alemanes. Tienen oídos en todas partes."
        banderas "El caso es que necesitamos dinero. Por suerte en Hollywood somos una gran familia. Pedí un par de favores y unas cuantas estrellas de cine me contrataron para que firme sus autógrafos por ellos."
        pov "¿Y no se darán cuenta los fans?"
        banderas "Son los que venden en las convenciones de cómics. Esos frikazos comprarían cualquier cosa."
        banderas "Me pondría a hacerlo yo, pero ya que habéis venido... Además, estuve practicando y ahora he mezclado la firma verdadera que tenéis que escribir con varias pruebas que hice."
        banderas "Tendréis que escoger cual es la firma que corresponde al personaje cuyo nombre aparezca en pantalla."
        r "Parece fácil."
        banderas "Aquí os dejo la carpeta con las firmas, escogéis la que creeis que es la verdadera firma del famoso en cuestión y listo. Un voto al bolsillo."
        r "Así se las ponían a Fernando VII."
        banderas "¿El qué? ¿Las pelotas?"
        r "..."
        banderas "No sé a qué ha venido eso. A veces me pasa. Creo que es stress postraumático de cuando estuve en una fiesta de Robert Downey Jr."
        banderas "Os dejo, mientras voy a tomar un poco el sol."
        hide zorro
        
        $ result = renpy.imagemap("images/clooneygraf.jpg", "images/clooneygraf.jpg", [
            (872, 462, 1308, 754, "clooney1"),  
            (90, 451, 532, 756, "clooney2"),
            (781, 6, 1252, 305, "clooney3"),
            ], focus="imagemap")
        
        if result == "clooney1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "¡Excelente! que uno de vosotros comience a firmar esos bañadores turbo del rincón mientras los demás continuáis."
        if result == "clooney2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Tú has visto a George Clooney cara de retrasado?"
            pov "Oiga, se llaman deficientes mentales, y seguro que escriben mejor que yo."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        if result == "clooney3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Tú has visto a George Clooney cara de retrasado?"
            pov "Oiga, se llaman deficientes mentales y seguro que escriben mejor que yo."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "A ver qué tal se os da el siguiente."
        pov "¿Usted no estaba poniéndose moreno?"
        banderas "Fíjate que se ha nublado. 364 días al año que no deja el sol de caer a plomo sobre esta ciudad y precisamente hoy que venís, todo lleno de nubes."
        banderas "Terminad cuanto antes que no quiero más mal fario en mi casa."
        
        $ result = renpy.imagemap("images/gibsongraf.jpg", "images/gibsongraf.jpg", [
            (91, 454, 532, 754, "gibsongraf1"),  
            (872, 462, 1308, 754, "gibsongraf2"),
            (781, 6, 1252, 305, "gibsongraf3"),
            ], focus="imagemap")
        
        if result == "gibsongraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Perfecto. Yo no lo hubiera hecho mejor."
            extend " A decir verdad, sí, pero no quiero desmotivaros."

        if result == "gibsongraf2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Con lo loco que está Mel?"
            banderas "Le ha dejado toda su herencia a una marioneta de castor que sacó de un contenedor de la basura. Dice que por las noches le recita versos de la Biblia y que hace un goulash riquísimo."
            banderas "Mi Melania dice que no es para tanto pero con lo especialita que es para la gastronomía, es todo un elogio."
            pov "¿Pero usted no estaba soltero ya?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        if result == "gibsongraf3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Con lo loco que está Mel?"
            banderas "Le ha dejado toda su herencia a una marioneta de castor que sacó de un contenedor de la basura. Dice que por las noches le recita versos de la Biblia y que hace un goulash riquísimo."
            banderas "Mi Melania dice que no es para tanto pero con lo especialita que es para la gastronomía, es todo un elogio."
            pov "¿Pero usted no estaba soltero ya?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "El último y ya os podréis marchar."
        
        $ result = renpy.imagemap("images/spielbergraf.jpg", "images/spielbergraf.jpg", [
            (872, 462, 1308, 754, "spielbergraf1"),  #coordenadas para los boliches, etc
            (91, 454, 532, 754, "spielbergraf2"),
            (781, 6, 1252, 305, "spielbergraf3"),
            ], focus="imagemap")
        
        if result == "spielbergraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "¡Olé tus huevos morenos!"
            extend " Que no te los he visto, ojo. Es una forma de hablar. Lo digo porque los de la meseta lleváis muy mal estos requiebros, a otros ojos, escatológicos."

            
        if result == "spielbergraf2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "No te digo yo que pudiera ser, por el trazo infantil, pero se nota a la legua que está escrito con un rotulador Carioca y Stewie es alérgico. Parece mentira que no lo sepas."
            pov "¿Y cómo se supone que voy a saber eso?"
            banderas "¿Es que no os enseñan nada en la escuela?"
            banderas "¿Acaso no sabéis que no puedes darle cacahuetes a Samuel L. Jackson?"
            pov "¿Es alérgico?"
            banderas "¡Maldita sea, NO! Piensa que si alguien le ofrece es porque piensa que él es un mono."
            banderas "Aparte de ignorante, insensible racista."
            pov "Pero si yo..."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
            
        if result == "spielbergraf3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "No te digo yo que pudiera ser, por el trazo infantil pero se nota a la legua que está escrito con un rotulador Carioca y Stewie es alérgico. Parece mentira que no lo sepas."
            pov "¿Y cómo se supone que voy a saber eso?"
            banderas "¿Es que no os enseñan nada en la escuela?"
            banderas "¿Acaso no sabéis que no puedes darle cacahuetes a Samuel L. Jackson?"
            pov "¿Es alérgico?"
            banderas "¡Maldita sea, NO! Piensa que si alguien le ofrece es porque piensa que él es un mono."
            banderas "Aparte de ignorante, insensible racista."
            pov "Pero si yo..."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "Hemos terminado. Ya os llamará mi agente para ver dónde os tiene que enviar los cheques."
        montoto "¿Nos va a pagar encima?"
        banderas "Os puedo pagar debajo."
        extend " Jajajajaj."
        montoto "Me refiero a que no nos ha hecho contrato ni estamos dados de alta como autónomos."
        pov "Habla por ti."
        montoto "¿Ah sí? Eres una caja de sorpresas."
        $ nombre2 = renpy.input("Y dime, ¿cómo te llamabas?")
        if "[jugador]" != "[nombre2]":
            montoto "Vienes con nosotros en un viaje alrededor de la península, te acojemos en nuestro seno como si fueras uno más, te bebes el champán de la limusina y tienes la indecencia de reirte de mí?"
            montoto "¿Es así como nos lo pagas?"
            pov "Vamos, era solo una broma. Además, si ya sabes cómo me llamaba para qué preguntas?"
            montoto "En estos tiempos difíciles hay que saber en quién se puede confiar, y tú, [jugador] has demostrado no ser una de esas personas."
        montoto "Dime, ¿estás al corriente de tus pagos con la Administración?"
        pov "¿Por quién me toma?"
        montoto "Por un ciudadano de este país."
        montoto "Déjeme que haga una llamada."
        banderas "Vaya sanguijuela, ¿no?"
        banderas "Ya lo siento por los pobres."
        montoto "Debe de ser el único que paga. Podemos irnos."
        banderas "Y recordad: El zorro os acompañará..."
        extend " siempre."
        
                  

        
    if ken == True:
 
        scene malaga1
        $ renpy.pause(0.5, hard=True)
        espejo "Málaga, la Ponderosa."
        k "Vamos a la playa un rato."
        pov "Qué tópico, ¿no? Málaga ha hecho en los ultimos años un esfuerzo por ofrecer al visitante ocasional una amplia oferta cultural y de ocio más allá del sol y playa que tan bien ha definido esta localidad durante décadas pasadas."
        pov "En este movimiento se engloba la creacion de los museos dedicados a Picasso, el Museo de Arte Ruso y el Pompidou, junto al renovado puerto deportivo (cuña publicitaria pendiente de remuneración)"
        k "Si eso está muy bien, pero ¿hay suecas en esos sitios?"
        espejo "¿Para qué quieres ver a las suecas? ¿No te basta con mi visión, que es la tuya?"
        k "Está bien. Nada de diversión hasta que no sea presidente."
        scene malaga2 with wipeleft
        $ renpy.pause(1, hard=True)
        pov "Oye, Ken, ¿has pensado qué harías si no llegaras a ganar?"
        k "Lo intentaría de nuevo."
        espejo "Ese es mi Ken, un optimista patológico."
        pov "¿No hay otra cosa que te gustaría hacer?"
        k "Ahora que lo dices, me gustaría protagonizar mi propia serie de televisión."
        k "No tendría un hilo conductor, ni un tema fijo, simplemente iría de mi vida como político aspirante."
        k "Recibiría a mis peculiares amigos en mi apartamento de Madrid. Uno de ellos sería un oficinista de media edad, calvo, con gafas y muy bailarín."
        k "Luego estaría mi ex, que me visitaría solo para sabotear cualquier intento de rehacer mi vida, mientras ella es incapaz de salir de su burbuja sentimental."
        k "Y por último ese amigo un poco loco que cree en las cosas más absurdas e intenta arrastrarte a hacer cosas muy estúpidas."
        k "Tengo escrito el piloto..."
        k "Pero basta de hablar de mí."
        k "¿Y bien, [jugador], ¿dónde vamos?"
        menu:
            "El Torrington Street":
                pass
            "Mr. Roboto Avenue":
                pass
            "Marmalade Road":
                pass
            "Mollete Square":
                pass
        scene malaga3 with wipeleft
        $ renpy.pause(1, hard=True)
        stop music
        k "Hay algo que no me gusta de este lugar..."
        play sound "llamada.ogg"
        $ renpy.pause(2, hard=True)
        play sound "llamada.ogg"
        $ renpy.pause(2, hard=True)
        k "¿Lo cogemos?"
        espejo "No veo por qué no."
        scene black with fade
        iker "Y ahora pasemos a las llamadas de nuestros televidentes."
        scene ikerfinal with blinds
        k "¿Hola?"
        iker "Buenas noches, amigo del misterio. ¿Cual es la cuestión que querría exponer a nuestros expertos?"
        scene malaga3 
        k "¿Qué le digo?"
        espejo "Se te tiene que ocurrir algo, galán de telenovela. Estamos en directo para toda España."
        scene ikerfinal
        k "Verás, Íker, me gustaría saber si los reptilianos existen."
        iker "Inquietante tema."
        extend " Reptilianos. ¿Extras de la serie V que no lograron reinsertarse en el mercado laboral?"
        extend " ¿Leyenda urbana?"
        extend " ¿Verdaderos amos de la Tierra?"
        scene enriquefin1
        enrique "Si me permites, Íker, me gustaría responderle a nuestro espectador."
        enrique "Querido amigo, los reptilianos no solo existen, sino que uno de ellos me debe 5.000 pesetas de las de antes."
        extend " Además, era un reptiliano famoso, no uno de esos de segunda fila que trabajan en los parques temáticos."
        scene ikerfinal
        iker "¿No nos puedes decir su nombre?"
        scene enriquefin1
        enrique "En fin... levantaría muchas ampollas, y más en la situación actual del país, pero si hay algo que me caracteriza es la búsqueda de la verdad sin importar el precio a pagar."
        scene nievesfin
        nieves "Eso, y la barba de chivo que gastas."
        scene enriquefin2
        enrique "Nieves, me aburres."
        enrique "Que lo sepa toda España, el nombre del reptiliano es Ken Sánchez."
        k "¡Pero sí soy yo!"
        k "Y no te debo nada."
        enrique "¿Cómo que no, Ken?"
        extend " Te presté cinco berenjenas para pagar los pelotazos en el Pub Roma durante la caza del monstruo del pantano de Somosierra."
        k "Pero hombre, Enrique, yo pensaba que entre amigos..."
        enrique "En temas de dinero, no hay amistad que valga. Tú mejor que nadie debería saberlo."
        enrique "Si es que todos los reptilianos son iguales."
        enrique "Otro caso, Íker. En los 70, en una de las primeras ediciones del Festival de Benicasim, por aquel entonces llamado \"Festival del Caudillo Redentor\", recibí una llamada de la Reina de Inglaterra."
        enrique "Quería asistir al evento y como yo vivía al lado... Total, que le digo: vente y te dejo mi sofá. Así te ahorras el alojamiento. Y allá estuvo varios días. Lo pasamos muy bien."
        enrique "Lo normal, vaya."
        extend " Hace cinco años, fui a Londres para un congreso de druidas conservadores y me dije: voy a visitar a Elizabeth a Buckingham Palace."
        enrique "Pues, oye, ¡que los guardias me echaron de allí a patadas!"
        enrique "Me puse a gritarle por la ventana: Elizabeth, no puedo creer que después de dejarme el baño lleno de compresas usadas ahora no me dejes ni entrar a decirte hola."
        scene ikerfinal
        iker "Aterrador..."
        scene enriquefin1
        enrique "Claro, aquello tiene muchas ventanas y no sé si me escucharía, pero desde ese día, reniego de los reptilianos."
        enrique "Antes me afeito la barba que hacerles otro favor."
        enrique "A partir de ahora, soy #TeamAnnunaki"
        enrique "Así que, sí, los reptilianos existen y como te pille uno cerca te va a joder la vida."
        scene ikerfinal
        iker "Creo que el telespectador ha colgado."
        enrique "Con tal de no pagar, hace lo que sea."
        iker "Me dicen que hay otra llamada."
        iker "Buenas noches, amigo."
        santi "Hola, Íker. ¿Te acuerdas de mí? Creo que no, porque si lo hicieras me hubieras llamado. ¿Ya no me quieres? ¿Así es como pagas mi entrega?"
        iker "Sí, me dicen que se ha cortado la conexión."
        iker "Volvemos tras unos anuncios."
        scene malaga3 with wiperight
        pov "¿Le debes dinero al señor de Vicente?"
        k "¿Qué le voy a deber?"
        k "No digas tonterías, [jugador]."
        pov "Tontería ninguna, que te he dejado cinco euros para un paquete de condones."
        k "Ya te lo reembolsaré cuando los estrene."
        espejo "Primero vayamos al gimnasio."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmalaga1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmalaga2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmalaga with fade
        show zorro at center
        k "¡Eres Tony Banderolas, el equilibrista que triunfó en las Américas y cumplió mi sueño de dar un braguetazo y tener la vida resulta."
        banderas "El mismo, y aquí está mi mujer."
        show zorro at left with move
        show zorraimg at right
        zorra "Como me llames Zorra te parto la cara."
        k "No te preocupes, guapa."
        hide zorraimg
        show zorro at center with move
        banderas "¿Qué se os ofrece?"
        extend " ¿Venís a por una muestra de mi nueva colonia: Priapo, y que todos se enteren de que estas siempre a punto.?"
        espejo "Nos preguntábamos si nos querría votar para ser presidente del país."
        banderas "A mi plim, yo solo vengo de vacaciones. Mientras no me tiréis abajo la casa..."
        k "Palabra de boy scout."
        banderas "Una cosa os quería pedir ya que estamos. ¿Me podéis echar una mano con unos autógrafos?"
        k "¿Quiere que le firme uno?"
        banderas "No, verás, resulta que aquí la..."
        show zorro at left with move
        show zorraimg at right
        zorra "Como me llames zorra pido el divorcio."
        banderas "Pero que perra te ha dado con el tema. Nadie te va a llamar zorra."
        banderas "¿Acaso te dice alguien que eres la Desperada?"
        zorra "¿Con estas tetas? Hay que estar loco."
        hide zorraimg
        show zorro at center with move
        banderas "Como iba diciendo, mi mujer ha sufrido varios reveses en la bolsa. Invirtió en Gowex, FCC y el banco Monte del Paschi."
        k "Sssh, no diga nada malo de los italianos. Estoy negociando un contrato con Berlusconi para una serie que va a ser un pelotazo."
        banderas "El problema es que necesitamos dinero. Por suerte en Hollywood somos una gran familia, pedí un par de favores y unas cuantas estrellas de cine me contrataron para que firme sus autógrafos por ellos."
        pov "¿Y no se darán cuenta los fans?"
        banderas "Son los que venden en las convenciones. Esos frikazos comprarían cualquier cosa."
        banderas "Me pondría a hacerlo yo, pero ya que habéis venido... Además, estuve practicando y ahora he mezclado la firma verdadera que tenéis que escribir con varias pruebas que hice."
        banderas "Tendréis que escoger cuál es la firma que corresponde al famoso cuyo nombre aparezca en pantalla."
        k "Parece fácil."
        banderas "Aquí os dejo la carpeta con las firmas, escogéis la que creeis que es la verdadera firma del personaje en cuestión y listo. Un voto al bolsillo."
        k "Así se las ponían a Fernando VII."
        banderas "¿El qué? ¿Las pelotas?"
        k "..."
        banderas "No sé a qué ha venido eso. A veces me pasa. Creo que es stress postraumático de cuando estuve en una fiesta de Robert Downey Jr."
        banderas "Os dejo mientras. Voy a tomar un poco el sol."
        hide zorro
        
        $ result = renpy.imagemap("images/clooneygraf.jpg", "images/clooneygraf.jpg", [
            (872, 462, 1308, 754, "clooney1"), 
            (90, 451, 532, 756, "clooney2"),
            (781, 6, 1252, 305, "clooney3"),
            ], focus="imagemap")
        
        if result == "clooney1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "¡Excelente! que uno de vosotros comience a firmar esos bañadores turbo del rincón mientras los demás continuais."
        if result == "clooney2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Tú has visto a George Clooney cara de retrasado?"
            pov "Oiga, se llaman deficientes mentales y seguro que escriben mejor que yo."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        if result == "clooney3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Tú has visto a George Clooney cara de retrasado?"
            pov "Oiga, se les llama deficientes mentales y seguro que escriben mejor que yo."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "A ver qué tal se os da el siguiente."
        pov "¿Usted no estaba tostándose al sol?"
        banderas "Fíjate que se ha nublado. 364 días al año que no deja el sol de caer a plomo sobre esta ciudad y precisamente hoy que venís, nublado."
        banderas "Terminad cuanto antes que no quiero más mal fario en mi casa."
        
        $ result = renpy.imagemap("images/sandlergraf.jpg", "images/sandlergraf.jpg", [
            (781, 6, 1252, 305, "sandlergraf1"),  
            (872, 462, 1308, 754, "sandlergraf2"),
            (90, 453, 531, 754, "sandlergraf3"),
            ], focus="imagemap")
        
        if result == "sandlergraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Perfecto. Yo no lo hubiera hecho mejor."
            extend " A decir verdad, sí, pero no quiero desmotivaros."
            k "Mis amigos dicen que me parezco mucho a él."
            banderas "Sí, tenéis una personalidad muy similar, ahora que lo mencionas."

        if result == "sandlergraf2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? Puede parecer alocado en su vida profesional pero en las distancias cortas es muy conciso y perfeccionista."
            pov "Como en \"El aguador\" ¿no?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        if result == "sandlergraf3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? Puede parecer alocado en su vida profesional pero en las distancias cortas es muy conciso y perfeccionista."
            pov "Como en \"El aguador\" ¿no?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "El último y ya os podréis marchar."
        
        $ result = renpy.imagemap("images/spielbergraf.jpg", "images/spielbergraf.jpg", [
            (872, 462, 1308, 754, "spielbergraf1"),  
            (91, 454, 532, 754, "spielbergraf2"),
            (781, 6, 1252, 305, "spielbergraf3"),
            ], focus="imagemap")
        
        if result == "spielbergraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "¡Olé tus huevos morenos!"
            extend " Que no te los he visto, ojo. Es una forma de hablar. Lo digo porque los de la meseta lleváis muy mal estos requiebros, a otros ojos, escatológicos."

            
        if result == "spielbergraf2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "No te digo yo que pudiera ser, por el trazo infantil pero se nota a la legua que está escrito con un rotulador Carioca y Stewie es alérgico. Parece mentira que no lo sepas."
            pov "¿Y cómo se supone que voy a saber eso?"
            banderas "¿Es que no os enseñan nada en la escuela?"
            banderas "¿Acaso no sabéis que no puedes darle cacahuetes a Samuel L. Jackson?"
            pov "¿Es alérgico?"
            banderas "¡Maldita sea, NO! Piensa que si alguien le ofrece es porque piensa que él es un mono."
            banderas "Aparte de ignorante, insensible racista."
            pov "Pero si yo..."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
            
        if result == "spielbergraf3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "No te digo yo que pudiera ser, por el trazo infantil pero se nota a la legua que está escrito con un rotulador Carioca y Stewie es alérgico. Parece mentira que no lo sepas."
            pov "¿Y cómo se supone que voy a saber eso?"
            banderas "¿Es que no os enseñan nada en la escuela?"
            banderas "¿Acaso no sabéis que no puedes darle cacahuetes a Samuel L. Jackson?"
            pov "¿Es alérgico?"
            banderas "¡Maldita sea, NO! Piensa que si alguien le ofrece es porque piensa que él es un mono."
            banderas "Aparte de ignorante, insensible racista."
            pov "Pero si yo..."
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
            
        banderas "Hemos terminado. Ya os llamará mi agente para ver dónde os tiene que enviar los cheques."
        espejo "¿Nos va a pagar encima?"
        banderas "Os puedo pagar debajo."
        extend " Jajajajaj."
        k "Aunque no lo creas, me han hecho muchas veces esa proposición."
        k "Pero ahora no tengo tiempo. Con los votos basta. Done el dinero a la Asociación de Huérfanos del Socialismo"

        
    if coletas == True:

        scene malaga1 with dissolve
        $renpy.pause(1,hard=True)
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿Puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        c "Ya estamos en Málaga. Nunca había estado aunque mi amigo Errejota me ha hablado muy bien de ella. Estudió en la universidad local."
        stalin "Ya... \"estudiar\"."
        c "Seguro que también se fumó sus clases jugando al Magic The Gathering en la cafetería, pero todo el mundo lo ha hecho."
        stalin "Yo no. El estado pagó una fortuna por mi matrícula en el Politécnico Industrial de Minsk en el que me gradué como Ingeniero Industrial de Minas."
        stalin "No teníamos tiempo para juegos, ocupados como estábamos en liderar la vanguardia tecnológica de la Unión Soviética."
        pov "Pues yo estuve un par de años sin entrar a clase."
        stalin "Dada tu actual situación, no es algo de lo que enorgullecerse."
        c "Y bien, [jugador], ¿dónde vamos?"
        menu:
            "El Torrington Street":
                pass
            "Mr. Roboto Avenue":
                pass
            "Marmalade Road":
                pass
            "Mollete Square":
                pass
        scene malaga3 with wipeleft
        $ renpy.pause(1, hard=True)
        stop music
        c "Hay algo que no me gusta de este lugar..."
        play sound "llamada.ogg"
        $ renpy.pause(2, hard=True)
        play sound "llamada.ogg"
        $ renpy.pause(2, hard=True)
        c "¿Lo cogemos?"
        stalin "O eso o deleitarnos con su estridente melodía."
        scene black with fade
        iker "Y ahora pasemos a las llamadas de nuestros televidentes."
        scene ikerfinal with blinds
        c "¿Hola?"
        iker "Buenas noches, amigo del misterio. ¿Cual es la cuestión que querría exponer a nuestros expertos?"
        scene malaga3 
        stalin "Ni se te ocurra decir lo que creo que vas a decir."
        c "Lo hemos hablado muchas veces. Si existe la oportunidad de conocer la verdad, tengo que intentarlo."
        scene ikerfinal
        c "Verás, Íker, me gustaría saber si los reptilianos existen."
        iker "Inquietante tema."
        extend " Reptilianos. ¿Extras de la serie V que no lograron reinsertarse en el mercado laboral?"
        extend " ¿Leyenda urbana?"
        extend " ¿Verdaderos amos de la Tierra?"
        scene enriquefin1
        enrique "Si me permites, Íker, me gustaría responderle a nuestro espectador."
        enrique "Querido amigo, los reptilianos no solo existen, sino que además uno de ellos me debe 5.000 pesetas de las de antes."
        extend " Además, era un reptiliano famoso, no uno de esos de segunda fila que trabajan en los parques temáticos."
        scene ikerfinal
        iker "¿No nos puedes decir su nombre?"
        scene enriquefin1
        enrique "En fin... levantaría muchas ampollas, y más en la situación actual del país, pero si hay algo que me caracteriza es la búsqueda de la verdad sin importar el precio a pagar."
        scene nievesfin
        nieves "Eso, y la barba de chivo que gastas."
        scene enriquefin2
        enrique "Nieves, me aburres."
        enrique "Que lo sepa toda España, el nombre del reptiliano es Staline."
        stalin "¡Yo no te debo nada, leprechaun diabético!"
        enrique "¿Cómo que no, Staline?"
        extend " Te presté cinco berenjenas para pagar los pelotazos en el Pub Roma durante la grabación de psicofonías de soldados republicanos en el valle del Jerte."
        stalin "Y yo que pensaba que eras un buen comunista, creyendo que estaba entre amigos..."
        enrique "En temas de dinero, no hay amistad que valga. Tú mejor que nadie deberías saberlo."
        enrique "Si es que todos los reptilianos son iguales."
        enrique "Otro caso, Íker. En los 70, en una de las primeras ediciones del Festival de Benicasim, por aquel entonces llamado \"Festival del Caudillo Redentor\", recibí una llamada de la Reina de Inglaterra."
        enrique "Quería asistir al evento y como yo vivía al lado... Total, que le digo: vente y te dejo mi sofá. Así te ahorras el alojamiento. Y allá estuvo varios días. Lo pasamos muy bien."
        enrique "Lo normal, vaya."
        extend " Hace cinco años, fui a Londres para un congreso de druidas seniles y me dije: voy a visitar a Elizabeth a Buckingham Palace."
        enrique "Pues, oye, ¡que los guardias no me dejaron entrar!"
        enrique "Me puse a gritarle por la ventana: Elizabeth, no puedo creer que después de dejarme el baño lleno de compresas usadas ahora no me dejes ni entrar a decirte hola."
        scene ikerfinal
        iker "Aterrador..."
        scene enriquefin1
        enrique "Claro, aquello tiene muchas ventanas y no sé si me escucharía, pero desde ese día, reniego de los reptilianos."
        enrique "Antes me afeito la barba que hacerles otro favor."
        enrique "A partir de ahora, soy #TeamAnnunaki"
        enrique "Así que, sí, los reptilianos existen y como te pille uno cerca te va a joder la vida."
        scene ikerfinal
        iker "Creo que el telespectador ha colgado."
        enrique "Con tal de no pagar, hace lo que sea."
        iker "Me dicen que hay otra llamada."
        iker "Buenas noches, amigo."
        santi "Hola, Íker. ¿Te acuerdas de mí? Creo que no, porque si lo hicieras me hubieras llamado. Llevo dos años sin apagar el móvil, esperando tu llamada..."
        iker "Sí, me dicen que se ha cortado la conexión."
        iker "Volvemos tras unos anuncios."
        scene malaga3 with wiperight
        pov "¿Le debe dinero al señor de Vicente?"
        stalin "¿Qué le voy a deber?"
        stalin "No digas tonterías, [jugador]."
        pov "Tontería ninguna, que te he dejado cinco euros para comprarte El Jueves."
        stalin "No esperes volverlos a ver."
        extend " Vayamos al gimnasio."
        $ renpy.pause(0.5, hard=True)
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextmalaga1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmalaga2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmalaga with fade
        show zorro at center
        c "¡Eres Tony Banderolas, el equilibrista que triunfó en las Américas y cumplió el sueño español de dar un braguetazo y tener la vida resulta!"
        banderas "El mismo, y aquí está mi mujer."
        show zorro at left with move
        show zorraimg at right
        zorra "Como me llames Zorra te parto la cara."
        c "No se preocupe, señora."
        hide zorraimg
        show zorro at center with move
        banderas "¿Qué se os ofrece?"
        extend " ¿Venís a por una muestra de mi nueva colonia: Priapo, y que todos se enteren de que estas siempre a punto.?"
        stalin "¿Va a votar por la alternativa adecuada en las elecciones?"
        banderas "¿Y esa cuál es?"
        stalin "La nuestra, por supuesto."
        banderas "A mi plim, yo solo vengo de vacaciones. Mientras no me tiréis abajo la casa..."
        c "Prometido."
        stalin "Siempre que no interfiera con los intereses del pueblo."
        banderas "No lo hace. Está construida sobre un acuífero sobre el que hay unas ruinas cartaginesas, sobre las que hay un cementerio indio."
        banderas "Una cosa os quería pedir ya que estamos. ¿Me podéis echar una mano con unos autógrafos?"
        c "¿Quieres que Staline te firme uno?"
        banderas "No, verás, resulta que aquí la..."
        show zorro at left with move
        show zorraimg at right
        zorra "Como me llames zorra pido el divorcio."
        banderas "Pero que perra te ha dado con el tema. Nadie te va a llamar zorra."
        banderas "¿Acaso te dice alguien que eres la Desperada?"
        zorra "¿Con estas tetas? Nadie se lo creería."
        hide zorraimg
        show zorro at center with move
        banderas "Como iba diciendo, mi mujer ha sufrido varios reveses en la bolsa. Invirtió en Gowex, FCC y Papel Higiénico Venezolano SA, entre otras commodities."
        c "Es que a quién se le ocurre..."
        banderas "Eso digo yo. Como habréis imaginado, necesitamos dinero. Por suerte en Hollywood somos una gran familia, pedí un par de favores y unas cuantas estrellas de cine me contrataron para que firme sus autógrafos por ellos."
        pov "¿Y no se darán cuenta los fans?"
        banderas "Son los que venden en las convenciones. Esos frikazos comprarían cualquier cosa."
        banderas "Lo haría yo mismo, pero ya que habéis venido... Además, estuve practicando y ahora he mezclado la firma verdadera que tenéis que escribir con varias pruebas que hice."
        banderas "Tendréis que escoger cual es la firma que corresponde a la celebridad que aparezca en pantalla."
        c "Parece fácil."
        banderas "Aquí os dejo la carpeta con las firmas, escogéis la que creeis que es la verdadera rúbrica del personaje en cuestión y listo. Un voto al bolsillo."
        c "Así se las ponían a Fernando VII."
        banderas "¿El qué? ¿Las pelotas?"
        c "..."
        banderas "No sé a qué ha venido eso. A veces me pasa. Creo que es stress postraumático de cuando estuve en una fiesta de Robert Downey Jr."
        banderas "Os dejo. Voy a tomar un poco el sol."
        hide zorro
        
        $ result = renpy.imagemap("images/gibsongraf.jpg", "images/gibsongraf.jpg", [
            (91, 454, 532, 754, "gibsongraf1"),  
            (872, 462, 1308, 754, "gibsongraf2"),
            (781, 6, 1252, 305, "gibsongraf3"),
            ], focus="imagemap")
        
        if result == "gibsongraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Perfecto. Yo no lo hubiera hecho mejor."
            extend " A decir verdad, sí, pero no quiero desmotivaros."

        if result == "gibsongraf2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Con lo loco que está Mel?"
            banderas "Le ha dejado toda su herencia a una marioneta de castor que sacó de un contenedor de la basura. Dice que por las noches le recita versos de la Biblia y que hace un goulash riquísimo."
            banderas "Mi Melania dice que no es para tanto pero con lo especialita que es para la gastronomía, es todo un elogio."
            pov "¿Pero usted no estaba soltero ya?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
            
        if result == "gibsongraf3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? ¿Con lo loco que está Mel?"
            banderas "Le ha dejado toda su herencia a una marioneta de castor que sacó de un contenedor de la basura. Dice que por las noches le recita versos de la Biblia y que hace un goulash riquísimo."
            banderas "Mi Melania dice que no es para tanto pero con lo especialita que es para la gastronomía, es todo un elogio."
            pov "¿Pero usted no estaba soltero ya?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "A ver qué tal se os da el siguiente."
        pov "¿Usted no estaba tomando el sol?"
        banderas "Fíjate que se ha nublado. 364 días al año que no deja el sol de caer a plomo sobre esta ciudad y precisamente hoy que venís, nublado."
        banderas "Terminad cuanto antes que no quiero más mal fario en mi casa."
        
        $ result = renpy.imagemap("images/sandlergraf.jpg", "images/sandlergraf.jpg", [
            (781, 6, 1252, 305, "sandlergraf1"),  #coordenadas para los boliches, etc
            (872, 462, 1308, 754, "sandlergraf2"),
            (90, 453, 531, 754, "sandlergraf3"),
            ], focus="imagemap")
        
        if result == "sandlergraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Perfecto. Yo no lo hubiera hecho mejor."
            extend " A decir verdad, sí, pero no quiero desmotivaros."


        if result == "sandlergraf2":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? Puede parecer alocado en su vida profesional pero en las distancias cortas es muy conciso y perfeccionista."
            pov "Como en \"El aguador\" ¿no?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
            
        if result == "sandlergraf3":
            scene gymmalaga
            show zorro at center with dissolve
            banderas "Pero pichita, ¿cómo va a ser esa? Puede parecer alocado en su vida profesional pero en las distancias cortas es muy conciso y perfeccionista."
            pov "Como en \"El aguador\", ¿no?"
            banderas "No trates de desviar el tema. Os habéis equivocado. Que no se vuelva a repetir."
        
        banderas "El último y ya os podréis marchar."
        
        $ result = renpy.imagemap("images/stallonegraf.jpg", "images/stallonegraf.jpg", [
            (91, 454, 532, 754, "stallonegraf1"),  #coordenadas para los boliches, etc
            (91, 454, 532, 754, "stallonegraf2"),
            (872, 462, 1308, 754, "stallonegraf3"),
            ], focus="imagemap")
        
        if result == "stallonegraf1":
            $ puntosj += 1
            scene gymmalaga
            show zorro at center with dissolve
            banderas "¡Olé tus huevos morenos!"
            extend " Que no te los he visto, ojo. Es una forma de hablar. Lo digo porque los de la meseta lleváis muy mal estos requiebros, a otros ojos, escatológicos."

            
        if result == "stallonegraf2":
            scene gymmalaga
            show zorro at center with dissolve
            stalin "¡Estúpido! Yo nunca firmaría así."
            banderas "Se nota a la legua que está escrito con un rotring de baratillo y Sly no toca nada que no haya costado al menos 3.000 dólares."
            banderas "Insistió durante siete años a su mujer para que se operara los pechos para poder sobárselos. Con eso te digo todo."
            stalin "Eso no es del todo cierto..."
            banderas "No trates de desviar el tema. Os habéis equivocado."
            
        if result == "stallonegraf3":
            scene gymmalaga
            show zorro at center with dissolve
            stalin "¡Estúpido! Yo nunca firmaría así."
            banderas "Se nota a la legua que está escrito con un rotring de baratillo y Sly no toca nada que no haya costado al menos 3.000 dólares."
            banderas "Insistió durante siete años a su mujer para que se operara los pechos para poder sobárselos. Con eso te digo todo."
            stalin "Eso no es del todo cierto..."
            banderas "No trates de desviar el tema. Os habéis equivocado."
            
        banderas "Hemos terminado. Ya os llamará mi agente para ver dónde os tiene que enviar los cheques."
        pov "¿Nos va a pagar encima?"
        banderas "Os puedo pagar debajo."
        extend " Jajajajaj."
        c "Antes de irnos, podría decir: Me llamo Iñigo Montoya. Tú mataste a mi padre, prepárate a morir?"
        banderas "No por menos de 300 euros."
        c "Descuéntelos de nuestra paga."
        banderas "Habéis firmado unos fetiches, no erigido El Escorial. Con lo que os pago solo os da para:"
        banderas "Mi caaaasa. Llamar a caaaaasa."
        stalin "Impresionante."
        banderas "Y recordad: El zorro os acompañará..."
        extend " siempre."
        banderas "Esa va de gratis."
    jump mapa