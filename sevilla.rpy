label sevilla:
    $ sevilla = True
    
    #personajes dialogo
    define fosforo = Character("El Fósforo", color="#20AE27", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define paciente = Character("Enfermo de fimosis", color="#E699A2", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define doctor = Character("Dr. Lolailo", color="#3A5984", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define enfermera = Character("Enfermera Joy", color="#F527A2", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define sorpresa = Character("Sor Presa", color="#F034E0", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define lacasitos = Character("Lacasitos", color="#D0AD13", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define megafonia = Character("Megafonía", color="#664545", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define loco = Character("Señor algo loco", color="#1F9529", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define portero1 = Character("Portero dicharachero", color="#1F9529", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define portero2 = Character("Portero sin pelo", color="#1F9529", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define duque = Character("Duque de Lerma", color="#1F9529", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)



    
    #imagenes ciudad
    image gymsevilla = "images/gymsevilla.jpg"
    image sevilla1 = "images/sevilla1.jpg"
    image entradahospital = "images/hospitalentrada.jpg"
    image consulta = "images/consulta.jpg"
    image saladeespera = "images/saladeespera.jpg"
    image sevilla1 = "images/sevilla1.jpg"
    image caseta1 = "images/caseta1.jpg"
    image caseta2 = "images/caseta2.jpg"
    image caseta3 = "images/caseta3.jpg"
    image tablero = "images/tablero.jpg"
    image wasted = "images/wasted.jpg"
    
    #imagenes personaje
    image cuñadosevilla = "images/carlos.png"
    image doctor = "images/doctor.png"
    image paciente = "images/paciente.png"
    image sorpresa = "images/sorpresa.png"
    image lacasitos = "images/lacasitos.png"
    image portero1 = "images/portero1.png"
    image portero2 = "images/portero2.png"
    image enfermera = "images/enfermera.png"
    image loco = "images/loco.gif"
    
    #cartas
    image finidi = "images/finidi.png"
    image lopera = "images/lopera.png"
    image monchi = "images/monchi.png"
    image uefa = "images/uefa.png"




    
    image gymtextse1 = Text("{size=40}Gimnasio Láudano de acero",color="#fff", text_align=0.3)
    image gymtextse2 = Text("{size=40}Amor y sudor",color="#fff", text_align=0.3)
    image textsep = Text("{size=40}Tres días después...",color="#fff", text_align=0.3)

    
    scene travelsevilla at Pan((0, 0), (300,0), 20.0)
    play music "entradillasevilla.mp3"
    $ renpy.pause(19, hard=True)
    
    play music "cancionciudad.mp3"
    
    if mrajao == True:
 
        scene sevilla1 with dissolve
        $ renpy.pause(1, hard=True)
        r "Aaaaay... Me duele la tripa, Montoto."
        r "Dame friegas con ricino."
        montoto "Presidente, eso no creo que sea legal ya siquiera."
        pov "¿Has comido algo que te haya podido sentar mal?"
        r "Nada. Lo único que he comido hoy ha sido un puñado de Ferrero Rocher que había en la limusina."
        pov "¿Ferrero Rocher?"
        r "Sí."
        pov "Ahora."
        r "¿Es que no me has escuchado?"
        pov "Ahora en verano."
        r "Sí, ¿pasa algo?"
        pov "No se pueden comer en estas fechas. Por eso los retiran de las tiendas."
        r "Yo pensaba que lo de no poder venderlos ahora era para que los pobres no los pidieran y la gente como yo pudiera comprar más."
        r "¿Y ahora me dices que habia un motivo sanitario?"
        montoto "A lo mejor ha sido el caviar o el Moet Chandon."
        r "No lo descarto, ¡malditos franchutes!"
        pov "Mucho insultar pero bien que consume sus productos."
        r "Alguien de mi categoría tiene que hacerlo. ¿No querrá que me coma un bocata de choped?"
        extend " Ni que fuera yo un vulgar funcionario." 
        pov "Las malas lenguas dirían que eso es lo que es."
        r "Insidias. Yo me saqué la oposición a guarda forestal, la más dura del estado, a la primera. Y tiene su mérito porque me senté lejos del estrado y no podía ver bien al presidente del tribunal señalándome las respuestas..."
        r "Aaaaayyy..."
        montoto "Tenemos que llevarte a un hospital."
        r "No quiero ir al médico en esta ciudad, que mira los de la serie esa..."
        r "Habrá gente que hable raro, y cuando me pregunten qué me duele, ¿y si no me entienden y me quitan un riñon?"
        montoto "No dejaré que te quiten nada que no sea necesario."
        r "Especialmente la virtud."
        montoto "Déjalo en mis manos."
        scene entradahospital with dissolve
        $ renpy.pause(1, hard=True)
        show paciente at center with dissolve
        paciente "Miarma, ¿cáces aquí enmedio como un pasmarote?"
        r "Te lo dije Montoto, tiene un arma. Es un ladrón de órganos."
        paciente "¿Qué via sé yo un ladrón, polla?"
        r "Montoto, solo he entendido \"polla\"."
        montoto "Otra vez no, Presidente. Céntrate."
        pov "Pasemos dentro mejor."
        scene saladeespera with fade 
        $ renpy.pause(0.5, hard=True)
        show enfermera at center with moveinleft
        enfermera "Quillo, ¿c´apasao? ¿T´asnucao?"
        r "Ay, Montoto, que ya me veo formando parte de un niño de los Emiratos Árabes."
        montoto "Pero un niño de clase alta, que son los únicos que se podrían permitir el proceso. El hijo de un jeque o un rey."
        r "No es consuelo. Quizás un poco, pero no demasiado."
        enfermera "Siéntate ahí, picha. Voy a ver qué dice el doctó."
        hide enfermera with moveoutleft
        r "Montoto, si me pasa algo, quiero que entierren lo que quede de mí junto a Praga."
        montoto "¿En la República Checa?"
        r "Jajaja, has caído."
        extend " Siempre quise hacer un chiste de gangosos."
        show enfermera with moveinright
        enfermera "Miarma, ven acá p´acá que, por lo pronto, tengo que sacarte la sangre."
        hide enfermera with moveoutleft
        montoto "¿Y qué hacemos mientras vuelve?"
        pov "Podríamos hablar un poco."
        montoto "Mejor leo este número del Pronto de 1997."
        montoto "..."
        montoto "Las intimidades de Daniel Ducruet y Estefanía."
        pov "Qué morbo."
        montoto "Y que lo digas. En Mónaco tienen un sistema fiscal con el que sueño todas las noches."
        montoto "Por desgracia no me dejan implantarlo."
        pov "¿Quiénes?"
        montoto "Bah, gentuza."
        r "Ya estoy aquí. La enfermera ha sido muy amable, me ha pinchado diez veces para comprobar que la aguja estaba bien."
        r "Me gusta la gente meticulosa en su trabajo."
        r "Lo raro es que me duele un poco el brazo y cuando bebo agua me chorrea el codo."
        stop music
        play sound "alarma.mp3"
        $ renpy.pause(4, hard=True)
        megafonia "Se ha escapado un paciente del ala de psiquiatría. Se teme que esté armado y es muy peligroso."
        extend " Si le ve, no le lleve la contraria y espere a que el personal sanitario se encargue de él."
        show loco at center with moveinleft
        r "¡Sapristi! ¡El loco!"
        pov "Sssh. No hables tan alto que te va a oir."
        loco "Ya le he oído y sí, no lo niego. ¡Estoy como una regadera!"
        loco "¡¡Leí un hilo en Twitter y me volvi loco!! ¿Pero por qué no se hacen un blog?? ¿Por qué no siguen las leyes de Internet que establecieron sus creadores en 1736?"
        loco "¿Qué les cuesta? Yo entro en Twitter para leer juegos de palabras y criticar al patriarcado y me encuentro con un folletín desnutrido y millones de RT sobre niños rata que viven en Youtube."
        loco "¿No voy a estar loco?"
        loco "¿Queréis saber lo más curioso?"
        menu:
            "Sí":
                loco "1) El martes pasado fui a sacar al perro al jardin a que hiciera sus necesidades, ya que le gusta hacerlo siempre en el mismo sitio."
                loco "2) Y no creáis, sería las once y pico de la noche, porque yo siempre aprovecho cuando termina Cazamariposas para estas cosas."
                loco "3) Pues bien, el perro no pudo hacer nada porque unos obreros habían acordonado la zona y estaban quitando el mobiliario urbano."
                loco "4) Que, claro, yo me quedé todo loco por las horas que eran. Nunca había visto a alguien trabajando tan tarde. Ni los basureros."
                loco "5) Intenté que el perro pasara, así de extranjis, y dejara el recuerdo, pero un obrero salió corriendo con una machota en la mano."
                loco "6) Y tuvimos que salir por patas. Dos calles más allá nos paramos. Miré hacia atrás. No nos perseguía. Tomé un pequeño respiro."
                loco "7) Y me dispuse a volver a casa por otro camino que pasaba delante de un bar. Allí estaba la tía más buena que vi jamás."
                loco "8) Se me acercó y me susurró al oído si quería tomar algo con ella. Yo rechacé su oferta pues mi perro tenía que defecar."
                loco "9) Incomprensiblemente, fue sensible a las necesidades de mi can. Creo que en ese momento me enamoré un poquito."
                loco "10) Fuimos a un parque cercano y mientras el perro añadía un pino a la arboleda local, nos perdimos la chica y yo tras unos matojos."
                loco "11) Y cuando le quité la ropa... No os lo váis a creer. En serio. Pues resulta que..."
                play sound "blow.ogg"
                $ renpy.pause(1, hard=True)
                hide loco with blinds
                megafonia "El paciente ha sido neutralizado con un dardo tranquilizante. Gracias por su comprensión y disculpen las molestias que les hayamos podido ocasionar."
                
            "No":
                loco "¿Cómo que no? ¿Es que no has oído lo que han dicho los altavoces?" 
                loco "Te gusta saltarte la ley, ¿verdad?"
                loco "Como las leyes de Internet, ¿cierto? Seguro que te has pajeado con la historia del chaval que durmió en casa de una desconocida y al despertar tuvo que llevar al padre y al hermano al fútbol."
                loco "Y encima, cuando vuelvas a casa, seguro que escribes un maldito hilo sobre esta experiencia."
                extend " Pues no lo voy a permitir. Yo a ti te mato."
                loco "¡¡¡TE MATO!!!"
                scene black 
                play sound "blow.ogg"
                scene wasted with dissolve
                play sound "wasted.ogg"
                $ renpy.pause(4, hard=True)
                jump credits
        
        r "Nos quedamos sin conocer el final de la historia."
        pov "Está claro, la chica tenía más rabo que su perro."
        r "¿Existen mujeres así?"
        pov "Eh..."
        show enfermera at center with moveinright
        enfermera "Puede entrar a la consulta. El médico tiene los resultados."
        scene consulta with fade
        $ renpy.pause(1, hard=True)
        show doctor at center with moveinright
        doctor "¿Es usted el señor Rajoy?"
        r "No, Rajao. M. Rajao para los amigos"
        extend " y mamada para los muy amigos."
        doctor "..."
        r "¿No lo he dicho bien, Montoto?"
        r "Es que lo vimos en una película el martes pasado."
        doctor "No importa. He revisado su analítica y he cotejado los resultados con su historia clínica y he llegado a la conclusión de que..."
        extend " tiene..."
        play sound "palmas.mp3"
        $ renpy.pause(5, hard=True)
        r "¡¿Qué tengo?!"
        doctor "Tiene..."
        play sound "palmas.mp3"
        $ renpy.pause(5, hard=True)
        r "Doctor, por favor..."
        doctor "Tiene..."
        play sound "palmas.mp3"
        $ renpy.pause(5, hard=True)
        doctor "Cagalera."
        play sound "ole.mp3"
        $ renpy.pause(6, hard=True)
        r "¿Voy a morir?"
        doctor "Pues ojalá."
        doctor "Quiero decir, que todos lo haremos, eventualmente, pero hoy no le toca."
        doctor "Beba muchos líquidos y repose."
        r "Vamos a tomarnos unos finos a la feria entonces."
        pov "Creo que sería mejor ir directos al gimnasio. El tiempo corre en nuestra contra y hemos perdido mucho tiempo aquí."
        r "Por culpa de tus Ferrero caducados, Montoto."
        montoto "No me culpe, Presidente, que del cátering de la flota de vehículos se encarga el compañero Carromato."
        r "Pues a la calle con él."
        montoto "Superó el ritual de iniciación hace una semana. Ya es fijo."
        pov "Yo voy tirando para el gimnasio."
        r "Espera, vamos contigo."
        scene black with dissolve
        $ renpy.pause(1, hard=True)
        show gymtextse1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextse2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymsevilla with fade
        $ renpy.pause(0.5, hard=True)
        r "¿Quién nos iba a decir que el gimnasio estaba en una caseta de la feria?"
        show cuñadosevilla at center
        r "¡Hombre! Mi amigo el Fósforo. ¿Cómo tú por aquí?"
        fosforo "Es donde vivo, Presidente. Donde no ibas a encontrarme es el norte, con lo siesos que son."
        r "Además de verdad."
        fosforo "Pues mira, llegas en el momento justo. Estoy en mitad de una partida de \"Béticos vs Sevillistas\" y a mi compañero le han expulsado por antideportiva. ¿Te unes?"
        r "Cuenta con ello. Después podemos hablar de..."
        fosforo "Sí, lo de los votos. Esos son tuyos, hombre. Me llegó la circula esta mañana."
        r "Quédate aquí mientras, [jugador]."
        hide cuñadosevilla with moveoutright
        pov "¿Te trajiste el Pronto del hospital?"
        montoto "No, lo siento, no te puedo dar cháchara. Me voy con ellos."
        pov "¿Y por qué no puedo ir yo?"
        montoto "¿Conoces el ritual?"
        pov "¿El qué?"
        montoto "Por eso."
        pov "A ver cómo paso yo el tiempo en la feria..."
        scene black
        show textsep:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymsevilla with fade
        $ renpy.pause(0.5, hard=True)
        montoto "Rápido, [jugador]. Te necesitamos."
        pov "¿Qué queréis ahora?"
        montoto "El Fósforo ha sufrido un vahido y la partida se ha quedado coja. Tienes que cubrir el hueco."
        pov "Seguro que ha dicho esa frase muchas veces en su vida."
        montoto "... "
        extend "Demasiadas."
        scene tablero with fade
        duque "¿Este es el tolai?"
        pov "Tengo nombre."
        duque "Vaya mérito ese. Hasta un perro tiene uno. ¿Tienes acaso un árbol genealógico que se retrotrae 500 años o más?"
        pov "Eso no, pero tengo un rab..."
        r "Sigamos, que ya no queda nada para terminar la partida."
        show finidi at left:
            ypos 0.7
        duque "Ya se ha jugado esta carta. Ahora es tu turno."
        r "Lanza esta."
        show uefa at right:
            ypos 0.7
        pov "Si me dices qué cartas usar, ¿para qué me necesitáis?"
        r "Las reglas dicen que siempre debe de haber dos testigos por si la partida acaba en duelo al amanecer o en una pelea a muerte."
        duque "Béticos vs Sevillistas es un juego para hombres."
        r "Y ahora, nuestra jugada maestra."
        hide uefa
        show monchi at right:
            ypos 0.7
        $ renpy.pause(0.4, hard=True)
        hide finidi with blinds
        duque "Jajajaj, ¡estás donde quería!"
        extend " ¡Llegó tu hora!"
        show lopera at left:
            ypos 0.7
        $ renpy.pause(0.5, hard=True)
        duque "Te has quedado sin cartas. He ganado."
        hide monchi with blinds
        r "El Fósforo no va a estar muy contento..."
        hide lopera with blinds
        montoto "Menos mal que nos dio los votos antes de desmayarse."
        pov "¿Podemos irnos ya?"
        duque "Cuando queráis la revancha, aquí estaré. Bueno, aquí no, en mi palacete de Usera."
        $ puntosj += 3
        
        
        
        
    if ken == True:
  
        scene sevilla1 with fade
        $ renpy.pause(0.5, hard=True)
        show lacasitos at center with dissolve
        lacasitos "Perdonen, ¿han visto a un hombre con perilla y ojos claros de la mano de una niña rubia con rizos y muy pizpireta montada en un patinete de Cars?"
        lacasitos "Les he perdido de vista un momento y no sé dónde se han podido meter."
        k "¡Oh no! ¡Un bote de Lacasitos que habla!"
        k "¡Huyamos!"
        scene caseta1 with fade
        $ renpy.pause(0.5, hard=True)
        k "Por qué poco nos hemos librado."
        pov "No sé a qué viene tanta historia. Si parecía una chica muy simpática."
        k "Soy alérgico al chocolate."
        pov "No tenía ni idea..."
        k "Es un drama porque no puedo usar condones de dicho sabor. Por eso las divorciadas se me resisten."
        pov "Pero, oiga, usted no tiene verguenza."
        k "Ni lo pretendo."
        show portero1 with moveinleft
        $ renpy.pause(0.4, hard=True)
        portero1 "Irse a la mierda a discutir, anda."
        k "Vaya, qué modales."
        pov "Perdone, acabamos de llegar."
        portero1 "Bienvenidos a Andalucía entonces."
        portero1 "Ahora, ¡puerta!"
        k "¿Puedo entrar?"
        portero1 "Depende."
        espejo "¿De qué depende?"
        portero1 "De que esté en la lista."
        pov "¿Y está?"
        portero1 "No me ha dicho su nombre. Tan pronto puede estar como no. Esto es como lo del gato de Chuarcheneger."
        k "Ken Sánchez, gigoló y socialdemócrata."
        portero1 "Mmmm... "
        extend "Aquí está. Bienvenido, señor Sánchez. Su mesa está lista."
        k "Gracias."
        espejo "Me vendrá bien tomarme un fino."
        portero1 "Perdone... lo que sea usted. Pero aquí dice que no lleva acompañante."
        espejo "¡Ken...!"
        k "¿Hay buen género dentro?"
        portero1 "Creo que hay un par de ex del conde Lecquio y muchas borrachas."
        k "Lo siento, reflejo mío. Son las normas."
        pov "Yo mejor ni me molesto."
        portero1 "Me ahorrarías el trabajo, miarma."
        pov "A esperar tocan..."
        extend " ¿Jugamos a los chinos?"
        portero1 "Estoy un poco hasta los cojones de que me confundan. Chino no, japonés."
        pov "¿Jugamos o qué?"
        portero1 "Venga. Solo se cogen 3 monedas."
        portero1 "¿Tú juegas... espejo?"
        portero1 "¿Es un espejo de verdad?"
        pov "A mí también me cuesta asimilarlo."
        portero1 "Peores cosas he visto, desde luego."
        espejo "No puedo jugar. No tengo manos."
        portero1 "Hombre, haber dicho que eras disminuido. Hubieras podido pasar. La Junta nos da una subvención para que os dejemos entrar. Un rato solo, ¿eh?, que la gente normal tiene derecho a no ver cosas raras."
        jump chinos

        
    if coletas == True:

        scene sevilla1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        show lacasitos at center with moveinright
        lacasitos "Perdonen. ¿Han visto a un hombre con perilla y ojos claros de la mano de una niña rubia con rizos y muy pizpireta que iba con un patinete de Cars?"
        lacasitos "Me he puesto a mirar un escaparate de una librería y les he perdido de vista..."
        c "¿Usted es la famosa Lacasitos?"
        extend " ¿La mejor amiga del autor de este juego?"
        lacasitos "No sé de quién me habla."
        lacasitos "¿Ha visto a mi marido y a mi hija o no?"
        c "Se fueron por allí."
        lacasitos "Con sus indicaciones el Dr. Livingstone no se hubiera perdido."
        hide lacasitos with moveoutleft
        c "Según la Guía del Turismo Progresista, el gimnasio está en una de las casetas de la Feria de abril."
        stalin "Estamos en junio. Estará en otra parte."
        c "Recuerda que son sevillanos."
        stalin "Ah, claro..."
        scene caseta1 with fade
        $ renpy.pause(0.5, hard=True)
        stalin "No se vé ningún torero del brazo de una folclórica. ¿Sabes lo que creo?"
        c "Ilumínanos."
        stalin "Que esto no es más que un invento para sacar el dinero a los turistas. Ya la sola idea de una feria que dure tres meses es aberrante. La vida se convertiría en feria y ya nadie trabajaría."
        c "Siempre hay alguien que puede trabajar por ti."
        stalin "Conmigo que no cuenten."
        show portero1 with moveinleft
        $ renpy.pause(0.4, hard=True)
        portero1 "Irse a la mierda a discutir, anda."
        c "Vaya, qué modales."
        pov "Perdone, acabamos de llegar."
        portero1 "Bienvenidos a Andalucía entonces."
        portero1 "Ahora, ¡puerta!"
        c "¿Podemos entrar?"
        portero1 "Depende."
        stalin "¿De qué depende?"
        portero1 "De que esté en la lista."
        pov "¿Y está?"
        portero1 "No me ha dicho su nombre. Tan pronto puede estar como no. Esto es como lo del gato de Chuarcheneger."
        c "El Coletas, referencia e índice de la izquierda."
        portero1 "Mmmm... "
        extend "Lo siento. No puede pasar."
        c "¿Por qué no?"
        portero1 "¿Usted se ha visto el pelo?"
        extend " Láveselo, ¡guarro!"
        pov "¿Nos puede decir al menos si dentro hay un gimnasio?"
        portero1 "Uno muy bonito. Puedes ejercitar los bíceps levantando jarras de cerveza, las piernas bailando sevillanas y en los baños te puedes meter un viaje que ni con una maratón."
        stalin "Detecto cierto sarcasmo."
        portero1 "Las pilla al vuelo el Brus Guilis."
        stalin "Le acabo de incluir en mi lista."
        c "Probemos en aquella caseta."
        scene caseta2 with fade
        $ renpy.pause(0.5, hard=True)
        show portero2 with dissolve
        portero2 "¿Qué queréis?"
        stalin "Buscamos el gimnasio de Sevilla."
        portero2 "Mmmm, pues igual ahí al lado saben algo. En esta caseta solo se sabe de vicio."
        c "¿Podemos entrar?"
        extend " Soy El Coletas, faro y guía de la izquierda."
        portero2 "A ver... "
        extend " Está en la lista pero no puede entrar."
        c "Lo del pelo es cultural. Sigo las tradiciones de la tribu de los Sasoon, que no se lavaban el pelo hasta que no conseguían el puesto de líder de la tribu."
        portero2 "A mi eso me da igual. Es su amigo, que lleva calcetines blancos."
        stalin "¿Algún problema? Si llevamos los calcetines rojos, qué cutres son los comunistas, si los llevamos blancos, quejas también. No hay quien entienda a los capitalistas."
        portero2 "¿Tú eres comunista de esos? ¿De los de la Ursus?"
        stalin "Ursus era el nombre del oso estrella del Circo de Moscú. Tú te refieres a la URSS. Grábatelo a fuego en la mente para cuando volvamos."
        portero2 "Mucho pides, miarma. Llevo dos botellas de manzanilla y acabo de empezar el turno."
        pov "Mientras seguís de cháchara voy a la caseta de al lado a preguntar por lo del gimnasio. Está claro que aquí no es."
        scene caseta3 with fade
        $ renpy.pause(0.5, hard=True)
        pov "Qué raro que no haya portero aquí."
        show sorpresa at center with moveinleft
        sorpresa "Eso es porque estás en la Caseta de la Conferencia Episcopal, aquí son todos bienvenidos, moreno."
        pov "Muchas gracias, hermana."
        sorpresa "No me llames así que no es plan de añadir más pecados a la lista."
        pov "Por ahora no tengo ninguno apuntado."
        sorpresa "Por ahora..."
        stop music
        play sound "alarma.mp3"
        $ renpy.pause(4, hard=True)
        megafonia "Se ha escapado un paciente del ala de psiquiatría del Hospital de La Macarena. Se teme que esté armado y es muy peligroso."
        extend " Si le ve, no le lleve la contraria y espere a que el personal de seguridad se encargue de él."
        sorpresa "Uy, corre que aquí los colgaos tienen mucho malaje."
        hide sorpresa with moveoutright
        show loco at center with moveinleft
        pov "¡Sapristi! ¡El loco!"
        pov "Mierda, espero que no me haya escuchado..."
        loco "Le he oído. Y, sí, no lo niego. ¡Estoy como una regadera!"
        loco "¡¡Leí un hilo en Twitter y me volvi loco!! ¿Pero por qué no se hacen un blog?? ¿Por qué no siguen las leyes de Internet que establecieron sus creadores en 1736?"
        loco "¿Qué les cuesta? Yo entro en Twitter para leer juegos de palabras y criticar al patriarcado y me encuentro con un folletín desnutrido y millones de RT sobre niños rata que viven en Youtube."
        loco "¿No voy a estar loco?"
        loco "¿Quieres saber lo más curioso?"
        menu:
            "Sí":
                loco "1) El martes pasado fui a sacar al perro al jardin a que hiciera sus necesidades, ya que le gusta hacerlo siempre en el mismo sitio."
                loco "2) Y no creáis, sería las once y pico de la noche, porque yo siempre aprovecho cuando termina Cazamariposas para estas cosas."
                loco "3) Pues bien, el perro no pudo hacer nada porque unos obreros habían acordonado la zona y estaban quitando el mobiliario urbano."
                loco "4) Que, claro, yo me quedé todo loco por las horas que eran. Nunca había visto a alguien trabajando tan tarde. Ni los basureros."
                loco "5) Intenté que el perro pasara, así de extranjis, y dejara el recuerdo, pero un obrero salió corriendo con una machota en la mano."
                loco "6) Y tuvimos que salir por patas. Dos calles más allá nos paramos. Miré hacia atrás. No nos perseguía. Tomé un pequeño respiro."
                loco "7) Y me dispuse a volver a casa por otro camino que pasaba delante de un bar. Allí estaba la tía más buena que vi jamás."
                loco "8) Se me acercó y me susurró al oído si quería tomar algo con ella. Yo rechacé su oferta pues mi perro tenía que defecar."
                loco "9) Incomprensiblemente, fue sensible a las necesidades de mi can. Creo que en ese momento me enamoré un poquito."
                loco "10) Fuimos a un parque cercano y mientras el perro añadía un pino a la arboleda local, nos perdimos la chica y yo tras unos matojos."
                loco "11) Y cuando le quité la ropa... No os lo váis a creer. En serio. Pues resulta que..."
                play sound "blow.ogg"
                $ renpy.pause(1, hard=True)
                hide loco with blinds
                megafonia "El paciente ha sido neutralizado con un dardo tranquilizante. Gracias por su comprensión y disculpen las molestias que les hayamos podido ocasionar."
                
            "No":
                loco "¿Cómo que no? ¿Es que no has oído lo que han dicho los altavoces?" 
                loco "Te gusta saltarte la ley, ¿verdad?"
                loco "Como las leyes de Internet, ¿cierto? Seguro que te has pajeado con la historia del chaval que durmió en casa de una desconocida y al despertar tuvo que llevar al padre y al hermano al fútbol."
                loco "Y encima, cuando vuelvas a casa, seguro que escribes un maldito hilo sobre esta experiencia."
                extend " Pues no lo voy a permitir. Yo a ti te mato."
                loco "¡¡¡TE MATO!!!"
                scene black 
                play sound "blow.ogg"
                scene wasted with dissolve
                play sound "wasted.ogg"
                $ renpy.pause(4, hard=True)
                jump credits
        show sorpresa at center with moveinleft
        sorpresa "No te vayas a creer lo que dijo este, ¿eh? Que no llevaba perro cuando me lo encontré."
        sorpresa "Tengo que dejarte. Ha comenzado la hora feliz."
        hide sorpresa with moveoutright
        c "Ya estamos aquí. Venga, no pierdas el tiempo con la juerga que tenemos trabajo que hacer."
        c "El portero hizo buenas migas con Staline y le ha dicho dónde encontrar el gimnasio."
        stalin "Incluso se ha apuntado al partido. Pringado..."

        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextse1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextse2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymsevilla with fade
        show cuñadosevilla at center
        c "¡Hola!"
        fosforo "Dios, qué asco: ¡El Coletas!"
        stalin "Esto me recuerda a la última reunión de la directiva del partido."
        fosforo "Encima vienes cuando estoy en mitad de una partida de \"Béticos vs Sevillistas\"."
        stalin "¿Eso qué es?"
        c "¿Estás de broma? Es la última creación de GamePark, un juego de cartas en el que se enfrentan dos jugadores, cada uno representando a los equipos de la capital andaluza."
        fosforo "¡Caramba! Voy a tener que cambiar mi opinión interesada sobre ti, pero solo un poco."
        fosforo "Mira, te propongo algo. A mi compañero le han expulsado por antideportiva. Si me ayudas a ganar, te daré mis votos."
        c "Trato hecho."
        stalin "Sabía que en este país sois unos ludópatas sin parangón, pero esto ya es demasiado."
        c "Quédate aquí mientras, [jugador]."
        hide cuñadosevilla with moveoutright
        pov "A ver cómo paso yo el tiempo en la feria..."
        scene black
        show textsep:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymsevilla with fade
        $ renpy.pause(0.5, hard=True)
        stalin "Rápido, [jugador]. Te necesitamos."
        pov "¿Qué queréis ahora?"
        stalin "El Fósforo ha sufrido un vahido y la partida se ha quedado coja. Tienes que cubrir el hueco."
        pov "Seguro que ha dicho esa frase muchas veces en su vida."
        stalin "... "
        stalin "¿Tú eres gilipollas o qué?"
        scene tablero with fade
        duque "¿Este es el tolai?"
        pov "Tengo nombre."
        duque "Vaya mérito ese. Hasta un perro tiene uno. ¿Tienes acaso un árbol genealógico que se retrotrae 500 años o más?"
        pov "Eso no, pero tengo un rab..."
        c "Sigamos, que ya no queda nada para terminar la partida."
        show finidi at left:
            ypos 0.7
        duque "Ya se ha jugado esta carta. Ahora es tu turno."
        c "Lanza esta."
        show uefa at right:
            ypos 0.7
        pov "Si me dices qué cartas usar, ¿para qué me necesitáis?"
        c "Las reglas dicen que siempre debe de haber dos testigos por si la partida acaba en duelo al amanecer o en una pelea a muerte."
        duque "Béticos vs Sevillistas es un juego para hombres."
        c "Y ahora, nuestra jugada maestra."
        hide uefa
        show monchi at right:
            ypos 0.7
        $ renpy.pause(0.4, hard=True)
        hide finidi with blinds
        duque "Jajajaj, ¡estás donde quería!"
        extend " ¡Llegó tu hora!"
        show lopera at left:
            ypos 0.7
        $ renpy.pause(0.5, hard=True)
        duque "Te has quedado sin cartas. He ganado."
        hide monchi with blinds
        c "El Fósforo no va a estar muy contento..."
        hide lopera with blinds
        stalin "Menos mal que nos dio los votos antes de desmayarse."
        pov "¿Podemos irnos ya?"
        duque "Cuando queráis la revancha, aquí estaré. Bueno, aquí no, en mi palacete de Usera."
        $ puntosj += 3
        
    
    jump mapa