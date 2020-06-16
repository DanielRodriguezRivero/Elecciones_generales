label fin:
    #con el tema de los puntos, nunca usar puntoscoletas, etc, a la hora de puntuar a nuestro jugador, siempre puntosj
    #Se supone que ya hemos visto todas las ciudades y ahora vemos los resultados.
    $ puntoscoletas = renpy.random.randint(11, 17)
    $ puntosken = renpy.random.randint(11, 17)
    $ puntosrajao= renpy.random.randint(11, 17)
    image fin = Text("{size=80}¿FIN?",color="#fff", text_align=0.3)
    
    #final ken sanchez
    image tken1 = Text("{size=40}Con el Presoe al mando, España no pagó la multa al devolver al videoclub sin rebobinar el DVD de Hostal Royal Manzanares.",color="#fff", text_align=0.3)
    image tken2 = Text("{size=40}Los gatos se comieron a los perros.",color="#fff", text_align=0.3)
    image tken3 = Text("{size=40}Los de Bilbao follaron.",color="#fff", text_align=0.3)
    image tken4 = Text("{size=40}Las aguas se volvieron ácido clorhídrico.",color="#fff", text_align=0.3)
    image tken5 = Text("{size=40}Los secretarios de los banqueros fueron esclavizados y obligados a trabajar de sol a sol.",color="#fff", text_align=0.3)
    image tken6 = Text("{size=40}Beyoncé se volvió mora.",color="#fff", text_align=0.3)
    image bilbao = "images/bilbao.jpg"
    image beyonce = "images/beyonce.jpg"
    image gato = "images/gato.png"
    image ebro = "images/ebro.jpg"
    
    #final rajao
    image trajao1 = Text("{size=40}Rajao hundió el país hasta colocarlo a la altura de la Atlántida.",color="#fff", text_align=0.3)
    image trajao2 = Text("{size=40}Mientras los operarios alemanes embargaban la Moncloa, Rajao seguía insistiendo en un discurso televisado a la nación que su gobierno estaba sacando a España de la crisis.",color="#fff", text_align=0.3)
    image trajao3 = Text("{size=40}No pudo terminar su discurso. Los operarios se llevaron la cámara.",color="#fff", text_align=0.3)
    image trajao4 = Text("{size=40}Los españoles de bien tuvieron que huir de la península y solo se quedaron los facinerosos y los portugueses, que invadieron lo que antaño fue una gran nación.",color="#fff", text_align=0.3)
    image trajao5 = Text("{size=40}Portugal es hoy día la mayor potencia exportadora de cera para el bigote.",color="#fff", text_align=0.3)
    image atlantida = "images/atlantis.jpg"
    image embargo = "images/alegoria.jpg"
    image titanic = "images/titanic.jpg"

    
    #final coletas
    image tcoletas1 = Text("{size=40}Cuando llegó a Rusia la noticia de la victoria de Queremos, en el mausoleo de Lenin, su momia se levantó de improviso y comenzó su marcha de camino a España.",color="#fff", text_align=0.3)
    image tcoletas2 = Text("{size=40}Los Simpsons ya lo habían predicho. Otra vez.",color="#fff", text_align=0.3)
    image tcoletas3 = Text("{size=40}Las puertas del infierno se abrieron en Ruzafa, escupiendo miles de demonios que abarrotaron las calles.",color="#fff", text_align=0.3)
    image tcoletas4 = Text("{size=40}Doscientos quince de ellos fueron ingresados horas después por sobredosis y coma etílico.",color="#fff", text_align=0.3)
    image tcoletas5 = Text("{size=40}Del cielo cayó fuego y azufre. En Córdoba no notaron la diferencia.",color="#fff", text_align=0.3)
    image tcoletas6 = Text("{size=40}Y al final se acabó el mundo.",color="#fff", text_align=0.3)
    image tcoletas7 = Text("{size=40}Staline ganó el Oscar por su papel protagonista en \"El potro italiano\".",color="#fff", text_align=0.3)
    image finmundo = "images/finmundo.jpg"
    image leninzombi = "images/leninzombi.jpg"
    image ruzafa = "images/ruzafa.jpg"
    image cordoba = "images/cordoba.jpg"
    image oscar = "images/oscar.jpg"
    
    #puntuaciones especiales por visitar segun que ciudades
    if boliches == True and torrelavega == True:
        $ puntosj += 1
    if mallorca == True and tenerife == True and ceuta == True:
        $ puntosj += 2
    if bilbao == True and vigo == True and barcelona == True and valencia == True:
        $ puntosj += 3
    if barcelona == True and extrarradio == True and valencia == True and novalencia==True and mallorca== True:
        $ puntosj += 4
    if vigo == True and torrelavega== True and bilbao == True and larioja == True:
        $ puntosj += 3
    
    
    if mrajao == True:
        stop music
        r "Bien, volvamos a casa y comprobemos los resultados. Tengo un buen presentimiento."
        r "Se ha hecho corto el viaje, ¿verdad?"
        pov "Uy, sí. Ni me he dado cuenta."
        scene ppkhq with dissolve
        montoto "¡Corre, pon la tele!"
        if puntoscoletas > puntosj: 
            if puntoscoletas > puntosken:
                jump fincoletas
            else:
                jump finken
        elif puntosken > puntosj:
            jump finken
        else:
            scene noticias with fade
            presentador "... y de esa forma terminaron los Terceros juegos mundiales de Internet."
            presentador "Volviendo a las noticias locales, he aquí los resultados de la Gymkana nacional que ha mantenido en vilo al país durante las últimas horas."
            presentador "Me dicen desde el control central que el ganador es... "
            extend " M. Rajao, líder incuestionable del P.P.K."
            presentador "Esta noche seguro que hay fiesta en el Club de Caballeros de BlackFriars."
            presentador "He de romper mi inquebrantable parcialidad para comentar que no saben el peso que se me ha quitado de encima. "
            presentador "Seguro que se presenta un futuro brillante para nuestro país."
            presentador "Buenas noches."
            scene fin1 with fade
            pov "Lo hice cariño. Ayudé a limpiar el planeta Marte de rojos y M. Rajao logró ganar las elecciones."
            churri "Siempre confié en tí, amor."
            scene fin3 with dissolve
            pov "Cariño..."
            churri "¿Ocurre algo amor?"
            pov "Se me ocurre..." 
            extend "  ¿Y si todo fue un sueño?"
            churri "En ese caso... "
            extend "bésame antes de que despertemos."
            scene fin2 with fade
            play music "final.mp3"
            with Pause (8)
            jump credits
        
    if coletas == True:
        stop music
        c "Volvamos a casa y esperemos a los resultados."
        c "En estos momentos recuerdo esa escena de \"Solo ante el peligro\" y me veo en el papel de Gary Cooper enfrentando a mi destino mientras el pueblo observa, expectante."
        stalin "Te echaremos de menos, [jugador]"
        pov "No es verdad."
        stalin "No lo es, no. Pero no se me ocurre otra fórmula con la que despedirte más rápidamente."
        pov "¿Qué tal adios?"
        stalin "Demasiado religioso..."
        stalin "Hasta luego."
        scene queremoshq with fade
        stalin "¡Enciende la máquina capitalista de lavar cerebros!"
        if puntosrajao > puntosj: 
            if puntosrajao > puntosken:
                jump finrajao
            else:
                jump finken
        elif puntosken > puntosj:
            jump finken
        else:
            scene noticias with fade
            presentador "... antes de que le detuvieran, logró introducir en su cuerpo catorce polos de fresa. Todo un récord."
            presentador "Volviendo a las noticias locales, he aquí los resultados de la Gymkana nacional que ha mantenido en vilo al país durante las últimas horas."
            presentador "Me dicen que el ganador es... "
            extend "Oh, dios mío, tengo que llamar a casa para que mi sirvienta comience a tapiar las ventanas."
            presentador "El Coletas se ha alzado con la victoria por un gran margen de votos. Desconocemos el número exacto pero desde la Junta Electoral le dan por ganador."
            presentador "Habrá que fiarse."
            presentador "Por mi parte, solo me queda decirles: Buena suerte. Confíen en que los Estados Unidos de Norteamérica vendrán a rescatarnos."
            scene fin1 with fade
            pov "El capitalismo acabó con la vida en marte pero Queremos conseguirá que vuelva a florecer."
            churri "Pero, ¿y España?"
            scene fin3 with dissolve
            pov "Esos ya no tienen salvación."
            churri "No mucha, no."
            pov "Cariño, por las tesis de abril, dame un beso bolchevique."
            scene fin2 with fade
            play music "final.mp3"
            with Pause (8)
            jump credits
        
        
    if ken == True:
        stop music
        k "Volvamos a casa para que la victoria nos alcance en nuestro mullido sillón para las mechas."
        k "[jugador], ha sido un placer compartir tu tiempo conmigo."
        k "¿Lo de follar lo has reconsiderado?"
        pov "..."
        k "En otra ocasión será. Buena suerte en la vida y come muchos pepinos. Son buenos para todo."
        scene presoehq with dissolve
        espejo "Amado mío, prende la caja de sueños."
        if puntoscoletas > puntosj:
            if puntoscoletas > puntosrajao:
                jump fincoletas
            else:
                jump finrajao
        elif puntosrajao > puntosj:
            jump finrajao
        else:
            scene noticias with fade
            presentador "... el Real Madrid se complica así su ascenso a Primera División."
            presentador "Volviendo a las noticias locales, he aquí los resultados de la Gymkana nacional que ha mantenido en vilo al país durante las últimas horas."
            presentador "Me dicen desde el control central que el ganador es... "
            presentador "Pues ni tan mal: "
            extend " ¡Ken Sánchez, del Presoe!"
            presentador "Puede que ni él se lo crea todavía pero al menos podemos respirar aliviados: el peligro rojo ha sido conjurado."
            presentador "Claro que tampoco es que vaya a ir la cosa a mejor..."
            scene black 
            pov "¡Ganamos! Al fin ahora todos podrán comprobar cómo Ken Sánchez es el hombre que buscaban: el marido en el bar, el niño en la boda, el señor en el armario de una infidelidad..."
            scene fin1 with fade
            pov "Pero ocurre una cosa..."
            churri "¿A qué te refieres?"
            pov "Cariño, ¿cómo han podido los socialistas volver a convertir España en un erial?"
            churri "Acaban de llegar al gobierno. Esto es obra de otros."
            pov "Es verdad. Mucho tiempo hemos pasado en el taxi aquel."
            scene fin3 with dissolve
            churri "Bueno, ¿me vas a besar como si fueras Ken Sánchez, Líder del mundo libre?"
            pov "Lo intentaré."
            scene fin2 with fade
            play music "final.mp3"
            with Pause (8)
            jump credits

