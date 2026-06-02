#Importando o pygame
import pygame

from classe_inimigo import Inimigo
from classe_jogador import Jogador

#Dicionário de cores
cores = {"VERMELHO" : (255,0,0),
         "VERDE" : (0,255,0),
         "CINZA" : (100,100,100),
         "COR DE NEYMAR QUANDO FOGE": (255,255,0) }

pygame.init() #Inicializa os módulos do pygame, a maioria iria funcionar sem, mas alguns necessitam inicializar

clock = pygame.time.Clock()

#Criando a tela
tela  = pygame.display.set_mode((1200,900))

#Configurando a tela
pygame.display.set_caption("Perry 3000")
tela.fill(cores["VERDE"])

#Carregando imagens

# Carregando imagens
fundo = pygame.image.load("src/img/rua.jpg")

fundo = pygame.transform.rotate(fundo, 270)

fundo = pygame.transform.scale(fundo, (1200, 900))

inicio = pygame.image.load("src/img/tela_ini.png")

inicio = pygame.transform.scale(inicio, (1200, 900))


#Criando um inimigo, ou melhor, instanciando uma classe, melhor ainda, eu estou criando meu objeto
lista_inimigos = [Inimigo("src/img/carro1.png"),
                  Inimigo("src/img/carro2.png"),
                  Inimigo("src/img/carro3.png"),
                  Inimigo("src/img/carro4.png")]

#Instanciar um jogador, rriar objeto perry
perry = Jogador()

#status jogo
status_jogo = "INICIO"

#Vou criar um loping infinito para manter a janela aberta
while True:
     lista_eventos = pygame.event.get() #Pego todos os eventos que acontecem na janela
     for evento in lista_eventos: #Percorro os eventos 
        if evento.type == pygame.QUIT: #Verifico se um dos eventos é para sair
            pygame.quit() #Encerro o jogo

    

     #pegando a lista de teclas pressionadas
     teclas_pressionadas = pygame.key.get_pressed()

     if status_jogo == "INICIO":
         tela.blit(inicio,(0,0))
         if teclas_pressionadas[pygame.K_RETURN] or teclas_pressionadas[pygame.K_KP_ENTER]:
              status_jogo = "JOGANDO"
     
     if status_jogo == "JOGANDO":
          #exibindo o fundo
          tela.blit(fundo,(0,0))

          perry.exibir(tela)
          perry.andar(teclas_pressionadas)

               #fazendo inimigo andar
          for inimigo in lista_inimigos:
                    inimigo.andar()
                    inimigo.exibir(tela)
                    if perry.mascara.overlap(inimigo.mascara,(inimigo.pos_x_inimigo - perry.pos_x_perry, inimigo.pos_y_inimigo - perry.pos_y_perry )):
                         inimigo.voltar()
                         perry.som()
                         perry.voltar()
                    

     #Atualizando a tela
     pygame.display.update()

     #Controlar o FPS (frames por segundo)
     clock.tick(60)