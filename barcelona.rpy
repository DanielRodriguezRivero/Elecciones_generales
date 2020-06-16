init python:
    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play("prueba.ogg", channel="sound", loop="True")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")




label barcelona:
    $ barcelona = True
    
    define policia = Character("Asuntos Internos", color="#0922A1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define carme = Character("La Carme", color="#A10992", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define perroflauta = Character("Perroflauta Representativa", color="#A14B09", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define kebabd = Character("Tarik, el pakistaní feliz", color="#936641", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define pikachu= Character("Pikachu", color="#EABD54", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define charmander= Character("Charmander", color="#A4503B", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define squirtle= Character("Squirtle", color="#2AA7C0", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define fle= Character("Fleflis", color="#DCCE14", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define comicguy = Character("Durán i Mérida", color="#1FB71F", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    if ceuta == False:
        $ enta = False
    
    image gymbarna = "images/gymbarna.jpg"
    image kebab = "images/kebab.jpg"
    image kebabd = "images/kebabd.png"
    image barna1 = "images/barna1.jpg"
    image barna2 = "images/barna2.jpg"
    image carcel = "images/celda.jpg"
    
    image cuñadobarna = "images/perroflauta.png"
    image buenorra = "images/buenorra.png"
    image comicguy = "images/comicguy.png"
    image polibarna = "images/policia.png"
    image pokemon = "images/pokemon.png"
    image carmepic = "images/carme.png"
    image fle = "images/fle.png"
    image ripley = "images/ripley.png"
    image tarik = "images/tarik.png"
    
    image gymtextbar1 = Text("{size=40}Gimnasio Ignaci",color="#fff", text_align=0.3)
    image gymtextbar2 = Text("{size=40}Baixant de la font del gat",color="#fff", text_align=0.3)
    scene travelbarna at Pan((0, 0), (320,0), 20.0)
    play music "entradillabarna.mp3"
    $ renpy.pause(18, hard=True)
    
    if enta == True:
        stop music
        play sound "sirena.mp3"
        scene barna1 with fade
        $ renpy.pause(3, hard=True)
        show polibarna at center with dissolve
        policia "¡Deténgase! Queda detenido por ayudar al famoso terrorista internacional, Pin Laden."
        pov "¡Nosotros no tenemos nada que ver con ese señor!"
        policia "¿Y ese paquete que llevan?"
        pov "Me alegra que se fije en él. Sin relleno de ningún tipo, ¿eh?"
        extend " Toque, toque."
        policia "No se haga el gracioso. Estoy hasta el gorro del chiste del paquete."
        policia "Y no me venga con que si le voy a meter uno bien grande y duro porque no me hace gracia."
        pov "No sé a qué se refiere."
        policia "¿Niega que Pin Laden le diera un paquete para su primo Omar?"
        pov "No, pero nos dijo que solo contiene inofensivos ingredientes gastronómicos."
        policia "Eso no se lo cree ni el que asó la manteca. A la trena con vosotros. Asco me dais."
        policia "Tu aventura termina aquí."
        scene carcel with fade
        play sound "portazo.mp3"
        $ renpy.pause(1, hard=True)
        pov "Quién me mandaría a mí relacionarme con políticos..."
        pov "En fin, al menos podré dedicarme a licenciarme en Derecho sin gastarme un solo duro."
        jump credits
        
    play music "cancionciudad.mp3"
    
    if mrajao == True:
        scene barna2 with fade
        $ renpy.pause(1, hard=True)
        r "Se me ha hecho un poco largo el viaje."
        extend " Me ha extrañado que no hayas atravesado el famoso puente aéreo Madrid - Barcelona."
        montoto "Es un puente metafórico, Presidente."
        r "Estos catalanes, qué ganas de dar la nota tienen siempre."
        r "En fin, tengo hambre. ¿Habrá por aquí algún sitio donde comer tortilla de patatas?"
        montoto "Eso es demasiado español. Seguro que lo tienen prohibido, como los toros y Lola Flores."
        r "Pues ensaladilla rusa. Los de la Generalidad no tienen nada contra los rusos, ¿no?"
        montoto "Me temo que la ensaladilla es española también."
        r "¿Pero qué me estás contando, Montoto? ¿Ya te quieres ahorrar el dinero de la comida? Puede que no sepa distinguir entre el aceite y el vinagre, pero \"rusa\" viene de Rusia."
        montoto "Sí, pero es que el español que la inventó la llamó de esa manera porque la mahonesa parece nieve y tal."
        r "Mira, no puedo con este país."
        pov "¿Cataluña o España?"
        r "¡Vete a la mierda!"
        show carmepic at center with moveinright
        $ renpy.pause(0.5, hard=True)
        carme "Estos españoles y su educación primitiva y retrógrada cuajada de descalificaciones..."
        r "También tengo para ti, ¿eh? Y en tu dialecto de paletos."
        carme "¿Tú? Si seguro que no sabes ni cómo se dice miércoles en catalán."
        r "Se dice dimercromina. Razna me dio clases en la intimidad de su sótano cuando era su Ministro de Interior."
        pov "¿Quién?"
        r "Razna el grande, el mayor mago que haya salido de las planicies centrales. Con un meneo de su bigote podía hacer que los gatos le hablaran y una vez convirtió la sopa de ajo en vino."
        montoto "Perdónale, es que si no come se le va la cabeza."
        carme "Pfff... Pueblerinos."
        hide carmepic with moveoutleft
        $ renpy.pause(0.5, hard=True)
        r "Montoto."
        montoto "Díme, Presidente."
        r "Sigo teniendo hambre."
        pov "Conozco un kebab por aquí cerca."
        r "¿Qué es un kebab?"
        pov "Básicamente, carne con verduras y salsa picante."
        r "Cielos, ¡qué innovador!"
        extend " Lléveme allí antes de que sufra un vahido."
        scene kebab with wipeup
        $ renpy.pause(1, hard=True)
        show fle at right
        show ripley at center
        fle "Dígame, ¿cuánto es?"
        kebabd "Dos rupias y media cabra."
        fle "Qué cachondo, Tarik. Venga, dime lo que te debo o te doy un makiwara que te van a temblar las orejas."
        kebabd "Cinco euros."
        r "Es la primera vez que veo a una señora mayor disfrazada en lugar de su hija."
        fle "¿A quién estás llamando señora mayor?"
        r "Disculpe, señorita, era una simple formalidad."
        extend " ¿De quién se supone que copia el atuendo?"
        fle "Alguien a quien no conoces, seguro."
        fle "Y por cierto, mi hija sí va disfrazada."
        extend " Es un rollo conceptual. Como te pases de listo, le echa los cojones que le echaba Ripley contra la Reina Alien y te escamocha."
        r "Caray... una republicana."
        fle "Y así, además, todo el mundo puede ver lo guapa que es."
        fle "Nos vamos que se nos hace tarde y luego hay mucha cola para entrar en la ComiCon."
        hide ripley with moveoutleft
        hide fle with moveoutleft
        $ renpy.pause(0.5)
        show tarik at center
        $ renpy.pause(0.5)
        kebabd "¿Qué va a ser?"
        r "Dos kebab."
        kebabd "Sí, eso ya imaginar. No venir a pedir paella aquí."
        r "[jugador], ¿qué pido?"
        pov "Tres kebabs mixtos con poco picante. Uno sin cebolla, ¿no, Montoto?"
        montoto "No, no. Yo no como. Me alimento de las lágrimas de los autónomos."
        pov "Que sean dos entonces."
        kebabd "Marchando."
        hide tarik with moveoutleft
        pov "Después de comer iremos directos al gimnasio."
        r "Me parece bien. No quiero que la independencia me pille aquí."
        scene black with dissolve
        show gymtextbar1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbar2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymbarna with fade
        show cuñadobarna at center
        perroflauta "¿Otra vez dando por saco? He dicho mil veces que aquí no hay bichos de esos."
        extend " ¿No sabéis leer un triste cartel?"
        perroflauta "Guardad el móvil e idos a cazar Pichamenos a vuestra casa."
        r "Perdone, señorita. Creo que ha habido una equivocación. No tengo la más mínima idea de a qué se refiere."
        perroflauta "¿Ah, no?"
        r "No."
        perroflauta "¿Seguro?"
        r "Totalmente."
        perroflauta "¿Y entonces?"
        montoto "Verá, como usted sabrá si ve la tele a menudo..."
        perroflauta "No tengo tele. El único aparato que poseo... en fin, que no la veo."
        montoto "Pero estará usted al corriente de la actualidad política nacional."
        perroflauta "¿De la de Cataluña? Sí, claro. Ringo parece que se mantiene a flote, aunque yo creo que es porque Mccartney le controla desde la sombra. Ya sabes, como la Comisión Europea hace con M. Rajao."
        r "¡Pero si ese soy yo!"
        perroflauta "¿M. Rajao?"
        r "Sí."
        perroflauta "¿El mismo M. Rajao que dijo, y cito textualmente: Cataluña es un gran país, dentro de un gran país que es España, dentro de otro país que es la Unión Europea, dentro de otro país llamado Tierra, dentro de otro país llamado Franquilandia.?"
        r "El mismo."
        perroflauta "No le había reconocido. Me lo imaginaba más... alto."
        r "Es que hoy no llevo alzas, como tengo que andar mucho y no tengo costumbre, no quiero sufrir rozaduras incómodas."
        perroflauta "¿Y qué se le ha perdido por aquí?"
        r "[jugador], explícaselo."
        pov "Que si les das tus tres votos, te lo agradece."
        perroflauta "Pues no soy yo mucho de apuntalar el sistema con una papeleta, pero tengo cita con la esteticién y como llegue tarde igual les han desalojado del hogar social."
        perroflauta "Si me vigilas el chiringo un rato, te votaré."
        r "Delo usted por hecho."
        perroflauta "Os dejo entonces."
        extend " Si vienen los pesados esos de los teléfonos, no dejéis que toquen nada."
        hide cuñadobarna with moveoutright
        r "No sabía que aquí precisamente tuviera tan fácil conseguir votos."
        show pokemon with moveinright
        pikachu "¡Mirad, colegas! Tenemos un premio gordo."
        pikachu "¡Hemos pillado a un corruptino, un homini nocturno y un gilipollas!"
        charmander "Deja al gilipollas que ya tenemos muchos."
        squirtle "Y corruptinos también."
        charmander "Sí, pero esos valen el triple."
        r "Se equivocan, jóvenes. Somos los líderes políticos del ayer y del mañana."
        pikachu "¿Qué me estás contando? A la bola, corruptino."
        pov "A ver, chavales. Largaos o llamo a vuestras madres."
        squirtle "Vaya con el tío baranda..."
        hide pokemon with moveoutright
        montoto "Tendríamos que haber traído camisetas. Estos son nuestros futuros votantes. Están en la edad propicia para captarlos."
        show cuñadobarna with moveinleft
        perroflauta "Demasiado tarde. Cuando he llegado los Mossos estaban afilando las porras. Tendré que buscar otra que me arregle el matojo."
        perroflauta "Como soy una mujer de palabra, aquí tienes mis votos."
        perroflauta "¿Habéis tenido algún problema?"
        r "Ninguno. Ha ido todo como la seda."
        perroflauta "Entonces, ¡nos vemos!"
        $ puntosj +=3
        hide gymbarna with dissolve
        
    if ken == True:
        
        scene barna2 with fade
        $ renpy.pause(0.5, hard=True)
        show buenorra at left with moveinright
        hide buenorra with moveoutleft
        k "¡Oh no!"
        k "¡Es demasiado tarde! La modernidad ha llegado a Barcelona antes de que los socialistas pudieran estar a la vanguardia."
        pov "Ah, ¿pero hay gente suficiente como para que estéis en cabeza de algo que no sea la cola de la pescadería?"
        k "El PRESOE es un partido con una gran masa social..."
        pov "¿Por eso ha tenido que acompañarte tu espejo?"
        k "Es que todos los militantes están en Andalucía."
        espejo "De vacaciones."
        k "Dejémonos de historias. Empiezo a tener hambre."
        pov "Pues a ver dónde encontramos un sitio decente por aquí."
        espejo "Preguntemos a ese joven que viene."
        show comicguy at center with moveinleft
        $ renpy.pause(0.5, hard=True)
        k "Perdone..."
        comicguy "Este es el peor videojuego-barra-novela visual-cosa cutre digital a lo que he jugado jamás. Debería darle verguenza a su autor, si es que este la conservara después de haber enviado fotos de su miembro a todo su TL en Twitter."
        k "Ya, pero yo quería saber sí..."
        comicguy "Dos manzanas al este tienen un kebab. Díganle que van de parte de Muammar Gadaffi."
        k "¿Nos harán un descuento?"
        comicguy "No, me reiré un buen rato."
        hide comicguy with moveoutleft
        k "No dejemos que este desagradable encuentro enturbie nuestra opinión sobre los catalanes."
        pov "¿Y cual es?"
        espejo "Arreando que tengo hambre."
        scene kebab with wipeup
        $ renpy.pause(1, hard=True)
        show fle at right
        show ripley at center
        fle "¿Dígame cuánto es?"
        kebabd "Dos rupias y media cabra."
        fle "Qué cachondo, Tarik. Venga, dime lo que te debo o te doy un makiwara que te van a temblar las orejas."
        kebabd "Cinco euros."
        k "Es la primera vez que veo a una señora mayor disfrazada en lugar de su hija."
        fle "¿A quién estás llamando señora?"
        k "Disculpe, señorita, era una simple formalidad."
        k "¿De quién se supone que está vestida?"
        k "Y lo más importante: ¿está usted soltera?"
        fle "Alguien a quien no conoces, seguro."
        fle "No, estoy recién casada, para su desgracia."
        fle "Y por cierto, mi hija sí va disfrazada."
        extend " Es un rollo conceptual. Como te pases de listo, le echa los cojones que le echaba Ripley contra la Reina Alien y te escamocha."
        k "Una compañera republicana... Se me saltan las lágrimas."
        fle "Y así, además, todo el mundo puede ver lo guapa que es."
        fle "Nos vamos que se nos hace tarde y luego hay mucha cola para entrar en la ComiCon."
        hide ripley with moveoutleft
        hide fle with moveoutleft
        $ renpy.pause(0.5)
        show tarik at center
        kebabd "¿Qué van a tomar los señores?"
        k "¿Puedo darle un abrazo?"
        kebabd "¿Así en frío?"
        extend " ¿Acaso le gusto?"
        kebabd "Sabe lo que hacemos a la gente así en mi tierra, ¿no?"
        k "Es para sentir la distancia que ha recorrido su alma hasta llegar hasta aquí."
        kebabd "Esa fue la excusa que puso Kemal cuando le pillaron los ancianos del pueblo."
        extend " Una pista: no se libró."
        kebabd "¿Van a comer algo o van a continuar haciéndome perder el tiempo?"
        kebabd "A comer algo del restaurante, que le veo las intenciones."
        pov "Un shawarma con doble de picante."
        k "Yo longaniza."
        kebabd "No tener."
        k "¿Un frankfurt?"
        kebabd "Acabarse justo ayer."
        k "¿Salami en barra?"
        kebabd "Esto ser ya un poco vergonzoso."
        pov "Dele una botella de agua y ya está."
        hide tarik with dissolve
        pov "No se puede ir a ninguna parte contigo."
        k "¡Pero si ha empezado él!"
        scene black with dissolve
        show gymtextbar1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbar2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymbarna with fade
        show cuñadobarna at center
        perroflauta "¿Otra vez dando por saco? He dicho mil veces que aquí no hay bichos de esos."
        extend " ¿No sabéis leer un triste cartel?"
        perroflauta "Guardad el móvil e iros a cazar pichamenos a vuestra casa."
        k "Perdona, guapa. Es que me alegro mucho de verte."
        extend " Mucho."
        perroflauta "Mi madre me enseñó que no debo de fiarme de las alegrías de los desconocidos pues puede que sea a costa de mi bienestar."
        k "Pero es que yo no soy un sátiro desconocido."
        extend " Me llamo Ken Sánchez y he venido aquí a amarte o a que me hagas presidente."
        perroflauta "Ninguna de las dos opciones me atrae demasiado, aunque si he de escoger, elijo darte los votos que atesoro."
        k "Una sombra cubre mi corazón pero he de aceptar la negativa a mi proposición..."
        perroflauta "Eso sí, me tenéis que hacer el favor de cuidar del local un rato mientras me hacen la permamente en la peluquería."
        perroflauta "Espero llegar a tiempo antes de que los Mossos desalojen el edificio. Baya de oro es la mejor estilista del pueblo libre de toda la comarca."
        k "Cualquier cosa es poca con tal de verla sonreir."
        pov "Y las tetas."
        k "No hacía falta que verbalizaras lo que todos estamos pensando."
        perroflauta "Me marcho. Será cosa de una hora, o incluso menos."
        extend " Ah, no dejéis que entren los pesados esos de los móviles, ¿vale?"
        espejo "Descuide."
        hide cuñadobarna with moveoutleft
        k "No os voy a engañar, hubiera preferido yacer con ella sobre el potro. Quizá más adelante..."
        $ renpy.pause(0.5, hard=True)
        show pokemon with moveinleft
        pikachu "¡Mirad, colegas! Tenemos un premio gordo."
        pikachu "Tenemos un muñeco de acción con sus complementos y el típico gilipollas que siempre te aparece para rellenar, como los garbanzos en el revuelto de frutos secos."
        charmander "Bah, déjalos. No valen para nada."
        k "Os equivocáis, jóvenes. Somos los líderes políticos del hoy y del mañana."
        pikachu "¿Qué me estás contando? A la bola, muñeco."
        pov "A ver, chavales. Largaos o llamo a vuestras madres."
        squirtle "Vaya con el tío baranda..."
        hide pokemon with moveoutright
        montoto "Tendríamos que haber traído camisetas. Estos son nuestros futuros votantes. Están en la edad propicia para captarlos."
        show cuñadobarna with moveinleft
        perroflauta "Demasiado tarde. Cuando he llegado los Mossos estaban afilando las porras. Tendré que buscar otra que me arregle el matojo."
        perroflauta "Como soy una mujer de palabra, aquí tienes mis votos."
        perroflauta "¿Habéis tenido algún problema?"
        k "Ninguno. Ha ido todo como la seda."
        perroflauta "Entonces, ¡nos vemos!"
        k "¿Puedo dejarle mi número de teléfono?"
        perroflauta "Como quieras. De todas formas yo me comunico con el sonido de la brisa del estío."
        $ puntosj += 3
        
    if coletas == True:

        scene barna2 with fade
        $ renpy.pause(0.5, hard=True)
        c "Tengo hambre."
        stalin "Pareces un niño pequeño. El camarada Lenin estuvo 5 años sin comer y no se quejó tanto."
        c "Eso no es del todo así."
        stalin "Cierto, Se alimentaba con las lágrimas de los burgueses, pero estas no tenían valor nutritivo, este residía en la grasa de sus estómagos flácidos y capitalistas."
        c "Conectemos con la Progrepedia para conocer los mejores restaurantes alternativos de la ciudad."
        c "Supongo que no hace falta que explique qué es la Progrepedia, ¿verdad?"
        stalin "Me ofendes. La redactó mi equipo de propaganda subversiva."
        pov "Estoy familiarizado con ella, sí."
        c "Bien, veamos qué tenemos por aquí..."
        extend " La batucada Vegana... "
        extend " La vaca deshauciada..."
        extend " too much." 
        extend "Kebab Abdul..., mira, este tiene un nombre normal."
        show buenorra at left with moveinright
        hide buenorra with moveoutleft
        stalin "¿Qué ha sido eso?"
        c "Parecía un cuerpo humano del género femenino contoneándose de camino a un afortunado destino."
        pov "Casi se diría que ha aparecido solo por estar buena."
        c "Por favor, no digas tonterías. Eso nunca pasaría en una historia como esta."
        show comicguy at center with moveinleft
        $ renpy.pause(0.5, hard=True)
        comicguy "No solo es posible sino que ya ocurrió en la novela visual \"La casa de Marianela\", un mash-up que el autor de este mismo juego pergeñó hará cerca de un lustro."
        comicguy "En dicha aberración, reunió en una mansión a cinco conejitas de Playboy recitando a Lorca y Benito Pérez Galdós mientras se introducían dildos con diferentes formas y tamaños."
        comicguy "Pese a lo que pudiera parecer, el resultado fue aceptablemente estético y de buen gusto, aunque literariamente era aberrante."
        stalin "¿Y dónde dices que se puede descargar?"
        pov "Vale, ¿y a nosotros qué nos importa eso?"
        comicguy "Ya salió el señorito \"soy especial porque no me gusta la fantasía ni la sci fi ni esas cosas de frikis\". Pues que sepas que dentro de 10 años habrá un presidente friki en la Moncloa."
        c "Ese puedo ser yo si me das tu voto."
        comicguy "Lo siento. Yo voto a Kodos."
        hide comicguy with moveoutleft
        c "No dejemos que este desagradable encuentro enturbie nuestra opinión sobre los catalanes."
        pov "¿Y cual es?"
        stalin "Por mi parte, los odio por igual, como a todas las nacionalidades."
        scene kebab with wipeup
        $ renpy.pause(1, hard=True)
        show fle at right
        show ripley at center
        fle "¿Dígame cuánto es?"
        kebabd "Dos rupias y media cabra."
        fle "Qué cachondo, Tarik. Venga, dime lo que te debo o te doy un makiwara que te van a temblar las orejas."
        kebabd "Cinco euros."
        c "¡Qué disfraz más conseguido de Deedlit!"
        c "Lo que no consigo adivinar es de qué va tu hija..."
        fle "¿No está claro? De la Teniente Ripley."
        c "Mmmm..."
        stalin "¿Dónde está su uniforme?"
        c "Por muchas vueltas que le doy, no consigo pillarlo."
        fle "Es un rollo conceptual. Como te pases de listo, le echa los cojones que le echaba Ripley contra la Reina Alien y te escamocha."
        stalin "Seguro que sería una buena francotiradora."
        fle "Y así, además, todo el mundo puede ver lo guapa que es."
        fle "Nos vamos que se nos hace tarde y luego hay mucha cola para entrar en la ComiCon."
        hide ripley with moveoutleft
        hide fle with moveoutleft
        $ renpy.pause(0.5)
        show tarik at center
        kebabd "¿Qué van a tomar los señores?"
        c "Un kebab de pollo en pan durum con mitad de salsa de yogur y sin lechuga."
        stalin "Yo una patata hervida y una botella familiar de vodka."
        kebabd "Lo siento. Nos hemos quedado sin patatas."
        stalin "Pues entonces una cerveza sin alcohol."
        stalin "Siempre me pasa lo mismo."
        c "¿Tú no quieres nada?"
        pov "¿Invitáis vosotros?"
        stalin "Jajajajajaj"
        c "Jajaajajja"
        pov "Entonces, no."
        hide tarik with dissolve
        c "A ver, no me malinterpretes. Por mi, te invitaría, pero en las condiciones del crowdfunding con el que fundamos \"Queremos\" no se especificaba las comidas de confraternización."
        stalin "Ni el pago de prostitutas para altos ejecutivos de multinacionales. Un error. No podremos convencerles de nada si no tenemos a una esforzada ciudadana del este lamiéndoles el sable."
        pov "La alta política puede ser fascinante a veces."
        scene black with dissolve
        show gymtextbar1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextbar2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymbarna with fade
        show cuñadobarna at center
        perroflauta "¿Otra vez dando por saco? He dicho mil veces que aquí no hay bichos de esos."
        extend " ¿No sabéis leer un triste cartel?"
        perroflauta "Guardad el móvil e iros a cazar pichamemos a vuestra casa."
        c "¿Es que ya no se reconoce a un camarada cuando se le tiene cerca?"
        perroflauta "¡Pero si eres tú!"
        c "Sí, soy yo."
        perroflauta "¿Seguro?"
        c "Tan seguro como que el rojo es mi color favorito."
        perroflauta "¡Venga ya!"
        c "En serio."
        stalin "Tírale de la coleta si no le crees. Lo hace todo el mundo."
        stalin "Creo que obtiene cierto placer sexual cuando se lo hacen. Por eso yo no me acerco a su pelo nunca."
        perroflauta "¡Si eres clavadito a tu foto en la Progrepedia!"
        stalin "Ese es el objetivo de la fotografía."
        perroflauta "¿Qué puedo hacer por ti?"
        c "Necesitamos que nos des tus votos para hacer de este país una República artist-dogs friendly."
        perroflauta "Dalo por hecho."
        perroflauta "¿Puedo hacer algo más por ti?"
        c "Te dejo que te saques un selfie conmigo si quieres."
        stalin "A veces me pregunto: ¿vale la pena intentar dominar este mundo de frivolidad perpetua?"
        pov "Yo prefiero pasar el tiempo comiendo helado, pero allá cada cual."
        stalin "Sí, eso me dije cuando me uní al movimiento."
        perroflauta "Oye, una cosa sí que te voy a pedir, ¿me podrías echar una mano"
        c "Por una compañera del Círculo Psicodélico, lo que sea."             
        perroflauta "Gracias, amor. ¡Si es que nos tienes locas!"
        perroflauta "Me voy antes de que los Mossos desalojen la peluquería."
        extend " Si entran los pesados esos de los móviles, no dejéis que toquen nada."
        perroflauta "¡Chaito!"
        hide cuñadobarna with moveoutleft
        $ renpy.pause(0.5, hard=True)
        show pokemon with moveinright
        pikachu "Hemos pillado a otro gilipollas, a un coleta morada y a un... ¡camarada comunista!"
        stalin "¿Cómo? unos verdaderos heroes socialistas por estas tierras? me voy con vosotros a hacer la revolucion mundial."
        squirtle "Asé se habla, camarada."
        c "¿Nos vas a dejar de buenas a primeras?"
        stalin "Afróntalo, nunca tuviste ninguna posibilidad..."
        $ puntosj += 3
        hide gymbarna with dissolve
    $ yausado = False
    jump mapa