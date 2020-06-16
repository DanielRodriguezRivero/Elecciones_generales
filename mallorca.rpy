label mallorca:
    $ mallorca = True
    #personajes
    define merkel = Character("Frau Merkel", color="#C9293E", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define paella = Character("Das Paella", color="#A4A42C", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define aleman1 = Character("Hans Topt", color="#F7BE81", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define aleman2 = Character("Otto Kolner", color="#AD0017", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define aleman3 = Character("Fritz Hog", color="#C79748", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
        
    
    image gymmallorca = "images/gymmallorca.jpg"
    image mallorca1 = "images/mallorca1.jpg"
    image mallorca2 = "images/mallorca2.jpg"
    
    image cuñadomallorca = "images/merkel.png"
    image aleman1 = "images/aleman1.png"
    image aleman2 = "images/aleman2.png"
    image aleman3 = "images/aleman3.png"
    
    image gymtextmall1 = Text("{size=40}Gimnasio Shapes",color="#fff", text_align=0.3)
    image gymtextmall2 = Text("{size=40}Lorzas Uber Alles",color="#fff", text_align=0.3)
    scene travelmallorca at Pan((0, 0), (300,0), 20.0)
    play music "entradillamallorca.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "cancionciudad2.mp3"
    
    if mrajao == True:
        scene mallorca1 with fade
        $ renpy.pause(1, hard=True)
        r "Montoto, la tierra se mueve."
        montoto "Es el mareo, Presidente. No se está moviendo nada."
        r "¿Por qué hemos tenido que venir en ferry en lugar de en avión?"
        montoto "Es mejor no tener que pasar ningún control de seguridad. Recuerde la última vez."
        r "Ah, sí. Aquello..."
        montoto "Qué extraño cartel de bienvenida..."
        r "Willkommen to Mallorca."
        r "Los catalanes podrán decir lo que sea, pero el mallorquín me parece un idioma muy distinto al suyo."
        show aleman2 with moveinright
        aleman2 "Hallo!"
        montoto "Salut!"
        aleman2 "Sunt eu un..."
        extend " haiduc."
        r "¿Qué ha dicho?"
        montoto "Mis conocimientos de catalán no llegan a tanto, Presidente."
        montoto "Cuando era un joven notario me enviaron a casa de un señor de Ibiza al que había que desahuciar. Lo único que puedo repetir de todo lo que me dijo es eso."
        aleman2 "Ich möchte Ihre Hoden auf meinem Kinn zu fühlen."
        r "Ah, pues... encantado."
        pov "Ya que está, pregúntele si sabe de algún sitio bueno y barato para comer."
        r "¿Y cómo pretende que lo haga? Yo apenas el español, ya sabe."
        pov "Use el lenguaje universal de los gestos."
        r "De acuerdo, pero no le prometo nada. No parece muy despierto este señor."
        aleman2 "Oh, Füllen Sie mich mit Ihrer warme Milch!"
        montoto "Se ha puesto muy contento de pronto. ¿No?"
        aleman2 "Oh, un indígena. Mira, Fritz, unos espécimenes locales."
        show aleman2 at left with move
        show aleman3 at right with moveinright
        aleman3 "Si le tiramos unos marcos, ¿crees que bailará para nosotros?"
        aleman2 "Y cantará si es necesario, y nos hará reír, ilusionarnos y soñar con que Alemania es una gran nación y nosotros muy alemanes."
        pov "¿Acaso creen que no tenemos dignidad?"
        pov "No vamos a hacer nada por mucho dinero que nos lancen."
        r "Espera, [jugador]. Antes veamos de qué cifras estamos hablando..."
        aleman2 "Corre, Fritz. Te apuesto dos salchichas a que nos persiguen."
        hide aleman2 with moveoutleft
        hide aleman3 with moveoutleft
        r "¡Tras ellos!"
        scene mallorca2 with wipeleft
        $ renpy.pause(1, hard=True)
        montoto "Los hemos perdido..."
        show aleman1 with moveinright
        aleman1 "Ja, ja..."
        menu:
            "Ja":
                aleman1 "Was ist los?"
                menu:
                    "Was ist plas?":
                        aleman1 "Dass unkultivierten!"
                        hide aleman1 with moveoutleft
                        r "¿Qué he dicho?"
                        montoto "Parece que los mallorquines son gente susceptible."
                    "Was ist das?":
                        play music "polizei.mp3"
                        show aleman1:
                            xalign 1.0
                            linear 1.5 xalign 0.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videob behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videoc at right behind aleman1 with moveinbottom:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video1 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video2 behind aleman1 with moveinleft:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video4 at right behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video9 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video5 behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video6 at right behind aleman1 with moveinbottom:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videod at center behind aleman1:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video7 behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video8 behind aleman1 with moveinleft:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videof at right behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video3 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        scene mallorca2 with fade
                        r "¡Quiero jubilarme aquí!"
                        stop music
                        r "¿Dónde ha ido nuestro amigo?"
                        montoto "Le he perdido de vista cuando se han apagado los focos. Qué rabia. Justo cuando le iba a preguntar dónde tenía su residencia fiscal."
         
            "Nein":
                aleman1 "Dass unkultivierten!"
                hide aleman1 with moveoutleft
                r "¿Qué he dicho?"
                montoto "Parece que los mallorquines son gente susceptible."
        
        scene mallorca3 with wiperight
        $ renpy.pause(1, hard=True)
        show paella at center with moveinleft:
            ypos 0.7
        paella "Buenos días, caballeros."
        r "¡Qué alegría! Al fin alguien que es de aquí."
        paella "Siento defraudarles pero yo nací en tierras levantinas. Perdonen mis modales, me llamo Paella."
        r "Encantado."
        pov "Un momento..."
        paella "Oh, oh..."
        pov "Gambas y pollo en una paella, ¿desde cuándo?"
        paella "¡Está bien! Me habéis pillado pero, por favor, no vayáis contándolo por ahí."
        paella "Soy un arroz con cosas que hasta hace no mucho se ganaba la vida en un chiringuito de Castellón, pero tuve que exiliarme a las islas porque, un día, vino un técnico del ayuntamiento y descubrió que yo no hablo valenciano."
        r "Otra víctima de los bolivarianos. ¿Cuántas vidas de platos típicos arruinaremos en pos de unas ideas trasnochadas y caducas?"
        paella "Pues no te digo nada como te encuentres con el arroz cubano."
        pov "En cualquier caso, aquí la situación linguistica dista mucho de ser distinta. Diría incluso que es casi peor."
        paella "No crea. Los alemanes, en cuanto me ven, me gritan: \"Paella, ¡guapa! Te comía hasta el carabinero.\" Les caigo bien. Me gano la vida en un tablao flamenco y allí a nadie le importa en qué lengua me expreso."
        r "Un momento, ¿cómo que alemanes?"
        pov "Estamos buscando el gimnasio. ¿Sabes por dónde queda?"
        paella "Seguidme, os llevaré."
        
        
        scene black with wipeleft
        show gymtextmall1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmall2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmallorca with fade
        show merkel at center
        r "Volvemos a encontrarnos, Herr Merkkel."
        merkel "Wilkommen, perro. ¡Arrodíllate ante tu ama!"
        r "Ahora mismo, Ama."
        merkel "Así gustarme. Sehr gut."
        merkel "Di: ¿a qué venir tú a mis dominios?"
        r "Verá, excelentísima señora..."
        merkel "¡Los ojos al suelo, esclavo!"
        r "Sí, perdón, perdón."
        r "Venía a por si me pudiera dar su voto para conseguir el gobierno de la nación."
        merkel "Tú ser estúpido M. Rajao."
        montoto "Nos tiene calados."
        merkel "¿Cómo no dártelo si tú ser mi mejor esclavo?"
        extend " ¿Quién gobernar con desprecio mis dominios sureños mejor que tú?"
        merkel "¿Quién ser el mejor perrito de mamá?"
        r "¡Yo ser! ¡Yo ser!"
        merkel "Gut. Ahora ir, yo tener que buscar mi strap on para reunión con Eurogrupo."
        merkel "Tú no orinar sobre alfombra al salir, Ja?"
        r "Nein, mein fuhrer."
        merkel "Tsss, que luego ganar mala fama."
        $ puntosj +=3
        hide merkel
        montoto "Nada como doblar la cerviz para conseguir lo que se quiere."
        
    if ken == True:
        scene mallorca1 with fade
        $ renpy.pause(1, hard=True)
        k "¿No os parece que todo se moviera como cuando te pasas toda la noche pim pam, pim pam sin haber comido nada en todo el día?"
        espejo "Es el mareo, mi pirata de los mares del sur. No se está moviendo nada."
        k "¿Por qué hemos tenido que venir en ferry en lugar de en avión?"
        espejo "No me dejan montar en aviones, recuerda. Dicen que soy un peligro para la seguridad de los viajeros..."
        k "El único peligro que corren es el de quedar prendados de tu reflejo."
        espejo "Te quiero, Ken."
        k "Y yo a mí."
        pov "¿Podemos continuar?"
        k "Me da la sensación de que eres un poco aguafiestas. No te suelen llamar para las quedadas de tuiteros, ¿verdad?"
        pov "Yo no tengo Twitter."
        k "Uy, que asocial..."
        espejo "Políglota y rapsoda, ¿qué es lo que dice ese cartel de ahí?"
        k "Qué extraño cartel de bienvenida..."
        k "Willkommen to Mallorca."
        k "Los catalanes podrán decir lo que sea, pero el mallorquín me parece un idioma muy distinto al suyo."
        show aleman2 with moveinright
        aleman2 "Hallo!"
        espejo "Salut!"
        aleman2 "Sunt eu un..."
        extend " haiduc."
        k "¿Qué ha dicho?"
        espejo "Mis conocimientos de catalán no llegan a tanto, Presidente."
        espejo "Antes de conocerte estuve trabajando en los vestuarios de una sauna de Baviera. Jamás he visto tantos \"frankfurt\" en mi vida. No solían hablar mucho, empero."
        aleman2 "Ich möchte Ihre Hoden auf meinem Kinn zu fühlen."
        k "Ah, pues... encantado."
        pov "Ya que está, pregúntele si sabe de algún sitio bueno y barato para comer."
        k "¿Y cómo pretende que lo haga? Yo apenas el español, ya sabe."
        pov "Use el lenguaje universal de los gestos."
        k "De acuerdo, pero no le prometo nada. No parece muy despierto este señor."
        aleman2 "Oh, Füllen Sie mich mit Ihrer warme Milch!"
        espejo "Se ha puesto muy contento de pronto. ¿No? Era una mirada muy común en aquella sauna..."
        aleman2 "Oh, un indígena. Mira, Fritz, unos espécimenes locales."
        show aleman2 at left with move
        show aleman3 at right with moveinright
        aleman3 "Si le tiramos unos marcos, ¿crees que bailará para nosotros?"
        aleman2 "Y cantará si es necesario, y nos hará reír, ilusionarnos y soñar con que Alemania es una gran nación y nosotros muy alemanes."
        pov "¿Acaso creen que no tenemos dignidad?"
        pov "No vamos a hacer nada por mucho dinero que nos lancen."
        k "Espera, [jugador]. Antes veamos de qué cifras estamos hablando... ¿Les paga Willy Brandt?"
        aleman2 "Corre, Fritz. Te apuesto dos salchichas a que nos persiguen."
        hide aleman2 with moveoutleft
        hide aleman3 with moveoutleft
        k "¡Tras ellos!"
        scene mallorca2 with wipeleft
        $ renpy.pause(1, hard=True)
        espejo "Los hemos perdido..."
        show aleman1 with moveinright
        aleman1 "Ja, ja..."
        menu:
            "Ja":
                aleman1 "Was ist los?"
                menu:
                    "Was ist plas?":
                        aleman1 "Dass unkultivierten!"
                        hide aleman1 with moveoutleft
                        k "¿Qué he dicho?"
                        espejo "Parece que los mallorquines son gente susceptible."
                    "Was ist das?":
                        play music "polizei.mp3"
                        show aleman1:
                            xalign 1.0
                            linear 1.5 xalign 0.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videob behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videoc at right behind aleman1 with moveinbottom:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video1 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video2 behind aleman1 with moveinleft:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video4 at right behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video9 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video5 behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video6 at right behind aleman1 with moveinbottom:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videod at center behind aleman1:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video7 behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video8 behind aleman1 with moveinleft:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videof at right behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video3 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        scene mallorca2 with fade
                        k "¡Quiero jubilarme aquí!"
                        stop music
                        k "¿Dónde ha ido nuestro amigo?"
                        espejo "Le he perdido de vista cuando se han apagado los focos."
         
            "Nein":
                aleman1 "Dass unkultivierten!"
                hide aleman1 with moveoutleft
                k "¿Qué he dicho?"
                espejo "Parece que los mallorquines son gente susceptible."

        
        scene mallorca3 with wiperight
        $ renpy.pause(1, hard=True)
        show paella at center with moveinleft:
            ypos 0.7
        paella "Buenos días, caballeros."
        k "¡Qué alegría! Al fin alguien que es de aquí."
        paella "Siento defraudarles pero yo nací en tierras levantinas. Perdonen mis modales, me llamo Paella."
        k "Encantado."
        pov "Un momento..."
        paella "Oh, oh..."
        pov "Gambas y pollo en una paella, ¿desde cuándo?"
        paella "¡Está bien! Me habéis pillado pero, por favor, no vayáis contándolo por ahí."
        paella "Soy un arroz con cosas que hasta hace no mucho se ganaba la vida en un chiringuito de Castellón, pero tuve que exiliarme a las islas porque, un día, vino un técnico del ayuntamiento y descubrió que yo no hablo valenciano."
        k "Otra víctima de los extremismos. ¿Cuántas vidas de platos típicos arruinaremos en pos de unas ideas trasnochadas y caducas?"
        paella "Pues no te digo nada como te encuentres con el arroz cubano."
        pov "En cualquier caso, aquí la situación linguistica dista mucho de ser distinta. Diría incluso que es casi peor."
        paella "No crea. Los alemanes, en cuanto me ven, me gritan: \"Paella, ¡guapa! Te comía hasta el carabinero.\" Les caigo bien. Me gano la vida en un tablao flamenco y allí a nadie le importa en qué lengua me expreso."
        k "Un momento, ¿cómo que alemanes?"
        pov "Estamos buscando el gimnasio. ¿Sabes por dónde queda?"
        paella "Seguidme, os llevaré."
        
        scene black with dissolve
        call battle_def4 from _call_battle_def4
        show gymtextmall1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmall2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmallorca with fade
        $ renpy.pause(1, hard=True)
        k "¿Hola?"
        show merkel at center with dissolve
        merkel "Hail! ¿Quién ser tú?"
        k "Hola... "
        extend " guapa. ¿Cómo va eso?"
        merkel "¿Tú intentar ligar conmigo?"
        extend " ¿Venir aquí a intentar aprovecharte de inocente germana de prietas carnes y generosos pechos?"
        k "Yo solo..."
        merkel "¿Querer robar mi virtud como DB robar el dinero de los contribuyentes de los bancos de la periferia?"
        merkel "Tú ser joven atractivo..."
        k "Gracias. Me lo dicen mucho."
        merkel "Pero yo deber darte paliza antes para guardar las apariencias."
        merkel "Ser líder del mundo germano no ser fácil si creer que acostar con el primero que pasar y decirte cuatro cosas bonitas."
        k "Oiga, que yo es que tampoco..."
        merkel "¡Callar y bajar los pantalones mientras te voy golpeando eróticamente!"
        hide merkel
        call battle_presetup4 from _call_battle_presetup4
        call battle4 from _call_battle4
        stop music
        show merkel at center with pixellate
        merkel "¡Tú ganar!"
        merkel "Ser perro malo, ¿eh?"
        extend " ¡Matador!"
        k "Señora, le aseguro que mis intenciones son puras. Solo quiero que me vote."
        merkel "Pero tú follar conmigo, ¿ja?"
        k "Vale, pero luego, que ahora tengo prisa."
        merkel "Gut. Ir y volver rápido. Mi sauerkraut arde de ganas."
        
    if coletas == True:
 
        scene mallorca1 with dissolve
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        c "Bufff, se mueve todo como después de una sesión contínua de La Hora Chanante con los colegas..."
        c "¿Por qué hemos tenido que venir en ferry en lugar de en avión?"
        stalin "Ni loco me monto yo en una caja con alas. Si tú estás tan chiflado como para hacerlo, adelante. No cuentes conmigo."
        pov "A mi tampoco me hace mucha gracia volar."
        stalin "Gracias. No esperaba una nota de sensatez en ti."
        c "Dejaos de tonterías."
        c "¿Sabéis lo primero que se me viene a la cabeza cuando me hablan de Mallorca?"
        extend " Amarcord."
        stalin "Jo jo"
        pov "Jo jo jo"
        c "Jo jo jo jo jo"
        stalin "Jo jo jo jo jo jo"
        c "Podríamos hacer un tour por las localizaciones de la película."
        stalin "Sabes que no la vas a encontrar, ¿verdad?"
        c "Sí, pero..."
        pov "¿Os habéis fijado en ese cartel?"
        c "Willkommen to Mallorca."
        stalin "Recuerdo otro cartel similar a las afueras de Berlin..."
        show aleman2 with moveinright
        aleman2 "Hallo!"
        stalin "Salut!"
        aleman2 "¡Genosse Stalin , ich bin froh , Sie zu sehen!"
        extend " ¿Was machst du denn hier?"
        stalin "Ich bin begleiten diese infraser an ihrem Platz in der Welt zu finden.."
        aleman2 "¿Wann haben Sie zusammen mit den Juden ??"
        stalin "Es ist hässlich wie eine Ratte , aber nicht jew."
        aleman2 "Sie sollten Ihr Haar mindestens waschen."
        c "¿Qué está diciendo?"
        stalin "Que le gusta tu camisa."
        c "Dale las gracias de mi parte. Ya ves, es una camisa parda como cualquier otra..."
        aleman2 "Oh, ¿Habe ich mein Liebhaber präsentiert, Fritz?"
        show aleman2 at left with move
        show aleman3 at right with moveinright
        aleman3 "Erfreut."
        stalin "Vergnügen."
        stalin "Sie haben immer sehr fag gewesen, Otto. ¡Jajaja!"
        aleman2 "Und Sie sehen ihn immer noch, jajajaj."
        aleman2 "Wir müssen gehen."
        extend " Auf Wiedersehen!"
        stalin "Wir sehen uns auf der nächsten Oktoberfest."
        hide aleman2 with moveoutleft
        $ renpy.pause(0.5, hard=True)
        hide aleman3 with moveoutleft
        c "Se le veía simpático."
        stalin "Mucho, pero hasta que no le pierdas de vista, camina con la espalda pegada a la pared."
        scene mallorca2 with wipeleft
        $ renpy.pause(1, hard=True)
        stalin "Ya está. Puedes relajar el ano."
        show aleman1 with moveinright
        stalin "¡Maldición! ¡En guardia de nuevo!"
        aleman1 "Ja, ja..."
        menu:
            "Ja":
                aleman1 "Was ist los?"
                menu:
                    "Was ist plas?":
                        aleman1 "Dass unkultivierten!"
                        hide aleman1 with moveoutleft
                        c "¿Qué he dicho?"
                        stalin "Parece que los nuevos mallorquines son gente susceptible."
                    "Was ist das?":
                        play music "polizei.mp3"
                        show aleman1:
                            xalign 1.0
                            linear 1.5 xalign 0.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videob behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videoc at right behind aleman1 with moveinbottom:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video1 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video2 behind aleman1 with moveinleft:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video4 at right behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video9 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video5 behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video6 at right behind aleman1 with moveinbottom:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videod at center behind aleman1:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video7 behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video8 behind aleman1 with moveinleft:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show videof at right behind aleman1 with moveinright:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        show video3 behind aleman1 with moveintop:
                            zoom 1.0
                            linear 1.0 zoom 1.5
                            linear 1.0 zoom 1.0
                            repeat
                        $ renpy.pause(1, hard=True)
                        scene mallorca2 with fade
                        stop music
                        c "¡Me ha recordado a mis tiempos de fan de Kraftwerk!"
                        c "Escuchaba todos sus discos, hasta que descubrí que detrás se escondía una multinacional fabricante de quesos..."
                        c "¿Dónde ha ido nuestro amigo?"
                        stalin "Doy gracias al dios en que no creo por haberle perdido de vista."
         
            "Nein":
                aleman1 "Dass unkultivierten!"
                hide aleman1 with moveoutleft
                c "¿Qué he dicho?"
                stalin "Parece que los nuevos mallorquines son gente susceptible."

        scene mallorca3 with wiperight
        $ renpy.pause(1, hard=True)
        show paella at center with moveinleft:
            ypos 0.7
        paella "Buenos días, caballeros."
        c "¡Qué alegría! Al fin alguien que es de aquí."
        paella "Siento defraudarles pero yo nací en tierras levantinas. Perdonen mis modales, me llamo Paella."
        c "Encantado."
        pov "Un momento..."
        paella "Oh, oh..."
        pov "Gambas y pollo en una paella, ¿desde cuándo?"
        paella "¡Está bien! Me habéis pillado pero, por favor, no vayáis contándolo por ahí."
        paella "Soy un arroz con cosas que hasta hace no mucho se ganaba la vida en un chiringuito de Castellón, pero tuve que exiliarme a las islas porque, un día, vino un técnico del ayuntamiento y descubrió que yo no hablo valenciano."
        c "Otra víctima de los bolivarianos. ¿Cuántas vidas de platos típicos arruinaremos en pos de unas ideas trasnochadas y caducas?"
        stalin "Pst..."
        c "Ah, es verdad, que los bolivarianos somos nosotros. ¡Malditos neoliberales, me tienen la cabeza loca ya!"
        paella "Pues no te digo nada como te encuentres con el arroz cubano."
        pov "En cualquier caso, aquí la situación linguistica dista mucho de ser distinta. Diría incluso que es casi peor."
        paella "No crea. Los alemanes, en cuanto me ven, me gritan: \"Paella, ¡guapa! Te comía hasta el carabinero.\" Les caigo bien. Me gano la vida en un tablao flamenco y allí a nadie le importa en qué lengua me expreso."
        pov "Estamos buscando el gimnasio. ¿Sabes por dónde queda?"
        paella "Seguidme, os llevaré."
        scene black with dissolve
        call battle_def2 from _call_battle_def2
        show gymtextmall1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextmall2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymmallorca with fade
        show merkel at center
        merkel "Willkommen a mi hogar, trabajador aleatorio de mis dominios sureños."
        merkel "¿Qué se te ofrecer?"
        c "Hola, me llamo Coletas Montoya. Tú mataste a mi amigo Chiripas, prepárate a morir."
        stalin "Dios mío, debe de ser el primer gitano-burgués / comunista de palo que he conocido nunca."
        stalin "Si no fuera por lo que me paga..."
        merkel "Estos españoles estar todos majaras."
        hide merkel
        call battle_presetup2 from _call_battle_presetup2
        call battle2 from _call_battle2
        stop music
    
    jump mapa