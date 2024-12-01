#Importamos las librerias
import pygame, random, os, time
pygame.init()
os.system("cls")

# Crear Ventana
pygame.display.set_caption('Escaleras y Serpientes con emojis')
ancho, alto = 854, 480 #Dimensiones de pantalla
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
# Cargar Imagen de Fondo
background_image = pygame.image.load("escenario.jpg")
background_image = pygame.transform.smoothscale(background_image, (alto, alto))

#Texto Jugador1 y Jugador 2
testFont = pygame.font.Font('BubblegumSans-Regular.ttf', 35)
textoJugador1 = testFont.render('Player  1', True, 'white')
textoJugador2 = testFont.render('Player  2', True, 'white')
antes = testFont.render('<', True, 'white')
despues = testFont.render('>', True, 'white')

#Propiedades del dado y Turno
dadoText = pygame.font.Font('BubblegumSans-Regular.ttf', 75)
dadoAccion = False
num = 0
ultimo_num = 0

turnoActual = 1

posicionJugador1 = 1
posicionJugador2 = 1

#Posicion del Jugador y su aspecto
imagen1 = 1
imagen2 = 2
jugador1 = pygame.image.load(f'emojis/{imagen1}.png')
jugador2 = pygame.image.load(f'emojis/{imagen2}.png')
jugador1Victoria = pygame.image.load(f'victoria/{imagen1}.png')
jugador2Victoria = pygame.image.load(f'victoria/{imagen2}.png')

#Variables para coordenadas del jugador en Pantalla
casilla = alto/10
m = (casilla-24)/2 
x = [0,
	1,2,3,4,5,6,7,8,9,10,
	10,9,8,7,6,5,4,3,2,1,
	1,2,3,4,5,6,7,8,9,10,
	10,9,8,7,6,5,4,3,2,1,
	1,2,3,4,5,6,7,8,9,10,
	10,9,8,7,6,5,4,3,2,1,
	1,2,3,4,5,6,7,8,9,10,
	10,9,8,7,6,5,4,3,2,1,
	1,2,3,4,5,6,7,8,9,10,
	10,9,8,7,6,5,4,3,2,1,
    1,1,1,1,1,1,1,1,1,1,1
]
y = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 
 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 
 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def lanzar_dado():
    global dadoAccion, num
    
    if dadoAccion:
        dadoAccion = False  # Detener la generación de números
        moverjugador()
        return num
    else:
        num = 0
        dadoAccion = True   # Iniciar la generación de números

serpientes_y_escaleras = {
    # Escaleras:
    10: 29,
    15: 36,
    20: 39,
    54: 74,
    71: 91,
    76: 95,
    80: 99,

    # Serpientes:
    14: 9,
    19: 4,
    34: 27,
    37: 17,
    53: 32,
    57: 43,
    62: 42,
    66: 46,
    72: 68,
    83: 64,
    94: 88,
    97: 85

}

def moverjugador():
    global num, posicionJugador1, posicionJugador2, turnoActual
    jugador1Rebote = False
    jugador2Rebote = False

    print('Turno del Jugador ',turnoActual,' Debe avanzar ', num,' vece/s')

    if turnoActual == 1:
        # Mover jugador 1 paso a paso
        for _ in range(num):
            if posicionJugador1 == 100:
                jugador1Rebote = True
            if jugador1Rebote == True:
                posicionJugador1 -= 1
            else:
                posicionJugador1 += 1
            actualizar_posicion_jugador1()
            pygame.time.delay(200)  # Retardo para movimiento suave
            pygame.display.update()

        if posicionJugador1 in serpientes_y_escaleras:
            posicionJugador1 = serpientes_y_escaleras[posicionJugador1]
            actualizar_posicion_jugador1()
            pygame.time.delay(500)  # Para dar efecto de sorpresa
        jugador1Rebote = False
        turnoActual = 2
    else:
        # Mover jugador 2 paso a paso
        for _ in range(num):
            if posicionJugador2 == 100:
                jugador2Rebote = True
            if jugador2Rebote == True:
                posicionJugador2 -= 1
            else:
                posicionJugador2 += 1
            actualizar_posicion_jugador2()
            pygame.time.delay(200)  # Retardo para movimiento suave
            pygame.display.update()

        if posicionJugador2 in serpientes_y_escaleras:
            posicionJugador2 = serpientes_y_escaleras[posicionJugador2]
            actualizar_posicion_jugador2()
            pygame.time.delay(500)  # Para dar efecto de sorpresa
        jugador2Rebote = False
        turnoActual = 1



def actualizar_posicion_jugador1():
    global posicionX1, posicionY1
    posicionX1 = m + (casilla * (x[posicionJugador1] - 1))
    posicionY1 = m + (casilla * (y[posicionJugador1] - 1))
    screen.blit(background_image, (0, 0))  # Redibuja el fondo para borrar el anterior
    screen.blit(jugador1, (posicionX1, posicionY1))
    screen.blit(jugador2, (posicionX2, posicionY2))  # Mantener jugador 2 en pantalla

def actualizar_posicion_jugador2():
    global posicionX2, posicionY2
    posicionX2 = m + (casilla * (x[posicionJugador2] - 1))
    posicionY2 = m + (casilla * (y[posicionJugador2] - 1))
    screen.blit(background_image, (0, 0))  # Redibuja el fondo para borrar el anterior
    screen.blit(jugador1, (posicionX1, posicionY1))  # Mantener jugador 1 en pantalla
    screen.blit(jugador2, (posicionX2, posicionY2))

