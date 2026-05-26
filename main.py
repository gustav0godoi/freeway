#importando o pygame 
import pygame

#adicionando cores
cores = {"VERMELHO" : (255,0,0),
         "AZUL" : (0,255,255),
         "CINZA" : (100,100,100),
         "COR DO PERRY" : (208, 148, 220)} 
#inicilizando os módulos básicos do pygame,  maioriairia funcionar sem, mas alguns nessitam inicializar
pygame.init()

clock = pygame.time.Clock()
#Criando a tela
tela = pygame.display.set_mode((800,600))
#Mudando o nome da tela
pygame.display.set_caption("Super Jogo 3000")
#Mudando a cor da janela
tela.fill((208, 148, 220))

#Carregando Imagem
perry = pygame.image.load("src/img/perry.png")


#Diminuindo o tamanho da imagem
perry = pygame.transform.scale_by(perry, 0.5)

#criando uma variavel que  vai definir a posição do perry
pos_x_perry=0
pos_y_perry=0
#Vou criar um loop infinito para manter a janela aberta
while True:
    lista_eventos = pygame.event.get() #Pego todos os eventos que acontece na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pygame.QUIT: #Verifico se um dos eventos é para SAIR
            pygame.quit() #Encerro o jogo
            exit()

            #Pintando a tela novamente para apagar tudo
    tela.fill(cores["COR DO PERRY"])

    #Pegando a lista de teclas pressionadas
    teclas_pressisonadas = pygame.key.get_pressed()
            
    #Verifico se a tecla da direita está pressionada
    if teclas_pressisonadas[pygame.K_RIGHT]:
            pos_x_perry += 1

    if teclas_pressisonadas[pygame.K_LEFT]:
         pos_x_perry -= 1
         
    if teclas_pressisonadas[pygame.K_UP]:
         pos_y_perry -= 1

    if teclas_pressisonadas[pygame.K_DOWN]:
         pos_y_perry += 1
    #Exibindo a imagem da vaca
    tela.blit(perry, (pos_x_perry,pos_y_perry))

    #Atualizando a tela
    pygame.display.update()

    #Controlando o FPS
    clock.tick(60)