label fincoletas:
    stop music
    scene noticias with fade
    presentador "... a lo que el Papa respondió: Mis cojones."
    presentador "Volviendo a las noticias locales, he aquí los resultados de la Gymkana nacional que ha mantenido en vilo al país durante las últimas horas."
    presentador "Me dicen que el ganador es... "
    extend "Oh, dios mío, tengo que llamar a casa para que mi sirvienta comience a tapiar las ventanas."
    presentador "El Coletas se ha alzado con la victoria por un gran margen de votos. Desconocemos el número exacto pero desde la Junta Electoral le dan por ganador."
    presentador "Habrá que fiarse."
    presentador "Por mi parte, solo me queda decirles: Buena suerte. Confíen en que los Estados Unidos de Norteamérica vendrán a rescatarnos."
    #todo el rollo de las imágenes.
    play music "ganacoleta.mp3"
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show tcoletas1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide tcoletas1
    show leninzombi:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide leninzombi
    show tcoletas2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide tcoletas2
    show tcoletas7:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3, hard=True)
    show oscar with dissolve
    $ renpy.pause(2, hard=True)
    hide oscar
    show tcoletas3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(6, hard=True)
    hide tcoletas3
    show tcoletas4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(6, hard=True)
    hide tcoletas4
    show ruzafa with dissolve
    $ renpy.pause(4, hard=True)
    hide ruzafa
    show tcoletas5:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide tcoletas5
    show cordoba with dissolve
    $ renpy.pause(4, hard=True)
    hide cordoba
    show tcoletas6:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide tcoletas6
    show finmundo with dissolve
    $ renpy.pause(4,hard=True)
    hide finmundo
    $ renpy.pause(4, hard=True)
    show fin:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide fin
    $ renpy.pause(3, hard=True)
    jump credits

