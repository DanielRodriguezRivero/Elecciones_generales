label chinos:
        portero1 "Enseña esa mano."
        pov "Mmm, a ver cuántas cojo..."
        $ respuesta = renpy.input("Número de monedas")
        $ chinos = renpy.random.randint(0, 3)
        $ chinos3 = renpy.random.randint(0, 6)
        $ chinos2 = renpy.random.randint(0, 6)
        portero1 "¿Cuántas dices que hay en total?"
        $ totalrespuesta = renpy.input("Respuesta:")
        $ totalchinos = int(respuesta) + int(chinos)
        portero1 "Yo digo...[chinos3]"
        if int(totalrespuesta) == totalchinos:
            if totalchinos == chinos3:
                portero1 "Abre la mano..."
                portero1 "Tú tienes [respuesta] y yo [chinos]."
                portero1 "Vaya, un empate. Hemos dicho lo mismo."
            else:
                portero1 "Abre la mano..."
                portero1 "Tú tienes [respuesta] y yo [chinos]."
                portero1 "Has ganado."
                portero1 "Qué suerte has tenido, malandrín."
        elif int(totalchinos) == chinos3:
            portero1 "Abre la mano..."
            portero1 "Tú tienes [respuesta] y yo [chinos]."
            portero1 "He ganado. Lástima que no estemos jugando al dinero. Poco me pagan para apostármelo."
        else:
            portero1 "Abre la mano..."
            portero1 "Tú tienes [respuesta] y yo [chinos]."
            portero1 "No ha acertado ninguno."
                
        $ portero1("¿Quieres seguir jugando?", interact=False)
        menu:
            "Mientras no salga el otro...":
                jump chinos
            "He llegado a mi límite.":
                portero1 "Hemos echado un rato bueno."
                pov "Y que lo digas."
                k "Ya estoy aquí."
                extend " Uff, me han dejado seco."
                k "Ahí dentro me han dicho que en una de estas casetas está el gimnasio que buscamos. ¿Es eso cierto?"
                portero1 "Ni papa, macho. Ve y pregunta al Anselmo, que ese se las sabe todas."
                portero1 "Está allí, dos manzanas al norte."
                scene caseta2 with fade
                $ renpy.pause(0.5, hard=True)
                show portero2 with dissolve
                portero2 "¿Qué queréis?"
                espejo "Buscamos el gimnasio de Sevilla."
                portero2 "Mmmm, pues igual ahí al lado saben algo. En esta caseta solo se sabe de vicio."
                k "¿Puedo entrar?"
                k "Me llamo Ken Sánchez, filatélico y colombifílico."
                portero2 "A ver... "
                extend " Está en la lista."
                k "Luego vuelvo."
                pov "Otra vez lo mismo..."
                espejo "Yo soy disminuida."
                portero2 "Ay, pobrecilla. Ven que te de un abrazo."
                pov "Mientras voy a la caseta de al lado a preguntar."
                scene caseta3 with fade
                $ renpy.pause(0.5, hard=True)
                pov "Qué raro que no haya portero aquí."
                show sorpresa at center with moveinleft
                sorpresa "Eso es porque estás en la Caseta de la Conferencia Episcopal, aquí son todos bienvenidos, moreno."
                pov "Muchas gracias, hermana."
                sorpresa "No me llames así, que no es plan de añadir más pecados a la lista."
                pov "Por ahora no tengo ninguno apuntado."
                sorpresa "Por ahora..."
                stop music
                play sound "alarma.mp3"
                $ renpy.pause(4, hard=True)
                megafonia "Se ha escapado un paciente del ala de psiquiatría del Hospital de La Macarena. Se teme que esté armado y es muy peligroso."
                extend " Si le ve, no le lleve la contraria y espere a que el personal de seguridad se encargue de él."
                sorpresa "Uy, corre que aquí los locos tienen mucho malaje."
                hide sorpresa with moveoutright
                $ renpy.pause(0.4, hard=True)
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
                k "Ya estamos aquí. Venga, no pierdas el tiempo con la juerga que tenemos trabajo que hacer."
                k "La nieta de Gunilla Von Bismarck me ha dicho dónde encontrar el gimnasio."
        
                scene black with dissolve
                $ renpy.pause(0.5, hard=True)
                show gymtextse1:
                    yanchor 0.5 ypos 0.5
                    xanchor 0.5 xpos 0.5
                with dissolve
                $ renpy.pause(0.5, hard=True)
                show gymtextse2:
                    yanchor 0.5 ypos 0.55
                    xanchor 0.5 xpos 0.5
                with dissolve
                $ renpy.pause(3, hard=True)
                scene gymsevilla with fade
                show cuñadosevilla at center
                k "¡Hola!"
                fosforo "¡Hombre! Mi buen amigo Ken Sánchez. Cuánto bueno por aquí."
                espejo "Yo no diría que les una una relación de amistad, precisamente."
                fosforo "Todo se andará."
                extend " Mira, llegas en el momento justo. Estoy en mitad de una partida de \"Béticos vs Sevillistas\" y a mi compañero le han expulsado por antideportiva. ¿Te unes?"
                k "Con gusto. Pero antes quería hablar de..."
                fosforo "Sí, lo de los votos. Esos son tuyos, hombre. Me llegó la circula esta mañana. Tú y yo podemos entendernos, seguro."
                fosforo "No te voy a engañar, no eres mi primera opción, pero mejor tú que... "
                extend "otros."
                k "Quédate aquí mientras, jugador."
                hide cuñadosevilla with moveoutright
                pov "Nunca me dejan participar en nada interesante."
                espejo "Bienvenido a mi mundo."
                pov "Debe de ser duro..."
                espejo "¿Tenerle sobre mí y no poder tocarle?"
                extend " ¿Sentir lo que él siente y no poder abrazarle?"
                espejo "Una tortura, [jugador], una tortura."
                k "¿Vienes, amor mío?"
                espejo "Ay, SIIIIII."
                pov "A ver qué hago mientras yo solo en la feria..."
                scene black
                show textsep:
                    yanchor 0.5 ypos 0.5
                    xanchor 0.5 xpos 0.5
                with dissolve
                $ renpy.pause(3, hard=True)
                scene gymsevilla with fade
                $ renpy.pause(0.5, hard=True)
                espejo "Rápido, [jugador]. Te necesitamos."
                pov "¿Qué queréis ahora?"
                espejo "El Fósforo ha sufrido un vahido y la partida se ha quedado coja. Tienes que cubrir el hueco."
                pov "Seguro que ha dicho esa frase muchas veces en su vida."
                espejo "... "
                extend "Ojalá..."
                scene tablero with fade
                duque "¿Este es el tolai?"
                pov "Tengo nombre."
                duque "Vaya mérito ese. Hasta un perro tiene uno. ¿Tienes acaso un árbol genealógico que se retrotrae 500 años o más?"
                pov "Eso no, pero tengo un rab..."
                k "Sigamos, que ya no queda nada para terminar la partida."
                show finidi at left:
                    ypos 0.7
                duque "Ya se ha jugado esta carta. Ahora es tu turno."
                k "Lanza esta."
                show uefa at right:
                    ypos 0.7
                pov "Si me dices qué cartas usar, ¿para qué me necesitáis?"
                k "Las reglas dicen que siempre debe de haber dos testigos por si la partida acaba en duelo al amanecer o en una pelea a muerte."
                duque "Béticos vs Sevillistas es un juego para hombres."
                k "Y ahora, nuestra jugada maestra."
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
                k "El Fósforo no va a estar muy contento..."
                hide lopera with blinds
                espejo "Menos mal que nos dio los votos antes de desmayarse."
                pov "¿Podemos irnos ya?"
                duque "Cuando queráis la revancha, aquí estaré. Bueno, aquí no, en mi palacete de Usera."
                $ puntosj += 3
                jump mapa