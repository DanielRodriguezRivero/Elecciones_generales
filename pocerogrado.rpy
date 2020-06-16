label pocerogrado:
    $ pocerogrado = True
    $ barna = False
    if barcelona == True:
        $ barna = True
    #personajes
    define rueda = Character("Flaming Wheel", color="#002927", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define kenshiro = Character("Kenshiro", color="#0024D6", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define prop = Character("Antonio, el propietario", color="#31B422", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define concejal = Character("Nacho, el concejal", color="#169EC7", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define promotor = Character("Chisco, el promotor", color="#0Bff0B", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    #escenarios
    image gympocero = "images/gympocero.jpg"
    image pocerotrav = "images/pocerotrav.jpg"
    image pocero1 = "images/pocero1.jpg"
    image pocero2 = "images/pocero2.jpg" 
    image pocero3 = "images/pocero3.jpg" 
    image pocero4 = "images/pocero4.jpg" 
    #imagenes de personajes
    image cuñadopocero = "images/neumatico.png"
    image propietario = "images/propietario.png"
    image kentravel = "images/ken41.gif"
    image kenlucha = "images/kenlucha.gif"
    image kenshi = "images/kenshiro.png"
    image concejal = "images/concejalurbanismo.png"
    image promotor = "images/promotor.png"
    #texto
    image gymtextpo1 = Text("{size=40}Gimnasio Butan",color="#fff", text_align=0.3)
    image gymtextpo2 = Text("{size=40}Quema grasa sin usar las manos",color="#fff", text_align=0.3)
    image btext1 = anim.Blink(Text("¡Un voto!", color="#ff0", size=76))
    #entradilla
    scene travelpocerogrado at Pan((0, 0), (300,0), 20.0)
    play music "entradillapocerogrado.mp3"
    $ renpy.pause(15, hard=True)
    
    if mrajao == True:
        stop music
        scene pocero1 with dissolve
        $ renpy.pause(0.5, hard=True)
        r "¿Y dices que aquí vive gente?"
        montoto "Eso pone en los papeles."
        r "Pues para venir a este agujero hay que ser un completo gilip..."
        show kenshiro:
            ypos 0.1
            xpos 0.3
        with dissolve
        kenshiro "¿Quiénes sois? ¿Matones de Los Constructores?"
        r "No, no, solo somos un humilde grupo de politicos errantes."
        kenshiro "Pues más os hubiera valido ser matones. ¡Hijos de puta!"
        r "¡Protesto! La doble moral presente en esta novelucha visual, un género que por otra parte solo disfrutan niños y maricones, es intolerable." 
        r "¿Cómo se permite que este personaje de musculos cincelados en carne por el mismísimo mercurio y bañado en aceite de motor nos insulte alegremente mientras que nosotros no podemos decir "
        r "que quienes se hipotecan de por vida por un zulo en un lugar que haría del Desierto de los Monegros el Jardín del Edén, son unos auténticos y soberanos gilip..."
        r "¿VEIS?"
        pov "Puede que sea porque el jugador es un Man from the people contrario a un sistema apoyado por ustedes que aliena a las personas para crear la necesidad de hacerse con un hogar al precio que sea y donde sea."
        r "Un gilipollas es lo que es. ¡Él y todos los que viven aqui!"
        r "Anda, si hablo como en el congreso no me afecta la censura."
        r "Gilipollas los primeros"
        r "Cabronazos los segundos"
        r "Pichaflojas los terceros"
        r "Hideputas el mundo entero"
        pov "Eso ha sido un ataque muy gratuito."
        r "¿Y quién va a venir a enjuiciarme por eso? ¿El fiscal general?"
        r "Jajaj si le tengo encadenado dentro de una jaula y solo le dejo salir para que enchirone a mis enemigos y para que cague por las noches al aire."
        r "De hecho, mira, al man of the people, lo que quiera que signifique eso, le va a caer una querella y no habrá nadie en Twitter que se indigne por él. No tendrá la misma suerte que Froilán."
        kenshiro "Me van diciendo a quién le tengo que atizar primero, por favor. Tengo prisa por llegar al Gimnasio Butan."
        pov "¿Usted también va hacia allí?"
        kenshiro "Sí, allí está la oficina de la promotora. Voy a poner una queja y a repartir hostias. Y voy sobrado de hostias."
        montoto "¿Podemos acompañarle? Este lugar no parece muy seguro."
        kenshiro "No lo es. Bandas de propietarios que de la noche a la mañana vieron cómo sus zulos perdían el 90 por ciento del valor recorren estas tierras en busca de viajeros ignorantes que les avalen una segunda hipoteca."
        r "¿Y si se niegan?"
        kenshiro "Les obligan a comprarles sellos."
        r "¿Y si se niegan?"
        kenshiro "Se los comen."
        montoto "Cielos..."
        kenshiro "Si queréis venir conmigo no puedo impedíroslo, pero no me estéis calentando la cabeza con vuestras desgracias económicas."
        r "Uy, por eso no tiene que preocuparse."
        kenshiro "En marcha. Y no miréis atrás."
        r "¿Por qué?"
        kenshiro "Porque lo digo yo."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero2 with dissolve
        $ renpy.pause(0.5, hard=True)
        show kentravel at left
        show propietario at right
        prop "Volvemos a encontrarnos, Kenshiro."
        kenshiro "Ha pasado mucho tiempo desde que fui a tirar la basura esta mañana, a Guadalajara, y me tiraste una de las bolsas."
        kenshiro "Apártate para que pueda dejar de ver tu mugrienta cara."
        prop "Ambos sabemos que eso no es posible."
        kenshiro "Así que ahora trabajas para Los Constructores..."
        prop "No me quedaba otra. Ya no solo porque me dejen el trastero a mitad de precio, sino porque no puedo permitir que te vayas del edificio. Tocaríamos a más en la cuota de la Comunidad y no abundamos los propietarios."
        kenshiro "Solo te lo diré una vez más. Déjanos pasar."
        prop "Encima que eres un tapayogurista, que te salió por dos perras el loft."
        prop "¡En guardia!"
        kenshiro "No quiero pelear contigo."
        pov "Creo que vamos a tener que enfurecerle para que le de una paliza a esta masa informe."
        r "¿Y cómo lo hacemos?"
        pov "Mmm... podemos decirle cosas."
        r "¿Por ejemplo?"
        menu:
            "¡Acaba con él!":
                pov "Creo que no ha servido de mucho."
            "El poder de Putin te obliga":
                pov "He visto por un instante su mirada asesina pero no ha sido suficiente."
            "Los pisos nunca bajan":
                hide kentravel
                show kenlucha at left
                play sound "tata.mp3"
                with Shake((0, 0, 0, 0), 7.0, dist=30)

        
        hide kenlucha
        show kentravel at left
        r "Esa mole no se mueve."
        pov "Habrá que intentarlo de nuevo."
        menu:
            "No conozco al tesorero de mi partido":
                pass
            "Los jóvenes que se marchan del país lo hacen por afán aventurero.":
                pass
            "Alquilar es tirar el dinero":
                pass
        
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide propietario with hpunch
        hide kenlucha
        show kentravel at center
        kenshiro "Parece que este mes aumentará la cuota de la comunidad."
        pov "Oiga, Kenshiro. Usted parece una persona sensata, al menos con toda la sensatez que da el poder reventar la cabeza de alguien con solo pegarle con el dedo meñique."
        extend " ¿Por qué se compró un piso aquí?"
        kenshiro "¿De verdad quieres saberlo?"
        pov "¿Por qué lo preguntaría si no?"
        kenshiro "Para matar el rato, para reirte del pobre Kenshiro, para espesar una historia que se queda algo floja..."
        kenshiro "Si tu interés es sincero, escucha bien la historia de un pobre desdichado hasta que se cruzó en su camino..."
        r "Una mujer, seguro."
        kenshiro "Eso es un poco machista, pero sí, así ocurrió."
        kenshiro "Corría el año 1999, la MIR no cayó sobre París como predijo Paco Rabané, el siglo XX daba sus últimas bocanadas y yo terminaba mi doble grado de Artes Marciales y Manipulador de alimentos."
        kenshiro "La vida parecía sonreirme, en apenas un par de meses sería libre para incorporarme al vibrante mercado de trabajo que ofrecía oportunidades para todo aquel que supiera aprovecharlas."
        kenshiro "Y entonces conocía a Sonia."
        montoto "¿Cumplía con sus obligaciones fiscales?"
        kenshiro "Con las tetas que tenía como si le robaba al Papa. El caso es que caí rendido a sus encantos. Durante 8 años estuvimos en su piso de estudiante mientras ella terminaba sus estudios de Repostería y Diseño Industrial."
        kenshiro "Hasta que se graduó y se acabó el chollo que le pagaban sus padres. Nos vimos en la calle de la noche a la mañana y justo cuando íbamos cargando con las cajas repletas de nuestras pertenencias y nuestros sueños"
        kenshiro "pasamos frente a la puerta de una sucursal. Uno de los empleados nos vio y salió corriendo a nuestro encuentro. Nos ofreció dinero para una hipoteca y un Porsche Cayenne y todo a cambio de..."
        kenshiro "¿Cómo dijo...? Ah, sí, a cambio de nuestra felicidad. No lo entendí muy bien, pero estaba desesperado y aquel dinero caído del cielo nos venía de perlas. Justo al salir nos topamos en la puerta con el promotor de Pocerogrado que nos ofreció"
        kenshiro "un bonito dúplex a un precio de risa. Una risa tan estruendosa como la del promotor cuando firmamos los papeles y dimos una entrada."
        pov "Pero si os hacía tanta falta un hogar, ¿por qué firmásteis sobre plano y no comprásteis una casa ya construida?"
        kenshiro "Porque nos regalaban los visillos. Sonia me insistió..."
        kenshiro "Al día siguiente, cayó Caja Madrid, el banco que nos había dado el préstamo. Los hombres se comieron a los hombres, Pocerogrado estalló en un caos de violencia y fuego. Los políticos hablaron y hablaron mientras los ciudadanos de la urbanización luchaban por los últimos vestigios de lo que una vez fue una próspera civilización."
        kenshiro "De la noche a la mañana nos vimos sin casa, debiendo mucho dinero y encima los visillos no le gustaban."
        kenshiro "Aquella noche, mientras dormíamos debajo del puente de la M30, noté a mi novia intranquila. Cuando desperté, se había marchado. Me había abandonado."
        kenshiro "Desde entonces vago por las Llanuras Centrales en busca del cabecilla detrás de mi desgracia, el que envió al promotor al banco, el sardónico Flaming Wheels."
        kenshiro "Y ayer por fin di con su paradero."
        pov "El Gimnasio Butan."
        kenshiro "Exacto."
        kenshiro "Podemos continuar."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero3 with dissolve
        show kentravel at left
        show concejal at right
        kenshiro "¿Y tú quién eres?"
        concejal "¿No me conoces? Soy tu concejal de urbanismo."
        kenshiro "..."
        concejal "Sí, hombre. Suelo estar en la barra americana del club de carretera de la N-23. Menos los domingos, que son sagrados y me voy al de la M-30."
        kenshiro "¿También te han pagado para impedir que recupere lo que es mío?"
        concejal "Me han pagado por tantas cosas... Pero esta vez me dijeron que viniera a partirte la cara y aquí estoy."
        concejal "No es personal, solo son negocios."
        pov "Creo que vamos a tener que hacer lo mismo de antes."
        menu:
            "Hazte Bankiero":
                pass
            "Estamos saliendo de la crisis":
                pass
            "España no ha sufrido ningún rescate":
                pass
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide concejal with zoomout
        hide kenlucha
        show kentravel at center
        r "Esta vez fue más fácil."
        pov "Ya me dirás. Contra un político..."
        r "Oiga, señor Kenshiro."
        kenshiro "¿Qué quieres?"
        r "Usted no me daría una paliza como a esos otros, ¿verdad?"
        kenshiro "¿Por qué lo preguntas?"
        extend " Ahora que caigo, no me has dicho tu nombre..."
        r "Jose Luís Rodríguez Zapatero. Para servirle."
        kenshiro "Ah, no, hombre. Bastante tienes tú ya."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero4 with dissolve
        show kentravel at left
        show promotor at right
        kenshiro "¿No os cansáis de dar la paliza?"
        promotor "Paliza la que te voy a dar."
        pov "Siempre igual, puñetazo por aquí, Hokuto no Ken por allá..."
        pov "¿Por qué no le dan su dinero y ya está?"
        promotor "¡Si lo hago por su bien! Se lo he dicho muchas veces, que no lo venda, que esto va a remontar y que se lo van a quitar de las manos."
        pov "Y el año que viene va a ser el de Linux en el escritorio."
        promotor "¿Qué?"
        kenshiro "Basta de cháchara insulsa que aquí hay gente que querrá irse a la cama ya."
        pov "Aquí vamos de nuevo..."
        menu:
            "Métete en una hipoteca en yenes":
                pass
            "¿Para qué estudiar si te puedes sacar 3000 euros de paleta?":
                pass
            "La NEP ya está aquí":
                pass
        
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide promotor with dissolve
        hide kenlucha
        show kentravel at center
        kenshiro "Creo que ya no nos molestará nadie más."
        r "¿Cómo puede estar seguro?"
        kenshiro "Porque llevamos mucho tiempo con lo mismo y no queremos que el jugador se aburra, así que, "
        extend "¡dentro gimnasio!"
        scene black with dissolve
        show gymtextpo1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextpo2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gympocero with fade
        show cuñadopocero at center
        rueda "Buenas tardes, caballeros. No suelo tener muchas visitas por aquí."
        rueda "¿Han pensado en adquirir una solución habitacional a un precio inmejorable en una de las zonas con más potencial de toda la península?"
        k "Tanto como potencial... Quizá si sube el nivel del mar dos kilómetros en unas décadas los nietos de alguien podrán disfrutar de un piso a pie de playa pero mientras tanto..."
        show gympocero at right with move
        show kentravel at left with dissolve
        kenshiro "¡Basta de engaños!"
        kenshiro "Prepárate, maldito. ¡Soy el fin de tu loca ambición!"
        rueda "Y dale. Las culpas al capitalismo. Yo solo aplico la ley. ¿O es que es ilegal vender estos pisos?"
        rueda "Cada uno con su responsabilidad."
        kenshiro "Te voy a dar hasta en el cielo del paladar."
        rueda "Y se puede saber exáctamente por qué razón."
        kenshiro "Quiero que me devuelvas la fianza que di por el piso en el complejo 3."
        rueda "¿Lo compraste bajo plano?"
        kenshiro "Sí."
        rueda "Pues lo siento pero no puedo hacer nada."
        kenshiro "Ven que te voy a meter un meco que vas a echar hasta la papilla que no te daba tu madre."
        rueda "No estoy interesado en involucrarme en una danza de puñetazos y golpes mortales. Si quieres que te devuelva la entrada del piso tendrás que pasar un test sobre seguridad antiincendios."
        kenshiro "¿Y si te pego igual?"
        rueda "Soy de caucho. Buena suerte."
        kenshiro "¡Estoy perdido!"
        extend " ¡Ni siquiera sé leer!"
        pov "Pues ya tienes una edad."
        kenshiro "Si te parece le digo al maestro: Oye, que tengo que ir a empaparme de las obras de Jose María Pemán, que lo de aprender el Puño de la Estrella del Norte lo dejamos para luego."
        pov "Ya nos encargamos nosotros entonces."
        pov "Pero oiga, Señor Wheels..."
        rueda "Llámame Ruedines."
        pov "Si pasamos el test, aparte del dinero, nos dará sus tres votos para la elección del Presidente."
        rueda "De acuerdo. Total, vais a perder."
        hide cuñadopocero
        hide kentravel
        $ rueda("¿Con qué se apaga el fuego?", interact=False)
        menu:
            "Agua":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                rueda "Habéis tenido suerte. Poca gente la acierta."
            "La voluntad de los bomberos":
                rueda "Si de voluntad dependiera tendría un rabo que me daría vueltas a la llanta, pero no, aquí estoy, impotente ante las decenas de calendarios de Playboy con los que están empapeladas las paredes del Gimnasio."
                pass
            "El amor de una madre":
                rueda "Eso pensaba San Epidoro de Ipéstrote cuando los romanos le condenaron a morir en la hoguera por robar el contenido del platillo del Templo de Juno durante la Caleindades."
                rueda "Pero por mucho que su progenitora le quisiera, se quemó igual."
                rueda "Que la madre le había desheredado un par de años antes, pero la esperanza la tenía."
                pass
            "Más fuego":
                pass
        rueda "Siguiente pregunta..."
        $ rueda("Si te prenden fuego tienes que...", interact=False)
        menu:
            "Aprovechar para encenderte un cigarro":
                rueda "También podrías hacerlo pero fumar es malo para la salud. Bastante tienes con las llamas."
                pass
            "Rodar por el suelo":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                rueda "¡Maldición! Esta era la última difícil que me quedaba."
            "Correr hacia tus enemigos para, al menos, no morir solo":
                pass
            "Pagar a Hacienda. Nunca dejes de pagar":
                montoto "Me da igual lo que digas. Esta es siempre la opción correcta."
                rueda "Estás en mi gimnasio y además te envié un sobre muy bonito el otro día. No sé si te acuerdas."
                montoto "Hemos fallado entonces, ¿no?"
                rueda "Totalmente."
                pass
        rueda "He de aceptar lo inaceptable. Seguramente consigáis todos mis votos. La pregunta que os haré es la más fácil de todas:"
        $ rueda("¿Qué Real Decreto aprueba el Reglamento de Seguridad contra incendios en establecimientos industriales, y que afecta a los edificios o recintos, cuya actividad principal sea de tipo industrial?", interact=False)
        menu:
            "2245/2004":
                rueda "Inaudito. ¡Habéis fallado!"
            "2154/2003":
                rueda "Inaudito. ¡Habéis fallado!"
            "2347/2005":
                rueda "Inaudito. ¡Habéis fallado!"
            "2267/2004":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                show gympocero at right with dissolve
                show kentravel at left with dissolve
                rueda "Estaba cantado que íbais a saberlo."
                pov "¿Quién no conoce ese dato?"
                rueda "No te creas, algún inconsciente hay por ahí suelto."
                kenshiro "Mi dinero, escoria."
                rueda "De acuerdo, pero no vayas contándolo por ahí. Tengo una reputación que mantener y no quiero tener que estar pensando más preguntas."
                rueda "Y vosotro tenéis los votos también. Idos."
                r "Muchas gracias, señor caucho."
                rueda "Tú llámame Flaming Wheels."
                jump mapa
        show gympocero at right with dissolve
        show kentravel at left with dissolve
        rueda "Aunque hayáis ganado algún voto, vuestro amigo no podrá recuperar la entrada que dio para el piso."
        kenshiro "¿Cómo? Será inútil pero te voy a dar de hostias hasta que se me acabe el cintrón."
        play sound "tata.mp3" #sonido del puño de la estrella del norte
        $ renpy.pause(2, hard=True) #pausa que dure el sonido
        scene pocero1
        r "Al final no hemos escapado tan mal."
        pov "Desde luego, podríamos haber sido la cena de alguno de estos indeseables."
        montoto "O nos podrían haber colado un aval."
        jump mapa

        
    if ken == True:
        stop music
        scene pocero1 with dissolve
        k "¿Y dices que aquí vive gente?"
        espejo "Eso pone en la Guía Míchel."
        pov "Será Michelín."
        espejo "No, esa recomienda lugares que todo el mundo debería visitar. la Guía Míchel muestra los peores lugares de la península, como Muñecar de Totana y Lamprea de Abajo."
        k "Está muy bien incluido este lugar."
        show kenshiro:
            ypos 0.1
            xpos 0.3
        with dissolve
        kenshiro "¿Quiénes sois? ¿Matones de Los Constructores?"
        k "No, no, solo somos un humilde grupo de politicos errantes."
        kenshiro "Pues más os hubiera valido ser matones. ¡Hijos de puta!"
        k "Afronto mi destino como solo un líder socialista haría: mirando desafiante a mi agresor, la frente bien alta y el ruego de que no me pegue muy fuerte."
        espejo "Por eso te quiero tanto, mi Espartaco."
        k "¡Y yo te quiero a ti! ¡Bésame!"
        espejo "Hazlo tú que yo no me puedo mover. La creación fue tan injusta que me negó los medios para desplazarme."
        k "Por eso Dios debe de ser de derechas y los socialistas nos llevamos regular con él."
        pov "¿En serio? ¿Llevo más de media hora escuchando gilipolleces para llegar a esto?"
        pov "Yo podría estar ahora viendo vídeos de Deauxma y haciéndom..."
        kenshiro "Me van diciendo a quién le tengo que atizar primero, por favor. Tengo prisa por llegar al Gimnasio Butan."
        pov "¿Usted también va hacia allí? Y que conste que podría estar pajeándome con una MILF."
        kenshiro "No sé qué es eso. Pero sí, en el gimnasio está la oficina de la promotora. Voy a poner una queja y a repartir hostias. Y voy sobrado de hostias."
        espejo "¿Podemos acompañarle? Este lugar no parece muy seguro."
        kenshiro "Tu apreciación es acertada. Bandas de propietarios que de la noche a la mañana vieron cómo sus zulos perdían el 90 por ciento del valor recorren estas tierras en busca de viajeros ignorantes que les avalen una segunda hipoteca."
        k "¿Y si se niegan?"
        kenshiro "Les obligan a comprarles sellos."
        k "¿Y si se niegan?"
        kenshiro "Se los comen."
        espejo "Pues buena suerte conmigo."
        k "No puedo creer que solo pienses en ti. Conmigo harían cosas inimaginables. Soy un caramelito para sus ansias desbocadas..."
        kenshiro "Si queréis venir conmigo no puedo impedíroslo, pero no me estéis calentando la cabeza con vuestras desgracias económicas."
        k "Tranquilo, no sé qué es eso de \"económicas\"."
        kenshiro "En marcha. Y no miréis atrás."
        k "¿Por qué?"
        kenshiro "Porque lo digo yo."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero2 with dissolve
        show kentravel at left
        show propietario at right
        prop "Volvemos a encontrarnos, Kenshiro."
        kenshiro "Ha pasado mucho tiempo desde que fui a tirar la basura esta mañana, a Guadalajara, y me tiraste una de las bolsas."
        kenshiro "Apártate para que pueda dejar de ver tu mugrienta cara."
        prop "Ambos sabemos que eso no es posible."
        kenshiro "Así que ahora trabajas para Los Constructores..."
        prop "No me quedaba otra. Ya no solo porque me dejen el trastero a mitad de precio, sino porque no puedo permitir que te vayas del edificio. Tocaríamos a más en la cuota de la Comunidad y no abundamos los propietarios."
        kenshiro "Solo te lo diré una vez más. Déjanos pasar."
        prop "Encima que eres un tapayogurista, que te salió por dos perras el loft."
        prop "¡En guardia!"
        kenshiro "No quiero pelear contigo."
        pov "Creo que vamos a tener que enfurecerle para que le de una paliza a esta masa informe."
        k "¿Y cómo lo hacemos?"
        pov "Mmm... podemos decirle cosas."
        k "¿Por ejemplo?"
        menu:
            "¡Acaba con él!":
                pov "Creo que no ha servido de mucho."
            "El poder de Putin te obliga":
                pov "He visto por un instante su mirada asesina pero no ha sido suficiente."
            "Los pisos nunca bajan":
                hide kentravel
                show kenlucha at left
                play sound "tata.mp3"
                with Shake((0, 0, 0, 0), 7.0, dist=30)

        
        hide kenlucha
        show kentravel at left
        k "Esa mole no se mueve."
        pov "Habrá que intentarlo de nuevo."
        menu:
            "No conozco al tesorero de mi partido":
                pass
            "Los jóvenes que se marchan del país lo hacen por afán aventurero.":
                pass
            "Alquilar es tirar el dinero":
                pass
        
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide propietario with dissolve
        hide kenlucha
        show kentravel at center
        kenshiro "Parece que este mes aumentará la cuota de la comunidad."
        pov "Oiga, Kenshiro. Usted parece una persona sensata, al menos con toda la sensatez que da el poder reventar la cabeza de alguien con solo pegarle con el dedo meñique."
        extend " ¿Por qué se compró un piso aquí?"
        kenshiro "¿De verdad quieres saberlo?"
        pov "¿Por qué lo preguntaría si no?"
        kenshiro "Para matar el rato, para reirte del pobre Kenshiro, para espesar una historia que se queda algo floja..."
        kenshiro "Si tu interés es sincero, escucha bien la historia de un pobre desdichado hasta que se cruzó en su camino..."
        k "Una mujer, seguro."
        kenshiro "Eso es un poco machista, pero sí, así ocurrió."
        kenshiro "Corría el año 1999, la MIR no cayó sobre París como predijo Paco Rabané, el siglo XX daba sus últimas bocanadas y yo terminaba mi doble grado de Artes Marciales y Manipulador de alimentos."
        kenshiro "La vida parecía sonreirme, en apenas un par de meses sería libre para incorporarme al vibrante mercado de trabajo que ofrecía oportunidades para todo aquel que supiera aprovecharlas."
        kenshiro "Y entonces conocía a Sonia."
        montoto "¿Cumplía con sus obligaciones fiscales?"
        kenshiro "Con las tetas que tenía como si le robaba al Papa. El caso es que caí rendido a sus encantos. Durante 8 años estuvimos en su piso de estudiante mientras ella terminaba sus estudios de Repostería y Diseño Industrial."
        kenshiro "Hasta que se graduó y se acabó el chollo que le pagaban sus padres. Nos vimos en la calle de la noche a la mañana y justo cuando íbamos cargando con las cajas repletas de nuestras pertenencias y nuestros sueños"
        kenshiro "pasamos frente a la puerta de una sucursal. Uno de los empleados nos vio y salió corriendo a nuestro encuentro. Nos ofreció dinero para una hipoteca y un Porsche Cayenne y todo a cambio de..."
        kenshiro "¿Cómo dijo...? Ah, sí, a cambio de nuestra felicidad. No lo entendí muy bien, pero estaba desesperado y aquel dinero caído del cielo nos venía de perlas. Justo al salir nos topamos en la puerta con el promotor de Pocerogrado que nos ofreció"
        kenshiro "un bonito dúplex a un precio de risa. Una risa tan estruendosa como la del promotor cuando firmamos los papeles y dimos una entrada."
        pov "Pero si os hacía tanta falta un hogar, ¿por qué firmásteis sobre plano y no comprásteis una casa ya construida?"
        kenshiro "Porque nos regalaban los visillos. Sonia me insistió..."
        kenshiro "Al día siguiente, cayó Caja Madrid, el banco que nos había dado el préstamo. Los hombres se comieron a los hombres, Pocerogrado estalló en un caos de violencia y fuego. Los políticos hablaron y hablaron mientras los ciudadanos de la urbanización luchaban por los últimos vestigios de lo que una vez fue una próspera civilización."
        kenshiro "De la noche a la mañana nos vimos sin casa, debiendo mucho dinero y encima los visillos no le gustaban."
        kenshiro "Aquella noche, mientras dormíamos debajo del puente de la M30, noté a mi novia intranquila. Cuando desperté, se había marchado. Me había abandonado."
        kenshiro "Desde entonces vago por las Llanuras Centrales en busca del cabecilla detrás de mi desgracia, el que envió al promotor al banco, el sardónico Flaming Wheels."
        kenshiro "Y ayer por fin di con su paradero."
        pov "El Gimnasio Butan."
        kenshiro "Exacto. Se ve que hay una chispa de inteligencia dentro de esa cabeza tan grande que tienes. Cualquiera lo diría si te viera perdiendo el tiempo con esto."
        pov "Oiga, eso no sé muy bien a qué ha venido."
        kenshiro "Es hora de partir."
        pov "¡Pero no me ignore!"
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero3 with dissolve
        show kentravel at left
        show concejal at right
        kenshiro "¿Y tú quién eres?"
        concejal "¿No me conoces? Soy tu concejal de urbanismo."
        kenshiro "..."
        concejal "Sí, hombre. Suelo estar en la barra americana del club de carretera de la N-23. Menos los domingos, que son sagrados."
        kenshiro "¿También te han pagado para impedir que recupere lo que es mío."
        concejal "Me han pagado por tantas cosas... Pero esta vez me dijeron que viniera a partirte la cara y aquí estoy."
        concejal "No es personal, solo son negocios."
        pov "Creo que vamos a tener que hacer lo mismo."
        menu:
            "Hazte Bankiero":
                pass
            "Estamos saliendo de la crisis":
                pass
            "España no ha sufrido ningún rescate":
                pass
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide concejal with dissolve
        hide kenlucha
        show kentravel at center
        k "Esta vez fue más fácil."
        pov "Ya me dirás. Contra un político..."
        k "Oiga, señor Kenshiro."
        kenshiro "¿Qué quieres?"
        k "Usted no me daría una paliza como a esos otros, ¿verdad?"
        kenshiro "¿Por qué lo preguntas?"
        extend " ¿Quién eres tú exactamente?"
        k "Joaquín Almunia. Para servirle."
        kenshiro "¿Y no te da verguenza?. Puaggg."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero4 with dissolve
        show kentravel at left
        show promotor at right
        kenshiro "¿No os cansáis de dar la paliza?"
        promotor "Paliza la que te voy a dar."
        pov "Siempre igual, puñetazo por aquí, Hokuto no Ken por allá..."
        pov "¿Por qué no le dan su dinero y ya está?"
        promotor "¡Si lo hago por su bien! Se lo he dicho muchas veces, que no lo venda, que esto va a remontar pronto y que se lo van a quitar de las manos."
        k "¿Pero cómo va a vender algo que solo está en un plano?"
        promotor "Díselo a millones de gilip... españoles."
        kenshiro "Basta de cháchara insulsa que aquí hay gente que querrá irse a la cama ya."
        pov "Vamos de nuevo..."
        menu:
            "Métete en una hipoteca en yenes":
                pass
            "¿Para qué estudiar si te puedes sacar 3000 euros de paleta?":
                pass
            "La NEP ya está aquí":
                pass
        
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide promotor with dissolve
        hide kenlucha
        show kentravel at center
        kenshiro "Creo que ya no nos molestará nadie más."
        k "¿Cómo puede estar seguro?"
        kenshiro "Porque llevamos mucho tiempo con lo mismo y no queremos que el jugador se aburra, así que, "
        extend "¡dentro gimnasio!"
        scene black with dissolve
        show gymtextpo1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextpo2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gympocero with fade
        show cuñadopocero at center
        rueda "Buenas tardes, caballeros. No suelo tener muchas visitas por aquí."
        rueda "¿Han pensado en adquirir una solución habitacional a un precio inmejorable en una de las zonas con más potencial de toda la península?"
        k "Tanto como potencial... Quizá si sube el nivel del mar dos kilómetros en unas décadas los nietos de alguien podrán disfrutar de un piso a pie de playa pero mientras tanto..."
        show gympocero at right with move
        show kentravel at left with dissolve
        kenshiro "¡Basta de engaños!"
        kenshiro "Prepárate, maldito. ¡Soy el fin de tu loca ambición!"
        rueda "Y dale. Las culpas al capitalismo. Yo solo aplico la ley. ¿O es que es ilegal vender estos pisos?"
        rueda "Cada uno con su responsabilidad."
        kenshiro "Te voy a dar hasta en el cielo del paladar."
        rueda "Y se puede saber exáctamente por qué razón."
        kenshiro "Quiero que me devuelvas la fianza que di por el piso en el complejo 3."
        rueda "¿Lo compraste bajo plano?"
        kenshiro "Sí."
        rueda "Pues lo siento pero no puedo hacer nada."
        kenshiro "Ven que te voy a meter un meco que vas a echar hasta la papilla que no te daba tu madre."
        rueda "No estoy interesado en involucrarme en una danza de puñetazos y golpes mortales. Si quieres que te devuelva la entrada del piso tendrás que pasar un test sobre seguridad antiincendios."
        kenshiro "¿Y si te pego igual?"
        rueda "Soy de caucho. Buena suerte."
        kenshiro "¡Estoy perdido!"
        extend " ¡Ni siquiera sé leer!"
        pov "Pues ya tienes una edad."
        kenshiro "Si te parece le digo al maestro: Oye, que tengo que ir a empaparme de las obras de Jose María Pemán, que lo de aprender el Puño de la Estrella del Norte lo dejamos para luego."
        pov "Ya nos encargamos nosotros entonces."
        pov "Pero oiga, Señor Wheels..."
        rueda "Llámame Ruedines."
        pov "Si pasamos el test, aparte del dinero, nos dará sus tres votos para la elección del Presidente."
        rueda "De acuerdo. Total, vais a perder."
        rueda "Atención, pregunta..."
        hide cuñadopocero
        hide kentravel
        $ rueda("¿Con qué se apaga el fuego?", interact=False)
        menu:
            "Agua":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                rueda "Habéis tenido suerte. Poca gente la acierta."
            "La voluntad de los bomberos":
                rueda "Si de voluntad dependiera tendría un rabo que me daría vueltas a la llanta, pero no, aquí estoy, impotente ante las decenas de calendarios de Playboy con los que están empapeladas las paredes del Gimnasio."
                pass
            "El amor de una madre":
                rueda "Eso pensaba San Epidoro de Ipéstrote cuando los romanos le condenaron a morir en la hoguera por robar el contenido del platillo del Templo de Juno durante la Caleindades."
                rueda "Pero por mucho que su progenitora le quisiera, se quemó igual."
                rueda "Que la madre le había desheredado un par de años antes, pero la esperanza la tenía."
                pass
            "Más fuego":
                pass
        rueda "Siguiente pregunta..."
        $ rueda("Si te prenden fuego tienes que...", interact=False)
        menu:
            "Aprovechar para encenderte un cigarro":
                rueda "También podrías hacerlo pero fumar es malo para la salud. Bastante tienes con las llamas."
                pass
            "Rodar por el suelo":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                rueda "¡Maldición! Esta era la última difícil que me quedaba."
            "Correr hacia tus enemigos para, al menos, no morir solo":
                pass
            "Pagar a Hacienda. Nunca dejes de pagar":
                montoto "Me da igual lo que digas. Esta es siempre la opción correcta."
                rueda "Estás en mi gimnasio y además te envié un sobre muy bonito el otro día. No sé si te acuerdas."
                espejo "Hemos fallado entonces, ¿no?"
                rueda "Totalmente."
                pass
        rueda "He de aceptar lo inaceptable. Seguramente consigáis todos mis votos. La pregunta que os haré es la más fácil de todas:"
        $ rueda("¿Qué Real Decreto aprueba el Reglamento de Seguridad contra incendios en establecimientos industriales, y que afecta a los edificios o recintos, cuya actividad principal sea de tipo industrial?", interact=False)
        menu:
            "2245/2004":
                rueda "Inaudito. ¡Habéis fallado!"
            "2154/2003":
                rueda "Inaudito. ¡Habéis fallado!"
            "2347/2005":
                rueda "Inaudito. ¡Habéis fallado!"
            "2267/2004":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                show gympocero at right with dissolve
                show kentravel at left with dissolve
                rueda "Estaba cantado que íbais a saberlo."
                pov "¿Quién no conoce ese dato?"
                rueda "No te creas, algún inconsciente hay por ahí suelto."
                kenshiro "Mi dinero, escoria."
                rueda "De acuerdo, pero no vayas contándolo por ahí. Tengo una reputación que mantener y no quiero tener que estar pensando más preguntas."
                rueda "Y vosotro tenéis los votos también. Idos."
                k "Muchas gracias, señor caucho."
                rueda "Tú llámame Flaming Wheels."
                jump mapa
        show gympocero at right with dissolve
        show kentravel at left with dissolve
        rueda "Aunque hayáis ganado algún voto, vuestro amigo no podrá recuperar la entrada que dio para el piso."
        kenshiro "¿Cómo? Será inútil pero te voy a dar de hostias hasta que se me acabe el cintrón."
        play sound "tata.mp3" #sonido del puño de la estrella del norte
        $ renpy.pause(2, hard=True) #pausa que dure el sonido
        scene pocero1
        k "Al final no hemos escapado tan mal."
        pov "Desde luego, podríamos haber sido la cena de alguno de estos indeseables."
        espejo "O nos podrían haber colado un aval."
        jump mapa
        
    if coletas == True:
        stop music
        scene pocero1 with dissolve
        if barna == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        c "¿Y dices que aquí vive gente?"
        stalin "Y si no, deberían. He visto gulags que a su lado parecen el Hotel Ritz."
        c "Pues se deben de montar unas partidas de rol en vivo al Fallout del cagarse."
        pov "O al Vampiro."
        c "Es un poco antiguo ya pero también valdría. Aunque no le veo la gracia."
        pov "Eso es porque seguro que siempre te eliges un personaje del clan Toreador."
        c "Sí, pero no se lo digas a los animalistas, ¿eh? Jejeje"
        stalin "Niños, comportáos. Viene alguien."
        show kenshiro:
            ypos 0.1
            xpos 0.3
        with dissolve
        kenshiro "¿Quiénes sois? ¿Matones de Los Constructores?"
        c "No, no, solo somos un humilde grupo de representantes errantes del pueblo oprimido por el gran capital."
        kenshiro "Políticos, querrás decir."
        stalin "Sería la primera persona que nos calificara así."
        kenshiro "Pues más os hubiera valido ser matones. ¡Hijos de puta!"
        pov "Oiga que yo no tengo nada que ver. A mí me encalomaron el marrón justo cuando iba a tragarme Stranger Things."
        c "¿Ese acertado intento de captar la atención de una generación que amó a Los Goonies por encima de todas las cosas?"
        stalin "Pues a mi me parece basura consumista."
        c "Eso es porque en la Unión Soviética lo único que podíais hacer los adolescentes de los 80 era calcular las trayectorias de los misiles nucleares que acabarían con Occidente."
        c "Buen trabajo, por cierto."
        stalin "Mejor que dejar que productos audiovisuales decadentes agujereen vuestros cerebros con historias predecibles de camaradería y bonhomía."
        stalin "¿Sabes dónde se encuentran los amigos de verdad? En el frente occidental camino de Berlín, con las balas nazis rozando tu gaznate y el cañón del comisario político clavándose en tus riñones."
        pov "Eso del cañón ha sonado un poco..."
        kenshiro "Ejem."
        kenshiro "Me van diciendo a quién le tengo que atizar primero, por favor. Tengo prisa por llegar al Gimnasio Butan."
        pov "¿Usted también va hacia allí?"
        kenshiro "Sí, allí está la oficina de la promotora. Voy a poner una queja y a repartir hostias. Y voy sobrado de hostias."
        pov "¿Podemos acompañarle? Este lugar no parece muy seguro."
        kenshiro "No lo es. Bandas de propietarios que de la noche a la mañana vieron cómo sus zulos perdían el 90 por ciento del valor recorren estas tierras en busca de viajeros ignorantes que les avalen una segunda hipoteca."
        c "¿Y si se niegan?"
        kenshiro "Les obligan a comprarles sellos."
        c "¿Y si se niegan?"
        kenshiro "Se los comen."
        stalin "Bah, cosas peores he visto en Vorkuta."
        stalin "En el duro invierno del 52 un prisionero se comió un pico. Estuvo defecando clavos durante cuatro meses."
        stalin "Gracias a él aumentó la producción de clavos en la Unión Soviética un 34 por ciento."
        extend " El Cagador de Hierro, le llamábamos. No era muy original pero la imaginación es para los decadentes y afeminados."
        kenshiro "¿Siempre habla tanto?"
        c "La verdad es que no. Debe de ser el ambiente, que le trae recuerdos."
        kenshiro "Si queréis venir conmigo no puedo impedíroslo, pero no me estéis calentando la cabeza con vuestras desgracias económicas."
        stalin "La única desgracia es la existencia del Capitalismo en pleno siglo XXI."
        kenshiro "En marcha. Y no miréis atrás."
        c "¿Por qué?"
        kenshiro "Porque lo digo yo."
        stalin "Pues yo pienso ir caminando de espaldas todo el trayecto."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero2 with dissolve
        show kentravel at left
        show propietario at right
        prop "Volvemos a encontrarnos, Kenshiro."
        stalin "¿Quién está hablando?"
        pov "Sshh, que no me entero."
        kenshiro "Ha pasado mucho tiempo desde que fui a tirar la basura esta mañana a Guadalajara y me rompiste una de las bolsas."
        extend " La que tenía los restos de los camarones en salsa que me hizo la Puri para cenar, precisamente."
        kenshiro "Apártate para que pueda dejar de ver tu mugrienta cara."
        prop "Ambos sabemos que eso no es posible."
        kenshiro "Así que ahora trabajas para Los Constructores..."
        prop "No me quedaba otra. Ya no solo porque me dejen el trastero a mitad de precio, sino porque no puedo permitir que te vayas del edificio. Tocaríamos a más en la cuota de la Comunidad y no abundamos los propietarios."
        kenshiro "Solo te lo diré una vez más. Déjanos pasar."
        prop "Encima que eres un tapayogurista, que te salió por dos perras el loft."
        prop "¡En guardia!"
        kenshiro "No quiero pelear contigo."
        pov "Creo que vamos a tener que enfurecer a Kenshiro para que le de una paliza a esta masa informe."
        c "¿A lo Increible Hulk?"
        stalin "Pero no el Hulk chino. Malditos dibujantes vendidos. Prostituirían a su madre por un vaso de agua."
        c "¿Y cómo lo hacemos?"
        pov "Mmm... podemos decirle cosas."
        c "¿Por ejemplo?"
        menu:
            "¡Acaba con él!":
                pov "Creo que no ha servido de mucho."
            "El poder de Putin te obliga":
                pov "He visto por un instante su mirada asesina pero no ha sido suficiente."
            "Los pisos nunca bajan":
                hide kentravel
                show kenlucha at left
                play sound "tata.mp3"
                with Shake((0, 0, 0, 0), 7.0, dist=30)

        hide kenlucha
        show kentravel at left
        c "Esa mole no se mueve."
        pov "Habrá que intentarlo de nuevo."
        menu:
            "No conozco al tesorero de mi partido":
                pass
            "Los jóvenes que se marchan del país lo hacen por afán aventurero.":
                pass
            "Alquilar es tirar el dinero":
                pass
        
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide propietario with dissolve
        hide kenlucha
        show kentravel at center
        kenshiro "Parece que este mes aumentará la cuota de la comunidad."
        pov "Oiga, Kenshiro. Usted parece una persona sensata, al menos con toda la sensatez que da el poder reventar la cabeza de alguien con solo pegarle con el dedo meñique."
        extend " ¿Por qué se compró un piso aquí?"
        kenshiro "¿De verdad quieres saberlo?"
        pov "¿Por qué lo preguntaría si no?"
        kenshiro "Para matar el rato, para reirte del pobre Kenshiro, para espesar una historia que se queda algo floja..."
        kenshiro "Si tu interés es sincero, escucha bien la historia de un pobre desdichado hasta que se cruzó en su camino..."
        stalin "Una mujer, seguro."
        kenshiro "Eso es un poco machista, pero sí, así ocurrió."
        kenshiro "Corría el año 1999, la MIR no cayó sobre París como predijo Paco Rabané, el siglo XX daba sus últimas bocanadas y yo terminaba mi doble grado de Artes Marciales y Manipulador de alimentos."
        kenshiro "La vida parecía sonreirme, en apenas un par de meses sería libre para incorporarme al vibrante mercado de trabajo que ofrecía oportunidades para todo aquel que supiera aprovecharlas."
        kenshiro "Y entonces conocí a Sonia."
        stalin "¿Era una buena comunista?"
        kenshiro "Con las tetas que tenía como si le robaba al Papa. El caso es que caí rendido a sus encantos. Durante 8 años estuvimos en su piso de estudiante mientras ella terminaba sus estudios de Repostería y Diseño Industrial."
        kenshiro "Hasta que se graduó y se acabó el chollo que le pagaban sus padres. Nos vimos en la calle de la noche a la mañana y justo cuando íbamos cargando con las cajas repletas de nuestras pertenencias y nuestros sueños"
        kenshiro "pasamos frente a la puerta de una sucursal. Uno de los empleados nos vio y salió corriendo a nuestro encuentro. Nos ofreció dinero para una hipoteca y un Porsche Cayenne y todo a cambio de..."
        kenshiro "¿Cómo dijo...? Ah, sí, a cambio de nuestra felicidad. No lo entendí muy bien, pero estaba desesperado y aquel dinero caído del cielo nos venía de perlas. Justo al salir nos topamos en la puerta con el promotor de Pocerogrado que nos ofreció"
        kenshiro "un bonito dúplex a un precio de risa. Una risa tan estruendosa como la del promotor cuando firmamos los papeles y dimos una entrada."
        pov "Pero si os hacía tanta falta un hogar, ¿por qué firmásteis sobre plano y no comprásteis una casa ya construida?"
        kenshiro "Porque nos regalaban los visillos. Sonia me insistió..."
        kenshiro "Al día siguiente, cayó Caja Madrid, el banco que nos había dado el préstamo. Los obreros estuvieron seis meses sin cobrar. Al séptimo se marcharon y nos dejaron con el edificio medio a hacer."
        kenshiro "Los hombres se comieron a los hombres, Pocerogrado estalló en un caos de violencia y fuego. Los políticos hablaron y hablaron mientras los ciudadanos de la urbanización luchaban por los últimos muebles de un Ikea cercano que estaban desmantelando."
        kenshiro "De la noche a la mañana nos vimos con un ático sin tabiques y sin ascensor, debiendo mucho dinero y encima los visillos no le gustaban."
        kenshiro "Aquella noche, mientras dormíamos debajo del puente de la M30, noté a mi novia intranquila. Cuando desperté, se había marchado. Me había abandonado."
        kenshiro "Desde entonces vago por las Llanuras Centrales en busca del cabecilla detrás de mi desgracia, el que envió al promotor al banco, el sardónico Flaming Wheels."
        kenshiro "Y ayer por fin di con su paradero."
        pov "El Gimnasio Butan."
        kenshiro "Exacto."
        kenshiro "Podemos continuar."
        stalin "Avisadme si hay alguna piedra por el camino."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero3 with dissolve
        show kentravel at left
        show concejal at right
        kenshiro "¿Y tú quién eres?"
        concejal "¿No me conoces? Soy tu concejal de urbanismo."
        kenshiro "..."
        concejal "Sí, hombre. Suelo estar en la barra americana del club de carretera de la N-23. Menos los domingos, que son sagrados."
        kenshiro "¿También te han pagado para impedir que recupere lo que es mío?"
        concejal "Me han pagado por tantas cosas... Pero esta vez me dijeron que viniera a partirte la cara, y aquí estoy."
        concejal "No es personal, solo son negocios."
        pov "Creo que vamos a tener que hacer lo mismo."
        menu:
            "Hazte Bankiero":
                pass
            "Estamos saliendo de la crisis":
                pass
            "España no ha sufrido ningún rescate":
                pass
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide concejal with dissolve
        hide kenlucha
        show kentravel at center
        c "Esta vez fue más fácil."
        pov "Ya me dirás. Contra un político..."
        c "Oiga, señor Kenshiro."
        kenshiro "¿Qué quieres?"
        c "Usted no me daría una paliza como a esos otros, ¿verdad?"
        kenshiro "¿Por qué lo preguntas?"
        extend " ¿Has hecho algo de lo que te arrepientas?"
        stalin "¿Aparte de traicionar su ideario primigenio?"
        kenshiro "Creo que Staline está antes en la cola para zurrarte."
        c "En el fondo me quiere."
        scene pocerotrav at Pan((0, 0), (400,0), 18.0)
        show kentravel:
            xpos 0.2
            ypos 0.2
        with dissolve
        play music "pocerogrado2.mp3"
        $ renpy.pause(15, hard=True)
        stop music
        scene pocero4 with dissolve
        show kentravel at left
        show promotor at right
        kenshiro "¿No os cansáis de dar la paliza?"
        promotor "Paliza la que te voy a dar."
        pov "Siempre igual, puñetazo por aquí, Hokuto no Ken por allá..."
        pov "¿Por qué no le dan su dinero y ya está?"
        promotor "¡Si lo hago por su bien! Se lo he dicho muchas veces, que no lo venda, que esto va a remontar y que se lo van a quitar de las manos."
        pov "Y el año que viene va a ser el de Linux en el escritorio."
        promotor "¿Qué?"
        kenshiro "Basta de cháchara insulsa que aquí hay gente que querrá irse a la cama ya."
        pov "Aquí vamos de nuevo..."
        menu:
            "Métete en una hipoteca en yenes":
                pass
            "¿Para qué estudiar si te puedes sacar 3000 euros de paleta?":
                pass
            "La NEP ya está aquí":
                pass
        
        hide kentravel
        show kenlucha at left
        play sound "tata.mp3"
        with Shake((0, 0, 0, 0), 7.0, dist=30)
        hide promotor with dissolve
        hide kenlucha
        show kentravel at center
        kenshiro "Creo que ya no nos molestará nadie más."
        c "¿Cómo puedes estar seguro?"
        kenshiro "Porque llevamos mucho tiempo con lo mismo y no queremos que el jugador se aburra, así que, "
        extend "¡dentro gimnasio!"
        
        scene black with dissolve
        show gymtextpo1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextpo2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gympocero with fade
        show cuñadopocero at center
        rueda "Buenas tardes, caballeros. No suelo tener muchas visitas por aquí."
        rueda "¿Han pensado en adquirir una solución habitacional a un precio inmejorable en una de las zonas con más potencial de toda la península?"
        c "Tanto como potencial... Quizá si sube el nivel del mar dos kilómetros en unas décadas los nietos de alguien podrán disfrutar de un piso a pie de playa pero mientras tanto..."
        show gympocero at right with move
        show kentravel at left with dissolve
        kenshiro "¡Basta de engaños!"
        kenshiro "Prepárate, maldito. ¡Soy el fin de tu loca ambición!"
        rueda "Y dale. Las culpas al capitalismo. Yo solo aplico la ley. ¿O es que es ilegal vender estos pisos?"
        rueda "Cada uno con su responsabilidad."
        kenshiro "Te voy a dar hasta en el cielo del paladar."
        rueda "Y se puede saber exáctamente por qué razón."
        kenshiro "Quiero que me devuelvas la entrada que di por el piso en el Complejo Esmeralda."
        rueda "¿Lo compraste bajo plano?"
        kenshiro "Sí."
        rueda "Pues lo siento pero no puedo hacer nada."
        kenshiro "Ven que te voy a meter un meco que vas a echar hasta la papilla que no te daba tu madre."
        rueda "No estoy interesado en involucrarme en una danza de puñetazos y golpes mortales. Si quieres que te devuelva la entrada del piso tendrás que pasar un test sobre seguridad antiincendios."
        kenshiro "¿Y si te pego igual?"
        rueda "Soy de caucho. Buena suerte."
        kenshiro "¡Estoy perdido!"
        extend " ¡Ni siquiera sé leer!"
        pov "Pues ya tienes una edad."
        kenshiro "Si te parece le digo al maestro: Oye, que tengo que ir a empaparme de las obras de Jose María Pemán, que lo de aprender el Puño de la Estrella del Norte lo dejamos para luego."
        pov "Ya nos encargamos nosotros entonces."
        pov "Pero oiga, Señor Wheels..."
        rueda "Llámame Ruedines."
        pov "Si pasamos el test, aparte del dinero, nos dará sus tres votos para la elección del Presidente."
        rueda "De acuerdo. Total, vais a perder."
        hide cuñadopocero
        hide kentravel
        $ rueda("¿Con qué se apaga el fuego?", interact=False)
        menu:
            "Agua":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                rueda "Habéis tenido suerte. Poca gente la acierta."
            "La voluntad de los bomberos":
                rueda "Si de voluntad dependiera tendría un rabo que me daría vueltas a la llanta, pero no, aquí estoy, impotente ante las decenas de calendarios de Playboy con los que están empapeladas las paredes del Gimnasio."
                pass
            "El amor de una madre":
                rueda "Eso pensaba San Epidoro de Ipéstrote cuando los romanos le condenaron a morir en la hoguera por robar el contenido del platillo del Templo de Juno durante la Caleindades."
                rueda "Pero por mucho que su progenitora le quisiera, se quemó igual."
                rueda "Que la madre le había desheredado un par de años antes, pero la esperanza la tenía."
                pass
            "Más fuego":
                rueda "También podría valer en según qué circunstancias, pero esta respuesta denota un comportamiento agresivo y por eso no es válida."
                pass
        rueda "Siguiente pregunta..."
        $ rueda("Si te prenden fuego tienes que...", interact=False)
        menu:
            "Aprovechar para encenderte un cigarro":
                rueda "También podrías hacerlo pero fumar es malo para la salud. Bastante tienes con las llamas."
                pass
            "Rodar por el suelo":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                rueda "¡Maldición! Esta era la última difícil que me quedaba."
            "Correr hacia tus enemigos para, al menos, no morir solo":
                pass
            "Pagar a Hacienda. Nunca dejes de pagar":
                montoto "Me da igual lo que digas. Esta es siempre la opción correcta."
                rueda "Estás en mi gimnasio y además te envié un sobre muy bonito el otro día. No sé si te acuerdas."
                stalin "Hemos fallado entonces, ¿no?"
                rueda "Totalmente."
                pass
        rueda "He de aceptar lo inaceptable. Seguramente consigáis todos mis votos. La pregunta que os haré es la más fácil de todas:"
        $ rueda("¿Qué Real Decreto aprueba el Reglamento de Seguridad contra incendios en establecimientos industriales, y que afecta a los edificios o recintos, cuya actividad principal sea de tipo industrial?", interact=False)
        menu:
            "2245/2004":
                rueda "Inaudito. ¡Habéis fallado!"
            "2154/2003":
                rueda "Inaudito. ¡Habéis fallado!"
            "2347/2005":
                rueda "Inaudito. ¡Habéis fallado!"
            "2267/2004":
                $ puntosj +=1
                show btext1:
                    ypos 0.3
                    xpos 0.3
                $ renpy.pause(3,hard=True)
                show gympocero at right with dissolve
                show kentravel at left with dissolve
                rueda "Estaba cantado que íbais a saberlo."
                pov "¿Quién no conoce ese dato?"
                rueda "No te creas, algún inconsciente hay por ahí suelto."
                kenshiro "Mi dinero, escoria."
                rueda "De acuerdo, pero no vayas contándolo por ahí. Tengo una reputación que mantener y no quiero tener que estar pensando más preguntas."
                rueda "Y vosotro tenéis los votos también. Idos."
                c "Muchas gracias, señor caucho."
                rueda "Tú llámame Flaming Wheels."
                jump mapa
        show gympocero at right with dissolve
        show kentravel at left with dissolve
        rueda "Aunque hayáis ganado algún voto, vuestro amigo no podrá recuperar la entrada que dio para el piso."
        kenshiro "¿Cómo? Será inútil pero te voy a dar de hostias hasta que se me acabe el cintrón."
        play sound "tata.mp3" #sonido del puño de la estrella del norte
        $ renpy.pause(2, hard=True) #pausa que dure el sonido
        scene pocero1
        c "Al final no hemos escapado tan mal."
        pov "Desde luego, podríamos haber sido la cena de alguno de estos indeseables."
        montoto "O nos podrían haber colado un aval."
        jump mapa
    
    jump mapa