label finken:
    stop music
    scene noticias with fade
    presentador "... y entonces el seleccionador nacional le agarró un pecho y le susurró al oído: Morientes was right."
    presentador "Volviendo a las noticias locales, he aquí los resultados de la Gymkana nacional que ha mantenido en vilo al país durante las últimas horas."
    presentador "Me dicen desde el control central que el ganador es... "
    presentador "Pues ni tan mal: "
    extend " ¡Ken Sánchez, del Presoe!"
    presentador "Puede que ni él se lo crea todavía pero al menos podemos respirar aliviados: el peligro rojo ha sido conjurado."
    presentador "Claro que tampoco es que vaya a ir la cosa a mejor..."
    play music "ganaken.mp3"
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show tken1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(6, hard=True)
    hide tken1
    show tken2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide tken2
    show gato with dissolve
    $ renpy.pause(4, hard=True)
    hide gato
    show tken3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide tken3
    show bilbao with dissolve
    $ renpy.pause(4, hard=True)
    hide bilbao
    show tken4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide tken4
    show ebro with dissolve
    $ renpy.pause(4, hard=True)
    hide ebro
    show tken5:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide tken5
    show tken6:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide tken6
    show beyonce with dissolve
    $ renpy.pause(4,hard=True)
    hide beyonce
    $ renpy.pause(4, hard=True)
    show fin:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide fin
    $ renpy.pause(3, hard=True)
    jump credits

