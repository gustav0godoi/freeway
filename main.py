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
pygame.display.set_caption("Perry 3000")
#Mudando a janela
rua = pygame.image.load("src/img/rua.jpg")

#Carregando Imagem
perry = pygame.image.load("src/img/perry.png")
    #Carregando os carros
carro1 = pygame.image.load("src/img/carro1.png")
carro2 = pygame.image.load("src/img/carro2.png")
carro3 = pygame.image.load("src/img/carro3.png")
carro4 = pygame.image.load("src/img/carro4.png")



#Diminuindo o tamanho da imagem
perry = pygame.transform.scale_by(perry, 0.5)
carro1 = pygame.transform.scale_by(carro1, 0.7)
#criando uma variavel que  vai definir a posição das imagens
pos_x_perry=170
pos_y_perry= 300

pos_x_rua = 0
pos_y_rua = 40

pos_X_c1 = 290
pos_y_c1 = 100
#Vou criar um loop infinito para manter a janela aberta
while True:
    lista_eventos = pygame.event.get() #Pego todos os eventos que acontece na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pygame.QUIT: #Verifico se um dos eventos é para SAIR
            pygame.quit() #Encerro o jogo
            exit()


    #Pegando a lista de teclas pressionadas
    teclas_pressisonadas = pygame.key.get_pressed()
            
    #Verifico se a tecla da direita está pressionada
    if teclas_pressisonadas[pygame.K_RIGHT]:
            pos_x_perry += 5

    if teclas_pressisonadas[pygame.K_LEFT]:
         pos_x_perry -= 5
         
    if teclas_pressisonadas[pygame.K_UP]:
         pos_y_perry -= 5

    if teclas_pressisonadas[pygame.K_DOWN]:
         pos_y_perry += 5

    #Barreira esquerda e parte de cima
    if pos_x_perry < 0:
         pos_x_perry +=5
    if pos_y_perry < 0:
         pos_y_perry +=5

    #Barreira Direita e parte de baixo
    if pos_x_perry > 725:
         pos_x_perry -=5
    if pos_y_perry > 530:
         pos_y_perry -=5
     
    #Exibindo a imagem da vaca
    tela.blit(rua, (pos_x_rua, pos_y_rua))
    tela.blit(perry, (pos_x_perry,pos_y_perry))
    tela.blit(carro1, (pos_X_c1, pos_y_c1))
    #Atualizando a tela
    pygame.display.update()

    #Controlando o FPS
    clock.tick(60)