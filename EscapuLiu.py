from PPlay.gameobject import*
from PPlay.gameimage import*
from PPlay.sound import*
from PPlay.window import*
from PPlay.keyboard import*
from PPlay.sprite import*
import random

def movimento_p(plataforma,limite_e,limite_d,limite_c,limite_b,vx,vy):
    plataforma.move_x(vx)
    plataforma.move_y(vy)
    if plataforma.x <=limite_e or plataforma.x>=limite_d:
        vx *= -1
    if plataforma.y <= limite_c or plataforma.y >= limite_b:
        vy *= -1
    return vx, vy

def movimento_g(guarda,limite_e,limite_d,v):
    guarda.move_x(v)
    if guarda.x<=limite_e or guarda.x>=limite_d:
        return v*-1
    else:
        return v

def colisao(animacaod, animacaoe,plataforma,jump_enable,go_down,vp):
    #colisão peach plataformas
    if animacaod.collided(plataforma):
        #colisão cima
        if (animacaod.y+animacaod.height>=plataforma.y) and (animacaod.y+animacaod.height<=plataforma.y+10 ):
            animacaod.set_position(animacaod.x,plataforma.y-animacaod.height)
            animacaoe.set_position(animacaoe.x,plataforma.y-animacaoe.height)
            animacaod.move_x(vp)
            animacaoe.move_x(vp)
            jump_enable = True
        #colisão baixo
        elif (animacaod.y<=plataforma.y+plataforma.height)and (animacaod.y>plataforma.y+plataforma.height-5):
            if ((animacaod.x+animacaod.width)>=plataforma.x) and not(animacaod.x+animacaod.width>=plataforma.x+2) :
                animacaod.set_position(plataforma.x-animacaod.width,animacaod.y)
                animacaoe.set_position(plataforma.x-animacaoe.width,animacaoe.y)
            #colisão lateral esquerda
            elif ((animacaod.x)<=plataforma.x+plataforma.width) and not((animacaod.x)<=plataforma.x+plataforma.width-2):
                animacaod.set_position(plataforma.x+plataforma.width,animacaod.y)
                animacaoe.set_position(plataforma.x+plataforma.width,animacaoe.y)
            else:
                animacaod.set_position(animacaod.x, plataforma.y+plataforma.height)
                animacaoe.set_position(animacaoe.x, plataforma.y+plataforma.height)
                go_down = True
        #colisão lateral
        else:
            #colisão lateral esquerda
            if ((animacaod.x+animacaod.width)>=plataforma.x) and (animacaod.x+20<=plataforma.x+plataforma.width) :
                animacaod.set_position(plataforma.x-animacaod.width,animacaod.y)
                animacaoe.set_position(plataforma.x-animacaoe.width,animacaoe.y)
            #colisão lateral direita
            elif ((animacaod.x)<=plataforma.x+plataforma.width):
                animacaod.set_position(plataforma.x+plataforma.width,animacaod.y)
                animacaoe.set_position(plataforma.x+plataforma.width,animacaoe.y)
    return jump_enable, go_down

