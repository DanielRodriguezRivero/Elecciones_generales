# there needs to be 4 players at the moment, I don't think the implementation is all there for players < 4 yet
# there can be 1, 2, 3 monsters, just make sure you define that
# player dead should work but there might be bugs that I haven't fixed yet
# look at how the script is set up in script.rpy and then go through it in battle.rpy to see how it works behind the scenes


image bb = im.FactorScale("images/gymvigo.jpg", 1.0)
init python:
    #custom bar HP
    style.bar_hp = Style(style.default)
    style.bar_hp.left_bar = Frame("battle/hp.png",20, 20)
    style.bar_hp.right_bar = Frame("battle/empty_bar.png", 20, 20)
    style.bar_hp.xmaximum = 181 # bar width
    style.bar_hp.ymaximum = 28 # bar height 
    #custom bar MP
    style.bar_mp = Style(style.default)
    style.bar_mp.left_bar = Frame("battle/mp.png",20, 20)
    style.bar_mp.right_bar = Frame("battle/empty_bar.png", 20, 20)
    style.bar_mp.xmaximum = 181 # bar width
    style.bar_mp.ymaximum = 28 # bar height 
    
    style.battlebutton = Style(style.button)
    style.battlebutton.xminimum = 150
    style.battlebutton.yminimum = 30
    style.battlebutton_text = Style(style.text)
    style.battlebutton_text.size = 31
    style.battlebutton_text.outlines = [(1, "#000000", 0, 0)]
    style.battlebutton_text.hover_size = 31
    style.battlebutton_text.hover_outlines = [(2, "#E28308", 0, 0)]
    
   
label battle_def:#you usually call this in the very beginning of your game, it will set up all the variables being used for the battle system

####You can change everything below##################################################################################
#the base stats for the four characters
    #warrior type class
    $ player1_hp_max = 50
    $ player1_mp_max = 100    
    $ player1_attack = 12
    $ player1_defense = 20


    #thief type class
    $ player2_hp_max = 50
    $ player2_mp_max = 70    
    $ player2_attack = 17
    $ player2_defense = 15
 
    
    # archer-ish type class
    $ player3_hp_max = 50
    $ player3_mp_max = 150    
    $ player3_attack = 14
    $ player3_defense = 12
    
    # mage type
    $ player4_hp_max = 50
    $ player4_mp_max = 300    
    $ player4_attack = 15
    $ player4_defense = 10
####You can change everything above##################################################################################

    # default for message, leave it as is
    #check the battle_message screen to see how this is used
    $ message = "none"
    
    $ player1_hp = player1_hp_max
    $ player2_hp = player2_hp_max
    $ player3_hp = player3_hp_max
    $ player4_hp = player4_hp_max
    $ player1_mp = player1_mp_max
    $ player2_mp = player2_mp_max
    $ player3_mp = player3_mp_max
    $ player4_mp = player4_mp_max
    $ player1_dead = False
    $ player2_dead = False
    $ player3_dead = False
    $ player4_dead = False
    
    
    return
    
label battle_presetup: 
    
    #this all the variables needed before you call battle each time
####You can change everything below##################################################################################
    # right now, it is all in one set up but it can be seperated for more variety of monsters
    # your player names and the image being used for them, please take a look at how images are used in the battle folder so you understand the size of each image should be
    $ player1 = "Coletas" #names, set as none to not display image
    $ player2 = "Staline"
    $ player3 = "Tú"
    $ player4 = "none"
    $ p1name = "Coletas" #name only field, so the status messages do not say "none"
    $ p2name = "Staline"
    $ p3name = "Tú"
    $ p4name = "Menchenique"
    $ player1_image_selected = "battle/player1_selected.png" #the images
    $ player1_image_default = "battle/player1_default.png"
    $ player2_image_selected = "battle/player2_selected.png" #the images
    $ player2_image_default = "battle/player2_default.png"
    $ player3_image_selected = "battle/player3_selected.png" #the images
    $ player3_image_default = "battle/player3_default.png"
    $ player4_image_selected = "battle/player4_selected.png" #the images
    $ player4_image_default = "battle/player4_default.png"
    # number of players, and the default is turn based so player goes first then monster afterwards and repeat
    $ player_numbers = 3 
    $ turn = 1 #turn starts with player 1
    $ m_turn = 1 #starts with monster1
    $ player_turn = "Coletas"
    $ monster_turn = "monster1"
    $ check_win = False

    
    # if you want your player is start with full hp each battle, if not, you tinker around with this code
    # so maybe you might comment it out if you want the player's hp to remain what it was

