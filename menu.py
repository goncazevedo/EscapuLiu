from PPlay.window import*
from PPlay.gameimage import* 
from PPlay.sprite import*
from PPlay.gameobject import*
from PPlay.mouse import*
from PPlay.sound import*

import fases

def menu():

    mainsound = Sound("sound/sound.ogg")
    mainsound.play()
    mainsound.sound.set_volume(15/100)

    janela = Window(1050,639)
    fundo = GameImage("imagens/menu/tela.png")
    jogar = Sprite("imagens/menu/jogar.png")
    jogar_click = Sprite("imagens/menu/jogar_c.png")
    tutorial = Sprite("imagens/menu/tutorial.png")
    tutorial_click = Sprite("imagens/menu/tutorial_c.png")
    som = Sprite("imagens/menu/som.png")
    som_click = Sprite("imagens/menu/sound_c.png")
    sair = Sprite("imagens/menu/exit.png")
    sair_click = Sprite("imagens/menu/exit_c.png")

    s_som = Sprite("imagens/menu/no_sound.png")
    s_som_click = Sprite("imagens/menu/no_sound_c.png")
    

    mouse = janela.get_mouse()
    sound = True

    jogar.set_position(janela.width/2-jogar.width/2,janela.height/2)
    som.set_position(0,579)
    s_som.set_position(0,579)
    sair.set_position(76,579)
     
    jogar_click.set_position(janela.width/2-jogar.width/2,janela.height/2)
    som_click.set_position(0,579)
    s_som_click.set_position(0,579)
    sair_click.set_position(76,579)

    while True:
        fundo.draw()
        
        if mouse.is_over_object(jogar):
            jogar_click.draw()
            if mouse.is_button_pressed(1):
                fases.selecionafase()
        else:
            jogar.draw()
        if mouse.is_over_object(som) and sound:
            som_click.draw()
            if mouse.is_button_pressed(1):
                sound = False
                mainsound.pause()
        elif sound:
            som.draw()
        if mouse.is_over_object(s_som) and not(sound):
            s_som_click.draw()
            if mouse.is_button_pressed(2):
                sound = True
                mainsound.unpause()
        elif not(sound):
            s_som.draw() 
        if mouse.is_over_object(sair):
            sair_click.draw()
            if mouse.is_button_pressed(1):
                break
        else:
            sair.draw()

        janela.update()

menu()
