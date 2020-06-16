label torrelavega:
    $ torrelavega = True
    
    #personajes
    define revilla = Character("Rebilla", color="#031DA0", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define vaca = Character("Ramón Colmenar", color="#BDDCC1", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define lauris = Character("Lauris", color="#BF4E32", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    #imagenes
    image gymtorre = "images/gymtorre.jpg"
    image prado = "images/prado.jpg"
    image torre2 = "images/torre2.jpg"
    image torre1 = "images/torre1.jpg"
    
    image cuñadotorre = "images/revilla.png"
    image vaca = "images/cow.png"
    image lauris = "images/lauris.png"
    
    image gymtextto1 = Text("{size=40}Gimnasio Telémaco",color="#fff", text_align=0.3)
    image gymtextto2 = Text("{size=40}Piernas como columnas Dóricas",color="#fff", text_align=0.3)
    
    scene travelvega at Pan((0, 0), (300,0), 20.0)
    play music "entradillavega.mp3"
    $ renpy.pause(14, hard=True)
    
    play music "cancionciudad2.mp3"
    
    if mrajao == True:
      
        scene torre2 with fade
        $ renpy.pause(0.5, hard=True)
        show lauris at center with moveinright
        r "Perdone, joven, ¿sabe por dónde queda el prado?"
        lauris "Sí, ahí al lado de Bilbado, jaajajja."
        montoto "Creo que se ha reído de nosotros, pero no estoy muy seguro."
        lauris "Lo siento, pero tenía que decirlo. Es algo típico de aquí, como los sobaos y lo buena que estoy."
        lauris "¿Tenéis en mente algún prado en especial? Aquí hay muchos."
        r "Buscamos el lugar donde está el gimnasio local."
        lauris "Ah, es fácil de llegar allí."
        lauris "Girad a mano derecha, seguid recto hasta la rotonda, luego a la izquierda hasta que veáis una estatua de unas manos agarrando un globo terráqueo "
        extend " Y ya desde ahí, llamáis a un taxi para que os lleve."
        r "..."
        pov "Gracias, señorita. Nos ha sido de mucha ayuda."
        lauris "A mandar."
        extend " Ah, y si queréis hacer un regalo al bebé de vuestros amigos, buscad a Doña Pito Piturra. No os fallará."
        hide lauris
        r "Qué chica más enigmática."
        montoto "Pero tenía algo..."
        pov "Un buen par de te..."
        r "En marcha. Id buscando suelto para llamar al taxi y rezad para que encontremos una cabina, de lo contrario te tendrás que transformar y buscar uno, Montoto."
        montoto "Ni hablar, que luego los viejos me tiran piedras porque piensan que transmito el ébola."
        scene prado with dissolve
        $ renpy.pause(1, hard=True)
        pov "Fue una suerte que hubiera un taxi junto a la estatua."
        r "Y que lo digas, aunque no sé si nos habrá traído al sitio correcto. Por aquí no se ve nada más que campo y una estúpida vaca."
        show vaca at center with dissolve
        vaca "Oiga, un respeto."
        montoto "¡Una vaca que habla! No metafórica, quiero decir."
        vaca "No soy una vaca. Los animales no hablan. Un poco de seriedad."
        vaca "Me llamo Ramón y soy un actor."
        r "Un actor que hace de vaca..."
        vaca "Es usted muy sagaz."
        extend " Hace un par de años un virus acabó con gran parte de las vacadas de la región."
        vaca "Fue un desastre porque uno de sus atractivos turísticos eran precisamente las vacas."
        vaca "Sobre todo chinos que pensaban que \"La vaca que ríe\" era de aquí, cuando es de Suiza."
        r "Como todo lo bueno."
        vaca "Así que el gobierno autonómico decidió tomar cartas en el asunto y contrato a varios actores para que nos enfundaramos en estos trajes vacunos y dieramos un poco de color a los prados y los montes."
        r "Debe de ser un trabajo duro."
        vaca "A veces, aunque tiene sus recompensas. De vez en cuando alguna turista intenta ordeñarte. Esos días, vuelvo a casa contento."
        pov "Me alegro de ser intolerante a la lactosa."
        r "¿Sabe dónde queda el gimnasio?"
        vaca "Detrás de esa loma. No tiene pérdida."
        vaca "Ah, y a ver si bajan el IVA cultural, que lo de vaca está bien, pero me gustaría trabajar algún día con José Luís Moreno y al precio que está el cine no va nadie."
        r "Se ha...rá lo q...ue se pueda..."
        hide vaca with moveoutleft
        r "¡Creo que estoy hiperventilando! ¡Hemos sobrevivido al contacto con uno de los de \"la ceja\""
        r "No siento las piernas. Vámonos antes de que le de por volver."
        scene black with dissolve
        show gymtextto1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextto2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymtorre with fade
        show cuñadotorre at center
        revilla "¡Hombre! ¿A quién tenemos aquí? A tres ilustres señores que han venido a esta bendita tierra."
        r "Mucho gusto."
        revilla "¿Qué tal? ¿Cómo ha ido el viaje? Aquí las comunicaciones son excelentes. Unas carreteras como pocas hay en este país. Y todo muy bien señalizado, que es imposible perderse."
        revilla "Si es que ya lo digo yo siempre: ¿para qué te vas a ir a otro lado pudiendo venir a Cantabria?"
        revilla "Hay otros sitios: El Vaticano, Madagascar, Cancún, pero a ver dónde metes tú a las vacas en Cancún."
        extend " Y allí no hay pastos para que se alimenten. Ni siquiera... No me voy a permitir la licencia porque un caballero no habla de eso pero es que ya no se lleva el matojo agreste."
        revilla "No sé si me explico."
        r "Pues me he perdido un poco..."
        revilla "No se preocupe. Es la edad."
        revilla "No le estaré haciendo perder el tiempo, ¿verdad?"
        menu:
            "Para nada.":
                pass
            "Hombre, pues yo venía...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                r "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                r "Como se ha puesto por nada."
                montoto "Lo peor es que no hemos ganado un solo voto."
                r "Nadie dijo que fuera a ser fácil."
                jump mapa

        revilla "Pues me acabo de acordar, que iba yo en el taxi con el Rey un día"
        extend " (el de verdad, no el de ahora)"
        extend " y me fijé en su cabeza de pronto. Entonces, me quedo así mirándolo un rato y el Rey veo que se inquieta y me grita: Micky coño, que me estás poniendo nervioso." 
        revilla "Así, muy campechano. Y yo le dije: Perdone, majestad, pero tiene usted una frente que sería el orgullo de los cabezaconos. Y él, muy campechanamente, se echó a reír." 
        revilla "El pakistaní que iba a los mandos del vehículo no se enteró de nada y eso que tenía la hebra puesta, porque no siempre se lleva a un miembro de la realeza y a un Revilla en el coche, pero el pobre, en su salvajismo no sabía de qué estaba hablando."
        revilla "Luego cuando dejamos al Rey en el pub estuve charlando con él un rato. Me dijo que se llamaba..."
        extend " ¿Cómo me dijo?... "
        revilla "Rashid Japurt y que venía de un pueblecito pesquero llamado... no me acuerdo, pero le pregunté que si tenían anchoas por allí. ¡Y no tenían! Claro que aunque las hubieran tenido, seguro que tan buenas como las de Santoña no iban a ser."
        revilla "¿Quieres unas?"
        menu:
            "No me vendrían mal":
                revilla "Claro que no, hombre."
                revilla "Ten."
            "Mejor no":
                revilla "¿Cómo?"
                extend " ¿Me rechazas unas anchoas de primera calidad por las que el mismo Elvis Presley dijo que dejaría las drogas?"
                revilla "Corre lejos de aquí que no quiero saber nada de los de vuestra calaña. Os va a votar las vacas del Prao."
                hide cuñadotorre
                r "Como se ha puesto por unas anchoas. Si eso es incomestible."
                montoto "Lo peor es que no hemos ganado un solo voto."
                r "Pero salimos con el estómago en plena forma."
                jump mapa

        revilla "¿Por dónde iba?... Ah, sí, no tenían anchoas. Tenían otras cosas parecidas, lampresa salada, que, oye, es como el pobre que no tiene caviar y se tiene que conformar con las huevas de boquerón, que su ilusion tambien hace comerlas en navidad."
        revilla "El paquistaní se disculpó y me dijo que tenía que marcharse porque tenía cita con el peluquero, así que me dejó con el taxi y continué haciendo la ronda. Pero no quiero aburrirte..."
        menu:
            "No, tranquilo. Me parece muy interesante su historia.":
                pass
            "No, pero si me dijera ya si me va a votar...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                r "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                r "Como se ha puesto por nada."
                montoto "Lo peor es que no hemos ganado un solo voto."
                r "Nadie dijo que fuera a ser fácil."
                jump mapa

        revilla "Pues otro día, era más joven yo, todavía no me había comprado la licencia de taxi. Pues estaba en una feria... no recuerdo cual."
        revilla "Me encontré a Yuri Gagarin, que andaba por allí de turismo. No entendía ni papa de cántabro, pero ni papa, y le dije: Yuri, mai frend, ven que te voy a dar a probar los mejores sobaos que has probado en tu vida, seguro que te comes uno y te vuelves del Racing de Santander."
        r "¿Y los probo?"
        revilla "Coño, el socio 34.567. Luego me lo encontré tres años después en Peñíscola en unos ultramarinos comprando compresas para su señora y me comentó entristecido que había tenido que quemar el carné porque los fans del Dynamo de Moscú se pensaron que era el del Real Madrid."
        revilla "Y se ve que allí eran más de Barça. Por lo de los polacos, supongo."
        revilla "Que ya ves confundir al Madrid con el Racing. ¡Qué incultura futbolística!"
        revilla "¿Pero sabes lo peor?"
        r "No me lo puedo imaginar."
        revilla "Pues que con tanta charla cogió las compresas que no eran y su mujer le hizo dormir esa noche en el sofá."
        revilla "Me lo contó un lustro después en la caja de ahorros de Cabezón de la sal."
        revilla "\"Yo, un héroe de la Unión Soviética, que le lamí una oreja a la momia de Lenin, durmiendo en el sofá como un proletario más. Me dio ciática y no pude asistir al lanzamiento del día siguiente que me llevaría a la luna.\""
        revilla "\"Los americanos llegaron primero porque tratan a sus mujeres como muebles. Esa es la experiencia que saqué de todo ello.\""
        revilla "Pobre, metio 3.000 pesetas de la época en renta variable. Al menos le quedará siempre lo de haber sido el primer ruso socio del Racing."
        revilla "Y bueno... oye, que te estoy viendo y no te quiero molestar. Que si estás cansado nos damos la mano y hasta la próxima."
        menu:
            "No, no. No podría vivir sabiendo que quedan historias suyas por conocer.":
                pass
            "No, pero si me dijera ya si me va a votar...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                r "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                r "Como se ha puesto por nada."
                montoto "Lo peor es que no hemos ganado un solo voto."
                r "Nadie dijo que fuera a ser fácil."
                jump mapa
        
        revilla "Pues no te he contado cuando hice de comercial de Regma en las conversaciones de Reikjavik entre Reagan y Gorbachov!" 
        revilla "¡Se le puso la calva blanca de lo bueno que estaban los helados! Muchos dicen que si Reagan y la Guerra de las Galaxias, pero yo creo que fue el helado de turrón el que quitó la tontería a los comunistas."
        revilla "Eso sí, el pase de temporada a Cabárceno no me lo aceptó. Dijo que a los osos ya los tenía muy vistos."
        revilla "Uy, qué tarde se ha hecho. Me voy a dormir y a soñar con una Cantabria inmersa en pleno siglo XXI, donde los niños puedan llegar a ser presidente del gobierno, donde las vacas tengan los mismos derechos que los seres humanos y donde las anchoas estén al mismo nivel que el caviar iraní."
        revilla "Antes de iros, quiero daros mis votos por haber sido tan buenos oyentes. No me suele pasar, ¿eh?"
        revilla "Gente muy desagradecir hay por estas tierras de España."
        r "Muchas gracias. Descanse usted."
        revilla "¡Nos vemos!"
        hide cuñadotorre with moveoutleft
        r "Qué señor más simpático."
        montoto "Zzzzz... Zzzzz"
        r "¡Montoto!"
        montoto "¡Yo no blanqueé ese dinero, fue mi gemelo malvado dominicano!"
        r "..."
        montoto "Un mal sueño, Presidente."
        r "Anda, vámonos."
        pov "¿A qué tanta prisa?"
        extend " Me gustaría saber más del gemelo de Montoto."
        pov "¿Cómo se llama?"
        montoto "Master Wilfredo."
        pov "¿Y qué se dedica?"
        montoto "A ser malvado."
        extend " No quiero hablar más de él. Ha hecho mucho daño a la familia."
        r "En marcha. La presidencia está más cerca."
        $ puntosj +=3
        
        
    if ken == True:
        scene torre2 with fade
        $ renpy.pause(0.5, hard=True)
        show lauris at center with moveinright
        k "Hola, guapa. ¿Cómo va eso?"
        lauris "¿Usted quién es? ¿Por qué me habla?"
        k "Soy el príncip de tu reino, el fontanero de tu mundo champiñón, tu ciruela en el relleno del pavo..."
        lauris "Tengo un spray de pimienta en el bolso. No me obligue a sacarlo."
        pov "Perdónalo, ha esnifado demasiada laca durante el camino."
        k "Nunca tienes demasiada laca ni demasiada progresía."
        pov "¿Por dónde queda el prado?"
        lauris "Ahí, al lado de Bilbado, jaajajja."
        espejo "Creo que se ha reído de nosotros, pero no estoy muy seguro."
        lauris "Lo siento, pero tenía que decirlo. Es algo típico de aquí, como los sobaos y lo buena que estoy."
        lauris "¿Tenéis en mente algún prado en especial? Aquí hay muchos."
        k "Buscamos el lugar donde está el gimnasio local."
        lauris "Es fácil de llegar."
        lauris "Girad a mano derecha, seguid recto hasta la rotonda, luego a la izquierda hasta que veáis una estatua de unas manos agarrando un globo terráqueo "
        extend " Y ya desde ahí, llamáis a un taxi para que os lleve."
        k "..."
        pov "Gracias, señorita. Nos ha sido de mucha ayuda."
        lauris "A mandar."
        extend " Ah, y si queréis hacer un regalo al bebé de vuestros amigos, buscad a Doña Pito Piturra. No os fallará."
        hide lauris
        espejo "Qué chica más simpática."
        pov "Tenía algo..."
        k "Un buen par de te..."
        k "En marcha. Id buscando suelto para llamar al taxi y rezad para que encontremos una cabina, de lo contrario tendrás que enseñar cachas para que nos pare alguien, [jugador]."
        pov "No cuentes con ello."
        scene prado with dissolve
        $ renpy.pause(1, hard=True)
        pov "Fue una suerte que hubiera un taxi junto a la estatua."
        k "Y que lo digas, aunque no sé si nos habrá traído al sitio correcto. Por aquí no se ve nada más que campo y una estúpida vaca."
        show vaca at center with dissolve
        vaca "Oiga, un respeto."
        espejo "¡Una vaca que habla! No metafórica, quiero decir."
        vaca "No soy una vaca. Los animales no hablan. Un poco de seriedad."
        vaca "Me llamo Ramón y soy un actor."
        k "Un actor que hace de vaca..."
        vaca "Es usted muy sagaz."
        extend " Hace un par de años un virus acabó con gran parte de las vacadas de la región."
        vaca "Fue un desastre porque uno de sus atractivos turísticos eran precisamente las vacas."
        vaca "Sobre todo chinos que pensaban que \"La vaca que ríe\" era de aquí, cuando es de Suiza."
        k "Como las jubiladas rubias."
        vaca "Así que el gobierno autonómico decidió tomar cartas en el asunto y contrato a varios actores para que nos enfundaramos en estos trajes vacunos y dieramos un poco de color a los prados y los montes."
        k "Debe de ser un trabajo duro."
        vaca "A veces, aunque tiene sus recompensas. De vez en cuando alguna turista intenta ordeñarte. Esos días, vuelvo a casa contento."
        k "¿Sabes si hay plazas abiertas?"
        vaca "Me temo que hasta 2018 que se jubile Marcial, está el cupo completo."
        k "Mientras tanto tendré que continuar la carrera por la presidencia... ¿Sabe dónde queda el gimnasio?"
        vaca "Detrás de esa loma. No tiene pérdida."
        vaca "Ah, y a ver si bajan el IVA cultural, que lo de vaca está bien, pero me gustaría trabajar algún día con José Luís Moreno y al precio que está el cine no va nadie."
        k "Cuente con ello, compañero."
        hide vaca with moveoutleft
        k "¡Creo que estoy hiperventilando! ¡Qué emoción!"
        pov "¿Por qué?"
        k "¿Estás de broma? Era uno de los de \"La ceja\""
        k "¿Crees que me habrá reconocido?"
        espejo "Seguro, Ken Loach manchego."
        pov "Creí que había nacido en Madrid."
        k "Yo soy de donde el pueblo me necesite y se consiga plaza más fácilmente en un buen colegio."
        scene black with dissolve
        show gymtextto1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextto2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymtorre with fade
        show cuñadotorre at center
        k "Hola"
        revilla "¡Hombre! ¿A quién tenemos aquí? A tres ilustres señores que han venido a esta bendita tierra."
        k "Mucho gusto."
        revilla "¿Qué tal? ¿Cómo ha ido el viaje? Aquí las comunicaciones son excelentes. Unas carreteras como pocas hay en este país. Y todo muy bien señalizado, que es imposible perderse."
        revilla "Si es que ya lo digo yo siempre: ¿para qué te vas a ir a otro lado pudiendo venir a Cantabria?"
        revilla "Hay otros sitios: El Vaticano, Madagascar, Cancún, pero a ver dónde metes tú a las vacas en Cancún."
        extend " Y allí no hay pastos para que se alimenten. Ni siquiera... No me voy a permitir la licencia porque un caballero no habla de eso pero es que ya no se lleva el matojo agreste."
        revilla "No sé si me explico."
        k "Pues me he perdido un poco..."
        revilla "No se preocupe. Es la edad."
        revilla "No le estaré haciendo perder el tiempo, ¿verdad?"
        menu:
            "Para nada.":
                pass
            "Hombre, pues yo venía...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                r "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                r "Como se ha puesto por nada."
                montoto "Lo peor es que no hemos ganado un solo voto."
                r "Nadie dijo que fuera a ser fácil."
                jump mapa

        revilla "Pues me acabo de acordar, que iba yo en el taxi con el Rey un día"
        extend " (el de verdad, no el de ahora)"
        extend " y me fijé en su cabeza de pronto. Entonces, me quedo así mirándolo un rato y el Rey veo que se inquieta y me grita: Micky coño, que me estás poniendo nervioso." 
        revilla "Así, muy campechano. Y yo le dije: Perdone, majestad, pero tiene usted una frente que sería el orgullo de los cabezaconos. Y él, muy campechanamente, se echó a reír." 
        revilla "El pakistaní que iba a los mandos del vehículo no se enteró de nada y eso que tenía la hebra puesta, porque no siempre se lleva a un miembro de la realeza y a un Revilla en el coche, pero el pobre, en su salvajismo no sabía de qué estaba hablando."
        revilla "Luego cuando dejamos al Rey en el pub estuve charlando con él un rato. Me dijo que se llamaba..."
        extend " ¿Cómo me dijo?... "
        revilla "Rashid Japurt y que venía de un pueblecito pesquero llamado... no me acuerdo, pero le pregunté que si tenían anchoas por allí. ¡Y no tenían! Claro que aunque las hubieran tenido, seguro que tan buenas como las de Santoña no iban a ser."
        revilla "¿Quieres unas?"
        menu:
            "No me vendrían mal":
                revilla "Claro que no, hombre."
                revilla "Ten."
            "Mejor no":
                revilla "¿Cómo?"
                extend " ¿Me rechazas unas anchoas de primera calidad por las que el mismo Elvis Presley dijo que dejaría las drogas?"
                revilla "Corre lejos de aquí que no quiero saber nada de los de vuestra calaña. Os va a votar las vacas del Prao."
                hide cuñadotorre
                k "Como se ha puesto por unas anchoas. Si eso es incomestible."
                espejo "Lo peor es que no hemos ganado un solo voto."
                k "Pero salimos con el estómago en plena forma."
                jump mapa

        revilla "¿Por dónde iba?... Ah, sí, no tenían anchoas. Tenían otras cosas parecidas, lampresa salada, que, oye, es como el pobre que no tiene caviar y se tiene que conformar con las huevas de boquerón, que su ilusion tambien hace comerlas en navidad."
        revilla "El paquistaní se disculpó y me dijo que tenía que marcharse porque tenía cita con el peluquero, así que me dejó con el taxi y continué haciendo la ronda. Pero no quiero aburrirte..."
        menu:
            "No, tranquilo. Me parece muy interesante su historia.":
                pass
            "No, pero si me dijera ya si me va a votar...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                k "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                k "Como se ha puesto por nada."
                montoto "Lo peor es que no hemos ganado un solo voto."
                k "Nadie dijo que fuera a ser fácil."
                jump mapa

        revilla "Pues otro día, era más joven yo, todavía no me había comprado la licencia de taxi. Pues estaba en una feria... no recuerdo cual."
        revilla "Me encontré a Yuri Gagarin, que andaba por allí de turismo. No entendía ni papa de cántabro, pero ni papa, y le dije: Yuri, mai frend, ven que te voy a dar a probar los mejores sobaos que has probado en tu vida, seguro que te comes uno y te vuelves del Racing de Santander."
        k "¿Y los probo?"
        revilla "Coño, el socio 34.567. Luego me lo encontré tres años después en Peñíscola en unos ultramarinos comprando compresas para su señora y me comentó entristecido que había tenido que quemar el carné porque los fans del Dynamo de Moscú se pensaron que era el del Real Madrid."
        revilla "Y se ve que allí eran más de Barça. Por lo de los polacos, supongo."
        revilla "Que ya ves confundir al Madrid con el Racing. ¡Qué incultura futbolística!"
        revilla "¿Pero sabes lo peor?"
        k "No me lo puedo imaginar."
        revilla "Pues que con tanta charla cogió las compresas que no eran y su mujer le hizo dormir esa noche en el sofá."
        revilla "Me lo contó un lustro después en la caja de ahorros de Cabezón de la sal."
        revilla "\"Yo, un héroe de la Unión Soviética, que le lamí una oreja a la momia de Lenin, durmiendo en el sofá como un proletario más. Me dio ciática y no pude asistir al lanzamiento del día siguiente que me llevaría a la Luna.\""
        revilla "\"Los americanos llegaron primero porque tratan a sus mujeres como muebles. Esa es la experiencia que saqué de todo ello.\""
        revilla "Pobre, metio 3.000 pesetas de la época en renta variable. Al menos le quedará siempre lo de haber sido el primer ruso socio del Racing."
        revilla "Y bueno... oye, que te estoy viendo la cara y no te quiero molestar. Que si estás cansado nos damos la mano y hasta la próxima."
        menu:
            "No, no. No podría vivir sabiendo que quedan historias suyas por conocer.":
                pass
            "No, pero si me dijera ya si me va a votar...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                k "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                k "Como se ha puesto por nada."
                montoto "Lo peor es que no hemos ganado un solo voto."
                k "Nadie dijo que fuera a ser fácil."
                jump mapa
        
        revilla "Pues no te he contado cuando hice de comercial de Heladerías Regma en las conversaciones de Reikjavik entre Reagan y Gorbachov!" 
        revilla "¡Se le puso la calva blanca de lo bueno que estaban! Muchos dicen que si Reagan y la Guerra de las Galaxias, pero yo creo que fue el helado de turrón el que convirtió a los comunistas en miembros de pleno derecho de la cristiandad."
        revilla "Eso sí, el pase de temporada a Cabárceno no me lo aceptó. Dijo que a los osos ya los tenía muy vistos."
        revilla "Uy, qué tarde se ha hecho. Me voy a dormir y a soñar con una Cantabria inmersa en pleno siglo XXI, donde los niños puedan llegar a ser presidente del gobierno, donde las vacas tengan los mismos derechos que los seres humanos y donde las anchoas estén al mismo nivel que el caviar iraní."
        revilla "Antes de iros, quiero daros mis votos por haber sido tan buenos oyentes. No me suele pasar, ¿eh?"
        revilla "Gente muy desagradecir hay por estas tierras de España."
        k "Muchas gracias. Descanse usted."
        revilla "¡Nos vemos!"
        hide cuñadotorre with moveoutleft
        k "Qué señor más simpático."
        espejo "Por una vez me alegro de no tener oídos."
        pov "¿Y cómo puedes hablar con nosotros?"
        espejo "¿Lo estoy haciendo?"
        k "En marcha. La presidencia está más cerca."
        $ puntosj +=3
        
        
    if coletas == True:
 
        scene torre1 with fade
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? Sí que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvían a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        $ renpy.pause(0.5, hard=True)
        show lauris at center with moveinright
        c "Perdona, compañera, ¿sabes por dónde queda el prado?"
        lauris "Sí, ahí al lado de Bilbado, jaajajja."
        stalin "Creo que se ha reído de nosotros, pero no estoy muy seguro."
        lauris "Lo siento, pero tenía que decirlo. Es algo típico de aquí, como los sobaos y lo buena que estoy."
        lauris "¿Tenéis en mente algún prado en especial? Aquí hay muchos."
        c "Buscamos el Gimnasio local."
        lauris "Ah, es fácil de llegar allí."
        lauris "Girad a mano derecha, seguid recto hasta la rotonda, luego a la izquierda hasta que veáis una estatua de unas manos agarrando un globo terráqueo "
        extend " Y ya desde ahí, llamáis a un taxi para que os lleve."
        c "..."
        pov "Gracias, señorita. Nos ha sido de mucha ayuda."
        lauris "A mandar."
        extend " Ah, y si queréis hacer un regalo al bebé de vuestros amigos, buscad a Doña Pito Piturra. No os fallará."
        hide lauris
        c "Qué chica más simpática."
        stalin "Tenía algo..."
        pov "Un buen par de te..."
        stalin "No, ahora que lo he pensado mejor. Sí que se ha reído de nosotros."
        c "En marcha. Id buscando suelto para llamar al taxi y rezad para que encontremos una cabina, de lo contrario a ver qué vamos a hacer..."
        stalin "Nacionalizar el primer coche que se cruce en nuestro camino."
        c "¿Sabes conducir?"
        stalin "Por supuesto que no, es cosa de burgueses. ¿Qué pasa, que tú tampoco sabes?"
        c "A mi me pones un Escalextric y te gano el campeonato del mundo, pero me sacas de ahí..."
        pov "No os preocupéis, por conveniencias del guión, apareceremos allí al instante."
        scene prado with wipedown
        $ renpy.pause(1, hard=True)
        pov "¿Véis?"
        stalin "Curioso... lo que no me explico es por qué no aparecemos directamente en el gimnasio y nos dejamos de tanto rodeo sin gracia."
        stalin "Encima apesta a estiércol. A saber lo que ha debido comer esa sucia vaca."
        show vaca at center with dissolve
        vaca "Oiga, un respeto."
        c "¡Una vaca que habla!"
        vaca "No soy una vaca. Los animales no hablan. Un poco de seriedad."
        vaca "Me llamo Ramón y soy un actor."
        stalin "Un actor que hace de vaca..."
        vaca "Es usted muy sagaz."
        extend " Hace un par de años un virus acabó con gran parte de las vacadas de la región."
        c "¿La encefalopatía espongiforme bovina?"
        vaca "No, el capitalismo."
        stalin "Mmm, un animal contestatario... No me gusta."
        vaca "Fue un desastre porque uno de sus atractivos turísticos eran precisamente las vacas."
        vaca "Sobre todo chinos que pensaban que \"La vaca que ríe\" era de aquí, cuando es de Suiza."
        c "Otra patriota de pulsera."
        vaca "Así que el gobierno autonómico decidió tomar cartas en el asunto y contrato a varios actores para que nos enfundaramos en estos trajes vacunos y dieramos un poco de color a los prados y los montes."
        c "Debe de ser un trabajo duro."
        vaca "A veces, aunque tiene sus recompensas. De vez en cuando alguna turista intenta ordeñarte. Esos días, vuelvo a casa contento."
        pov "¿Sabe dónde queda el gimnasio?"
        vaca "Detrás de esa loma. No tiene pérdida."
        vaca "Ah, y a ver si bajan el IVA cultural, que lo de vaca está bien, pero me gustaría trabajar algún día con José Luís Moreno y al precio que está el cine no va nadie."
        hide vaca with moveoutleft
        stalin "Nos hemos librado por un pelo. Uno de los agentes de la pérfida organización \"De la ceja\" ha intentado sabotear nuestro viaje."
        stalin "Menos mal que no nos ha reconocido."
        c "Eso me están comentando últimamente."
        scene black with dissolve
        show gymtextto1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextto2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymtorre with fade
        show cuñadotorre at center
        c "Hola"
        revilla "¡Hombre! ¿A quién tenemos aquí? A tres ilustres señores que han venido a esta bendita tierra."
        c "Mucho gusto."
        revilla "¿Qué tal? ¿Cómo ha ido el viaje? Aquí las comunicaciones son excelentes. Unas carreteras como pocas hay en este país. Y todo muy bien señalizado, que es imposible perderse."
        revilla "Si es que ya lo digo yo siempre: ¿para qué te vas a ir a otro lado pudiendo venir a Cantabria?"
        revilla "Hay otros sitios: El Vaticano, Madagascar, Cancún, pero a ver dónde metes tú a las vacas en Cancún."
        extend " Y allí no hay pastos para que se alimenten. Ni siquiera... No me voy a permitir la licencia porque un caballero no habla de eso pero es que ya no se lleva el matojo agreste."
        revilla "No sé si me explico."
        c "Pues me he perdido un poco..."
        revilla "No se preocupe. Es la edad."
        revilla "No le estaré haciendo perder el tiempo, ¿verdad?"
        menu:
            "Para nada.":
                pass
            "Hombre, pues yo venía...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                c "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                c "Como se ha puesto por nada."
                stalin "Lo peor es que no hemos ganado un solo voto."
                c "Nadie dijo que fuera a ser fácil."
                jump mapa

        revilla "Pues me acabo de acordar, que iba yo en el taxi con el Rey un día"
        extend " (el de verdad, no el de ahora)"
        extend " y me fijé en su cabeza de pronto. Entonces, me quedo así mirándolo un rato y el Rey veo que se inquieta y me grita: Micky coño, que me estás poniendo nervioso." 
        revilla "Así, muy campechano. Y yo le dije: Perdone, majestad, pero tiene usted una frente que sería el orgullo de los cabezaconos. Y él, muy campechanamente, se echó a reír." 
        revilla "El pakistaní que iba a los mandos del vehículo no se enteró de nada y eso que tenía la hebra puesta, porque no siempre se lleva a un miembro de la realeza y a un Revilla en el coche, pero el pobre, en su salvajismo no sabía de qué estaba hablando."
        revilla "Luego cuando dejamos al Rey en el pub estuve charlando con él un rato. Me dijo que se llamaba..."
        extend " ¿Cómo me dijo?... "
        revilla "Rashid Japurt y que venía de un pueblecito pesquero llamado... no me acuerdo, pero le pregunté que si tenían anchoas por allí. ¡Y no tenían! Claro que aunque las hubieran tenido, seguro que tan buenas como las de Santoña no iban a ser."
        revilla "¿Quieres unas?"
        menu:
            "No me vendrían mal":
                revilla "Claro que no, hombre."
                revilla "Ten."
            "Mejor no":
                revilla "¿Cómo?"
                extend " ¿Me rechazas unas anchoas de primera calidad por las que el mismo Elvis Presley dijo que dejaría las drogas?"
                revilla "Corre lejos de aquí que no quiero saber nada de los de vuestra calaña. Os va a votar las vacas del Prao."
                hide cuñadotorre
                c "Como se ha puesto por unas anchoas. Si eso es incomestible."
                stalin "Lo peor es que no hemos ganado un solo voto."
                c "Pero salimos con el estómago en plena forma."
                jump mapa

        revilla "¿Por dónde iba?... Ah, sí, no tenían anchoas. Tenían otras cosas parecidas, lampresa salada, que, oye, es como el pobre que no tiene caviar y se tiene que conformar con las huevas de boquerón, que su ilusion tambien hace comerlas en navidad."
        revilla "El paquistaní se disculpó y me dijo que tenía que marcharse porque tenía cita con el peluquero, así que me dejó con el taxi y continué haciendo la ronda. Pero no quiero aburrirte..."
        menu:
            "No, tranquilo. Me parece muy interesante su historia.":
                pass
            "No, pero si me dijera ya si me va a votar...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                c "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                c "Como se ha puesto por nada."
                stalin "Lo peor es que no hemos ganado un solo voto."
                c "Nadie dijo que fuera a ser fácil."
                jump mapa

        revilla "Pues otro día, era más joven yo, todavía no me había comprado la licencia de taxi. Pues estaba en una feria... no recuerdo cual."
        revilla "Me encontré a Yuri Gagarin, que andaba por allí de turismo. No entendía ni papa de cántabro, pero ni papa, y le dije: Yuri, mai frend, ven que te voy a dar a probar los mejores sobaos que has probado en tu vida, seguro que te comes uno y te vuelves del Racing de Santander."
        c "¿Y los probo?"
        revilla "Coño, el socio 34.567. Luego me lo encontré tres años después en Peñíscola en unos ultramarinos comprando compresas para su señora y me comentó entristecido que había tenido que quemar el carné porque los fans del Dynamo de Moscú se pensaron que era el del Real Madrid."
        revilla "Y se ve que allí eran más de Barça. Por lo de los polacos, supongo."
        revilla "Que ya ves confundir al Madrid con el Racing. ¡Qué incultura futbolística"
        revilla "¿Pero sabes lo peor?"
        c "No me lo puedo imaginar."
        revilla "Pues que con tanta charla cogió las compresas que no eran y su mujer le hizo dormir esa noche en el sofá."
        revilla "Me lo contó un lustro después en la caja de ahorros de Cabezón de la sal."
        revilla "\"Yo, un héroe de la Unión Soviética, que le lamí una oreja a la momia de Lenin, durmiendo en el sofá como un proletario más. Me dio ciática y no pude asistir al lanzamiento del día siguiente que me llevaría a la luna."
        revilla "\"Los americanos llegaron primero porque tratan a sus mujeres como muebles. Esa es la experiencia que saqué de todo ello.\""
        revilla "Pobre, metio 3.000 pesetas de la época en renta variable. Al menos le quedará siempre lo de haber sido el primer ruso socio del Racing."
        revilla "Y bueno... oye, que te estoy viendo y no te quiero molestar. Que si estás cansado nos damos la mano y hasta la próxima."
        menu:
            "No, no. No podría vivir sabiendo que quedan historias suyas por conocer.":
                pass
            "No, pero si me dijera ya si me va a votar...":
                revilla "Así que te aburres, ¿eh?"
                revilla "Pues nadie dirá que Rebilluca es un pesado."
                extend " Hasta luego, señores."
                c "¿Pero los votos...?"
                revilla "Adiós muy buenas. Cierren al salir que yo me voy a ordeñar a las vacas."
                hide cuñadotorre
                c "Como se ha puesto por nada."
                stalin "Lo peor es que no hemos ganado un solo voto."
                c "Nadie dijo que fuera a ser fácil."
                jump mapa
        
        revilla "Pues no te he contado cuando hice de comercial de Regma en las conversaciones de Reikjavik entre Reagan y Gorbachov!" 
        revilla "¡Se le puso la calva blanca de lo bueno que estaban! Muchos dicen que si Reagan y la Guerra de las Galaxias, pero yo creo que fue el helado de turrón el que convirtió a los comunistas en miembros de pleno derecho de la cristiandad."
        revilla "Eso sí, el pase de temporada a Cabárceno no me lo aceptó. Dijo que a los osos ya los tenía muy vistos."
        revilla "Uy, qué tarde se ha hecho. Me voy a dormir y a soñar con una Cantabria inmersa en pleno siglo XXI, donde los niños puedan llegar a ser presidente del gobierno, donde las vacas tengan los mismos derechos que los seres humanos y donde las anchoas estén al mismo nivel que el caviar iraní."
        revilla "Antes de iros, quiero daros mis votos por haber sido tan buenos oyentes. No me suele pasar, ¿eh?"
        revilla "Gente muy desagradecir hay por estas tierras de España."
        c "Muchas gracias. Descanse usted."
        revilla "¡Nos vemos!"
        hide cuñadotorre with moveoutleft
        c "Qué señor más simpático."
        stalin "Zzzzz... Zzzzz"
        c "..."
        pov "..."
        stalin "Buff, qué sueño más bueno he echado. Ese hombre sería el instrumento de tortura perfecto."
        stalin "Recuérdame que hable con él cuando hayamos terminado nuestro viaje."
        c "En marcha. La presidencia está más cerca."
        $ puntosj +=3
        
    
    jump mapa