def fase0(vida,mana):

    game = True

    while game:
        #Arquivos de som
        """
        mainsound = Sound("sound/trilha.ogg")
        mainsound.play()
        mainsound.sound.set_volume(15/100)
        
        cast = Sound("sound/")
        
        hit = Sound("sound/")
        hit.sound.set_volume(20/100)
        
        abrindo = Sound("sound/")
        morte  = Sound("sound/")
        
        """

        janela = Window(1050,639)
        janela.set_title("EscapuLiu")
        teclado = janela.get_keyboard()
        cursor = janela.get_mouse()


        #Imagens e Sprites
        fundo = GameImage("imagens/cenario.png")
        limit_l = Sprite("imagens/limit.png")
        limit_r = Sprite("imagens/limit.png")

        #peach
        paradod = Sprite("imagens/peach/peach_stand_right.png")
        paradoe = Sprite("imagens/peach/peach_stand_left.png")
        animacaod = Sprite("imagens/peach/peach_right.png",3)
        animacaoe = Sprite("imagens/peach/peach_left.png",3)
        peach_hit = Sprite("imagens/magia_princesa.png",4)

        manabar = Sprite("imagens/manabar.png",4)
        lifepoints = Sprite("imagens/lifepoint.png",4)
        
        animacaoe.set_total_duration(333)
        animacaod.set_total_duration(333)
        peach_hit.set_total_duration(333)


        #mago = Sprite("imagens/mago_1.png")
        #bosshit = Sprite("imagens/mago_poder.png")

        guarda = Sprite("imagens/guard.png")
        smoke = Sprite("imagens/smoke.png",2)

        plataformamana=Sprite("imagens/bloco3.png")
        plataforma3=Sprite("imagens/bloco3.png")
        plataforma= Sprite("imagens/bloco8.png")
        plataformaporta = Sprite("imagens/bloco8.png")
        chave = Sprite("imagens/chave.png")
        potion = Sprite("imagens/potion.png")
        porta = Sprite("imagens/porta.png")

        #Posicionamento inicial
        limit_l.set_position(janela.width/4,0)
        limit_r.set_position(janela.width*3/4,0)
        guarda.set_position(janela.width-2*guarda.width,janela.height-guarda.height)
        manabar.set_position(0,lifepoints.height)
        lifepoints.set_position(15,0)
        porta.set_position(janela.width-porta.width-10,40)
        plataformamana.set_position(0,1.5*(40+porta.height))
        potion.set_position(potion.width,plataformamana.y-potion.height)
        plataforma.set_position(plataformaporta.width,janela.height-190)
        plataformaporta.set_position(janela.width-plataformaporta.width,40+porta.height)
        plataforma3.set_position(plataformaporta.x-plataforma3.width,plataformaporta.y+ 80)
        animacaod.set_position(20,janela.height-animacaod.height)
        chave.set_position(janela.width-2*chave.width,janela.height-2*chave.height)
        paradod.x=paradoe.x=animacaoe.x=animacaod.x
        paradod.y=paradoe.y=animacaoe.y=animacaod.y


        #Variáveis de jogo
        tiro = False
        key = False
        open = False
        pegoumana= False
        bossmorto = False
        pegouchave = False
        pos = 1
        go_down = True
        jump_enable = False
        cont = 0
        vg = 0.5
        vp = 0.3
        limite_eg = 804
        limite_dg = 974
        limite_ep = 0
        limite_dp = janela.width-plataforma.width

        #Mana potion
        pegoumana= False
        
        while True:
            
            fundo.draw()
            plataformaporta.draw()
            plataforma.draw()
            plataformamana.draw()
            plataforma3.draw()
            porta.draw()

            #descida
            if go_down:
                animacaod.move_y(2)
                animacaoe.move_y(2)
            
            #colisão com o chão
            if animacaod.y >= janela.height-animacaod.height:
                animacaod.set_position(animacaod.x,janela.height-animacaod.height)
                jump_enable = True
            if animacaoe.y >= janela.height-animacaod.height:
                animacaoe.set_position(animacaoe.x,janela.height-animacaod.height)
                jump_enable = True
            
            #colisão peach paredes
            if animacaod.x<0:
                animacaod.set_position(0,animacaod.y)
                animacaoe.set_position(0,animacaoe.y)
            if animacaod.x>janela.width-animacaod.width:
                animacaod.set_position(janela.width-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width-animacaoe.width,animacaoe.y)
                
            vg = movimento_g(guarda,limite_eg,limite_dg,vg)
            vp, vy = movimento_p(plataforma,limite_ep,limite_dp,0,0,vp,0)

            
            #movimento
            if(teclado.key_pressed("RIGHT")and not (teclado.key_pressed("LEFT"))):
                animacaod.draw()
                animacaod.update()
                pos = 1
            elif pos == 1:
                paradod.x=paradoe.x=animacaod.x
                paradod.y=paradoe.y=animacaod.y
                paradod.draw()
            if(teclado.key_pressed("LEFT") and not (teclado.key_pressed("RIGHT"))):
                animacaoe.draw()
                animacaoe.update()
                pos = -1
            elif pos == -1:
                paradoe.x=animacaoe.x
                paradoe.y=animacaoe.y
                paradoe.draw()
            animacaod.move_key_x(500*janela.delta_time())
            animacaoe.move_key_x(500*janela.delta_time())
            

            #movimento janela direita

            if (animacaod.x>=janela.width*3/4) and (teclado.key_pressed("RIGHT") or animacaod.collided(plataforma)) and animacaod.x<limit_r.x:
                if animacaod.collided(plataforma):
                    mv = 0.3
                else:
                    mv = 500*janela.delta_time()

                limite_dg -= mv 
                limite_eg -= mv
                limite_dp -= mv 
                limite_ep -= mv
                limit_r.move_x(-mv)
                limit_l.move_x(-mv)
                animacaod.set_position(janela.width*3/4,animacaod.y)
                animacaoe.set_position(janela.width*3/4,animacaoe.y)
                guarda.move_x(-mv)
                porta.move_x(-mv)
                plataformamana.move_x(-mv)
                potion.move_x(-mv)
                plataforma.move_x(-mv)
                plataforma3.move_x(-mv)
                plataformaporta.move_x(-mv)
                chave.move_x(-mv)

            #movimento janela esquerda

            if (animacaod.x+animacaod.width<=janela.width/4) and (teclado.key_pressed("LEFT") or animacaod.collided(plataforma)) and (animacaod.x+animacaod.width>limit_l.x) :
                if animacaod.collided(plataforma):
                    mv = -vp
                    #animacaod.move_x(vp)
                else:
                    mv = 500*janela.delta_time()
        
                limite_dg += mv 
                limite_eg += mv
                limite_dp += mv 
                limite_ep += mv
                limit_l.move_x(mv)
                limit_r.move_x(mv)
                animacaod.set_position(janela.width/4-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width/4-animacaoe.width,animacaoe.y)
                guarda.move_x(mv)
                porta.move_x(mv)
                plataformamana.move_x(mv)
                plataforma3.move_x(mv)
                potion.move_x(mv)
                plataforma.move_x(mv)
                plataformaporta.move_x(mv)
                chave.move_x(mv)
            
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma,jump_enable,go_down,vp)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataformaporta,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataformamana,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma3,jump_enable,go_down,0)
            #pulo
            if teclado.key_pressed("UP") and cont < 100 and jump_enable:
                go_down = False
                animacaod.move_y(-2)
                animacaoe.move_y(-2)
                paradod.move_y(-2)
                paradoe.move_y(-2)
                cont += 1

                #colisao teto
                if animacaod.y <= 0:
                    animacaod.move_y(2)
                    animacaoe.move_y(2)
                    paradod.move_y(2)
                    paradoe.move_y(2)
            else:
                go_down = True
                jump_enable = False
                cont = 0


            
            #Tiro da peach esquerda e direita
            if teclado.key_pressed("SPACE") and not tiro and mana>0:
                mana -= 1
                tiro = True
                peach_hit.set_position(animacaod.x,animacaod.y)
                if pos>0:
                    v = 1
                else:
                    v = -1
            if tiro:
                peach_hit.draw()
                if (peach_hit.x < janela.width) and (peach_hit.x > 0 - peach_hit.width):
                    peach_hit.move_x(v*2.5)
                    peach_hit.update()
                else:
                    tiro = False


            #Aumento de magia(poção)
            if (animacaoe.collided(potion) or animacaod.collided(potion)) and not pegoumana:
                if mana<3: mana += 1
                pegoumana = True

            #Pegar chave
            if (animacaod.collided(chave)) and not pegouchave:
                pegouchave = True

            #Tipos de dano
            if (guarda.collided(peach_hit)) and not bossmorto:
                # smoke.set_position(guarda.x,guarda.y)
                # smoke.frame_duration = [1000,999999999]
                peach_hit.set_position(janela.width+10,peach_hit.y)
                bossmorto = True

            if (guarda.collided(animacaod)) and not bossmorto:
                vida -= 1
                animacaod.set_position(10,janela.height-animacaod.height)
                paradod.x=paradoe.x=animacaoe.x=animacaod.x
                paradod.y=paradoe.y=animacaoe.y=animacaod.y

            
            if not pegoumana:
                potion.draw()
            if not pegouchave:
                chave.draw()
            if not bossmorto:
                guarda.draw()
            # else:
            #     smoke.draw()
            #     smoke.update()
            #Desenhando sprites fixas
            lifepoints.curr_frame = vida
            lifepoints.draw()
            manabar.curr_frame = mana
            manabar.draw()
            janela.update()

            #Condições de saída

                #Morte
            if vida == 0:
                return 0 , 0 , 0

                #Passou de fase
            if pegouchave and (animacaod.x>porta.x and animacaod.x<porta.x + porta.width) and (animacaod.y>porta.y-15 and animacaod.y<porta.y + porta.width):
                return 1,vida,mana

                #Voltar pro menu
            if teclado.key_pressed("ESC") :
                return -1