#    $ player1_hp = player1_hp_max
#    $ player2_hp = player2_hp_max
#    $ player3_hp = player3_hp_max
#    $ player4_hp = player4_hp_max
#    $ player1_mp = player1_mp_max
#    $ player2_mp = player2_mp_max
#    $ player3_mp = player3_mp_max
#    $ player4_mp = player4_mp_max
#    $ player1_dead = False
#    $ player2_dead = False
#    $ player3_dead = False
#    $ player4_dead = False
    
    
    #the monster's graphics, hp points max and the range of their attack
    # example: monster 1 is a white sheep using sheep1.png for the image
    # it can attack between 10 to 30 damage on the player and has an hp of 100
    # you can get fancy with this but at the moment, you have a max of 3 monsters that can be on the battle field 
    $ monster1 = "M. Rajao"
    $ monster2 = "none"
    $ monster3 = "none" #if you want only two monsters on the field, replace this with $ monster 3 = "none" and make $ monster3_dead = True (see below)
    $ monster1_image = "battle/sheep1.png"
    $ monster2_image = "battle/sheep2.png"
    
    $ monster3_image = "battle/chest1.png"
    $ monster1_hp_max = 100
    $ monster2_hp_max = 100
    $ monster3_hp_max = 100
    $ monster1_hp = monster1_hp_max
    $ monster2_hp = monster2_hp_max
    $ monster3_hp = monster3_hp_max
    $ monster1_attack_min = 10
    $ monster1_attack_max = 30
    $ monster2_attack_min = 15
    $ monster2_attack_max = 25
    $ monster3_attack_min = 5
    $ monster3_attack_max = 20
    # the number of monsters, if you use less monster then you would need to change this number too
    $ monster_numbers = 3
    $ monster1_dead = False
    $ monster2_dead = True
    $ monster3_dead = True # make this true if you don't want a third monster on the field, remember to set monster3 = "none" too
    
    $ monster_life = monster1_hp + monster2_hp + monster3_hp
    
####You can change everything above##################################################################################
    
    #default values, leave it as is
    $ damage = 1
    $ m_damage = 1
    $ p_skill = "none" #player skill being used
    $ m_target = "none" #the player the monster is targetting
    $ monster_target = 0
    $ p_action = "none"
    $ player1_defend = False
    $ player2_defend = False
    $ player3_defend = False
    $ player4_defend = False
    $ target = "none" #monster1,2,3

    return

#################################################################################################################
label battle: # the battle screen uses this general set up
    play music "battle.mp3"
    show screen battle_overlay_players
    show screen battle_overlay_monsters
    show screen battle_message
    jump battling
label battling:
    call player_turn from _call_player_turn
    $ turn = 0 #this is so that player 1 is not 'selected', that wouldn't make sense when it's not their turn
    if check_win == True:
        jump battle_win
    call monster_turn from _call_monster_turn
    $ m_turn = 1
    $ turn = 1
    $ player1_defend = False
    $ player2_defend = False
    $ player3_defend = False
    $ player4_defend = False
    jump battling
    
    
label battle_win: #the aftermath message
    "¡Has ganado!"
    $ turn = 0
    $ puntosj += 3 #los puntos que recibes al ganar
    $ m_turn = 0
    $ player_turn = "none"
    hide screen battle_overlay_players
    hide screen battle_overlay_monsters
    hide screen battle_message
    hide screen player_actions
    return


#################################################################################################################


