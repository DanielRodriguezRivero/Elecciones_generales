label valencia:
    $ valencia = True
    
    #personajes
    define chimo = Character("Chimo Valla", color="#469539", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define mario = Character("Mario Herreno", color="#89AC28", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define gordi = Character("Gordi", color="#842D50", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define lori = Character("Moni Lori", color="#3D280F", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    #imagenes
    image gymvalencia = "images/gymvalencia.jpg"
    image valencia1 = "images/valencia1.jpg"
    image valencia2 = "images/valencia2.jpg"
    
    image cuñadovalencia = "images/chimo.png"
    image lori = "images/lori.png"
    image gordi = "images/gordi.png"
    image herreno = "images/herreno.png"
    
    
    image gymtextval = Text("{size=40}Gimnasio Mujeres, Hombres y Mancuernas",color="#fff", text_align=0.3)
    image gymtextval2 = Text("{size=40}La puerta al estrellato",color="#fff", text_align=0.3)
    image textfifa = Text("{size=40}La FIFA (Federación Internacional de Fallas Around the World) nos impide mostrar las imágenes.",color="#fff", text_align=0.3)
    
    scene travelvalencia at Pan((0, 0), (800,0), 14.0)
    play music "entradillavalencia.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "cancionciudad2.mp3"
    
    if mrajao == True:
        scene valencia1 with fade
        $ renpy.pause(1, hard=True)
        show herreno at center with dissolve
        mario "¡Valenciaaaaaaa, es la tierra de las fallas, de la horchata y del amooooor...!"
        mario "Hombre, ¡turistas por aquí!"
        mario "¿No habréis venido a ver las Fallas(tm)?"
        r "Ya que estamos, nos gustaría. Nos han hablado muy bien de ellas."
        mario "Y mejor que os iba a hablar."
        extend " Ocurre una cosa, acabaron justo ayer."
        r "Qué mala suerte."
        mario "Como decimos los valenciás, \"La mala suerte, que un petardazo, no dura más.\""
        mario "¡Mañana mismo vuelven a comenzar las Fallas(tm)!"
        montoto "Solo estaremos hoy en la ciudad."
        mario "¡Pero eso no puede ser!"
        extend " ¡No puedo permitirlo!"
        mario "Venir a Valencia y no ver las Fallas(tm) es como escupirle al Papa en el carajillo."
        r "Oiga, le veo un poco borroso."
        mario "¿Tan temprano y ya borracho?"
        extend " ¡Ese es el espíritu, me cago en dios!"
        mario "Me has caído bien. Los valenciás somos gente y si no puedes disfrutar de las fiestas, al menos vivirás una parte de la experiencia."
        mario "¡Moni!"
        show herreno at left with move
        show lori at right with moveinright
        lori "¿Quieres una horchata, maderfacka?"
        mario "Después. Ve a por los petardos de emergencia."
        hide lori with moveoutright
        $ renpy.pause(1, hard=True)
        show lori at right with moveinright
        lori "¿Dónde los coloco, jefe?"
        mario "Ahí, junto al ninot del Capitán Pescanova."
        mario "Tengan ustedes un petardo de esos que explotan al lanzarlos contra el suelo."
        r "No se moleste."
        mario "No es ninguna molestia, es un deber nacional."
        mario "Lori, enciende la mecha."
        lori "¿Con mucho suaj?"
        mario "Con fuego, Lori. Estoy cansado de repetírtelo."
        scene black with dissolve
        show textfifa:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        play sound "fallas.mp3"
        $ renpy.pause(10, hard=True)
        scene valencia3 with dissolve
        show herreno at center with fade
        r "Ha sido lo más bonito que he visto en mi vida."
        mario "¿Se lo dije o no se lo dije?"
        montoto "¿Nos hemos movido de lugar? No me he dado cuenta."
        mario "El poder de las fallas..."
        r "Volveremos en otra ocasión."
        mario "Ya saben, cualquier día menos hoy."
        mario "Venga esa horchata, Lori."
        
        scene valencia2 with dissolve
        $ renpy.pause(0.5, hard=True)
        show gordi at center with fade
        r "Disculpe, señora. No queríamos molestarla."
        gordi "No son ninguna molestia. Simplemente estaba aquí, reflexionando..."
        pov "¿Sobre algún tema en particular?"
        gordi "Sobre todo y sobre nada. Sobre lo divino y lo... No, solamente sobre lo humano."
        gordi "¿Te ha fallado alguien alguna vez?"
        pov "Imagino que como a todos."
        gordi "Supongo que sí..."
        extend " ¿Y te dolió?"
        pov "Las primeras veces. Luego comprendí que quizá sea lo normal."
        gordi "Pero lo \"normal\" no tendría que ser siempre lo aceptado. Soy una buena persona, amable, inteligente, simpática... ¿por qué tengo que sentirme sola?"
        gordi "¿Dónde están todos los que deberían estar pegándose por compartir sus experiencias conmigo?"
        pov "¿No tienes amigos?"
        gordi "Muchos y muy buenos."
        gordi "O quizás no tantos, pero los que están, cuentan. Y, sin embargo, no puedo evitar sentirme sola."
        pov "Todos lo estamos. Cargamos con el peso de nuestro mundo y lo único que podemos hacer es aliviar el peso apoyándolo en los hombros de otro, pero si el tiempo es demasiado, ese otro termina por cansarse."
        pov "Por eso yo creo que lo mejor es ir cediendo nuestra carga en multitud de hombros, por pequeños períodos de tiempo."
        gordi "Es una forma como otra cualquiera de justificar la poligamia."
        pov "Por desgracia con mi anterior pareja no funcionó."
        gordi "En fin, tengo que marcharme."
        pov "Adiós. Sé que le irá bien."
        gordi "Gracias."
        hide gordi with moveouttop
        pov "Desde aquí se ve el gimnasio. En marcha."
        
        scene black with dissolve
        show gymtextval:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextval2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymvalencia with fade
        show cuñadovalencia at center
        r "Hola"
        chimo "Saludos, amigos de la fiesta."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        r "Qué señor más extraño, Montoto. Parece que lleve un sampler encima."
        montoto "De Valencia se puede esperar cualquier cosa, Presidente."
        pov "¿Por qué no vamos al gran para que podamos marcharnos rápido?"
        r "Qué impaciente eres, [jugador]. Como para tener una pareja frígida."
        pov "Oiga, ¿eso a qué viene?"
        r "Mire, zanjemos el asunto."
        r "Perdone usted, señor..."
        chimo "Valla. Chimo Valla."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        montoto "¿Va a hacer ese ruido cada vez que hable?"
        chimo "¿Cual?"
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        montoto "Ese."
        chimo "No entiendo."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        pov "¡Ya está bien!"
        extend " ¿Nos va a dar su voto o no?"
        play sound "sirena.mp3"
        $ renpy.pause(1, hard= True)
        chimo "¡La policía!"
        chimo "¡Rápido, cógeme esto!"
        call pong from _call_pong
        r "Pues nada. Volvamos a la carretera."
        
    if ken == True:
        scene valencia1 with dissolve
        $ renpy.pause(1, hard=True)
        show herreno at center with fade
        mario "¡Valenciaaaaaaa, es la tierra de las fallas, de la horchata y del amooooor...!"
        mario "Hombre, ¡turistas por aquí!"
        mario "¿No habréis venido a ver las Fallas(tm)?"
        k "Ya que estamos, nos gustaría. Nos han hablado muy bien de ellas."
        mario "Y mejor que os iba a hablar."
        extend " Ocurre una cosa, acabaron justo ayer."
        k "Qué mala suerte."
        mario "Como decimos los valenciás, \"La mala suerte, que un petardazo, no dura más.\""
        mario "¡Mañana mismo vuelven a comenzar las Fallas(tm)!"
        espejo "Solo estaremos hoy en la ciudad."
        mario "¡Pero eso no puede ser!"
        extend " ¡No puedo permitirlo!"
        mario "Venir a Valencia y no ver las Fallas(tm) es como escupirle al Papa en el carajillo."
        k "Oiga, le veo un poco borroso."
        mario "¿Tan temprano y ya borracho?"
        extend " ¡Ese es el espíritu, me cago en dios!"
        mario "Me has caído bien. Los valenciás somos gente y si no puedes disfrutar de las fiestas, al menos vivirás una parte de la experiencia."
        mario "¡Moni!"
        show herreno at left with move
        show lori at right with moveinright
        lori "¿Quieres una horchata, maderfacka?"
        mario "Después. Ve a por los petardos de emergencia."
        hide lori with moveoutright
        $ renpy.pause(1, hard=True)
        show lori at right with moveinright
        lori "¿Dónde los coloco, jefe?"
        mario "Ahí, junto al ninot del Capitán Pescanova."
        mario "Tengan ustedes un petardo de esos que explotan al lanzarlos contra el suelo."
        k "No se moleste."
        mario "No es ninguna molestia, es un deber nacional."
        mario "Lori, enciende la mecha."
        lori "¿Con mucho suaj?"
        mario "Con fuego, Lori. Estoy cansado de repetírtelo."
        scene black with dissolve
        show textfifa:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        play sound "fallas.mp3"
        $ renpy.pause(10, hard=True)
        scene valencia3 with dissolve
        show herreno at center with fade
        k "Ha sido lo más bonito que he visto en mi vida."
        mario "¿Se lo dije o no se lo dije?"
        montoto "¿Nos hemos movido de lugar? No me he dado cuenta."
        mario "El poder de las fallas..."
        k "Volveremos en otra ocasión."
        mario "Ya saben, cualquier día menos hoy."
        mario "Venga esa horchata, Lori."
        
        scene valencia2 with dissolve
        $ renpy.pause(0.5, hard=True)
        show gordi at center with fade
        k "Disculpe, señora. No queríamos molestarla."
        gordi "No son ninguna molestia. Simplemente estaba aquí, reflexionando..."
        pov "¿Sobre algún tema en particular?"
        gordi "Sobre todo y sobre nada. Sobre lo divino y lo... No, solamente sobre lo humano."
        gordi "¿Te ha fallado alguien alguna vez?"
        pov "Imagino que como a todos."
        gordi "Supongo que sí..."
        extend " ¿Y te dolió?"
        pov "Las primeras veces. Luego comprendí que quizá sea lo normal."
        gordi "Pero lo \"normal\" no tendría que ser siempre lo aceptado. Soy una buena persona, amable, inteligente, simpática... ¿por qué tengo que sentirme sola?"
        gordi "¿Dónde están todos los que deberían estar pegándose por compartir sus experiencias conmigo?"
        pov "¿No tienes amigos?"
        gordi "Muchos y muy buenos."
        gordi "O quizás no tantos, pero los que están, cuentan. Y, sin embargo, no puedo evitar sentirme sola sin esa otra persona con la que conectar."
        pov "Todos lo estamos. Cargamos con el peso de nuestro mundo y lo único que podemos hacer es aliviar el peso apoyándolo en los hombros de otro, pero si el tiempo es demasiado, ese otro termina por cansarse."
        pov "Por eso yo creo que lo mejor es ir cediendo nuestra carga en multitud de hombros, por pequeños períodos de tiempo."
        gordi "Es una forma como otra cualquiera de justificar la poligamia."
        pov "Por desgracia con mi anterior pareja no funcionó."
        gordi "En fin, tengo que marcharme."
        pov "Adiós. Sé que le irá bien."
        gordi "Gracias."
        hide gordi with moveouttop
        pov "Desde aquí se ve el gimnasio. En marcha."
        
        
        scene black with dissolve
        show textfifa:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        play sound "fallas.mp3"
        $ renpy.pause(10, hard=True)
        scene valencia3 with dissolve
        show herreno at center with fade
        k "Ha sido lo más bonito que he visto en mi vida."
        mario "¿Se lo dije o no se lo dije?"
        montoto "¿Nos hemos movido de lugar? No me he dado cuenta."
        mario "El poder de las fallas..."
        k "Volveremos en otra ocasión."
        mario "Ya saben, cualquier día menos hoy."
        mario "Venga esa horchata, Lori."
      
        scene black with dissolve
        show gymtextval:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextval2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymvalencia with fade
        show cuñadovalencia at center
        k "Hola"
        chimo "Saludos, amigos de la fiesta."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        k "Qué señor más extraño, Montoto. Parece que lleve un sampler encima."
        espejo "De Valencia se puede esperar cualquier cosa, Candor de féminas."
        pov "¿Por qué no vamos al gran para que podamos marcharnos rápido?"
        k "Qué impaciente eres, [jugador]. Como para tener una pareja frígida."
        pov "Oiga, ¿eso a qué viene?"
        k "Mire, zanjemos el asunto."
        k "Perdone usted, señor..."
        chimo "Valla. Chimo Valla."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        espejo "¿Va a hacer ese ruido cada vez que hable?"
        chimo "¿Cual?"
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        espejo "Ese."
        chimo "No entiendo."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        pov "¡Ya está bien!"
        extend " ¿Nos va a dar su voto o no?"
        play sound "sirena.mp3"
        $ renpy.pause(1, hard= True)
        chimo "¡La policía!"
        chimo "¡Rápido, cógeme esto!"
        call pong from _call_pong_1
        k "Pues nada. Volvamos a la carretera."

        
    if coletas == True:
 
        scene valencia1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        
        
        scene valencia1 with fade
        $ renpy.pause(1, hard=True)
        show herreno at center with dissolve
        mario "¡Valenciaaaaaaa, es la tierra de las fallas, de la horchata y del amooooor...!"
        mario "Hombre, ¡turistas por aquí!"
        mario "¿No habréis venido a ver las Fallas(tm)?"
        c "Ya que estamos, nos gustaría. Nos han hablado muy bien de ellas."
        mario "Y mejor que os iba a hablar."
        extend " Ocurre una cosa, acabaron justo ayer."
        c "Qué mala suerte."
        mario "Como decimos los valenciás: \"La mala suerte, que un petardazo, no dura más.\""
        mario "¡Mañana mismo vuelven a comenzar las Fallas(tm)!"
        stalin "Solo estaremos hoy en la ciudad."
        mario "¡Pero eso no puede ser!"
        extend " ¡No puedo permitirlo!"
        mario "Venir a Valencia y no ver las Fallas(tm) es como ir al estadio del Elche C.F. y no cagarse en la puerta."
        c "Oiga, le veo un poco borroso."
        mario "¿Tan temprano y ya borracho?"
        extend " ¡Ese es el espíritu, me cago en dios!"
        mario "Me has caído bien. Los valenciás somos gente y si no puedes disfrutar de las fiestas, al menos vivirás una parte de la experiencia."
        mario "¡Moni!"
        show herreno at left with move
        show lori at right with moveinright
        lori "¿Quieres una horchata, maderfacka?"
        mario "Después. Ve a por los petardos de emergencia."
        hide lori with moveoutright
        $ renpy.pause(1, hard=True)
        show lori at right with moveinright
        lori "¿Dónde los coloco, jefe?"
        mario "Ahí, junto al ninot del Capitán Pescanova."
        mario "Tengan ustedes un petardo de esos que explotan al lanzarlos contra el suelo."
        c "No se moleste."
        mario "No es ninguna molestia, es un deber nacional."
        mario "Lori, enciende la mecha."
        lori "¿Con mucho suaj?"
        mario "Con fuego, Lori. Estoy cansado de repetírtelo."
        scene black with dissolve
        show textfifa:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        play sound "fallas.mp3"
        $ renpy.pause(10, hard=True)
        scene valencia3 with dissolve
        show herreno at center with fade
        c "Ha sido lo más bonito que he visto en mi vida."
        mario "¿Se lo dije o no se lo dije?"
        stalin "Bah, nada como los fuegos de Berlín cuando nos adentramos en el Reichstag en llamas para colocar la bandera roja en el tejado."
        stalin "Eso sí que fue todo un espectáculo..."
        pov "¿Nos hemos movido de lugar? No me he dado cuenta."
        mario "El poder de las fallas..."
        c "Volveremos en otra ocasión."
        mario "Ya saben, cualquier día menos hoy."
        mario "Venga esa horchata, Lori."
        
        scene valencia2 with wiperight
        $ renpy.pause(0.5, hard=True)
        show gordi at center with dissolve
        c "Disculpe, señora. No queríamos molestarla."
        gordi "No son ninguna molestia. Simplemente estaba aquí, reflexionando..."
        pov "¿Sobre algún tema en particular?"
        gordi "Sobre todo y sobre nada. Sobre lo divino y lo... No, solamente sobre lo humano."
        gordi "¿Te ha fallado alguien alguna vez?"
        pov "Imagino que como a todos."
        gordi "Supongo que sí..."
        extend " ¿Y te dolió?"
        pov "Las primeras veces. Luego comprendí que quizá sea lo normal."
        gordi "Pero lo \"normal\" no tendría que ser siempre lo aceptado. Soy una buena persona, amable, inteligente, simpática... ¿por qué tengo que sentirme sola?"
        gordi "¿Dónde están todos los que deberían estar pegándose por compartir sus experiencias conmigo?"
        pov "¿No tienes amigos?"
        gordi "Muchos y muy buenos."
        gordi "O quizás no tantos, pero los que están, cuentan. Y, sin embargo, no puedo evitar sentirme sola sin esa otra persona con la que conectar."
        pov "Todos lo estamos. Cargamos con el peso de nuestro mundo y lo único que podemos hacer es aliviar el peso apoyándolo en los hombros de otro, pero si el tiempo es demasiado, ese otro termina por cansarse."
        pov "Por eso yo creo que lo mejor es ir cediendo nuestra carga en multitud de hombros, por pequeños períodos de tiempo."
        gordi "Es una forma como otra cualquiera de justificar la poligamia."
        pov "Por desgracia mi anterior pareja no pensaba lo mismo."
        gordi "En fin, mejor dejar de divagar. Tengo que marcharme."
        pov "Adiós. Sé que le irá bien."
        gordi "Gracias."
        hide gordi with moveouttop
        pov "Desde aquí se ve el gimnasio. En marcha."
        
        
        scene black with dissolve
        show gymtextval:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextval2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymvalencia with fade
        show cuñadovalencia at center
        stop music
        c "¡Hola!"
        chimo "Saludos, amigos de la fiesta."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        c "Qué tío más raro, Staline. Parece que lleve un sampler encima."
        stalin "De la decadente Valencia se puede esperar cualquier cosa, camarada."
        pov "¿Por qué no vamos al grano para que podamos marcharnos rápido?"
        c "Qué impaciente eres, [jugador]. Como para tener una pareja frígida."
        pov "¿Eso a qué viene?"
        c "Mira, zanjemos el asunto."
        c "Perdone usted, señor..."
        chimo "Valla. Chimo Valla."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        stalin "¿Va a hacer ese ruido cada vez que hable?"
        chimo "¿Cual?"
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        stalin "Ese."
        chimo "No entiendo."
        play sound "uhha.mp3"
        $ renpy.pause(1, hard= True)
        pov "¡Ya está bien!"
        extend " ¿Nos va a dar su voto o no?"
        play sound "sirena.mp3"
        $ renpy.pause(1, hard= True)
        chimo "¡La pasma!"
        chimo "¡Rápido, guárdame esto!"
        call pong from _call_pong_2
        c "Pues nada. Volvamos a la carretera."
    jump mapa