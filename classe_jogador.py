import pygame
import random

from caminho_relativo import resource_path as rp

class Jogador :
    def __init__(self):
        self.imagem = perry = pygame.image.load(rp("src/img/perry.png"))
        self.imagem = perry = pygame.transform.scale_by(self.imagem, 0.5)
        
        #Posição da imagem
        self.pos_x_perry=500
        self.pos_y_perry= 630


         #criando a mascara para ser utilizado na verificação da colissão
        self.mascara = pygame.mask.from_surface(self.imagem)
        
        self.som_colisao = pygame.mixer.Sound(rp("src/sound/dragon-studio-car-honk-386166.mp3"))


    def andar(self, teclas_pressisonadas):
        if teclas_pressisonadas[pygame.K_RIGHT]:
            self.pos_x_perry += 5

        if teclas_pressisonadas[pygame.K_LEFT]:
            self.pos_x_perry -= 5
            
        if teclas_pressisonadas[pygame.K_UP]:
            self.pos_y_perry -= 5

        if teclas_pressisonadas[pygame.K_DOWN]:
            self.pos_y_perry += 5

        #Barreira esquerda e parte de cima
        if self.pos_x_perry < 0:
            self.pos_x_perry +=5
        if self.pos_y_perry < 0:
            self.pos_y_perry +=5

        #Barreira Direita e parte de baixo
        if self.pos_x_perry > 1130:
            self.pos_x_perry -=5
        if self.pos_y_perry > 800:
            self.pos_y_perry -=5


    def exibir(self, tela_do_jogo):
     tela_do_jogo.blit(self.imagem,(self.pos_x_perry,self.pos_y_perry))

    def voltar(self):
        self.pos_x_perry=500
        self.pos_y_perry= 630

    
    def som(self):
        self.som_colisao.play()