label player_turn:
    while player_numbers >= turn:
        if turn == 1:
            if player1_dead:
                "[p1name] está inconsciente."
                #$ message = "player_dead_message"
            else:
                $ message = "player1_turn"
                $ player_turn = player1
                call screen player_actions  
                $ p_action = _return
                call player_dealt_damage from _call_player_dealt_damage
        elif turn == 2:
            if player2_dead:
                "[p2name] está inconsciente."
                #$ message = "player_dead_message"
            else:
                $ message = "player2_turn"
                $ player_turn = player2
                call screen player_actions  
                $ p_action = _return
                call player_dealt_damage from _call_player_dealt_damage_1
        elif turn == 3:
            if player3_dead:
                "[p3name] está inconsciente."
                #$ message = "player_dead_message"
            else:
                $ message = "player3_turn"
                $ player_turn = player3
                call screen player_actions  
                $ p_action = _return
                call player_dealt_damage from _call_player_dealt_damage_2
        elif turn == 4:
            if player4_dead:
                "[p4name] está inconsciente."
                #$ message = "player_dead_message"
            else:
                $ message = "player4_turn"
                $ player_turn = player4
                call screen player_actions  
                $ p_action = _return
                call player_dealt_damage from _call_player_dealt_damage_3
        #call screen player_actions  
        #$ p_action = _return
        #call player_dealt_damage
        call monster_dead_check from _call_monster_dead_check
        call player_dead_check from _call_player_dead_check
        if check_win:
            jump battle_win
        else:
            $ turn += 1
    return
    
label player_dealt_damage:
    $ target = "none"
    if player_turn == player1:
        if p_action == "attack":
            $ damage = player1_attack
        elif p_action == "skills":
            call player1_skills from _call_player1_skills
        elif p_action == "defend":
            $ damage = -1
            $ player1_defend = True
        
    elif player_turn == player2:
        if p_action == "attack":
            $ damage = player2_attack
        elif p_action == "skills":
            call player2_skills from _call_player2_skills
        elif p_action == "defend":
            $ damage = -1
            $ player2_defend = True
    elif player_turn == player3:
        if p_action == "attack":
            $ damage = player3_attack
        elif p_action == "skills":
            call player3_skills from _call_player3_skills 
        elif p_action == "defend":
            $ damage = -1
            $ player3_defend = True
    elif player_turn == player4:
        if p_action == "attack":
            $ damage = player4_attack
        elif p_action == "skills":
            call player4_skills from _call_player4_skills
        elif p_action == "defend":
            $ damage = -1
            $ player4_defend = True
    if damage < 0:
        return
    else:
        call screen player_target
        $ target = _return
        if target == "monster1":
            $ monster1_hp = monster1_hp - damage
            call monster_dead_check from _call_monster_dead_check_1
        elif target == "monster2":
            $ monster2_hp = monster2_hp - damage
            call monster_dead_check from _call_monster_dead_check_2
        elif target == "monster3":
            $ monster3_hp = monster3_hp - damage
            call monster_dead_check from _call_monster_dead_check_3
        elif target == "all":
            $ monster1_hp = monster1_hp - damage
            $ monster2_hp = monster2_hp - damage
            $ monster3_hp = monster3_hp - damage
            call monster_dead_check from _call_monster_dead_check_4
        if p_action == "attack":
            $ message = "player_attack"
        elif p_action == "skills":
            $ message = "player_skill"
        $ renpy.pause(1.0)
        return

label player1_skills:
    hide screen battle_overlay_players
    call screen noel_skills
    $ p_skill = _return
    if p_skill == "Latigazo Coleta":
        $ player1_mp = player1_mp - 10
        $ damage = player1_attack * 2
    elif p_skill == "Dolor Bolivariano":
        $ player1_mp = player1_mp - 15
        $ damage = player1_attack*4
    elif p_skill == "Daño de Maduro":
        $ player1_mp = player1_mp - 20
        $ damage = player1_attack * 6
    elif p_skill == "Expropiación":
        $ player1_mp = player1_mp - 25
        $ damage = player1_attack*5
        $ target = "all"
    elif p_skill == "Spain´s Crush":
        $ player1_mp = player1_mp - 30
        $ damage = player1_attack * 10
        $ target = "all"
    elif p_skill == "Catapulta Infernal":
        $ player1_mp = player1_mp - 35
        $ damage = player1_attack*3
        $ target = "all"
    elif p_skill == "Monedero´ Trial":
        $ player1_mp = player1_mp - 40
        $ damage = player1_attack * 5 
    show screen battle_overlay_players
    return
    
