label boliches:
    $ boliches = True
    $ cuento = ""
    
    #personajes
    define roboto = Character("Mr. Roboto", color="#327A39", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define criado = Character("Umpopo", color="#5C4A33", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define rizos = Character("La Lisos", color="#662864", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define master = Character("Master Wilfredo", color="#23B9B1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define creador = Character("El Creador", color="#327A39", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define carcelero = Character("Carcelero", color="#A4BF73", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    image gymboliches = "images/gymboliches.jpg"
    image boliches1 ="images/boliches1.jpg"
    image boliches2 ="images/boliches2.jpg"
    image finlandia ="images/finlandia.jpg"
    image boliches3 ="images/boliches3.jpg"
    image bolichesb ="images/bolichesb.jpg"    
    image bolichesc ="images/bolichesc.jpg"
    image bolichesd ="images/bolichesd.jpg"
    image bolichesf ="images/bolichesf.jpg"
    image bolichesg ="images/bolichesg.jpg"
    image carcelfrontal ="images/carcelfrontal.jpg"
    image corredor ="images/corredor.jpg"
    
    image cuñadoboliches = "images/roboto.png"
    image lalisos = "images/lalisos.png"
    image criado = "images/criado.png"
    image master = "images/master.png"
    
    
    image gymtextbo1 = Text("{size=40}Gimnasio Metallic Proud",color="#fff", text_align=0.3)
    image gymtextbo2 = Text("{size=40}Las ideas se rebaten, los biceps no",color="#fff", text_align=0.3)
    scene travelboliches at Pan((0, 0), (300,0), 14.0)
    play music "entradillaboliches.mp3"
    $ renpy.pause(15, hard=True)
    
    play music "cancionciudad2.mp3"
    
    if mrajao == True:
        scene boliches1 with fade
        r "Así que esta es la última ciudad en conseguir la independencia..."
        extend " Pensaba que esas cosas en España no pasaban."
        montoto "Curiosamente, a nivel de población sí que es posible escindirse de la ciudad madre. Se permite para tener contentos a los aldeanos."
        montoto "Total, mientras sigan dentro de España les podemos cobrar igual. No importa que se crean los reyes del barrio. Al contrario, más impuestos para el erario público."
        r "Quizá deberíamos dar la independencia a todos los pueblos de España para solucionar el problema del déficit."
        montoto "Me temo que no funcionaria. Es como la metadona, una dosis está bien pero si estás siempre dándole al final sube su precio en el mercado."
        pov "Qué conversaciones más extrañas tenéis."
        show criado at center with moveinright
        r "¡Montoto, un negro!"
        criado "Buenas tardes, caballeros."
        criado "Si no me equivoco, vienen ustedes en busca de los votos de Mr. Roboto."
        r "Le han informado bien."
        criado "Este me envía para acompañarles y de paso, si no les importa, mostrárles las bondades de Los Boliches, su cultura, sus lugares y sus tradiciones."
        r "Yo no tengo nada más importante que hacer."
        extend " ¿Tienes un puro que te sobre?"
        criado "Sí, pero no creo que se lo quiera fumar."
        criado "Detrás mía podrán admirar la Peseta Masona."
        montoto "No se ve."
        criado "Perdón."
        show criado at right with move
        criado "Su historia se cuenta en el libro \"Crónicas de Mr. Roboto\" Volumen II, escrito por Mr. Roboto en persona, por lo que no ahondaré mucho en ella."
        criado "Si están interesados, no duden en comprarlo en su punto de venta más cercano o visitar su blog, donde también aparece."
        criado "Solo decir que desde las obras de ampliación del pasadizo, la puerta no abre, por lo que ahora simplemente es un homenaje egocéntrico a la gloria del ayer."
        criado "Si me acompañan..."
        scene boliches2 with fade
        $ renpy.pause(1.0, hard=True)
        show criado at right with moveinright
        criado "Behold! El Pene de Ramses."
        pov "Esto no es Los Boliches, es el centro de Fuengirola."
        criado "Los bolicheros nos apropiamos el terreno que queremos."
        criado "Durante la invasión napoleónica de Egipto, el soldado fuengiroleño Corbet Martínez, enrolado en el ejército francés engañado por su padre que le hizo creer que había dejado embarazada a la hija de la panadera, cuando en realidad había sido él, se vio fascinado por este obelisco que se alzaba por aquel entonces frente al templo de Apis, en Memfis."
        criado "Durante la batalla del Loco Cojo, Corbet se libró de la muerte en forma de proyectil de artillería escondiéndose tras él y prometió que cuando terminara la guerra se lo llevaría a su tierra."
        criado "Como no pudo esperar tanto, huyo esa misma noche. Los de Fuengirola dirán que desertó, pero ¿acaso no combate otro día el soldado que corre?"
        criado "No fue el caso de Martínez, que terminó sus días recogiendo cobre de las casas de los indianos y revendiéndolo al doble del precio de mercado."
        extend " Se arruinó."
        criado "A modo de anécdota, fue necesario el esfuerzo de quinientos coinos para poner la marcha atrás en el camión que transportó el obelisco hasta su ubicación actual."
        r "Desde la punta, 6.500 años nos contemplan."
        pov "¿6.500?"
        r "Cuando Dios creó el mundo lo adornó con estos monumentos. Ningún ser humano podría haber tallado la piedra con unos ángulos rectos tan perfectos."
        criado "Continuemos..."
        scene finlandia with fade
        $ renpy.pause(1, hard=True)
        show criado at left with moveinleft
        criado "Finlandia... "
        extend " El país."
        criado "Trasladado a este edificio tras la gran nevada de 1985 en la que el país escandinavo quedó sepultado tras una tormenta que duró 324 días, dos más de lo acostumbrado."
        criado "Uno de los paises más pacíficos del mundo, solo se le conoce un conflicto de importancia, cuando el 18 de abril de 1997, un gitano entró a robar al segundo piso y se dio de bruces con la guardia presidencial, que también realizaba las funciones de conserje, y que repelió la agresión lanzando contra el asaltante un bote de lejía a medio gastar." 
        criado "El ladrón se lanzó por la ventana, causando graves daños a las petunias de la Ministra de Defensa, que, afectada por el suceso, no volvió a dedicar la misma pasión que antaño al cuidado de su jardín."
        criado "Desde entonces, todos los 18 de abril se conmemora la Batalla de Lejía, un conflicto que reforzó la existencia de la nación y su soberanía."
        r "Permítame que le diga que esta es una ciudad muy rara: independiente, albergando a un país dentro de ella, con personas de color..."
        criado "Como nos gusta decir en Los Boliches: Somos especiales, pero no de \"Ay mira lo que hace el pobre Juan Pedro. Con lo listo que podría haber sido.\""
        criado "Se hace un poco tarde, así que solo nos detendremos en un lugar más antes de llevarles al gimnasio."
        pov "¿Y no podríamos ir ahora?"
        criado "Mr. Roboto no está disponible. Se está depilando."
        scene boliches3 with fade
        $ renpy.pause(1, hard=True)
        show criado at right with moveinright
        criado "¡Maravíllense con los recuerdos del pasado!"
        criado "Las ruinas de la locura"
        criado "Según se cuenta en los papiros encontrados muy cerca de estas ruinas, escritos en babilónico antiguo, en el siglo VI a.c. un grupo de adoradores de los dioses primigenios se estableció en una pequeña villa de la costa de Bolichis para poder llevar a cabo sus rituales oscuros con tranquilidad."
        criado "Se dice que cuando intentaron despertar a su dios, Cthulhu, un tentáculo gigantesco salió de las aguas y destrozó el lugar mientras la voz atronadora del dios gritaba: ¡QUE ME DEJÉIS DORMIR, COÑO! Un grito cuyos ecos todavía reverberan en las montañas las noches en que no hay estrellas."
        pov "Si es del período babilónico, ¿por qué pone en un muro: Romanes Eunt Domus?"
        criado "Los romanos eran unos gamberros. No quieran saber lo que dejaron escrito en los baños de mujeres del ayuntamiento."
        scene boliches4 with fade
        $ renpy.pause(1,hard=True)
        show criado at center with moveinleft
        criado "Espero que hayan disfrutado con la visita. Mr. Roboto les espera en el edificio que tienen a su espalda."
        r "Oiga, antes de marcharse. ¿Usted no será de Níger por casualidad?"
        criado "... No."
        hide criado with moveoutright
        r "Parece que le ha sentado mal la pregunta."
        pov "¿A qué ha venido eso?"
        r "No sé, el otro día vi una película y se lo preguntaban a todos los actores de color."
        pov "Entremos al gimnasio..."
        scene black with dissolve
        show gymtextbo1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbo2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymboliches with fade
        show cuñadoboliches at center 
        r "Hola."
        roboto "Bienvenidos a mi humilde morada."
        roboto "Y vosotros sois..."
        r "M. Rajao, librepensador y saqueador."
        roboto "¡Enseñame las tetas!"
        r "¿Cómo?"
        roboto "Perdona, es un tic que tengo desde hace años."
        montoto "¿Alguna vez le ha funcionado? Porque yo no paro de preguntar y nada."
        roboto "Funciona si llevas más cadenas de oro al cuello que M.A. Barracus."
        montoto "Yo no puedo llevar oro, va contra mi religión. Nosotros lo guardamos en cámaras acorazadas a gran profundidad que visitamos cada vez que queremos aparearnos, para que el fulgor dorado nos inspire durante la cópula."
        pov "Tío, qué asco."
        r "Hemos estado recorriendo el lugar. Muy bonito su barrio."
        roboto "Ciudad."
        r "¿Pero no es un barrio?"
        roboto "Ciudad."
        r "Pero en el PGU pone que..."
        roboto "¡CIUDAD! ¡Canalillo, culo, tetas, follar, sexo anal!"
        r "..."
        roboto "El tic..."
        roboto "Me alegro de que hayan disfrutado de la ciudad. Está en su mejor momento pues dentro de una semana vendrán los turistas en masa a dejar su dinero y conseguir a cambio sueños imperecederos."
        r "Quizá vengamos en agosto. Hoy estamos aquí por..."
        roboto "Si, para ganaros mis votos y ¡te voy a comer to´l potorro!"
        montoto "¡Pero si no le he dicho mi nombre!"
        roboto "Me llegó la nota del juzgado hace un rato."
        roboto "Si quieres mis votos tendrás que ganártelos con las artes escritas."
        roboto "Escribid un cuento interesante."
        pov "¿Por qué pide algo que usted no es capaz de hacer?"
        roboto "Porque no tengo dinero para pagar a alguien por ello."
        $ cuento = renpy.input("Podéis empezar:")
        if len(cuento) < 140:
            roboto "¿Ya está? Eso cabe en un tuit. ¿Te estás cachondeando de mí?"
            extend " Te dije que escribieras un cuento. Al menos el esfuerzo, hombre."
            roboto "Te has quedado sin votos. Lárgate de aquí antes de que le diga a Umpopo que represente contigo el chiste de la clínica de adelgazamiento."
        else:
            roboto "Mmmm... No está mal. Le veo algunos defectos de estilo, la gramática un poco forzada, la ortografía no desentona..."
            roboto "De acuerdo. ¡Tres votos para Slytherin!"
            $ puntosj += 3
            roboto "Podéis ir en paz."
            r "¿Puedo ir al baño antes?"
            roboto "No."
        
        
    if ken == True:
        stop music
        scene boliches1 with fade
        $ renpy.pause(1, hard=True)
        k "Así que esta es la última ciudad en conseguir la independencia..."
        extend " Se nota que aquí el PRESOE fue una vez fuerte."
        pov "¿Quién gobierna ahora?"
        espejo "El partido del malvado M. Rajao. se hizo con el poder hace poco."
        pov "¿En las últimas elecciones?"
        espejo "Pues ahí, ahí... Hace 25 años."
        show criado at center with moveinright
        criado "Buenas tardes, caballeros."
        criado "Si no me equivoco, vienen ustedes en busca de los votos de Mr. Roboto."
        k "Le han informado demasiado bien..."
        criado "Mi maestro me envía para escoltarles y de paso, si no les importa, mostrarles las bondades de Los Boliches, su cultura, sus lugares y sus tradiciones."
        k "La verdad es que no nos interesa mucho."
        criado "Aquellos que lo deseen, síganme."
        hide criado with moveoutright
        pov "¿No vamos?"
        k "¿Bromeas? No me fío de nadie que tenga un rabo más grande que el mío."
        espejo "Guía de los falos rosados, no deberías ser tan vulgar."
        pov "Oye, ¿y qué pasa conmigo?"
        k "He leído los comentarios que hacen sobre ti en el Tinder Premium. Estoy por darte un abrazo."
        pov "¿Existe un Tinder Premium?"
        k "Sí, para la gente que folla."
        espejo "Todo eso está muy bien, pero ¿dónde estará el gimnasio aquí?"
        k "Seguro que [jugador] lo sabe."
        extend " Dinos, ¿a dónde vamos?"
        pov "Al olvido."
        k "Esa no es una opción."
        pov "Deja que mire la Guía Michelín que he robado de la gasolinera donde paramos antes."
        espejo "No deberías robar estando con nosotros. Puede hacer que la gente recuerde... cosas."
        menu:
            "Pandorino Street":
                scene bolichesb with wipeleft
            "Lacey Street":
                scene bolichesc with wiperight
            "Piturra Avenue":
                scene bolichesd with wipedown
            "Calimero Road":
                scene bolichesf with wipeup
                pov "¿Quién hay allí?"
                espejo "Algún espontáneo que quiere conocer a la piedra filosofal del progresismo."
        k "Lo único que se ve aquí es depravación, suciedad, maldad y tristeza."
        pov "¿Qué estás mirando?"
        k "Las fotos de la última junta del partido. No fue agradable."
        espejo "Sigamos. Intuyo que no debe de quedar mucho."
        menu:
            "Alter Ego Avenue":
                scene bolichesg with wiperight
                k "Aquí no hay nada. Debimos haber tomado la calle con el nombre ridículo."
                k "Giremos aquí a la izquierda y que sea lo que dios quiera."
            "Lebanon Street":
                scene bolichesg with wiperight
                k "Aquí no hay nada. Debimos haber tomado la calle con el nombre ridículo."
                k "Paguemos a ese taxista para que nos lleve a algún sitio interesante y que sea lo que dios quiera."
            "Portobello Road":
                scene bolichesg with wiperight
                k "Aquí no hay nada. Debimos haber tomado la calle con el nombre ridículo."
                k "Introduzcámonos en esta alcantarilla y que sea lo que dios quiera."
            "Calle Almirante Tancredi":
                scene bolichesg with wiperight
                k "Aquí no hay nada. Debimos haber tomado la calle con el nombre ridículo."
                k "Giremos aquí a la derecha y que sea lo que dios quiera."
             
        scene carcelfrontal with wipedown
        $ renpy.pause(1, hard=True)
        k "¿Por qué siempre terminamos en la cárcel?"
        pov "Debe de ser un gen español."
        k "Vamos a entrar. Me duelen los pies y tengo que ir al baño."
        scene corredor with fade
        $ renpy.pause(0.6, hard=True)
        show carcelero at center with dissolve
        carcelero "Bienvenidos al Penal Internacional para Supercriminales y Bloggeros."
        carcelero "¿Qué puedo hacer por ustedes?"
        espejo "Nos hemos perdido."
        k "Y yo necesito ir al baño con urgencia."
        carcelero "A todos nos ocurre alguna vez. No se preocupen, la justicia siempre termina por encontrarnos y por eso se creó esta penitenciaría, para todos aquellos que piensan que la ley es solo un estado de opinión y que puedes escribir un blog únicamente publicando listas."
        k "Eso es muy interesante. Los socialistas estamos con la reinserción y el reeeducamiento de nuestros presos..."
        carcelero "¿Reeducación? Déjeme que le enseñe alguno de nuestros más ilustres invitados. Le harán recapacitar."
        pov "¿Es necesario?"
        carcelero "Sí."
        show carcelero at left with move
        $ renpy.pause(0.6, hard=True)
        show lalisos at right with dissolve
        carcelero "Aquí tenemos a La Lisos, bloggera y bomba sexual (sic)"
        k "Creo que vi su perfil una vez en el Tinder Premium."
        rizos " 1..2...3... y 4, ¡¡¡La rizos viene a por ti!!! (A que la invites a un gin tonic y lo que surja)"
        k "¿Quién es La Rizos?"
        carcelero "Es una de las múltiples personalidades que ha desarrollado. También dice ser una oveja, un cojin morado y arquitecta."
        k "¿Arquitecta?"
        extend " Pobre, está chiflada."
        carcelero "Pero es muy buena chica, que es lo que importa. No nos tira la comida, no se resiste cuando la pinchamos para sacarle sangre y no nos hace descaradas propuestas sexuales."
        carcelero "Bueno, a Hans sí, pero es sueco y no se entera de nada. Es que es de intercambio."
        k "¿Por qué la encerraron?"
        carcelero "Vino por su propia voluntad. Una tarde vio en un documental de Divinity que los presos reciben muchas cartas de admiradores y pensó que era la única manera de conseguir novio."
        espejo "Cada vez me da más pena esa chica."
        carcelero "Que no se la de. No quiere salir conmigo y eso que le he propuesto una reducción de condena a cambio."
        carcelero "Dice que soy muy frío."
        carcelero "Pero yo no tengo la culpa, es que me hicieron así."
        rizos "Digan que no. Lo que pasa es que no quiere ponerse una goma."
        carcelero "Es que con preservativo no siento nada."
        rizos "Ni sin él tampoco. ¡Si tienes un Rampant Rabbit en la entrepierna!"
        carcelero "¿Entonces?"
        rizos "Ya lo hemos hablando muchas veces. Lo nuestro es imposible."
        rizos "Además, piensas que Lost es mala."
        k "Es que lo es."
        espejo "Malísima."
        pov "Terrible."
        carcelero "Apocalíptica."
        rizos "¡No puedo con los hombres!"
        hide lalisos with moveoutright
        $ renpy.pause(1, hard=True)
        carcelero "Se le pasará. Siempre terminamos igual. Basta con ponerle la última temporada y ni siquiera su fanatismo ciego es capaz de negar la evidencia."
        show master at right with moveinright
        master "Ya te digo, brothel. Donde esté Doctor en Alaska, que se quite el resto."
        master "Con el reno me partía la polla."
        k "¿Y este por qué está aquí?"
        carcelero "Entre sus muchos delitos destaca el de postureo en tercer grado. Ahí donde le ven, vio un anuncio de la serie del Dr. Fleischman durante un descanso del Juventut de Badalona - Jugoplastika en el 92 y se cree el fan número 1 de la misma."
        master "Y lo soy. Es la serie que me hizo amar a los judios de Nueva York."
        carcelero "No le hagan caso. Mató a varios en el 98. Esto es una cárcel, no se vayan a pensar que encerramos a la gente solo por gilipolleces."
        master "Yo no maté a nadie, simplemente les vendí una cinta de correr. La naturaleza hizo el resto."
        carcelero "No tienes corazón, Master Wilfredo."
        master "Tú tampoco lo tendrás cuando mi hermano me saque de aquí y te lo arranque con las propias manos de un inspector de Hacienda."
        hide master with moveoutright
        show carcelero at center with move
        k "¿Quién es su hermano?"
        carcelero "No lo sabemos, pero no deja de hacer referencias a él. Algunas veces dice que lo ha visto en Los Simpsons, otras que Bela Lugossi se ha cagado en su legado, palabras textuales."
        carcelero "Creemos que simplemente está loco."
        k "¿Nadie ha podido certificarlo?"
        carcelero "Somos funcionarios de prisiones. ¿Entiende? Funcionarios... de prisiones."
        espejo "Creo que debemos marcharnos ya. Se nos hace tarde."
        pov "¿Sabe por dónde queda el gimnasio de Mr. Roboto?"
        carcelero "Sí, no tiene pérdida. Termine de leer esto y en el próximo clic del ratón, allí estará."
        scene black with fade
        stop music
        creador "¡Hola! Perdona que te interrumpa. Soy el creador."
        creador "No el creador de todo, solo de este juego. Te he estado observando un rato y..."
        k "Pues a ver si os ponéis de acuerdo que según el carcelero ya debería estar frente a Roboto. Y no sé por cuánto tiempo podré contener las \"fuentes del Nilo\"."
        creador "Ya pero es que... mira, que tu cara lo dice todo y no quiero que lo pases mal, así a lo tonto..."
        creador "Te doy la oportunidad de poner fin a la experiencia y salir con las mismas neuronas con las que comenzaste a jugar, aunque habiendo perdido un tiempo precioso para descargarte videos de Xhamster, o de continuar jugando..."
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
                        creador "Jo, no puedo ser más afortunado. Me la enviarás de verdad, ¿no? Mi dirección de correo es: veranodeldescontento\@gmail.com"
                        creador "Si no me la envías, que sepas que el karma puede que te la devuelva, que una mañana te despiertes y entre los mensajes privados de WA lleno de fotopollas no socilitadas."
                        creador "¡Disfruta del juego!"
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextbo1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbo2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymboliches with fade
        k "Oye, pues se me han quitado las ganas de orinar."
        show cuñadoboliches at center with dissolve
        k "¡Hola!"
        roboto "Bienvenidos a mi humilde morada."
        roboto "Y vosotros sois..."
        k "Me llamo Ken Sánchez."
        roboto "¡Enseñame las tetas!"
        k "¿Cómo?"
        roboto "Perdona, es un tic que tengo desde hace años."
        k "No te preocupes, así suelo saludar a las mujeres que conozco."
        k "Hemos recorrido el lugar. Muy bonito su barrio."
        roboto "Ciudad."
        k "¿Pero no es un barrio?"
        roboto "Ciudad."
        k "Pero en el PGU pone que..."
        roboto "¡CIUDAD! ¡Canalillo, culo, tetas, follar, sexo anal!"
        k "..."
        roboto "El tic..."
        roboto "Me alegro de que hayan disfrutado de la ciudad. Está en su mejor momento pues dentro de una semana vendrán los turistas en masa a intercambiar sus fajos de inútiles billetes sin valor por sueños imperecederos."
        k "Quizá vengamos en agosto. Hoy estamos aquí por..."
        roboto "Si, para ganaros mis votos y ¡quiero hundirme en tu entreteto!"
        roboto "Me llegó la nota del juzgado hace un rato."
        roboto "Si quieres mis votos tendrás que ganártelos con las artes escritas."
        roboto "Escribid un cuento interesante."
        pov "¿Por qué pide algo que usted no es capaz de hacer?"
        roboto "Porque quiero presentarme a un concurso de relatos y no tengo dinero para pagar a alguien que lo escriba por mí."
        $ cuento = renpy.input("Podéis empezar:")
        if len(cuento) < 140:
            roboto "¿Ya está? Eso cabe en un tuit. ¿Te estás cachondeando de mí?"
            extend " Te dije que escribieras un cuento. Al menos el esfuerzo, hombre."
            roboto "Te has quedado sin votos. Lárgate de aquí antes de que le diga a Umpopo que represente contigo el chiste de la clínica de adelgazamiento."
        else:
            roboto "Mmmm... No está mal. Le veo algunos defectos de estilo, la gramática un poco forzada, la ortografía no desentona..."
            roboto "De acuerdo. ¡Tres votos para Hufflepuf!"
            $ puntosj += 3
        
        
        
        
    if coletas == True:
        stop music
        scene boliches1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        c "Así que esta es la última ciudad en conseguir la independencia..."
        extend " Me alegra saber que por esta envejecida nación todavía corre la sangre fresca del progreso."
        stalin "Curiosamente, a nivel de población sí que es posible escindirse de la ciudad madre. Se permite para tener contentos a los aldeanos."
        stalin "Mientras sigan dentro de España les pueden cobrar igual. No importa que se crean los reyes del barrio. Al contrario, más impuestos para el erario público."
        c "Sabía yo que alguna trampa administrativa tenía que haber."
        stalin "El capital nunca permitiría el libre desarrollo de las comunidades. Se podrían poner de acuerdo para hacerse con sus medios de producción si llegaran a darse cuenta de que los burgueses solo son intermediarios entre su trabajo y la plusvalía."
        pov "Qué conversaciones más extrañas tenéis."
        show criado at center with moveinright
        c "¡Staline, un amigo africano!"
        criado "Buenas tardes, caballeros."
        criado "Si no me equivoco, vienen ustedes en busca de los votos de Mr. Roboto."
        c "Le han informado bien."
        criado "Este me envía para acompañarles y de paso, si no les importa, mostrárles las bondades de Los Boliches, su cultura, sus lugares y sus tradiciones."
        c "Yo no tengo nada más importante que hacer."
        criado "Detrás mía podrán admirar la Peseta Masona."
        stalin "No se ve."
        criado "Perdón."
        show criado at right with move
        criado "Su historia se cuenta en el libro \"Crónicas de Mr. Roboto\" Volumen II, escrito por Mr. Roboto en persona, por lo que no ahondaré mucho en ella."
        criado "Si están interesados, no duden en comprar en su punto de venta más cercano o visitar su blog, donde también aparece."
        criado "Solo decir que desde las obras de ampliación del pasadizo, la puerta no abre, por lo que ahora simplemente es un homenaje egocéntrico a la gloria del ayer."
        criado "Si me acompañan..."
        scene boliches2 with fade
        $ renpy.pause(1.0, hard=True)
        show criado at right with moveinright
        criado "Behold! El Pene de Ramses."
        pov "Esto no es Los Boliches, es el centro de Fuengirola."
        criado "Los bolicheros nos apropiamos el terreno que queremos."
        criado "Durante la invasión napoleónica de Egipto, el soldado fuengiroleño Corbet Martínez, enrolado en el ejército francés engañado por su padre que le hizo creer que había dejado embarazada a la hija de la panadera, cuando en realidad había sido él, se vio fascinado por este obelisco que se alzaba por aquel entonces frente al templo de Apis, en Memfis."
        criado "Durante la batalla del Loco Cojo, Corbet se libró de la muerte en forma de proyectil de artillería escondiéndose tras él y prometió que cuando terminara la guerra se lo llevaría a su tierra."
        criado "Como no pudo esperar tanto, huyo esa misma noche. Los de Fuengirola dirán que desertó, pero ¿acaso no combate otro día el soldado que corre?"
        criado "No fue el caso de Martínez, que terminó sus días recogiendo cobre de las casas de los indianos y revendiéndolo al doble del precio de mercado."
        extend " Se arruinó."
        criado "A modo de anécdota, fue necesario el esfuerzo de quinientos coinos para poner la marcha atrás en el camión que transportó el obelisco hasta su ubicación actual."
        c "Cada vez que veo una plaza se me ponen los pelos de punta..."
        stalin "Al igual que a los capital-burgueses. En las plazas comenzó la desarticulación del movimiento ciudadano." 
        stalin "Les ofrecísteis una esperanza en forma de partido, de cambio desde dentro, totalmente irrealista. Las calles quedaron libres para que las limusinas de los oligarcas puedan circular por ellas en su búsqueda de riqueza sin fin."
        pov "¿Qué tiene de malo la esperanza?"
        stalin "Es el arma más peligrosa de las élites. Paradojicamente puede desarmar al espíritu más aguerrido y privarle de su ansia de justicia en el momento para postergarla a un futuro por definir."
        stalin "Un hombre esperanzado es un ser débil, sumiso, pusilánime. Por eso en la Unión Soviética los soldados no tenían calcetines y los trabajadores debían esperar años para conseguir un coche."
        pov "Pero sin esperanza no se puede vivir."
        stalin "El hombre tiene la curiosa cualidad de querer vivir a toda costa. Date una vuelta por cualquiera de nuestros gulags para comprobarlo."
        c "Zzz...zzzz..."
        pov "..."
        stalin "Siempre hace lo mismo."
        c "¿Cómo? ... Perdona, ha sido un breve episodio de narcolepsia."

        criado "Si me acompañan..."
        scene finlandia with fade
        $ renpy.pause(1, hard=True)
        show criado at left with moveinleft
        criado "Finlandia... "
        extend " El país."
        stalin "Así que aquí se escondieron esas ratas cuando el ejercito rojo invadi... liberó su país del capitalismo atroz?"
        criado "Trasladado a este edificio tras la gran nevada de 1985 en la que el país escandinavo quedó sepultado tras una tormenta que duró 324 días, dos más de lo acostumbrado."
        criado "Uno de los paises más pacíficos del mundo, solo se le conoce un conflicto de importancia, cuando el 18 de abril de 1997, un gitano entró a robar al segundo piso y se dio de bruces con la guardia presidencial, que también realizaba las funciones de conserje, y que repelió la agresión lanzando contra el asaltante un bote de lejía a medio gastar." 
        criado "El ladrón se lanzó por la ventana, causando graves daños a las petunias de la Ministra de Defensa, que, afectada por el suceso, no volvió a dedicar la misma pasión que antaño al cuidado de su jardín."
        criado "Desde entonces, todos los 18 de abril se conmemora la Batalla de Lejía, un conflicto que reforzó la existencia de la nación y su soberanía."
        c "Permítame que le diga que esta es una ciudad muy rara: independiente, albergando a un país dentro de ella, con personas de color..."
        criado "Como nos gusta decir en Los Boliches: Somos especiales, pero no de \"Ay mira lo que hace el pobre Juan Pedro. Con lo listo que podría haber sido.\""
        criado "Se hace un poco tarde, así que solo nos detendremos en un lugar más antes de llevarles al gimnasio."
        pov "¿Y no podríamos ir ahora?"
        criado "Mr. Roboto se está depilando."
        scene boliches3 with fade
        $ renpy.pause(1, hard=True)
        show criado at right with moveinright
        criado "¡Maravíllense con los recuerdos del pasado!"
        criado "Las ruinas de la locura"
        criado "Según se cuenta en los papiros encontrados muy cerca de estas ruinas, escritos en babilónico antiguo, en el siglo VI a.c. un grupo de adoradores de los dioses primigenios se estableció en una pequeña villa de la costa de Bolichis para poder llevar a cabo sus rituales oscuros con tranquilidad."
        criado "Se dice que cuando intentaron despertar a su dios, Cthulhu, un tentáculo gigantesco salió de las aguas y destrozó el lugar mientras la voz atronadora del dios gritaba: ¡QUE ME DEJÉIS DORMIR, COÑO! Un grito cuyos ecos todavía reverberan en las montañas las noches en que no hay estrellas."
        c "Eso les pasa por creer en el dios del capital, que devora a sus hijos por un aumento de la plusvalía."
        pov "Si es del período babilónico, ¿por qué pone en un muro: Romanes Eunt Domus?"
        criado "Los romanos eran unos gamberros. No quieran saber lo que dejaron escrito en los baños de mujeres del ayuntamiento."
        scene boliches4 with fade
        $ renpy.pause(1,hard=True)
        show criado at center with moveinleft
        criado "Espero que hayan disfrutado con la visita. Mr. Roboto les espera en el edificio que tienen a su espalda."
        c "Muchas gracias. Si necesita formar un movimiento de liberación progresista en su país, no dude en llamarme."
        hide criado with moveoutright
        pov "Entremos al gimnasio..."
        scene black with dissolve
        show gymtextbo1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbo2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymboliches with fade
        show cuñadoboliches at center 
        c "Hola."
        roboto "Bienvenidos a mi humilde morada."
        roboto "Y vosotros sois..."
        c "Yo soy El Coletas."
        roboto "¡Enseñame las tetas!"
        c "¿Cómo?"
        roboto "Perdona, es un tic que tengo desde hace años."
        stalin "Pues mejor no le digo cómo me llamo yo. Y [jugador] que ni abra la boca."
        c "Hemos recorrido el lugar. Muy bonito su barrio."
        roboto "Ciudad."
        c "¿Pero no es un barrio?"
        roboto "Ciudad."
        c "Pero en el PGU pone que..."
        roboto "¡CIUDAD! ¡Canalillo, culo, tetas, follar, sexo anal!"
        c "..."
        roboto "El tic..."
        roboto "Me alegro de que hayan disfrutado de la ciudad. Está en su mejor momento pues dentro de una semana vendrán los turistas en masa a dejar su dinero y conseguir a cambio sueños imperecederos."
        c "Quizá vengamos en agosto. Hoy estamos aquí por..."
        roboto "Si, para ganaros mis votos y ¡enseñadme los cataplines!"
        stalin "¡Pero si no le he dicho mi nombre!"
        roboto "Me llegó la nota del juzgado hace un rato."
        roboto "Si quieres mis votos tendrás que ganártelos con las artes escritas."
        roboto "Escribid un cuento interesante."
        pov "¿Por qué pide algo que usted no es capaz de hacer?"
        roboto "Porque no tengo dinero para pagar a alguien por ello."
        $ cuento = renpy.input("Podéis empezar:")
        if len(cuento) < 140:
            roboto "¿Ya está? Eso cabe en un tuit. ¿Te estás cachondeando de mí?"
            extend " Te dije que escribieras un cuento. Al menos el esfuerzo, hombre."
            roboto "Te has quedado sin votos. Lárgate de aquí antes de que le diga a Umpopo que represente contigo el chiste de la clínica de adelgazamiento."
        else:
            roboto "Mmmm... No está mal. Le veo algunos defectos de estilo, la gramática un poco forzada, la ortografía no desentona..."
            roboto "De acuerdo. ¡Tres votos para Ravenclaw!"
            $ puntosj += 3
    jump mapa