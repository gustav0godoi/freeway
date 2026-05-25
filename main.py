#importando o pygame 
import pygame

#inicilizando os módulos básicos do pygame,  maioriairia funcionar sem, mas alguns nessitam inicializar
pygame.init()

#Criando a tela
tela = pygame.display.set_mode((800,600))
#Mudando o nome da tela
pygame.display.set_caption("Super Jogo 3000")
#Mudando a cor da janela
tela.fill((255, 100, 00))


#Vou criar um loop infinito para manter a janela aberta
while True:
    lista_eventos = pygame.event.get() #Pego todos os eventos que acontece na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pygame.QUIT: #Verifico se um dos eventos é para SAIR
            pygame.quit() #Encerro o jogo

    #Atualizando a tela
    pygame.display.update()