label player2_skills:
    hide screen battle_overlay_players
    call screen kuroi_skills
    $ p_skill = _return
    if p_skill == "Soviet Crunch":
        if player2_mp >= 10:
            $ player2_mp = player2_mp - 10
            $ damage = player2_attack * 2
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    elif p_skill == "Trotski´ Piolet":
        if player2_mp >= 15:
            $ player2_mp = player2_mp - 15
            $ damage = player2_attack*4
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    elif p_skill == "Das Kapital Bomb":
        if player2_mp >= 20:
            $ player2_mp = player2_mp - 20
            $ damage = player2_attack * 6
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    elif p_skill == "Red Kick":
        if player2_mp >= 25:
            $ player2_mp = player2_mp - 25
            $ damage = player2_attack*5
            $ target = "all"
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    elif p_skill == "Gulag Spirit":
        if player2_mp >= 30:
            $ player2_mp = player2_mp - 30
            $ damage = player2_attack * 10
            $ target = "all"
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    elif p_skill == "Soviet ThunderStorm":
        if player2_mp >= 35:
            $ player2_mp = player2_mp - 35
            $ damage = player2_attack*3
            $ target = "all"
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    elif p_skill == "Chernobyl Redux":
        if player2_mp >= 40:
            $ player2_mp = player2_mp - 40
            $ damage = player2_attack * 5
        else:
            #$ message = "player2_nomana"
            "[p2name] no tiene suficiente maná."
    show screen battle_overlay_players
    return
    
label player3_skills:
    hide screen battle_overlay_players
    call screen shiro_skills
    $ p_skill = _return
    if p_skill == "Voto en blanco":
        $ player3_mp = player3_mp - 10
        $ damage = player3_attack * 2
    elif p_skill == "Resistencia Pasiva":
        $ player3_mp = player3_mp - 15
        $ damage = player3_attack*4
    elif p_skill == "Insumisión Fiscal":
        $ player3_mp = player3_mp - 20
        $ damage = player3_attack * 6
    elif p_skill == "Crochet de Izquierda":
        $ player3_mp = player3_mp - 25
        $ damage = player3_attack*5
        $ target = "all"
    elif p_skill == "ThunderBlaster":
        $ player3_mp = player3_mp - 30
        $ damage = player3_attack * 10
        $ target = "all"
    elif p_skill == "Pago en B":
        $ player3_mp = player3_mp - 35
        $ damage = player3_attack*3
        $ target = "all"
    elif p_skill == "Crítica en Twitter":
        $ player3_mp = player3_mp - 40
        $ damage = player3_attack * 5
    show screen battle_overlay_players
    return
    
label player4_skills:
    hide screen battle_overlay_players
    call screen luna_skills
    $ p_skill = _return
    if p_skill == "Magic Attack 1":
        $ damage = player4_attack * 2
        $ player4_mp = player4_mp - 10
    elif p_skill == "Magic Attack 2":
        $ damage = player4_attack*4
        $ player4_mp = player4_mp - 15
    elif p_skill == "Magic Attack 3":
        $ damage = player4_attack * 6
        $ player4_mp = player4_mp - 20
    elif p_skill == "Magic Attack 4":
        $ damage = player4_attack*5
        $ player4_mp = player4_mp - 25
        $ target = "all"
    elif p_skill == "Magic Attack 5":
        $ damage = player4_attack * 10
        $ player4_mp = player4_mp - 30
        $ target = "all"
    elif p_skill == "Magic Attack 6":
        $ damage = player4_attack*3
        $ player4_mp = player4_mp - 40
        $ target = "all"
    elif p_skill == "Magic Attack 7":
        $ damage = player4_attack * 5
        $ player4_mp = player4_mp - 50
    show screen battle_overlay_players
    return
screen noel_skills:
    add "battle/battlebox2.png" xalign 0.2 yalign .99
    textbutton "Latigazo Coleta" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.8 action Return("Latigazo Coleta")  
    textbutton "Dolor Bolivariano" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.8 action Return("Dolor Bolivariano") 
    textbutton "Daño de Maduro" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.85 action Return("Daño de Maduro") 
    textbutton "Expropiación" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.85 action Return("Expropiación")
    textbutton "Spain´s Crush" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.9 action Return("Spain´s Crush")
    textbutton "Catapulta Infernal" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.9 action Return("Catapulta Infernal")
    textbutton "Monedero´ Trial" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.95 action Return("Monedero´ Trial")    
