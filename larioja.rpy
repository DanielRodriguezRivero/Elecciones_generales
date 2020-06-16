label larioja:
    $ larioja = True
    $ rescate = 0 #cancion de bunbury
    $ letra1 = ""
    $ letra2 = ""
    $ letra3 = ""
    $ letra4 = ""
    
    #personajes
    define bunbury = Character("Enrique B.", color="#457C28", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    define festivalero = Character("Festivalero", color="#871A32", ctc="ctc_blink", ctc_position="fixed", show_two_window=True, callback=callback)
    
    #escenarios
    image gymlogroño = "images/gymlogroño.jpg"
    image logro1 = "images/logro4.jpg"
    image logro2 = "images/logro2.jpg"
    
    #imagenes personajes
    image cuñadologroño = "images/bunbury.png"
    image festivalero = "images/festivalero.png"
    
    image gymtextri1 = Text("{size=40}Gimnasio Héroes del Linimento",color="#fff", text_align=0.3)
    image gymtextri2 = Text("{size=40}Este es tu sitio. Esta es tu espina: dieta nutritiva",color="#fff", text_align=0.3)
    image rioja34 = Text("{size=60}(Motherfuckers)",color="#000", text_align=0.2)
    scene travelrioja at Pan((0, 0), (270,0), 17.0)
    play music "entradillarioja.mp3"
    $ renpy.pause(12, hard=True)
    show rioja34:
        xpos 0.3
        ypos 0.3
    with dissolve
    $ renpy.pause(2, hard=True)
    
    play music "cancionciudad.mp3"
    
    if mrajao == True:
        
        scene logro1 with dissolve
        pov "Aquí pone La Rioja, pero estamos más concretamente en Logroño."
        r "Jejeje."
        pov "¿Qué pasa?"
        r "Jejeje. ¿Qué va a pasar? Jejejej."
        montoto "¿Y esa risa?"
        r "Jijiji, pues eso..."
        montoto "¿Eso que?"
        r "¡Logroño! Jijiji."
        pov "..."
        r "Logroño rima con..."
        pov "Ya, con coño."
        r "Ah, pues es verdad. También rima con eso. Qué cosas..."
        scene logro2 with fade
        $ renpy.pause(0.5, hard=True)
        show festivalero at center with zoomin
        festivalero "¡Ey! ¡Ey! ¡Ey! Tú y yo lo sabemos. ¡Vamos a asistir al mejor concierto del año!"
        festivalero "¿Qué digo del año? ¡De hoy!"
        festivalero "¡A tope con drogas!"
        r "Este joven me resulta familiar..."
        festivalero "¿No es increible que el destino nos haya unido en estas tierras extrañas para contemplar el apoteosis de la mejor banda del mundo?"
        festivalero "¿Qué digo del mundo? ¡De mi puto barrio!"
        pov "¿Quién toca?"
        festivalero "¿Cómo?"
        extend " ¿No lo sabéis?"
        festivalero "¡Otoño en mi coño!"
        festivalero "Da fucking masters of the universe of flipadings!"
        montoto "No les he escuchado en mi vida."
        festivalero "Eso es porque eres un viejo moñas. ¡OMC son lo más!"
        festivalero "Tienen un bajo que hace así como guaung, guaung, pero con flow. Y la batería: pam, pam, tchus, parara, tchus, tchus..."
        festivalero "Tienen influencias de Sigur Ross."
        r "Ah, esa es la que ponen antes de El secreto de puente viejo, ¿no?"
        r "Aunque yo soy mas de Acacias 38."
        festivalero "Qué pena que murieran Manuela y el médico, ¿verdad?"
        r "Desde luego, aunque más triste fue la muerte del señor orondo ese, con la hija escritora casada con un mal partido..."
        r "Yo siempre pensé que le tendrían que haber puesto un monóculo. Ahora ya no sabremos lo bien que le habría quedado."
        r "Pocos monóculos veo yo en esa serie para la época que representa."
        montoto "Es que en España todos veiamos muy bien. No necesitábamos de gafas ni de otros objetos de ayuda a la visión."
        pov "Claro está, al no leer..."
        pov " Si es que todo son ventajas."
        festivalero "Venga, viejales, me vuelvo a la tienda que hemos montado los colegas para esperar la hora del concierto. Llevamos dos meses acampados a la entrada de Las Gaunas."
        pov "Creo que es mejor que continuemos nuestro camino."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextri1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextri2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)             
        scene gymlogroño with fade
        show cuñadologroño at center
        r "Hola."
        r "Vengo a pedir su voto."
        bunbury "Pero olvidame, que nadie te ha llamado. Ya estás otra vez."
        r "Pero oiga, que es la primera vez que vengo."
        bunbury "Dejalo ya. No seas membrillo y permite pasar."
        bunbury "Y si no piensas echar atrás. Tienes mucho barro que tragar."
        r "Pues no es lo que tenía pensado pero todo sea por ganar..."
        bunbury "Entre dos tierras estas. Y no dejas aire que respirar."
        r "Montoto... "
        extend " ¿está insinuando lo que creo?"
        pov "Yo lo vi una vez en una película de Russ Meyer."
        bunbury "¿Pero de qué estáis hablando?"
        bunbury "Está claro que ya no hay lírica en este país."
        r "Lo que sea, pero ¿me va a votar?"
        bunbury "Para eso antes tendrá que ayudarme a componer una canción."
        extend " Malú me ha dicho que le componga una y la verdad es que no controlo demasiado de sus temas."
        pov "¿Y por qué aceptó el encargo?"
        bunbury "A ver si te crees que la vida del rockero es barata."
        bunbury "Además, está el prestigio."
        bunbury "Va, ¿me ayudáis?"
        pov "Se hará lo que se pueda. Mi única formación musical son dos años tocándole la flauta a un siniestro profesor de secundaria."
        r "Precisamente anoche vi una película con ese argumento. No llegué a ver el final."
        bunbury "Yo voy tocando acordes y vosotros elegís la letra."
        play music "clasical.mp3"
        menu:
            "Estuve en el infierno el agosto pasado":
                $ letra1 = "Estuve en el infierno el agosto pasado."
                pass
            "Que pagues el rescate que abajo te indico":
                $ letra1 = "Que pagues el rescate que abajo te indico"
                $ rescate += 1
                pass
            "Cuan bellas brillan mis flores":
                $ letra1 = "Cuan bellas brillan mis flores"
                pass
        menu: 
            "y estuvo bastante guay":
                $ letra2 = "y estuvo bastante guay."
                pass
            "qué finos son sus colores":
                $ letra2 = "qué finos son sus colores"
                pass
            "Yo tampoco me explico, por qué no acudí antes a ti":
                $ letra2 = "Yo tampoco me explico, por qué no acudí antes a ti"
                $ rescate += 1
                pass
        
        menu:
            
            "Pero nadie puede salvarme, nadie sabe lo que sabes":
                $ letra3 = "Pero nadie puede salvarme, nadie sabe lo que sabes"
                $ rescate += 1
                pass
            "Chicas guapas, rock y sexo":
                $ letra3 = "Chicas guapas, rock y sexo"
                pass
            "te estás acercando demasiado":
                $ letra3 = "te estás acercando demasiado"
                pass
                
        menu:
            "no me toques los cojones":
                $ letra4 = "no me toques los cojones"
                pass
            "y el demonio fumaba Lucky Strikes.":
                $ letra4 = "y el demonio fumaba Lucky Strikes."
                pass
            "Y tampoco entregarían lo que vale mi rescate.":
                $ letra4 = "Y tampoco entregarían lo que vale mi rescate."
                $ rescate += 1
                
        stop music
        if rescate == 4:
            bunbury "Veamos..."
            bunbury "Que pagues el rescate que abajo te indico."
            extend " Yo tampoco me explico, por qué no acudí antes a ti."
            extend " Pero nadie puede salvarme, nadie sabe lo que sabes,"
            extend " Y tampoco entregarían lo que vale mi rescate."
            bunbury "..."
            bunbury "Una cosa te voy a decir: excelente gusto musical."
            extend " Cojonudo." 
            extend " Ni yo lo hubiera hecho mejor. Pero es que esa cancion se llama El Rescate."
            r "Ah, ¿ya le has puesto nombre?"
            bunbury "No, lo que quiero decir es que ya la tocaba yo en los antros más infectos de Aragón cuando tú no eras más que un simple funcionario de provincias."
            bunbury "¿Cómo le voy a enseñar esto a Malú? No me va a pagar y necesito tinte y un sombrero mejor, que la paja se desgasta, ¡joder!"
            pov "Pues que cante la canción pero en otro ritmo, en el estilo que cante ella. El que sea."
            bunbury "Mmmm... Sí, creo que canta rumba pop o una mierda de esas."
            extend " No es mala idea... Incluso podría abrir una nueva línea de negocio."
            bunbury "¡Muchas gracias! Tenéis mis votos."
            $ puntosj += 3
            bunbury "Y ahora, ¡dejadmé! que yo no tengo la culpa de veros caer."
            r "Adiós, señor Dylan."
            jump mapa
        else:
            bunbury "Veamos..."
            bunbury "[letra1] "
            extend "[letra2] "
            extend "[letra3] "
            extend "[letra4] "
            bunbury "..."
            bunbury "A ver, cosas peores he cantado."
            pov "¿Como Lady Blue?"
            bunbury "No, esa era buena."
            bunbury "En cualquier caso, como no es para mí..."
            bunbury "No me parece que sea muy del estilo de Malú, pero tampoco sabria decirte cual es, así que mira, mejor esto que nada."
            bunbury "Creo que podría colársela."
            bunbury "Eso sí, solo os voy a dar dos votos. El rock es sufrimiento y no puedo ser el vehículo de una felicidad plena si os los diera todos."
            $ puntosj += 2
            r "No se preocupe. Con dos es más que suficiente para aplastar a los inútiles de mis rivales."
            bunbury "Y ahora, ¡dejadmé! que yo no tengo la culpa de veros caer."
            r "Adiós, señor Dylan."
            jump mapa

        
    if ken == True:

        scene logro1 with dissolve
        pov "Aquí pone La Rioja, pero estamos más concretamente en Logroño."
        k "Yo creo que deberían darnos los votos automáticamente por venir aquí."
        extend " Ni siquiera sabía que existía esta región."
        k "Creo que de aquí no me he liado con ninguna."
        espejo "Sí que lo hiciste, Titán Sexual. Pero era familiar de Rodríguez de la Borbolla y lo borraste de tu memoria."
        k "Jo, que mal rollo, ¿no?"
        extend " Al menos supongo que ella disfrutaría."
        scene logro2 with fade
        $ renpy.pause(0.5, hard=True)
        show festivalero at center with zoomin
        festivalero "¡Ey! ¡Ey! ¡Ey! Tú y yo lo sabemos. ¡Vamos a asistir al mejor concierto del año!"
        festivalero "¿Qué digo del año? ¡De hoy!"
        festivalero "¡A tope con drogas!"
        k "Este chico me recuerda a alguien..."
        festivalero "¿No es increible que el destino nos haya unido en estas tierras extrañas para contemplar el apoteosis de la mejor banda del mundo?"
        festivalero "¿Qué digo del mundo? ¡De mi puto barrio!"
        pov "¿Quién toca?"
        festivalero "¿Cómo?"
        extend " ¿No lo sabéis?"
        festivalero "¡Otoño en mi coño!"
        festivalero "Da fucking masters of the universe of flipadings!"
        espejo "No les he escuchado en mi vida."
        festivalero "Eso es porque no tienes orejas."
        festivalero "En serio, ¿un espejo que habla? WTF!! Y eso que juro que no me he tomado nada."
        festivalero "¡OMC son lo más!"
        festivalero "Tienen un bajo que hace así como guaung, guaung, pero con flow. Y la batería: pam, pam, tchus, parara, tchus, tchus..."
        festivalero "Tienen influencias de Sigur Ross."
        k "Ah, esa es la que ponen antes de El secreto de puente viejo, ¿no?"
        k "Aunque yo soy mas de Acacias 38."
        festivalero "Qué pena que murieran Manuela y el médico, ¿verdad?"
        k "Desde luego, aunque más triste fue la muerte del señor orondo ese, con la hija escritora casada con un mal partido..."
        k "Yo siempre pensé que le tendrían que haber puesto un monóculo. Ahora ya no sabremos lo bien que le habría quedado."
        k "Pocos monóculos veo yo en esa serie para la época que representa."
        espejo "Es que en España todos veiamos muy bien. No necesitábamos de gafas ni de otros objetos de ayuda a la visión."
        pov "Claro está, al no leer..."
        pov " Si es que todo son ventajas."
        festivalero "Venga, viejales, me vuelvo a la tienda que hemos montado los colegas para esperar la hora del concierto. Llevamos dos meses acampados a la entrada de Las Gaunas."
        pov "Creo que es mejor que continuemos nuestro camino."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextri1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextri2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymlogroño with fade 
        show cuñadologroño at center
        k "Hola"
        bunbury "Está claro que ya no hay lírica en este país."
        k "Lo que sea, pero ¿me va a votar?"
        bunbury "Para eso antes tendrá que ayudarme a componer una canción."
        extend " Malú me ha dicho que le componga una y la verdad es que no controlo demasiado de sus temas."
        pov "¿Y por qué aceptó el encargo?"
        bunbury "A ver si te crees que la vida del rockero es barata."
        bunbury "Además, está el prestigio."
        bunbury "Va, ¿me ayudáis?"
        pov "Se hará lo que se pueda. Mi única formación musical son dos años tocándole la flauta a un siniestro profesor de secundaria."
        r "Precisamente anoche vi una película con esa premisa."
        bunbury "Yo voy tocando acordes y vosotros elegís la letra."
        play music "clasical.mp3"
        menu:
            "Estuve en el infierno el agosto pasado":
                $ letra1 = "Estuve en el infierno el agosto pasado."
                pass
            "Que pagues el rescate que abajo te indico":
                $ letra1 = "Que pagues el rescate que abajo te indico"
                $ rescate += 1
                pass
            "Cuan bellas brillan mis flores":
                $ letra1 = "Cuan bellas brillan mis flores"
                pass
        menu: 
            "y estuvo bastante guay":
                $ letra2 = "y estuvo bastante guay."
                pass
            "qué finos son sus colores":
                $ letra2 = "qué finos son sus colores"
                pass
            "Yo tampoco me explico, por qué no acudí antes a ti":
                $ letra2 = "Yo tampoco me explico, por qué no acudí antes a ti"
                $ rescate += 1
                pass
        
        menu:
            
            "Pero nadie puede salvarme, nadie sabe lo que sabes":
                $ letra3 = "Pero nadie puede salvarme, nadie sabe lo que sabes"
                $ rescate += 1
                pass
            "Chicas guapas, rock y sexo":
                $ letra3 = "Chicas guapas, rock y sexo"
                pass
            "te estás acercando demasiado":
                $ letra3 = "te estás acercando demasiado"
                pass
        menu:
            "no me toques los cojones":
                $ letra4 = "no me toques los cojones"
                pass
            "y el demonio fumaba Lucky Strikes.":
                $ letra4 = "y el demonio fumaba Lucky Strikes."
                pass
            "Y tampoco entregarían lo que vale mi rescate.":
                $ letra4 = "Y tampoco entregarían lo que vale mi rescate."
                $ rescate += 1
                
        stop music
        if rescate == 4:
            bunbury "Veamos..."
            bunbury "Que pagues el rescate que abajo te indico."
            extend " Yo tampoco me explico, por qué no acudí antes a ti."
            extend " Pero nadie puede salvarme, nadie sabe lo que sabes,"
            extend " Y tampoco entregarían lo que vale mi rescate."
            bunbury "..."
            bunbury "Una cosa te voy a decir: excelente gusto musical."
            extend " Cojonudo."
            extend " Ni yo lo hubiera hecho mejor. Pero es que esa cancion se llama El Rescate."
            r "Ah, ¿ya le has puesto nombre?"
            bunbury "No, lo que quiero decir es que ya la tocaba yo en los antros más infectos de Aragón cuando tú no eras más que un simple funcionario de provincias."
            bunbury "¿Cómo le voy a enseñar esto a Malú? No me va a pagar y necesito tinte y un sombrero mejor, que la paja se desgasta, ¡joder!"
            pov "Pues que cante la canción pero en otro ritmo, en el estilo que cante ella. El que sea."
            bunbury "Mmmm... Sí, creo que canta rumba pop o una mierda de esas."
            extend " No es mala idea... Incluso podría abrir una nueva línea de negocio."
            bunbury "¡Muchas gracias! Tenéis mis votos."
            $ puntosj += 3
            bunbury "Y ahora, ¡dejadmé! que yo no tengo la culpa de veros caer."
            r "Adiós, señor Dylan."
            jump mapa
        else:
            bunbury "Veamos..."
            bunbury "[letra1] "
            extend "[letra2] "
            extend "[letra3] "
            extend "[letra4] "
            bunbury "..."
            bunbury "A ver, cosas peores he cantado."
            pov "¿Como Lady Blue?"
            bunbury "No, esa era buena."
            bunbury "En cualquier caso, como no es para mí..."
            bunbury "No me parece que sea muy del estilo de Malú, pero tampoco sabria decirte cual es, así que mira, mejor esto que nada."
            bunbury "Creo que podría colársela."
            bunbury "Eso sí, solo os voy a dar dos votos. El rock es sufrimiento y no puedo ser el vehículo de una felicidad plena si os los diera todos."
            $ puntosj += 2
            r "No se preocupe. Con dos es más que suficiente para aplastar a los inútiles de mis rivales."
            bunbury "Y ahora, ¡dejadmé! que yo no tengo la culpa de veros caer."
            r "Adiós, señor Dylan."
            jump mapa
            
            
    if coletas == True:

        scene logro1 with dissolve
        if barcelona == True:
            if yausado == False:
                stalin "Hola... ¿puedo unirme a vosotros?"
                c "¿Ya estás de vuelta? si que ha durado poco la revolucion."
                stalin "Es que nos derrotaron en el Gimnasio Margarita y los camaradas decidieron que mejor se volvian a casa a hacer los deberes."
                c "Venga, pero porque nos hace falta uno para jugar al Carcassonne."
                $ yausado = True
            else:
                pass
        pov "Aquí pone La Rioja, pero estamos más concretamente en Logroño."
        c "Además llegamos justo a tiempo para el Gaunas Fest."
        stalin "¿El qué?"
        c "Qué demodé estás. ¿Qué va a ser? El mayor festival de música indie de esta semana."
        stalin "A veces me pregunto si no serás un burgués encubierto. La coleta me impide escrutarte."
        scene logro2 with fade
        $ renpy.pause(0.5, hard=True)
        show festivalero at center with zoomin
        festivalero "¡Ey! ¡Ey! ¡Ey! Tú y yo lo sabemos. ¡Vamos a asistir al mejor concierto del año!"
        festivalero "¿Qué digo del año? ¡De hoy!"
        festivalero "¡A tope con drogas!"
        c "Si Joaquín Luqui no hubiera sido un fitoplancton asexual, apostaría todo mi patrimonio a que podrías ser su hijo."
        stalin "¿El no declarado también?"
        c "Vamos, ya sabes que yo no tengo de eso."
        festivalero "¿No es increible que el destino nos haya unido en estas tierras extrañas para contemplar el apoteosis de la mejor banda del mundo?"
        festivalero "¿Qué digo del mundo? ¡De mi puto barrio!"
        pov "¿Quién toca?"
        festivalero "¿Cómo?"
        extend " ¿No lo sabéis?"
        festivalero "¡Otoño en mi coño!"
        festivalero "Da fucking masters of the universe of flipadings!"
        c "¡OMC son lo más!"
        festivalero "¿Verdad que sí?"
        festivalero "Tienen un bajo que hace así como guaung, guaung, pero con flow. Y la batería: pam, pam, tchus, parara, tchus, tchus..."
        festivalero "Me flipan sus influencias de Sigur Ross."
        stalin "Ah, esa es la que ponen antes de El secreto de puente viejo, ¿no?"
        stalin "Aunque yo soy mas de Acacias 38."
        festivalero "Qué pena que murieran Manuela y el médico, ¿verdad?"
        stalin "Desde luego, aunque más triste fue la muerte del señor orondo ese, con la hija escritora casada con un mal partido..."
        stalin "Yo siempre pensé que le tendrían que haber puesto un monóculo. Ahora ya no sabremos lo bien que le habría quedado."
        stalin "Pocos monóculos veo yo en esa serie para la época que representa."
        pov "Es que en España todos veiamos muy bien. No necesitábamos de gafas ni de otros objetos de ayuda a la visión."
        pov "Claro está, al no leer..."
        pov " Si es que todo son ventajas."
        festivalero "Qué guay encontrar a unos viejales tan enrollados. Me hace mantener la fe en la humanidad."
        c "¿Nos votarás entonces?"
        festivalero "Bah, tí. Yo paso de esas cosas. Lo mío son las drogas."
        festivalero "Venga, troncos, me vuelvo a la tienda que hemos montado los colegas para esperar la hora del concierto. Llevamos dos meses acampados a la entrada de Las Gaunas."
        pov "Creo que es mejor que continuemos nuestro camino."
        scene black with dissolve
        $ renpy.pause(0.5, hard=True)
        show gymtextri1:
            yanchor 0.5 ypos 0.5
            xanchor 0.5 xpos 0.5
        with dissolve
        show gymtextri2:
            yanchor 0.5 ypos 0.55
            xanchor 0.5 xpos 0.5
        with dissolve
        $ renpy.pause(3, hard=True)
        scene gymlogroño with fade  
        $ renpy.pause(0.5, hard=True)
        show cuñadologroño at center
        c "Hola."
        bunbury "He oído que la noche es toda magia."
        c "Especialmente en Magaluf."
        bunbury "Y que un duende te invita a soñar."
        c "Ya te digo. Un poco de peyote del peruano que tengas más a mano y ya te digo si sueñas."
        bunbury "Está claro que ya no hay lírica en este país."
        c "Lo que sea, pero ¿me vas a votar?"
        bunbury "Para eso antes tendrá que ayudarme a componer una canción."
        extend " Malú me ha dicho que le componga una y la verdad es que no controlo demasiado de sus temas."
        pov "¿Y por qué aceptó el encargo?"
        bunbury "A ver si te crees que la vida del rockero es barata."
        bunbury "Además, está el prestigio."
        bunbury "Va, ¿me ayudáis?"
        pov "Se hará lo que se pueda. Mi única formación musical son dos años tocándole la flauta a un siniestro profesor de secundaria."
        bunbury "Yo voy tocando acordes y vosotros elegís la letra."
        play music "clasical.mp3"
        menu:
            "Estuve en el infierno el agosto pasado":
                $ letra1 = "Estuve en el infierno el agosto pasado."
                pass
            "Que pagues el rescate que abajo te indico":
                $ letra1 = "Que pagues el rescate que abajo te indico"
                $ rescate += 1
                pass
            "Cuan bellas brillan mis flores":
                $ letra1 = "Cuan bellas brillan mis flores"
                pass
        menu: 
            "y estuvo bastante guay":
                $ letra2 = "y estuvo bastante guay."
                pass
            "qué finos son sus colores":
                $ letra2 = "qué finos son sus colores"
                pass
            "Yo tampoco me explico, por qué no acudí antes a ti":
                $ letra2 = "Yo tampoco me explico, por qué no acudí antes a ti"
                $ rescate += 1
                pass
        
        menu:
            
            "Pero nadie puede salvarme, nadie sabe lo que sabes":
                $ letra3 = "Pero nadie puede salvarme, nadie sabe lo que sabes"
                $ rescate += 1
                pass
            "Chicas guapas, rock y sexo":
                $ letra3 = "Chicas guapas, rock y sexo"
                pass
            "te estás acercando demasiado":
                $ letra3 = "te estás acercando demasiado"
                pass
        menu:
            "no me toques los cojones":
                $ letra4 = "no me toques los cojones"
                pass
            "y el demonio fumaba Lucky Strikes.":
                $ letra4 = "y el demonio fumaba Lucky Strikes."
                pass

            "Y tampoco entregarían lo que vale mi rescate.":
                $ letra4 = "Y tampoco entregarían lo que vale mi rescate."
                $ rescate += 1
        
        stop music
        if rescate == 4:
            bunbury "Veamos..."
            bunbury "Que pagues el rescate que abajo te indico."
            extend " Yo tampoco me explico, por qué no acudí antes a ti."
            extend " Pero nadie puede salvarme, nadie sabe lo que sabes,"
            extend " Y tampoco entregarían lo que vale mi rescate."
            bunbury "..."
            bunbury "Una cosa te voy a decir: excelente gusto musical."
            extend " Cojonudo."
            extend " Ni yo lo hubiera hecho mejor. Pero es que esa cancion se llama El Rescate."
            c "Ya lo sé hombre. Por eso las he elegido. Soy un gran megalómano."
            stalin "Creo que te has confundido..."
            bunbury "¡Pero si ya la tocaba yo en los antros más infectos de Aragón cuando tú no eras más que un simple estudiante que se hacía pajas con las compañeras del bus universitario."
            bunbury "¿Cómo le voy a enseñar esto a Malú? No me va a pagar y necesito tinte y un sombrero mejor, que la paja se desgasta, ¡joder!"
            pov "Pues que cante la canción pero en otro ritmo, en el estilo que cante ella. El que sea."
            bunbury "Mmmm... Sí, creo que canta rumba pop o una mierda de esas."
            extend " No es mala idea... Incluso podría abrir una nueva línea de negocio."
            bunbury "¡Muchas gracias! Tenéis mis votos."
            $ puntosj += 3
            bunbury "Y ahora, ¡dejadmé! que yo no tengo la culpa de veros caer."
            c "Adiós, Quique."
            jump mapa
        else:
            bunbury "Veamos..."
            bunbury "[letra1] "
            extend "[letra2] "
            extend "[letra3] "
            extend "[letra4] "
            bunbury "..."
            bunbury "A ver, cosas peores he cantado."
            pov "¿Como Lady Blue?"
            bunbury "No, esa era buena."
            bunbury "En cualquier caso, como no es para mí..."
            bunbury "No me parece que sea muy del estilo de Malú, pero tampoco sabria decirte cual es, así que mira, mejor esto que nada."
            bunbury "Creo que podría colársela."
            bunbury "Eso sí, solo os voy a dar dos votos. El rock es sufrimiento y no puedo ser el vehículo de una felicidad plena si os los diera todos."
            $ puntosj += 2
            c "No te preocupes. Con dos es más que suficiente para aplastar a los inútiles de mis rivales."
            bunbury "Y ahora, ¡dejadmé! que yo no tengo la culpa de veros caer."
            c "Adiós, Quique."
            jump mapa
    
    jump mapa