label finrajao:
    stop music
    scene noticias with fade
    presentador "... antes de que pudiera abrir la boca, Madonna reconoció que se lo había follado."
    presentador "Volviendo a las noticias locales, he aquí los resultados de la Gymkana nacional que ha mantenido en vilo al país durante las últimas horas."
    presentador "Me dicen desde el control central que el ganador es... "
    extend " M. Rajao, líder incuestionable del P.P.K."
    presentador "Esta noche seguro que hay fiesta en el Club de Caballeros de BlackFriars."
    presentador "He de romper mi inquebrantable parcialidad para comentar que no saben el peso que se me ha quitado de encima. "
    presentador "Seguro que se presenta un futuro brillante para nuestro país."
    presentador "Buenas noches."
    play music "ganarajao.mp3"
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show trajao1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(5, hard=True)
    hide trajao1
    show atlantida with dissolve
    $ renpy.pause(4, hard=True)
    hide atlantida
    show trajao2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(7, hard=True)
    hide trajao2
    show embargo with dissolve
    $ renpy.pause(7, hard=True)
    hide embargo
    show trajao3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(7, hard=True)
    hide trajao3
    show titanic with dissolve
    $ renpy.pause(7, hard=True)
    hide titanic
    show trajao4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(7, hard=True)
    hide trajao4
    show trajao5:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(7, hard=True)
    hide trajao5
    show fin:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard=True)
    hide fin
    $ renpy.pause(3, hard=True)
    jump credits
    
    
    