screen kuroi_skills:
    add "battle/battlebox2.png" xalign 0.2 yalign .99
    textbutton "Soviet Crunch" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.8 action Return("Soviet Crunch")  
    textbutton "Trotski´ Piolet" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.8 action Return("Trotski´ Piolet") 
    textbutton "Das Kapital Bomb" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.85 action Return("Das Kapital Bomb") 
    textbutton "Red Kick" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.85 action Return("Red Kick")
    textbutton "Gulag Spirit" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.9 action Return("Gulag Spirit")
    textbutton "Soviet ThunderStorm" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.9 action Return("Soviet ThunderStorm")
    textbutton "Chernobyl Redux" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.95 action Return("Chernobyl Redux") 
screen shiro_skills:
    add "battle/battlebox2.png" xalign 0.2 yalign .99
    textbutton "Voto en blanco" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.8 action Return("Voto en blanco")  
    textbutton "Resistencia Pasiva" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.8 action Return("Resistencia Pasiva") 
    textbutton "Insumisión Fiscal" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.85 action Return("Insumisión Fiscal") 
    textbutton "Crochet de Izquierda" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.85 action Return("Crochet de Izquierda")
    textbutton "ThunderBlaster" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.9 action Return("ThunderBlaster")
    textbutton "Pago en B" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.9 action Return("Pago en B")
    textbutton "Crítica en Twitter" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.95 action Return("Crítica en Twitter") 
screen luna_skills:
    add "battle/battlebox2.png" xalign 0.2 yalign .99
    textbutton "Magic Attack 1" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.8 action Return("Magic Attack 1")  
    textbutton "Magic Attack 2" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.7 yalign 0.8 action Return("Magic Attack 2") 
    textbutton "Magic Attack 3" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.85 action Return("Magic Attack 3") 
    textbutton "Magic Attack 4" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.7 yalign 0.85 action Return("Magic Attack 4")
    textbutton "Magic Attack 5" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.9 action Return("Magic Attack 5")
    textbutton "Magic Attack 6" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.7 yalign 0.9 action Return("Magic Attack 6")
    textbutton "Magic Attack 7" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.1 yalign 0.95 action Return("Magic Attack 7") 
label monster_turn:
    while monster_numbers >= m_turn:
        if m_turn == 1:
            if monster1_dead:
                pass
            else:
                call player_dead_check from _call_player_dead_check_1
                $ monster_turn = "monster1"
                call monster_dealt_damage from _call_monster_dealt_damage
                $ message = "monster1_attack"
        elif m_turn == 2:
            if monster2_dead:
                pass
            else:
                call player_dead_check from _call_player_dead_check_2
                $ monster_turn = "monster2"
                call monster_dealt_damage from _call_monster_dealt_damage_1
                $ message = "monster2_attack"
        elif m_turn == 3:
            if monster3_dead:
                pass
            else:
                call player_dead_check from _call_player_dead_check_3
                $ monster_turn = "monster3"
                call monster_dealt_damage from _call_monster_dealt_damage_2
                $ message = "monster3_attack"

        $ renpy.pause(1.5)
        $ m_turn += 1
    return

label monster_dealt_damage:
    if monster_turn == "monster1":
        $ m_damage = renpy.random.randint(monster1_attack_min,monster1_attack_max)
    elif monster_turn == "monster2":
        $ m_damage = renpy.random.randint(monster1_attack_min,monster1_attack_max)
    elif monster_turn == "monster3":
        $ m_damage = renpy.random.randint(monster1_attack_min,monster1_attack_max)
    $ monster_target = renpy.random.randint(1,player_numbers)
    if monster_target == 1:
        if player1_hp >= 1:

            if player1_defend:
                $ m_damage = m_damage - player1_defense
                if m_damage < 0: #so there's no negative values
                        $ m_damage = 0
            $ player1_hp = player1_hp - m_damage
            $ m_target = player1
        else:
            $ player1_dead = True
            $ monster_target = renpy.random.randint(1,player_numbers)
            return 

    elif monster_target == 2:
        if player2_hp >= 1:
 
            if player2_defend:
                $ m_damage = m_damage - player2_defense
                if m_damage < 0:
                    $ m_damage = 0
            $ player2_hp = player2_hp - m_damage
            $ m_target = player2
        else:
            $ player2_dead = True
            $ monster_target = renpy.random.randint(1,player_numbers)
            return     
    elif monster_target == 3:
        if player3_hp >= 1:

            if player3_defend:
                $ m_damage = m_damage - player3_defense
                if m_damage < 0:
                    $ m_damage = 0
            $ player3_hp = player3_hp - m_damage
            $ m_target = player3
        else:
            $ player3_dead = True
            $ monster_target = renpy.random.randint(1,player_numbers)
            return
    elif monster_target == 4:
        if player4_hp >= 1:

            if player4_defend:
                $ m_damage = m_damage - player4_defense
                if m_damage < 0:
                    $ m_damage = 0
            $ player4_hp = player4_hp - m_damage
            $ m_target = player4
        else:
            $ player4_dead = True
            $ monster_target = renpy.random.randint(1,player_numbers)
            return        
    return
    