testStart = pygame.font.Font('BubblegumSans-Regular.ttf', 65)
textoV = 'JUGANDO'
######################################################################
while True:
    #Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Comprobamos si alguien ya ha ganado la partida
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if antesJugador1_rect.collidepoint(event.pos):
                if imagen1 == 1:
                    imagen1 = 8
                else:
                    imagen1 -= 1
                jugador1 = pygame.image.load(f'emojis/{imagen1}.png')  # Actualiza la imagen
                jugador1Victoria = pygame.image.load(f'victoria/{imagen1}.png')
            elif despuesJugador1_rect.collidepoint(event.pos):
                if imagen1 == 8:
                    imagen1 = 1
                else:
                    imagen1 += 1
                jugador1 = pygame.image.load(f'emojis/{imagen1}.png')  # Actualiza la imagen
                jugador1Victoria = pygame.image.load(f'victoria/{imagen1}.png')
            if antesJugador2_rect.collidepoint(event.pos):
                if imagen2 == 1:
                    imagen2 = 8
                else:
                    imagen2 -= 1
                jugador2 = pygame.image.load(f'emojis/{imagen2}.png')  # Actualiza la imagen
                jugador2Victoria = pygame.image.load(f'victoria/{imagen2}.png')
            elif despuesJugador2_rect.collidepoint(event.pos):
                if imagen2 == 8:
                    imagen2 = 1
                else:
                    imagen2 += 1
                jugador2 = pygame.image.load(f'emojis/{imagen2}.png')  # Actualiza la imagen
                jugador2Victoria = pygame.image.load(f'victoria/{imagen2}.png')
            # Dados
            if dado.collidepoint(event.pos):
                lanzar_dado()
            
                

    if dadoAccion:
        while True:
            num = 0
            num = random.randint(1, 6)
            if num != ultimo_num:
                break  # Sale del bucle si el número es diferente
        ultimo_num = num  # Actualiza el último número generado
        pygame.time.delay(100)


    # Dibujar Fondo
    screen.fill('white')
    screen.blit(background_image,(0,0))
    #Menu
    pygame.draw.rect(screen, (56, 203, 221), (480, (48*0)+4, 370, 44)) #Azul
    pygame.draw.rect(screen, (237, 60, 78), (480, (48*1)+4, 370, 44)) #Rojo
    pygame.draw.rect(screen, (255,207,71), (480, (48*2)+3, 370, 47*6)) #Amarillo
    botonStart = pygame.draw.rect(screen, (56, 203, 221), (480, (48*8)+1, 370, 91)) #Azul


    # Jugador 1
    screen.blit(textoJugador1, (alto + 10, (casilla - 35) / 2 - 2))

    antesJugador1 = screen.blit(antes, (720, (48 * 0) + 6))  # Dibuja el botón "<"
    antesJugador1_rect = antesJugador1  # Ya contiene el rectángulo de colisión.

    screen.blit(jugador1, (750, (48 * 0) + 14, 370, 40))  # Dibuja al jugador 1

    despuesJugador1 = screen.blit(despues, (785, (48 * 0) + 6))  # Dibuja el botón ">"
    despuesJugador1_rect = despuesJugador1  # Ya contiene el rectángulo de colisión.

    #Jugador 2
    screen.blit(textoJugador2,(alto+10,((casilla-35)/2)+casilla-2))

    antesJugador2 = screen.blit(antes,(720, (48*1)+6))
    antesJugador2_rect = antesJugador2  # Ya contiene el rectángulo de colisión.

    screen.blit(jugador2,(750, (48*1)+14, 370, 40))

    despuesJugador2 = screen.blit(despues,(785, (48*1)+6))
    despuesJugador2_rect = despuesJugador2

    #Dado
    dadoFondoBlanco = pygame.draw.rect(screen, (255,255,255), (480+120, (48*2)+45, 110, 110)) #Blanco
    dadoFondoVerde = pygame.draw.rect(screen, (178,203,33), (480+125, (48*2)+50, 100, 100)) #Verde

    texto_dado = dadoText.render(str(num), True, 'black')
    texto_rect = texto_dado.get_rect(center=(480 + 125 + 50, (48 * 2) + 50 + 50))
    screen.blit(texto_dado, texto_rect)
    dado = dadoFondoBlanco

    #Victoria
    textoStart = testStart.render(textoV, True, 'white')
    start = screen.blit(textoStart,(alto+22,390))

    if posicionJugador1 >= 100 or posicionJugador2 >= 100:
        textoV = 'Victoria de'
        victoriaX = alto+15+278
        victoriaY = 395
        if posicionJugador1 >= 100:
            screen.blit(jugador1Victoria,(victoriaX,victoriaY))
        else:
            screen.blit(jugador2Victoria,(victoriaX,victoriaY))
            

    #JUGADOR
    posicionX1 = m+(casilla*(x[posicionJugador1]-1))
    posicionY1 = m+(casilla*(y[posicionJugador1]-1))

    posicionX2 = m+(casilla*(x[posicionJugador2]-1))
    posicionY2 = m+(casilla*(y[posicionJugador2]-1))

    if posicionJugador1 == posicionJugador2:
        screen.blit(jugador1, (posicionX1-6+1, posicionY1-6))
        screen.blit(jugador2, (posicionX2+6+1, posicionY2+6))  # Mantener jugador 2 en pantalla
    else:
        screen.blit(jugador1,(posicionX1,posicionY1))
        screen.blit(jugador2,(posicionX2,posicionY2))

    pygame.display.update()
    clock.tick(100)