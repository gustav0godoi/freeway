import pygame
import random

class Inimigo:

    def __init__(self, endereco_imagem):
        self.imagem = pygame.image.load(endereco_imagem)
        self.imagem = pygame.transform.scale(self.imagem,(120,120))
        self.imagem = pygame.transform.flip(self.imagem,True,False)
        self.imagem = pygame.transform.rotate(self.imagem, 90)

        #Criando um atributo que vai definir a posição do  inimigo
        self.pos_x_inimigo = -100

        #criando um atributo para definir a posição y do inimigo
        self.pos_y_inimigo = random.randint(200,560)

        #criando um atributo para definir a velocidade
        self.velocidade = random.randint(3,6)
        
        #criando a mascara para ser utilizado na verificação da colissão
        self.mascara = pygame.mask.from_surface(self.imagem)


    def andar(self):
        self.pos_x_inimigo = self.pos_x_inimigo + self.velocidade
        #se o inimigo chegar até o final, ele volta
        if self.pos_x_inimigo > 900:
            self.voltar()

    def exibir(self, tela_do_jogo):
        tela_do_jogo.blit(self.imagem,(self.pos_x_inimigo,self.pos_y_inimigo))

    def voltar(self):
        self.pos_x_inimigo = -100
        self.pos_y_inimigo = random.randint(200,560)
        self.velocidade = random.randint(3,5)