label monster_dead_check:
    if monster1_dead == monster2_dead == monster3_dead == True:
        $ check_win = True
        $ monster1 = "none"
        $ monster2 = "none"
        $ monster3 = "none"
        return 
    if monster1_hp <=0:
        $ monster1_dead = True
        $ monster1 = "none"
    if monster2_hp <=0:
        $ monster2_dead = True
        $ monster2 = "none"
    if monster3_hp <=0:
        $ monster3_dead = True
        $ monster3 = "none"
    return 

label player_dead_check:
    if player1_hp <= 0:
        $ player1_dead = True
        $ player1 = "none"
    if player2_hp <= 0:
        $ player2_dead = True
        $ player2 = "none"
    if player3_hp <= 0:
        $ player3_dead = True
        $ player3 = "none"
    if player4_hp <= 0:
        $ player4_dead = True
        $ player4 = "none"
    if player1_hp <= 0 and player2_hp <= 0 and player3_hp <= 0 and player4_hp <= 0:
        "Estáis todos inconscientes"
        jump battle_lose
        #$ renpy.full_restart() # returns to main menu, game over 
    else:
        return
screen battle_overlay_players:
    add "battle/battlebox2.png" xalign 0.05 yalign .99
    add "battle/battlebox1.png" xalign .99 yalign .99
    #player 1 is assume to always exist
    if turn == 1:
        add player1_image_selected xalign 0.03 yalign .97        
    else:
        add player1_image_default xalign 0.03 yalign .97
    bar:
        xalign .032
        yalign .92
        style "bar_hp"
        value player1_hp xmaximum 181
        range player1_hp_max
    bar:
        xalign .032
        yalign .96
        style "bar_mp"
        value player1_mp xmaximum 181
        range player1_mp_max
    text"[player1_hp]/[player1_hp_max]" xalign 0.05 yalign 0.92
    text"[player1_mp]/[player1_mp_max]" xalign 0.05 yalign 0.96
    
    if player2 != "none":
       
        if turn == 2:
            add player2_image_selected xalign 0.26 yalign .97        
        else:
            add player2_image_default xalign 0.26 yalign .97
        bar:
            xalign .26
            yalign .92
            style "bar_hp"
            value player2_hp xmaximum 181
            range player2_hp_max
        bar:
            xalign .26
            yalign .96
            style "bar_mp"
            value player2_mp xmaximum 181
            range player2_mp_max
        text"[player2_hp]/[player2_hp_max]" xalign 0.26 yalign 0.92
        text"[player2_mp]/[player2_mp_max]" xalign 0.26 yalign 0.96   
        
    if player3 != "none":
      
        if turn==3:
            add player3_image_selected xalign 0.49 yalign .97
        else:
            add player3_image_default xalign 0.49 yalign .97
        bar:
            xalign .49
            yalign .92
            style "bar_hp"
            value player3_hp xmaximum 181
            range player3_hp_max
        bar:
            xalign .49
            yalign .96
            style "bar_mp"
            value player3_mp xmaximum 181
            range player3_mp_max
        text"[player3_hp]/[player3_hp_max]" xalign 0.47 yalign 0.92
        text"[player3_mp]/[player3_mp_max]" xalign 0.47 yalign 0.96  
        
    if player4 != "none":

        if turn == 4:
            add player4_image_selected xalign 0.73 yalign .97
        else:
            add player4_image_default xalign 0.73 yalign .97
        bar:
            xalign .73
            yalign .92
            style "bar_hp"
            value player4_hp xmaximum 181
            range player4_hp_max
        bar:
            xalign .73
            yalign .96
            style "bar_mp"
            value player4_mp xmaximum 181
            range player4_mp_max
        text"[player4_hp]/[player4_hp_max]" xalign 0.68 yalign 0.92
        text"[player4_mp]/[player4_mp_max]" xalign 0.68 yalign 0.96  