def fase1(vida,mana):

    game = True

    while game:
        #Arquivos de som
        """
        mainsound = Sound("sound/trilha.ogg")
        mainsound.play()
        mainsound.sound.set_volume(15/100)
        
        cast = Sound("sound/")
        
        hit = Sound("sound/")
        hit.sound.set_volume(20/100)
        
        abrindo = Sound("sound/")
        morte  = Sound("sound/")
        
        """

        janela = Window(1050,639)
        janela.set_title("EscapuLiu")
        teclado = janela.get_keyboard()
        cursor = janela.get_mouse()


        #Imagens e Sprites
        fundo = GameImage("imagens/cenario.png")
        limit_l = Sprite("imagens/limit.png")
        limit_r = Sprite("imagens/limit.png")

        #peach
        paradod = Sprite("imagens/peach/peach_stand_right.png")
        paradoe = Sprite("imagens/peach/peach_stand_left.png")
        animacaod = Sprite("imagens/peach/peach_right.png",3)
        animacaoe = Sprite("imagens/peach/peach_left.png",3)
        peach_hit = Sprite("imagens/magia_princesa.png",4)

        manabar = Sprite("imagens/manabar.png",4)
        lifepoints = Sprite("imagens/lifepoint.png",4)

        animacaoe.set_total_duration(333)
        animacaod.set_total_duration(333)
        peach_hit.set_total_duration(333)


        mago = Sprite("imagens/mago.png")
        magohit = Sprite("imagens/magohit.png")

        guarda = Sprite("imagens/guard.png")
        #smoke = Sprite("imagens/smoke.png",2)

        plataformaovermago = Sprite("imagens/bloco3.png")
        plataformamago = Sprite("imagens/bloco.png")
        plataformaextra = Sprite("imagens/bloco8.png")
        plataforma1=Sprite("imagens/bloco3.png")
        plataforma2 = Sprite("imagens/bloco8.png")
        plataforma3 = Sprite("imagens/bloco3.png")
        plataforma4 = Sprite("imagens/bloco6.png")
        plataforma5 = Sprite("imagens/bloco8.png")
        plataforma6 = Sprite("imagens/bloco3.png")
        chave = Sprite("imagens/chave.png")
        potion = Sprite("imagens/potion.png")
        porta = Sprite("imagens/porta.png")



        #Posicionamento inicial

        #Posicionamento das Plataformas
        plataformaovermago.set_position(380 + plataforma2.width,janela.height-350-150)
        plataformamago.set_position(plataformaovermago.x + 40,janela.height-350)
        plataformaextra.set_position(plataformaovermago.x + 40*5,janela.height-350)
        plataforma1.set_position(0,janela.height-430)
        plataforma2.set_position(300,janela.height-350)
        plataforma3.set_position(520,janela.height-190)
        plataforma4.set_position(1300,janela.height-250)
        plataforma5.set_position(1580,janela.height-430)
        plataforma6.set_position(2100-plataforma6.width,janela.height-paradod.height-40)

        #Interface
        manabar.set_position(0,lifepoints.height)
        lifepoints.set_position(15,0)

        #Itens de fase
        potion.set_position(janela.width-2*potion.width,janela.height-potion.height-5)
        porta.set_position(1700,55)
        chave.set_position(chave.width,plataforma1.y-chave.height-5)

        #Limites da fase
        limit_l.set_position(janela.width*3/8,0)
        limit_r.set_position(1840-(janela.width*1/8),0)

        #Enemy
        mago.set_position(plataformamago.x,plataformamago.y - mago.height)
        guarda.set_position(820,janela.height-guarda.height)

        #Posicionamento da Peach
        animacaod.set_position(10,janela.height-animacaod.height)
        paradod.x=paradoe.x=animacaoe.x=animacaod.x
        paradod.y=paradoe.y=animacaoe.y=animacaod.y


        #Variáveis de jogo

        tiro = False
        key = False
        open = False
        guardamorto = False
        magomorto = False
        pegouchave = False
        pos = 1
        go_down = True
        jump_enable = False
        cont = 0
        vplaty = -0.6
        vplatx = 0
        vg = 0.5
        limitee = 220
        limited = 821

        #Tiro mago
        delay = 2.5 #Tempo entre um tiro e outro
        shoottick = delay


        #mana potion
        pegoumana= False


        while True:

            #Mago e os seus hits (Alcance do tiro na parte do draw)
            magohit.move_x(1.5) #Velocidade do tiro
            shoottick += janela.delta_time()
            if shoottick > delay:
                magohit.set_position(mago.x+30, mago.y+2)
                shoottick = 0


            #if animacaod.x < plataforma4.x + 80 and animacaod.x > plataforma4.x:
            #    print(janela.time_elapsed())

            #if animacaod.x <= plataformaovermago.x + 100 and animacaod.x >= plataformaovermago.x:
            #    print(janela.time_elapsed())

            fundo.draw()
            plataforma6.draw()
            plataforma5.draw()
            plataforma4.draw()
            plataforma3.draw()
            plataforma2.draw()
            plataforma1.draw()
            plataformaextra.draw()
            plataformamago.draw()
            plataformaovermago.draw()

            porta.draw()

            #descida
            if go_down:
                animacaod.move_y(2)
                animacaoe.move_y(2)

            #colisão com o chão
            if animacaod.y >= janela.height-animacaod.height:
                animacaod.set_position(animacaod.x,janela.height-animacaod.height)
                jump_enable = True
            if animacaoe.y >= janela.height-animacaod.height:
                animacaoe.set_position(animacaoe.x,janela.height-animacaod.height)
                jump_enable = True

            #colisão peach paredes
            if animacaod.x<0:
                animacaod.set_position(0,animacaod.y)
                animacaoe.set_position(0,animacaoe.y)
            if animacaod.x>janela.width-animacaod.width:
                animacaod.set_position(janela.width-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width-animacaoe.width,animacaoe.y)



            #movimento
            if(teclado.key_pressed("RIGHT")and not (teclado.key_pressed("LEFT"))):
                animacaod.draw()
                animacaod.update()
                pos = 1
            elif pos == 1:
                paradod.x=paradoe.x=animacaod.x
                paradod.y=paradoe.y=animacaod.y
                paradod.draw()
            if(teclado.key_pressed("LEFT") and not (teclado.key_pressed("RIGHT"))):
                animacaoe.draw()
                animacaoe.update()
                pos = -1
            elif pos == -1:
                paradoe.x=animacaoe.x
                paradoe.y=animacaoe.y
                paradoe.draw()
            animacaod.move_key_x(500*janela.delta_time())
            animacaoe.move_key_x(500*janela.delta_time())

            vg = movimento_g(guarda,limitee,limited,vg)


            #Plataforma móvel
            vplatx, vplaty = movimento_p(plataforma6,0,0,janela.height-430,janela.height-animacaod.height-40,0,vplaty)

            #movimento janela direita
            if (animacaod.x>=janela.width*5/8) and teclado.key_pressed("RIGHT")and animacaod.x<limit_r.x:
                
                limited -= 500*janela.delta_time()
                limitee -= 500*janela.delta_time()
                limit_r.move_x(-500*janela.delta_time())
                limit_l.move_x(-500*janela.delta_time())
                animacaod.set_position(janela.width*5/8,animacaod.y)
                animacaoe.set_position(janela.width*5/8,animacaoe.y)
                guarda.move_x(-500*janela.delta_time())
                mago.move_x(-500*janela.delta_time())
                porta.move_x(-500*janela.delta_time())
                potion.move_x(-500*janela.delta_time())
                plataformaovermago.move_x(-500*janela.delta_time())
                plataformamago.move_x(-500*janela.delta_time())
                plataformaextra.move_x(-500*janela.delta_time())
                plataforma1.move_x(-500*janela.delta_time())
                plataforma2.move_x(-500*janela.delta_time())
                plataforma3.move_x(-500*janela.delta_time())
                plataforma4.move_x(-500*janela.delta_time())
                plataforma5.move_x(-500*janela.delta_time())
                plataforma6.move_x(-500*janela.delta_time())
                chave.move_x(-500*janela.delta_time())

            #movimento janela esquerda
            if (animacaod.x+animacaod.width<=janela.width*3/8) and teclado.key_pressed("LEFT") and animacaod.x+animacaod.width>limit_l.x:
                limited += 500*janela.delta_time()
                limitee += 500*janela.delta_time()
                limit_l.move_x(500*janela.delta_time())
                limit_r.move_x(500*janela.delta_time())
                animacaod.set_position(janela.width*3/8-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width*3/8-animacaoe.width,animacaoe.y)
                guarda.move_x(500*janela.delta_time())
                mago.move_x(500*janela.delta_time())
                porta.move_x(500*janela.delta_time())
                plataformaovermago.move_x(500*janela.delta_time())
                plataformamago.move_x(500*janela.delta_time())
                plataformaextra.move_x(500*janela.delta_time())
                plataforma1.move_x(500*janela.delta_time())
                plataforma2.move_x(500*janela.delta_time())
                potion.move_x(500*janela.delta_time())
                plataforma3.move_x(500*janela.delta_time())
                plataforma4.move_x(500*janela.delta_time())
                plataforma5.move_x(500*janela.delta_time())
                plataforma6.move_x(500*janela.delta_time())
                chave.move_x(500*janela.delta_time())

            jump_enable, go_down = colisao(animacaod,animacaoe,plataformaovermago,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataformamago,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataformaextra,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma1,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma2,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma3,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma4,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma5,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma6,jump_enable,go_down,0)

            #pulo
            if teclado.key_pressed("UP") and cont < 100 and jump_enable:
                go_down = False
                animacaod.move_y(-2)
                animacaoe.move_y(-2)
                paradod.move_y(-2)
                paradoe.move_y(-2)
                cont += 1

                #colisao teto
                if animacaod.y <= 0:
                    animacaod.move_y(2)
                    animacaoe.move_y(2)
                    paradod.move_y(2)
                    paradoe.move_y(2)
            else:
                go_down = True
                jump_enable = False
                cont = 0



            #Tiro da peach esquerda e direita
            if teclado.key_pressed("SPACE") and not tiro and mana>0:
                mana -= 1
                tiro = True
                peach_hit.set_position(animacaod.x,animacaod.y)
                if pos>0:
                    v = 1
                else:
                    v = -1
            if tiro:
                peach_hit.draw()
                if (peach_hit.x < janela.width) and (peach_hit.x > 0 - peach_hit.width):
                    peach_hit.move_x(v*2.5)
                    peach_hit.update()
                else:
                    tiro = False


            #Aumento de magia(poção)
            if (animacaoe.collided(potion) or animacaod.collided(potion)) and not pegoumana:
                if mana<3: mana += 1
                pegoumana = True

            #Pegar chave
            if (animacaod.collided(chave)) and not pegouchave:
                pegouchave = True

            #Tipos de dano

            if (magohit.collided(animacaod)) and magohit.x <= plataformaextra.x + plataformaextra.width and not magomorto:
                vida -= 1
                animacaod.set_position(10,janela.height-animacaod.height)
                paradod.x=paradoe.x=animacaoe.x=animacaod.x
                paradod.y=paradoe.y=animacaoe.y=animacaod.y

            if not magomorto and (mago.collided(peach_hit)):
                magomorto = True
                peach_hit.set_position(janela.width+10,peach_hit.y)

            if (guarda.collided(peach_hit)) and not guardamorto:
                peach_hit.set_position(janela.width+10,peach_hit.y)
                guardamorto = True

            if (guarda.collided(animacaod)) and not guardamorto:
                vida -= 1
                animacaod.set_position(10,janela.height-animacaod.height)
                paradod.x=paradoe.x=animacaoe.x=animacaod.x
                paradod.y=paradoe.y=animacaoe.y=animacaod.y

            #if (magohit.collided()):
            #    vida = 0

            #Desenhando sprites que podem desaparecer
            if not pegoumana:
                potion.draw()
            if not pegouchave:
                chave.draw()
            if not guardamorto:
                guarda.draw()
            # else:
            #     smoke.draw()
            #     smoke.update()

            if not magomorto:
                if magohit.x <= plataformaextra.x + plataformaextra.width: #Alcance do tiro do mago
                    magohit.draw()
                mago.draw()

            #Desenhando sprites fixas
            lifepoints.curr_frame = vida
            lifepoints.draw()
            manabar.curr_frame = mana
            manabar.draw()
            janela.update()

            #Condições de saída

                #Morte
            if vida == 0:
                return 0 , 0 , 0

                #Passou de fase
            if pegouchave and (animacaod.x>porta.x and animacaod.x<porta.x + porta.width) and (animacaod.y>porta.y-15 and animacaod.y<porta.y + porta.width):
                return 1,vida,mana

                #Voltar pro menu
            if teclado.key_pressed("ESC") :
                return -1
            
