label vigo:
    $ vigo = True
    $ lluvial = 0
    
    define dragui = Character("M. Draghi", color="#13AB05", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback)
    define felindra = Character("Felindra", color="#31F1A1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback)
    define caballo = Character("Félix Sáenz", color="#97AB6F", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback)
    define creador = Character("The Creator", color="#8678c7", ctc="ctc_blink", ctc_position="fixed", show_two_window=True,callback=callback)
    
    image gymvigo = "images/gymvigo.jpg"
    image vigo1 = "images/vigo1.jpg"
    image vigo2 = "images/vigo2.jpg"
    image vigo3 = "images/vigo3.jpg"
    image draguim = "images/dragui.jpg"
    
    image felindra = "images/felindra.png"
    image caballo = "images/caballo.png"
    
    image gymtextvi1 = Text("{size=40}Gimnasio Fulano",color="#fff", text_align=0.3)
    image gymtextvi2 = Text("{size=40}Lo levantamos con la polla",color="#fff", text_align=0.3)
    scene travelvigo at Pan((0, 0), (300,0), 20.0)
    play music "entradillavigo.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "cancionciudad2.mp3"
    $ lluvia = renpy.random.randint(1,20)

    if mrajao == True:
      
        scene vigo1 with dissolve
        if lluvia > 10:
            show rain
        r "¿Era necesario venir aquí?"
        montoto "Nos vendrá bien. Es un caladero de votos tradicional. Tenemos mucho apoyo."
        r "Es que..."
        pov "Es que, ¿qué?"
        r "..."
        montoto "Nada, nada. Pongámonos en marcha. El gimnasio no está muy lejos."
        pov "Creo que viene una chica hacia aquí."
        r "Mientras sea una mujer..."
        show felindra at center with moveinleft
        felindra "Buenos días, caballeros."
        r "¿No te habrá enviado tu padre, tu hermano o algún varón de tu círculo de allegados?"
        felindra "En absoluto. Me acerco a ustedes para ofrecerles en exclusiva una oferta que no podrán rechazar."
        montoto "¿Un 45 por ciento de retención en la nómina para la Seguridad Social?"
        felindra "Algo muchísimo mejor: ni más ni menos que la fantástica colección literaria de Mr. Roboto."
        r "¿De quién?"
        felindra "¿Ha vivido usted en una cueva esta última década?"
        r "Yo no llamaría así a la chabola en la que me he hospedado últimamente, pero tampoco es el Ritz. No le voy a engañar."
        felindra "Mr. Roboto es un jubilado que dedica su tiempo libre a escribir grandes obras de ayer y de hoy."
        felindra "Su colección literaria consta de los siguientes títulos: "
        extend " \"Crónicas de Mr. Roboto volúmenes I y II\""
        felindra " \"Crónicas de Moriarty\""
        felindra "\"A diario.\""
        felindra "\"A Mario le gusta Sandra.\""
        felindra "\"Jim del Espacio Exterior.\""
        felindra "\"Un día completo.\""
        felindra "\"Anuario Robótico 2015.\""
        felindra "Y finalmente: \"Twine, una aproximación.\""
        felindra "Puedes comprarlo en su tienda en Lulu, en la siguiente dirección:"
        extend " http://www.lulu.com/spotlight/mrroboto"
        felindra "Si se los pides a él personalmente, te saldrán un poco más baratos."
        r "Muy bien, joven. ¿Sabe dónde está la heladería más cercana?"
        if boliches == True:
            felindra "Y para que no os vayáis de vacío, os regalo su último relato."
            felindra "Tengan. Y recuerden: http://www.lulu.com/spotlight/mrroboto"
            hide felindra with moveoutleft
            r "[cuento]"
            montoto "Vaya chusta."
            pov "¡Oiga!"
            montoto "Es lo que es."
        else:
            felindra "¿Qué me dicen?"
            extend " ¿Comprarán alguno?"
            menu:
                "Desde luego":
                    felindra "Eso le hará muy feliz. Más que una fototetas."
                    felindra "¿Han apuntado la dirección de la web?"
                    felindra "En cuanto lleguen a casa no olviden hacerse con los títulos que más les gusten."
                    r "Descuida, chata. En cuanto a ese jacuzzi..."
                    felindra "Se me hace tarde. ¡Disfruten de la ciudad!"
                    hide felindra with moveoutleft
                "No me interesa":
                    show felindra at right with move
                    show cuñadoboliches at left with moveinleft
                    roboto "¿Me estás vacilando?"
                    roboto "Vienes a mi blog. Te descargas el juego. Echas un rato divertido con los colegas mientras os fumáis unos petas."
                    pov "Yo no he hecho nada de eso..."
                    roboto "Disfrutas de este maravilloso mundo que he creado para tí, ¿y no eres capaz de dejarte unos míseros euros, que seguro que te los gastas todos los fines de semana en condones que caducan años después porque no eres capaz de abrirlos?"
                    roboto "¿Sabes lo que te digo?"
                    roboto "GA "
                    extend "ME "
                    extend "O "
                    extend "VER"
                    pov "Ya ves tú que cosa."
                    roboto "Además te he metido un troyano y estoy viendo todas las fotos guarras que escondes en tu disco."
                    roboto "Por cierto, al de las fotos del directorio \"Facturas\", dile que no emita cheques que luego no puede pagar."
                    roboto "¡Que entren los créditos!"
                    jump credits
                    
        r "Continuemos antes de que nos encontremos con algún indeseable."
        scene vigo3 with wiperight
        $ renpy.pause(1, hard=True)
        r "Aquí me crié yo... "
        extend "Puede que no en esta ciudad, la que quiera que sea, pero sí en estas tierras galegas..."
        r "Era yo rapaz cuando el meu padre me llevaba al Ferrol y me decía: Algún día, serás tan grande como él."
        r "Yo no sabía muy bien a quién se refería, pero yo queria ser como Yul Brynner, con su calva reluciente y su mirada pícara y torva a la vez, un moderno Hércules cosaco."
        montoto "Presidente, por un momento creí que hablabas en otro idioma."
        r "Ha sido... "
        extend "un flash... "
        extend "una mansión en el campo, hace mucho..."
        r "Iba corriendo por el jardín gritando: ¡Papá! ¡Papá! ¡Falo galego!"
        r "Mi padre se levantaba, se quitaba el cinto y me pegaba mientras me gritaba que en esa casa solo se hablaba..."
        r "Montoto, soy una victima de mi época."
        montoto "Cuando volvamos a casa, recuérdame que solicite alguna subvención por aquello de la ley de la memoria histórica."
        scene vigo2 with dissolve
        $ renpy.pause(1, hard=True)
        r "¿Dónde vamos ahora?"
        pov "Pues por mí podríamos buscar un Centro Mail. Va a salir dentro de poco el nuevo FIFA y este año sí que van a incluir una novedad. Tengo que reservarlo."
        r "No tenemos tiempo para juegos. Hay que..."
        show caballo at center with moveinright
        caballo "¡Hombre, M. Rajao! Eso que llevas en el bolsillo es un sobre o es que..."
        r "¡No, tú no!"
        extend " ¡NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!"
        scene black with fade
        stop music
        creador "¡Hola! Perdona que te interrumpa. Soy el creador."
        creador "No el creador de todo, solo de este juego. Te he estado observando un rato y ... mira, que tu cara lo dice todo y no quiero que lo pases mal, así a lo tonto..."
        creador "Te doy la oportunidad de poner fin a la experiencia y salir con las mismas neuronas con las que comenzaste a jugar, aunque con menos tiempo para descargarte videos de Xhamster, o de continuar jugando..."
        creador "Tuya es la decisión."
        menu:
            "¡Quiero salir de aquí":
                $ renpy.play("error.wav")
                scene pantalla
                $ renpy.pause(2.5)
                creador "JAJAJAJA. Es todo mentira."
                creador "¡De aquí no se va nadie!"
                creador "Vuelve a la historia..."
                creador "¡AHORA!"
        
            "¿Bromeas? Llevo años esperando este juego. Quiero seguir hasta el final.":
                creador "Oh... ¡Muchas gracias! No esperaba que te fuera a gustar esto..."
                creador "Oye, ya que te gusta el juego, infiero que yo también te molo."
                extend " ¿Me enviarías una fototetas?"
                menu:
                    "¡No!":
                        creador "Lo esperaba, no te creas. Yo siempre lo digo: put your fototetas where your mouth is (or will be tomorrow night after an expensive dinner and a couple of bottles of wine) pero ya no hay ética entre los jugadores así que..."
                        creador "Puedes seguir jugando, pero piensa que mientras disfrutas con mi creación, estoy llorando en un rincón mientras intento excitarme viendo antiguas fotos de Terelu."
                        creador "¡Por tu culpa!"
                    "Solo porque eres tú":
                        creador "Jo, no puedo ser más afortunado. Me la enviarás de verdad, ¿no? Mi dirección de correo es: veranodeldescontento@gmail.com"
                        creador "Si no me la envías, que sepas que el karma puede que te la devuelva, que una mañana te despiertes y entre los mensajes privados de WA lleno de fotopollas no socilitadas."
                        creador "¡Disfruta del juego!"
        scene vigo3 with fade
        $ renpy.pause(1,hard=True)
        play music "cancionciudad2.mp3"
        r "¿Qué ha pasado?"
        montoto "Creo que nos hemos quedado traspuestos durante un instante."
        pov "¿Los tres?"
        r "A mí me suele pasar. La vida del político profesional es muy dura. Exige de una alta preparación y entrenamiento diario."
        r "La gente piensa que solo consiste en quedarse de pie en sitios y asentir con la cabeza mientras se mira al infinito en los ojos del que habla."
        r "Pero no. Es mucho más que eso."
        montoto "Presidente, ahí está el gimnasio."
        r "¡Seguidme, conozco el camino!"
        pov "Tú y cualquiera. Si está ahí al otro lado de la calle."
        scene black with dissolve
        show gymtextvi1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextvi2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymvigo with fade
        montoto "No te lo quería decir, [jugador], pero has sido muy sabio al escoger esta ciudad."
        extend " El dueño del gimnasio es M. Rajao."
        r "¿Ah sí?"
        montoto "Claro. ¿No te acuerdas?"
        r "Es que hace mucho que no pasaba por aquí..."
        r "¿Entonces qué hacemos ahora?"
        montoto "Pues consigues tu voto automáticamente."
        r "¡Qué bien! Así cualquiera puede llegar a presidente."
        pov "Y que lo digas..."
        $ puntosj += 3
        
        
    if ken == True:
        
        scene vigo1 with dissolve
        if lluvia > 10:
            show rain
        $ renpy.pause(1, hard=True)
        espejo "Pongámonos en marcha. El gimnasio no está muy lejos."
        pov "Creo que viene una chica hacia aquí."
        k "¿Es guapa?"
        show felindra at center with moveinleft
        felindra "Buenos días, caballeros."
        k "Buenos días, compañera socialista. Irradias energía con esa sonrisa tan refrescante."
        felindra "¡Gracias!"
        felindra "Es la energía que necesito para ofrecerles en exclusiva una oferta que no podrán rechazar."
        k "¿Tú y yo en un jacuzzi en las Islas Mauricio con todos los gastos pagados?"
        felindra "Algo muchísimo mejor. Ni más ni menos que la fantástica colección literaria de Mr. Roboto."
        k "¿De quién?"
        felindra "¿Ha vivido usted en una cueva esta última década?"
        k "Yo no llamaría así a la chabola en la que me he hospedado últimamente, pero tampoco es el Ritz. No le voy a engañar."
        felindra "Mr. Roboto es un jubilado que dedica su tiempo libre a escribir grandes obras de ayer y de hoy."
        felindra "Su colección literaria consta de los siguientes títulos: "
        extend " \"Crónicas de Mr. Roboto volúmenes I y II\""
        felindra " \"Crónicas de Moriarty\""
        felindra "\"A diario.\""
        felindra "\"A Mario le gusta Sandra.\""
        felindra "\"Jim del Espacio Exterior.\""
        felindra "\"Un día completo.\""
        felindra "\"Anuario Robótico 2015.\""
        felindra "Y finalmente: \"Twine, una aproximación.\""
        felindra "Puedes comprarlo en su tienda en Lulu, en la siguiente dirección:"
        extend " http://www.lulu.com/spotlight/mrroboto"
        felindra "Si se los pides a él personalmente, te saldrán un poco más baratos."
        k "Espejo, ¿a quién está hablando?"
        espejo "Mi azucarillo, está rompiendo la cuarta pared y hablando con el que controla los hilos de nuestra existencia."
        k "¿Felipe?"
        if boliches == True:
            felindra "Y para que no os vayáis de vacío, os regalo su último relato."
            felindra "Tengan. Y recordad: http://www.lulu.com/spotlight/mrroboto"
            hide felindra with moveoutleft
            k "[cuento]"
            espejo "Vaya chusta."
            pov "¡Oiga!"
            espejo "Es lo que es."
        else:
            felindra "¿Qué me dicen?"
            extend " ¿Comprarán alguno?"
            menu:
                "Desde luego":
                    felindra "Eso le hará muy feliz. Más que una fototetas."
                    felindra "¿Han apuntado la dirección de la web?"
                    felindra "En cuanto lleguen a casa no olviden hacerse con los títulos que más les gusten."
                    k "Descuida, chata. En cuanto a ese jacuzzi..."
                    felindra "Se me hace tarde. ¡Disfruten de la ciudad!"
                    hide felindra with moveoutleft
                "No me interesa":
                    show felindra at right with move
                    show cuñadoboliches at left with moveinleft
                    roboto "¿Me estás vacilando?"
                    roboto "Vienes a mi blog. Te descargas el juego. Echas un rato divertido con los colegas mientras os fumáis unos petas."
                    pov "Yo no he hecho nada de eso..."
                    roboto "Disfrutas de este maravilloso mundo que he creado para tí, ¿y no eres capaz de dejarte unos míseros euros, que seguro que te los gastas todos los fines de semana en condones que caducan años después porque no eres capaz de abrirlos?"
                    roboto "¿Sabes lo que te digo?"
                    roboto "GA "
                    extend "ME "
                    extend "O "
                    extend "VER"
                    pov "Ya ves tú que cosa."
                    roboto "Además te he metido un troyano y estoy viendo todas las fotos guarras que escondes en tu disco."
                    roboto "Por cierto, al de las fotos del directorio \"Facturas\", dile que no emita cheques que luego no puede pagar."
                    roboto "¡Que entren los créditos!"
                    jump credits
                    
        
       
        scene black with dissolve
        call battle_def3 from _call_battle_def3
        show gymtextvi1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextvi2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymvigo with fade
        k "¿Hola?"
        k "Nos ha dicho un caballo ahí fuera que este es el gimnasio local."
        extend " ¿Es eso cierto?"
        r "Totalmente. Y me alegro de que hayas venido, así podré machacar tu culo sin testigos."
        montoto "Presidente, recuerde, nada de hablar de culos que luego la gente hace comentarios maledicentes."
        r "Tienes razón."
        r "Olvida lo que he dicho, Señor Potato."
        k "Eso es un golpe bajo incluso para ti, Rajao."
        r "Pues ven, que te voy a dar unos cuantos."
        call battle_presetup3 from _call_battle_presetup3
        call battle3 from _call_battle3
        stop music
        k "¡Lo hicimos! ¡Hemos derrotado al malvado M. Rajao!"
        scene draguim with fade
        dragui "No tan rápido."
        espejo "¿Quién eres tú?"
        dragui "Escoria. Deberías conocerme."
        pov "Yo sí. ¿Tenéis confeti a mano?"
        dragui "Eso funcionó una vez, pero ya no."
        dragui "Estoy harto de vuestra palabrería sin fundamento producto de un escritor recién despertado de la siesta."
        dragui "¡Vuelve en ti M. Rajao!"
        play sound "resucitar.wav"
        $ renpy.pause(2, hard=True)
        r "¡Muchas gracias, amigo!"
        r "No sé qué haría yo sin ti."
        dragui "No vayas diciendo por ahí que te hemos ayudado."
        r "¿Ayudarme a qué?"
        dragui "Ese es nuestro chico."
        scene gymvigo
        $ renpy.pause(1, hard=True)
        call battle_presetup3 from _call_battle_presetup3_1
        call battle3 from _call_battle3_1
        stop music
        k "¡Maldición! Ha logrado escapar."
        espejo "Tendremos que ganarle en las urnas limpiamente."
        k "Como siempre hemos hecho."
        espejo "Como siempre hemos hecho."
        pov "Al menos hemos conseguido los votos necesarios."
        $ puntosj +=3
        
    if coletas == True:
    
        scene vigo1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        stalin "Pongámonos en marcha. El gimnasio no está muy lejos."
        pov "Creo que viene una chica hacia aquí."
        c "¿Será del Frente Popular Izquierdista?"
        show felindra at center with moveinleft
        felindra "Buenos días, caballeros."
        stalin "¡Disidente!"
        c "Buenos días, amiga. Llévame ante vuestro líder de izquierdas."
        felindra "Me temo que no entiendo de política."
        stalin "En este país esa es la respuesta por defecto."
        felindra "De lo que sí entiendo es de literatura, y por ello, vengo a ofrecerles en exclusiva una oferta que no podrán rechazar."
        c "¿Un pacto progresista que derribe lo viejo y aupe a lo algo menos viejo?"
        felindra "Algo muchísimo mejor: ni más ni menos que la fantástica colección literaria de Mr. Roboto."
        c "¿De quién?"
        felindra "¿Ha vivido usted en una cueva esta última década?"
        stalin "Él no, pero yo sí. Vivía en un agujero al sur de los Urales junto a un oso llamado Dostoievski. El maldito oso más inteligente que he conocido jamás. Podría haber presidido el consejo de los soviets si hubiera cuidado su higiene personal."
        stalin "Hibernábamos durante el invierno liberal y con el primer amanecer rojo, salíamos al bosque a cazar conejos y discutir sobre el materialismo dialéctico de los atunes."
        c "A la chica no le interesan tus batallitas, Staline."
        felindra "Es una historia muy interesante, pero no tanto como la de Mr. Roboto."
        felindra "Mr. Roboto es un jubilado que dedica su tiempo libre a escribir grandes obras de ayer y de hoy."
        felindra "Su colección literaria consta de los siguientes títulos: "
        extend " \"Crónicas de Mr. Roboto volúmenes I y II\""
        felindra " \"Crónicas de Moriarty\""
        felindra "\"A diario.\""
        felindra "\"A Mario le gusta Sandra.\""
        felindra "\"Jim del Espacio Exterior.\""
        felindra "\"Un día completo.\""
        felindra "\"Anuario Robótico 2015.\""
        felindra "Y finalmente: \"Twine, una aproximación.\""
        felindra "Puedes comprarlo en su tienda en Lulu, en la siguiente dirección:"
        extend " http://www.lulu.com/spotlight/mrroboto"
        felindra "Si se los pides a él personalmente, te saldrán un poco más baratos."
        stalin "¿Por qué no nos mira cuando habla?"
        stalin "¿A quién está hablando esta disidente?"
        c "Creo que está rompiendo la cuarta pared y dirigiéndose al que controla los hilos de nuestra existencia."
        c "He visto algo parecido... Ah, sí, en House of Cards."
        if boliches == True:
            felindra "Y para que no os vayáis de vacío, os regalo su último relato."
            felindra "Tengan. Y recuerden: http://www.lulu.com/spotlight/mrroboto"
            hide felindra with moveoutleft
            c "[cuento]"
            stalin "Vaya chusta."
            pov "¡Oiga!"
            stalin "He visto actas de reuniones del PCUS sobre la evolución de la cosecha de grano en Rostov más interesantes que esto."
        else:
            felindra "¿Qué me dicen?"
            extend " ¿Comprarán alguno?"
            menu:
                "Desde luego":
                    felindra "Eso le hará muy feliz. Más que una fototetas."
                    felindra "¿Han apuntado la dirección de la web?"
                    felindra "En cuanto lleguen a casa no olviden hacerse con los títulos que más les gusten."
                    c "¿No sabrás por dónde queda la sucursal del 15M local?"
                    felindra "Se me hace tarde. ¡Disfruten de la ciudad!"
                    hide felindra with moveoutleft
                "No me interesa":
                    show felindra at right with move
                    show cuñadoboliches at left with moveinleft
                    roboto "¿Me estás vacilando?"
                    roboto "Vienes a mi blog. Te descargas el juego. Echas un rato divertido con los colegas mientras os fumáis unos petas."
                    pov "Yo no he hecho nada de eso..."
                    roboto "Disfrutas de este maravilloso mundo que he creado para tí, ¿y no eres capaz de dejarte unos míseros euros, que seguro que te los gastas todos los fines de semana en condones que caducan años después porque no eres capaz de abrirlos?"
                    roboto "¿Sabes lo que te digo?"
                    roboto "GA "
                    extend "ME "
                    extend "O "
                    extend "VER"
                    pov "Ya ves tú que cosa."
                    roboto "Además te he metido un troyano y estoy viendo todas las fotos guarras que escondes en tu disco."
                    roboto "Por cierto, al de las fotos del directorio \"Facturas\", dile que no emita cheques que luego no puede pagar."
                    roboto "¡Que entren los créditos!"
                    jump credits   
            
        scene black with dissolve
        call battle_def from _call_battle_def
        show gymtextvi1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextvi2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymvigo with fade
        c "...Y entonces cogí de los huevos al peluquero y le dije: o me dejas como a Travolta en Pulp Fiction o te meto en el maletero de mi coche."
        stalin "Las amenazas son una herramienta de represión burguesa."
        c "Tenía que meterme en el papel, ya sabes."
        pov "Ahora me dirás que vosotros no amenazábais."
        stalin "Una Tokarev clavada en los riñones no era una amenaza, era la certeza de que si no obedecías, ibas a morir. Son conceptos muy distintos. El nuestro es más puro."
        c "Dejad las frivolidades y contemplad este templo al cuerpo humano."
        c "Me gusta este lugar, me recuerda al gimnasio de aquella telenovela costumbrista que narraba las desventuras de un grupo de jóvenes de la generación X en un instituto llamado Siete Robles."
        stalin "A mi Sócrates me caía como el culo."
        stalin " Además, tenía una cara así como si se la hubieran estampado contra la pared de pequeño."
        c "Me pregunto qué estará haciendo en estos momentos..."
        r "No lo sé, pero cuando acabe contigo podrás llamarle desde el hospital."
        pov "¡Es M. Rajao!"
        r "Sí, señor. Estoy aquí para hacerte llorar sangre y escupir derrota."
        pov "Caray, de adversario cambia usted mucho."
        r "No me gusta sacar las garras, pero cuando me pongo, me pongo."
        c "¿Y qué quieres, Rajao, que nos partamos aquí la cara como los miembros de dos bandas rivales portorriqueñas?"
        r "Ese es el plan, pero sin tanto etnicismo."
        stalin "Un comunista nunca rehuye una buena lucha."
        extend " Prepárate, jugador."
        call battle_presetup from _call_battle_presetup
        call battle from _call_battle
        stop music
        scene gymvigo with dissolve
        c "¡Lo hicimos! ¡Hemos derrotado al malvado M. Rajao!"
        scene draguim with fade
        dragui "No tan rápido."
        stalin "¿Quién eres tú?"
        dragui "Escoria. Deberías conocerme."
        pov "Yo sí. ¿Tenéis confeti a mano?"
        stalin "¿Confeti? Ahora me explico por qué tuvo que ser el Ejército Rojo el que acabara con Hitler. ¡Vosotros pretendíais asustarlo con matasuegras!"
        dragui "Eso funcionó una vez, pero ya no."
        dragui "Estoy harto de vuestra palabrería sin fundamento producto de un escritor recién despertado de la siesta."
        dragui "¡Vuelve en ti, M. Rajao!"
        play sound "resucitar.wav"
        $ renpy.pause(2, hard=True)
        r "¡Muchas gracias, amigo!"
        r "No sé qué haría yo sin ti."
        dragui "No vayas diciendo por ahí que te hemos ayudado."
        r "¿Ayudarme a qué?"
        dragui "Ese es nuestro chico."
        scene gymvigo
        $ renpy.pause(1, hard=True)
        call battle_presetup from _call_battle_presetup_1
        call battle from _call_battle_1
        stop music
        c "¡Por el cardado de Khan! Se ha escapado."
        stalin "Ya le llegará su hora cuando nos hagamos con el poder."
        pov "Al menos hemos conseguido los votos necesarios."
        $ puntosj +=3
    
    
    jump mapa