screen battle_overlay_monsters:
    if monster1 != "none":
        add monster1_image xalign 0.5 yalign 0.45
        bar:
            xalign .5
            yalign .3
            style "bar_hp"
            value monster1_hp xmaximum 181
            range monster1_hp_max
        text "[monster1_hp]/[monster1_hp_max]" xalign 0.5 yalign 0.3
    if monster2 != "none":
        add monster2_image xalign 0.2 yalign 0.6
        bar:
            xalign .2
            yalign .5
            style "bar_hp"
            value monster2_hp xmaximum 181
            range monster2_hp_max
        text "[monster2_hp]/[monster2_hp_max]" xalign 0.22 yalign 0.5
    
    if monster3 != "none":
        add monster3_image xalign 0.8 yalign 0.6
        bar:
            xalign .8
            yalign .5
            style "bar_hp"
            value monster3_hp xmaximum 181
            range monster3_hp_max
        text "[monster3_hp]/[monster3_hp_max]" xalign 0.75 yalign 0.5


screen battle_message:
    add "battle/messagebox.png" xalign 0 yalign 0
    if message == "player1_turn":
        text "¿Qué hará [p1name]?" xalign 0.02 yalign 0.05
    elif message == "player2_turn":
        text "¿Qué hará [p2name]?" xalign 0.02 yalign 0.05
    elif message == "player3_turn":
        text "¿Qué harás [p3name]?" xalign 0.02 yalign 0.05
    elif message == "player4_turn":
        text "¿Qué hará [p4name]?" xalign 0.02 yalign 0.05
        
    if message == "player_attack":
        text "¡[player_turn] ataca! ¡Causa [damage] de daño!" xalign 0.02 yalign 0.05
    if message == "player_skill":
        text "¡[player_turn] usó [p_skill]! ¡Causa [damage] de daño!" xalign 0.02 yalign 0.05

        
    elif message == "monster1_attack":
        text "¡[monster1] ataca! ¡[m_target] recibe [m_damage] de daño!" xalign 0.02 yalign 0.05
    elif message == "monster2_attack":
        text "¡[monster2] ataca! ¡[m_target] recibe [m_damage] de daño!" xalign 0.02 yalign 0.05
    elif message == "monster3_attack":
        text "¡[monster3] ataca! ¡[m_target] recibe [m_damage] de daño!" xalign 0.02 yalign 0.05
    
    #elif message == "player2_nomana":
    #    text "[p2name] doesn't have enough mana." xalign 0.02 yalign 0.05
        
    
    #if message == "player_dead_message":
    #    text "[player_turn] is dead." xalign 0.02 yalign 0.05
        

    

        

screen player_actions: #returns for player action
    textbutton "Ataque" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.97 yalign 0.81 action Return("attack") 
    textbutton "Especial" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.98 yalign 0.86 action Return("skills") 
    textbutton "Defensa" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.98 yalign 0.91 action Return("defend") #damage from monster is lowered depending on player's defense
    #textbutton "Items" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.95 yalign 0.96 action Return("items") #not implemented yet

screen player_target: #returns monster player wants to attack
    if target == "all":
        textbutton "Todos los enemigos" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.7 action Return("all")
    else:
        if monster1 != "none":
            textbutton "[monster1]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.5 yalign 0.7 action Return("monster1") 
        if monster2 != "none":
            textbutton "[monster2]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.2 yalign 0.4 action Return("monster2") 
        if monster3 != "none":
            textbutton "[monster3]" style "battlebutton" text_style "battlebutton_text" background "battle/transparent.png" xalign 0.8 yalign 0.4 action Return("monster3") 

label battle_lose: #the aftermath message
    "¡Has perdido, y contigo, una oportunidad de ganar un voto!"
    hide screen battle_overlay_players
    hide screen battle_overlay_monsters
    hide screen battle_message
    return