def fase2(vida,mana):
    game = True

    while game:
        #Arquivos de som
        """
        mainsound = Sound("sound/trilha.ogg")
        mainsound.play()
        mainsound.sound.set_volume(15/100)
        
        cast = Sound("sound/")
        
        hit = Sound("sound/")
        hit.sound.set_volume(20/100)
        
        abrindo = Sound("sound/")
        morte  = Sound("sound/")
        
        """

        janela = Window(1050,639)
        janela.set_title("EscapuLiu")
        teclado = janela.get_keyboard()
        cursor = janela.get_mouse()


        #Imagens e Sprites
        fundo = GameImage("imagens/cenario.png")
        limit_l = Sprite("imagens/limit.png")
        limit_r = Sprite("imagens/limit.png")

        #peach
        paradod = Sprite("imagens/peach/peach_stand_right.png")
        paradoe = Sprite("imagens/peach/peach_stand_left.png")
        animacaod = Sprite("imagens/peach/peach_right.png",3)
        animacaoe = Sprite("imagens/peach/peach_left.png",3)
        peach_hit = Sprite("imagens/magia_princesa.png",4)

        manabar = Sprite("imagens/manabar.png",4)
        lifepoints = Sprite("imagens/lifepoint.png",4)

        animacaoe.set_total_duration(333)
        animacaod.set_total_duration(333)
        peach_hit.set_total_duration(333)


        #mago = Sprite("imagens/mago_1.png")
        #bosshit = Sprite("imagens/mago_poder.png")
        #smoke = Sprite("imagens/smoke.png",2)
            #enemys
        guarda = Sprite("imagens/guard.png")
        magma = Sprite("imagens/magma_block.png")


        #escadas
            #direita
        escada_right_1=Sprite("imagens/bloco1.png")
        escada_right_2=Sprite("imagens/bloco2.png")
        escada_right_3=Sprite("imagens/bloco3.png")
        escada_right_4=Sprite("imagens/bloco4.png")
            #esquerda
        escada_left_1=Sprite("imagens/bloco1.png")
        escada_left_2=Sprite("imagens/bloco2.png")
        escada_left_3=Sprite("imagens/bloco3.png")
        escada_left_4=Sprite("imagens/bloco4.png")

        #pontes
            #baixo
        ponte_baixo_a=Sprite("imagens/bloco1.png")
        ponte_baixo_b=Sprite("imagens/bloco1.png")
        ponte_baixo_c=Sprite("imagens/bloco1.png")
        ponte_baixo_d=Sprite("imagens/bloco1.png")
            #cima
        ponte_cima_a=Sprite("imagens/bloco1.png")
        ponte_cima_b=Sprite("imagens/bloco1.png")
        ponte_cima_c=Sprite("imagens/bloco1.png")

        #moveis
        movel_vertical=Sprite("imagens/bloco3.png")
        movel_horizontal=Sprite("imagens/bloco4.png")

        #chave cage
        cage_floor = Sprite("imagens/bloco7.png")
        cage_wall = Sprite("imagens/blocov5.png")
        cage_right = Sprite("imagens/bloco2.png")
        cage_left = Sprite("imagens/bloco2.png")

        #itens
        chave = Sprite("imagens/chave.png")
        potion_1 = Sprite("imagens/potion.png")
        potion_2 = Sprite("imagens/potion.png")
        porta = Sprite("imagens/porta.png")

        #Posicionamento inicial

            #limites de tela
        limit_l.set_position(janela.width*3/8,0)
        limit_r.set_position(1447-(janela.width*3/8),0)

            #stats
        lifepoints.set_position(15,0)
        manabar.set_position(0,lifepoints.height)

            #enemys
        guarda.set_position(90,216)
        magma.set_position(435,519)

            #plataformas
                #escada direita
        escada_right_1.set_position(1035,479)
        escada_right_2.set_position(1035,519)
        escada_right_3.set_position(1035,559)
        escada_right_4.set_position(1035,599)
                #escada esquerda
        escada_left_1.set_position(395,479)
        escada_left_2.set_position(355,519)
        escada_left_3.set_position(315,559)
        escada_left_4.set_position(275,599)
                #moveis
        movel_horizontal.set_position(458,166)
        movel_vertical.set_position(1218,479)
                #ponte cima
        ponte_cima_a.set_position(715,166)
        ponte_cima_b.set_position(875,166)
        ponte_cima_c.set_position(1035,166)
                #ponte baixo
        ponte_baixo_a.set_position(475,444)
        ponte_baixo_b.set_position(635,444)
        ponte_baixo_c.set_position(795,444)
        ponte_baixo_d.set_position(955,444)
                #cage
        cage_floor.set_position(0,326)
        cage_wall.set_position(280,166)
        cage_left.set_position(200,166)
        cage_right.set_position(0,246)

            #itens
        porta.set_position(1334,484)
        potion_1.set_position(359,474)
        potion_2.set_position(1164,554)
        chave.set_position(200,286)

            #peach
        animacaod.set_position(10,janela.height-paradod.height)
        paradod.x=paradoe.x=animacaoe.x=animacaod.x
        paradod.y=paradoe.y=animacaoe.y=animacaod.y


        #Variáveis de jogo
            #booleanas
        tiro = False
        key = False
        open = False
        pegoumana= False
        pegoumana2 = False
        bossmorto = False
        pegouchave = False
        go_down = True
        jump_enable = False
            #velocidade
        vg = 0.5
        vpx = 0.3
        vpy = -0.3
            #limitadores
        limite_guarda_e = 90
        limite_guarda_d = cage_wall.x-guarda.width
        limite_p1_e = 320
        limite_p1_d = 555
        limite_p2_c = 166
        limite_p2_b = 478
            #pulo
        pos = 1
        cont = 0
            #Mana potion
        pegoumana= False

        while True:
            #drawing
            fundo.draw()
                #plataformas
            cage_floor.draw()
            cage_right.draw()
            cage_left.draw()
            cage_wall.draw()
            escada_left_1.draw()
            escada_left_2.draw()
            escada_left_3.draw()
            escada_left_4.draw()
            escada_right_1.draw()
            escada_right_2.draw()
            escada_right_3.draw()
            escada_right_4.draw()
            ponte_baixo_a.draw()
            ponte_baixo_b.draw()
            ponte_baixo_c.draw()
            ponte_baixo_d.draw()
            ponte_cima_a.draw()
            ponte_cima_b.draw()
            ponte_cima_c.draw()
            movel_horizontal.draw()
            movel_vertical.draw()
                #itens
            porta.draw()
                #enemys

            magma.draw()

            #descida
            if go_down:
                animacaod.move_y(2)
                animacaoe.move_y(2)

            #colisão com o chão
            if animacaod.y >= janela.height-animacaod.height:
                animacaod.set_position(animacaod.x,janela.height-animacaod.height)
                jump_enable = True
            if animacaoe.y >= janela.height-animacaod.height:
                animacaoe.set_position(animacaoe.x,janela.height-animacaod.height)
                jump_enable = True

            #colisão peach paredes
            if animacaod.x<0:
                animacaod.set_position(0,animacaod.y)
                animacaoe.set_position(0,animacaoe.y)
            if animacaod.x>janela.width-animacaod.width:
                animacaod.set_position(janela.width-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width-animacaoe.width,animacaoe.y)

            #movimento guarda
            vg = movimento_g(guarda,limite_guarda_e,limite_guarda_d,vg)
            #movimento plataformas
            vpx, lixo = movimento_p(movel_horizontal,limite_p1_e,limite_p1_d,0,0,vpx,0)
            lixo, vpy = movimento_p(movel_vertical,0,0,206,480,0,vpy)


            #movimento
            if(teclado.key_pressed("RIGHT")and not (teclado.key_pressed("LEFT"))):
                animacaod.draw()
                animacaod.update()
                pos = 1
            elif pos == 1:
                paradod.x=paradoe.x=animacaod.x
                paradod.y=paradoe.y=animacaod.y
                paradod.draw()
            if(teclado.key_pressed("LEFT") and not (teclado.key_pressed("RIGHT"))):
                animacaoe.draw()
                animacaoe.update()
                pos = -1
            elif pos == -1:
                paradoe.x=animacaoe.x
                paradoe.y=animacaoe.y
                paradoe.draw()
            animacaod.move_key_x(500*janela.delta_time())
            animacaoe.move_key_x(500*janela.delta_time())


            #movimento janela direita

            if (animacaod.x>=janela.width*5/8) and (teclado.key_pressed("RIGHT") or animacaod.collided(movel_horizontal)) and animacaod.x<limit_r.x:
                if animacaod.collided(movel_horizontal):
                    mv = 0.3
                else:
                    mv = 500*janela.delta_time()
                #add limites
                limit_l.move_x(-mv)
                limit_r.move_x(-mv)
                limite_guarda_d-= mv
                limite_guarda_e-= mv
                limite_p1_d-= mv
                limite_p1_e-= mv

                #set pos
                animacaod.set_position(janela.width*5/8,animacaod.y)
                animacaoe.set_position(janela.width*5/8,animacaoe.y)
                #move
                cage_floor.move_x(-mv)
                cage_right.move_x(-mv)
                cage_left.move_x(-mv)
                cage_wall.move_x(-mv)
                escada_left_1.move_x(-mv)
                escada_left_2.move_x(-mv)
                escada_left_3.move_x(-mv)
                escada_left_4.move_x(-mv)
                escada_right_1.move_x(-mv)
                escada_right_2.move_x(-mv)
                escada_right_3.move_x(-mv)
                escada_right_4.move_x(-mv)
                ponte_baixo_a.move_x(-mv)
                ponte_baixo_b.move_x(-mv)
                ponte_baixo_c.move_x(-mv)
                ponte_baixo_d.move_x(-mv)
                ponte_cima_a.move_x(-mv)
                ponte_cima_b.move_x(-mv)
                ponte_cima_c.move_x(-mv)
                movel_horizontal.move_x(-mv)
                movel_vertical.move_x(-mv)
                chave.move_x(-mv)
                potion_1.move_x(-mv)
                potion_2.move_x(-mv)
                porta.move_x(-mv)
                guarda.move_x(-mv)
                magma.move_x(-mv)

            #movimento janela esquerda
            if (animacaod.x+animacaod.width<=janela.width*3/8) and (teclado.key_pressed("LEFT") or animacaod.collided(movel_horizontal)) and (animacaod.x+animacaod.width>limit_l.x) :
                if animacaod.collided(movel_horizontal):
                    mv = 0.3
                else:
                    mv = 500*janela.delta_time()
                #add limites
                limit_l.move_x(mv)
                limit_r.move_x(mv)
                limite_guarda_d+= mv
                limite_guarda_e+= mv
                limite_p1_d += mv
                limite_p1_e += mv

                #set pos
                animacaod.set_position(janela.width*3/8-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width*3/8-animacaoe.width,animacaoe.y)
                #move
                cage_floor.move_x(mv)
                cage_right.move_x(mv)
                cage_left.move_x(mv)
                cage_wall.move_x(mv)
                escada_left_1.move_x(mv)
                escada_left_2.move_x(mv)
                escada_left_3.move_x(mv)
                escada_left_4.move_x(mv)
                escada_right_1.move_x(mv)
                escada_right_2.move_x(mv)
                escada_right_3.move_x(mv)
                escada_right_4.move_x(mv)
                ponte_baixo_a.move_x(mv)
                ponte_baixo_b.move_x(mv)
                ponte_baixo_c.move_x(mv)
                ponte_baixo_d.move_x(mv)
                ponte_cima_a.move_x(mv)
                ponte_cima_b.move_x(mv)
                ponte_cima_c.move_x(mv)
                movel_horizontal.move_x(mv)
                movel_vertical.move_x(mv)
                chave.move_x(mv)
                potion_1.move_x(mv)
                potion_2.move_x(mv)
                porta.move_x(mv)
                guarda.move_x(mv)
                magma.move_x(mv)

            #colisoes
            jump_enable, go_down = colisao(animacaod,animacaoe,cage_floor,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,cage_left,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,cage_right,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,cage_wall,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_left_1,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_left_2,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_left_3,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_left_4,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_right_1,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_right_2,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_right_3,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,escada_right_4,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_baixo_a,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_baixo_b,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_baixo_c,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_baixo_d,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_cima_a,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_cima_b,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,ponte_cima_c,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,movel_horizontal,jump_enable,go_down,vpx)
            jump_enable, go_down = colisao(animacaod,animacaoe,movel_vertical,jump_enable,go_down,0)

            #pulo
            if teclado.key_pressed("UP") and cont < 100 and jump_enable:
                go_down = False
                animacaod.move_y(-2)
                animacaoe.move_y(-2)
                paradod.move_y(-2)
                paradoe.move_y(-2)
                cont += 1
                #colisao teto
                if animacaod.y <= 0:
                    animacaod.move_y(2)
                    animacaoe.move_y(2)
                    paradod.move_y(2)
                    paradoe.move_y(2)
            else:
                go_down = True
                jump_enable = False
                cont = 0

            #Tiro da peach esquerda e direita
            if teclado.key_pressed("SPACE") and not tiro and mana>0:
                mana -= 1
                tiro = True
                peach_hit.set_position(animacaod.x,animacaod.y)
                if pos>0:
                    v = 1
                else:
                    v = -1
            if tiro:
                peach_hit.draw()
                if (peach_hit.x < janela.width) and (peach_hit.x > 0 - peach_hit.width):
                    peach_hit.move_x(v*2.5)
                    peach_hit.update()
                else:
                    tiro = False

            #Aumento de magia(poção)
            if (animacaoe.collided(potion_1) or animacaod.collided(potion_1)) and not pegoumana:
                if mana<3:
                    mana += 1
                pegoumana = True
            if (animacaoe.collided(potion_2) or animacaod.collided(potion_2)) and not pegoumana2:
                if mana<3:
                    mana += 1
                pegoumana2 = True

            #Pegar chave
            if (animacaod.collided(chave)) and not pegouchave:
                pegouchave = True

            #Tipos de dano
            if (guarda.collided(peach_hit)) and not bossmorto:
                # smoke.set_position(guarda.x,guarda.y)
                # smoke.frame_duration = [1000,999999999]
                peach_hit.set_position(janela.width+10,peach_hit.y)
                bossmorto = True
            if (guarda.collided(animacaod)) and not bossmorto:
                vida -= 1
                animacaod.set_position(10,janela.height-animacaod.height)
                paradod.x=paradoe.x=animacaoe.x=animacaod.x
                paradod.y=paradoe.y=animacaoe.y=animacaod.y
            if magma.collided(animacaod):
                vida -= 1
                animacaod.set_position(10,janela.height-animacaod.height)
                paradod.x=paradoe.x=animacaoe.x=animacaod.x
                paradod.y=paradoe.y=animacaoe.y=animacaod.y

            #draw coletable itens
            if not pegoumana:
                potion_1.draw()
            if not pegoumana2:
                potion_2.draw()
            if not pegouchave:
                chave.draw()
            if not bossmorto:
                guarda.draw()
            # else:
            #     smoke.draw()
            #     smoke.update()

            #draw stats
            lifepoints.curr_frame = vida
            lifepoints.draw()
            manabar.curr_frame = mana
            manabar.draw()

            janela.update()
            #Condições de saída
                #Morte
            if vida == 0:
                return 0 , 0 , 0

                #Passou de fase
            if pegouchave and (animacaod.x>porta.x and animacaod.x<porta.x + porta.width) and (animacaod.y>porta.y-15 and animacaod.y<porta.y + porta.width):
                return 1,vida,mana

                #Voltar pro menu
            if teclado.key_pressed("ESC") :
                return -1


