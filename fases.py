import EscapuLiu
from PPlay.gameimage import*
from PPlay.window import*
from PPlay.sprite import*
""""
    -1 -> Retorna ao meno
    0 -> Perdeu o jogo
    1 -> Passou de fase
"""


def selecionafase():
    vida = 3
    mana = 0
    fase,vida,mana = EscapuLiu.fase0(vida,mana) #Faz a fase0 sempre
    if fase == 1: #Se passou a 0 faz a fase1
        fase,vida,mana = EscapuLiu.fase1(vida,mana)
    if fase == 1: #Se passou a 1 faz a fase2
        fase,vida,mana = EscapuLiu.fase2(vida,mana)
    if fase == 1: #Se passou a 2 faz a fase3
        fase,vida,mana = EscapuLiu.fase3(vida,mana)
    if fase == 0 or fase ==1:
        fase = gameover(fase)
    if fase == -1: #Volta pro menu inicial
        return

def gameover(fase):
    janela = Window(1050,639)
    teclado = janela.get_keyboard()
    fundo = GameImage("imagens/menu/gameover.png") #Fazer o fundo do gameover
    if fase == 1:
        fundo = GameImage("imagens/menu/vitória.png")
    morte = Sprite("imagens/peach/morte.png",4)
    morte.set_total_duration(1500)
    morte.set_position(499,372)
    while True:
        fundo.draw()
        if fase == 0:
            morte.draw()
            if morte.get_curr_frame() == 3:
                morte.pause()
            morte.update()
        #Voltar ao menu inicial
        if teclado.key_pressed("ESC"):
            return -1
        janela.update()