def fase3(vida,mana):

    game = True

    while game:
        #Arquivos de som
        """
        mainsound = Sound("sound/trilha.ogg")
        mainsound.play()
        mainsound.sound.set_volume(15/100)
        
        cast = Sound("sound/")
        
        hit = Sound("sound/")
        hit.sound.set_volume(20/100)
        
        abrindo = Sound("sound/")
        morte  = Sound("sound/")
        
        """

        janela = Window(1050,639)
        janela.set_title("EscapuLiu")
        teclado = janela.get_keyboard()
        cursor = janela.get_mouse()


        #Imagens e Sprites
        fundo = GameImage("imagens/cenario.png")
        limit_l = Sprite("imagens/limit.png")
        limit_r = Sprite("imagens/limit.png")

        #peach
        paradod = Sprite("imagens/peach/peach_stand_right.png")
        paradoe = Sprite("imagens/peach/peach_stand_left.png")
        animacaod = Sprite("imagens/peach/peach_right.png",3)
        animacaoe = Sprite("imagens/peach/peach_left.png",3)
        peach_hit = Sprite("imagens/magia_princesa.png",4)

        manabar = Sprite("imagens/manabar.png",4)
        lifepoints = Sprite("imagens/lifepoint.png",4)
        healthbar = Sprite("imagens/healthbar.png",6)

        animacaoe.set_total_duration(333)
        animacaod.set_total_duration(333)
        peach_hit.set_total_duration(333)


        rei = Sprite("imagens/reid.png",6)
        rei.set_total_duration(1000)
        reie = Sprite("imagens/reie.png",6)
        reie.set_total_duration(1000)



        plataforma1= Sprite("imagens/bloco3.png")
        plataforma2a = Sprite("imagens/bloco3.png")
        plataforma2b = Sprite("imagens/bloco3.png")
        plataforma2c = Sprite("imagens/bloco3.png")
        plataforma3=Sprite("imagens/bloco3.png")

        chave = Sprite("imagens/chave.png")
        potion = Sprite("imagens/potion.png")
        porta = Sprite("imagens/porta.png")


        #Posicionamento inicial
        limit_l.set_position(janela.width/4,0)
        limit_r.set_position(janela.width*3/4,0)
        manabar.set_position(0,lifepoints.height)
        lifepoints.set_position(15,0)
        healthbar.set_position(janela.width/2-healthbar.width/2, healthbar.height)
        porta.set_position(janela.width-porta.width-10,40)
        potion.set_position(potion.width,plataforma1.y-potion.height)
        plataforma1.set_position(0,janela.height-390)
        plataforma2a.set_position(plataforma1.width,janela.height-190)
        plataforma2b.set_position(plataforma1.width*4,janela.height-190)
        plataforma2c.set_position(plataforma2b.x + plataforma2b.width*2,janela.height-310)
        plataforma3.set_position(janela.width-plataforma1.width,40+porta.height)
        animacaod.set_position(20,janela.height-animacaod.height)
        paradod.x=paradoe.x=animacaoe.x=animacaod.x
        paradod.y=paradoe.y=animacaoe.y=animacaod.y
        rei.set_position(240,janela.height-rei.height)
        reie.set_position(240,janela.height-rei.height)


        #Variáveis de jogo
        tiro = False
        open = False
        pegouchave = False
        pos = 1
        go_down = True
        jump_enable = False
        cont = 0
        vg = 0.5
        vp = 0
        limite_eg = 804
        limite_dg = 974
        limite_ep = 0
        limite_dp = janela.width-plataforma1.width
        vx = 0.5
        vy = 0.5

        #boss
        delay = 2.5 #Tempo entre um tiro e outro
        shoottick = delay
        bossmorto = False
        bossvida = 5
        bullets = []



        #Mana potion
        pegoumana= False
        potions = []
        for i in range(4):
            potions.append(Sprite("imagens/potion.png"))
        potions[0].set_position(plataforma1.x+plataforma1.width/2,plataforma1.y-potions[0].height)
        potions[1].set_position(plataforma2a.x+plataforma1.width/2,plataforma2a.y-potions[0].height)
        potions[2].set_position(plataforma2b.x+plataforma1.width/2,plataforma2b.y-potions[0].height)
        potions[3].set_position(plataforma2c.x+plataforma1.width/2,plataforma2c.y-potions[0].height)

        r = 0
        while True:

            fundo.draw()
            plataforma1.draw()
            plataforma2a.draw()
            plataforma2b.draw()
            plataforma2c.draw()
            plataforma3.draw()
            porta.draw()

            shoottick += janela.delta_time()

            #Tiro Inimigo
            if shoottick > delay and not bossmorto:
                posy = rei.y
                posx = rei.x
                bosshit = Sprite("imagens/rei_poder.png")
                bosshit.set_position(posx, posy)
                bullets.append(bosshit)

                if bosshit.y == bosshit.y and bosshit.x == bosshit.x:
                    bosshit.move_y((-300)* janela.delta_time())
                shoottick = 0

            for kunai in bullets:
                if kunai.collided(animacaod):
                    vida -= 1
                    bullets.remove(kunai)
                kunai.draw()
                kunai.move_y((-400)* janela.delta_time())
                if kunai.y >= janela.height-48:
                     bullets.remove(kunai)

            rei.move_x(vx)
            reie.move_x(vx)

            if rei.x+rei.width >= janela.width or rei.x<=0:
                vx*=-1

            #descida
            if go_down:
                animacaod.move_y(2)
                animacaoe.move_y(2)

            #colisão com o chão
            if animacaod.y >= janela.height-animacaod.height:
                animacaod.set_position(animacaod.x,janela.height-animacaod.height)
                jump_enable = True
            if animacaoe.y >= janela.height-animacaod.height:
                animacaoe.set_position(animacaoe.x,janela.height-animacaod.height)
                jump_enable = True

            #colisão peach paredes
            if animacaod.x<0:
                animacaod.set_position(0,animacaod.y)
                animacaoe.set_position(0,animacaoe.y)
            if animacaod.x>janela.width-animacaod.width:
                animacaod.set_position(janela.width-animacaod.width,animacaod.y)
                animacaoe.set_position(janela.width-animacaoe.width,animacaoe.y)


            #movimento
            if(teclado.key_pressed("RIGHT")and not (teclado.key_pressed("LEFT"))):
                animacaod.draw()
                animacaod.update()
                pos = 1
            elif pos == 1:
                paradod.x=paradoe.x=animacaod.x
                paradod.y=paradoe.y=animacaod.y
                paradod.draw()
            if(teclado.key_pressed("LEFT") and not (teclado.key_pressed("RIGHT"))):
                animacaoe.draw()
                animacaoe.update()
                pos = -1
            elif pos == -1:
                paradoe.x=animacaoe.x
                paradoe.y=animacaoe.y
                paradoe.draw()
            animacaod.move_key_x(500*janela.delta_time())
            animacaoe.move_key_x(500*janela.delta_time())


            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma1,jump_enable,go_down,vp)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma2a,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma2b,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma2c,jump_enable,go_down,0)
            jump_enable, go_down = colisao(animacaod,animacaoe,plataforma3,jump_enable,go_down,0)

            #pulo
            if teclado.key_pressed("UP") and cont < 100 and jump_enable:
                go_down = False
                animacaod.move_y(-2)
                animacaoe.move_y(-2)
                paradod.move_y(-2)
                paradoe.move_y(-2)
                cont += 1

                #colisao teto
                if animacaod.y <= 0:
                    animacaod.move_y(2)
                    animacaoe.move_y(2)
                    paradod.move_y(2)
                    paradoe.move_y(2)
            else:
                go_down = True
                jump_enable = False
                cont = 0

            #Tiro da peach esquerda e direita
            if teclado.key_pressed("SPACE") and not tiro and mana>0:
                mana -= 1
                tiro = True
                peach_hit.set_position(animacaod.x,animacaod.y)
                if pos>0:
                    v = 1
                else:
                    v = -1
            if tiro:
                peach_hit.draw()
                if (peach_hit.x < janela.width) and (peach_hit.x > 0 - peach_hit.width):
                    peach_hit.move_x(v*2.5)
                    peach_hit.update()
                else:
                    tiro = False


            #Aumento de magia(poção)
            if (animacaoe.collided(potions[r]) or animacaod.collided(potions[r])):
                if mana<3:
                    mana += 1
                    r = random.randint(0,3)

            if mana>3:
                mana -= 3

            #Pegar chave
            if (animacaod.collided(chave)) and not pegouchave and bossmorto: #boss morto, em cima da chave e ainda n pegou a chave
                pegouchave = True

            #Tipos de dano
            if(animacaod.collided(rei)) and not bossmorto:
                vida -=1
                animacaod.set_position(20,janela.height-animacaod.height)
                paradod.x=paradoe.x=animacaoe.x=animacaod.x
                paradod.y=paradoe.y=animacaoe.y=animacaod.y
                rei.set_position(240,janela.height-rei.height)
                reie.set_position(240,janela.height-rei.height)

            if (rei.collided(peach_hit)) and not bossmorto:
                bossvida -= 1
                peach_hit.set_position(janela.width+10,peach_hit.y)
                if bossvida == 0:
                    bossmorto = True


            if bossmorto:
                vx = 0
                chave.set_position(rei.x+rei.width/2,rei.y+rei.height/2)


            potions[r].draw()

            if not pegouchave and bossmorto:
                chave.draw()



            if not bossmorto:
                if vx>0 :
                    rei.draw()
                    rei.update()
                else:
                    reie.draw()
                    reie.update()

            #Desenhando sprites fixas
            lifepoints.curr_frame = vida
            healthbar.curr_frame = bossvida
            lifepoints.draw()
            healthbar.draw()
            manabar.curr_frame = mana
            manabar.draw()
            janela.update()

            #Condições de saída

                #Morte
            if vida == 0:
                return 0 , 0 , 0

                #Passou de fase
            if pegouchave and (animacaod.x>porta.x and animacaod.x<porta.x + porta.width) and (animacaod.y>porta.y-15 and animacaod.y<porta.y + porta.width):
                return 1,vida,mana

                #Voltar pro menu
            if teclado.key_pressed("ESC") :
                return -1, -1,-1
