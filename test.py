def lanzar_dado():
    global dadoAccion
    dadoAccion = not dadoAccion  # Alterna entre True y False

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dado.collidepoint(event.pos):  # Detectar clic en el rectángulo del dado
                lanzar_dado()  # Alternar el estado del dado

    # Si dadoAccion es True, genera un número aleatorio continuamente
    if dadoAccion:
        num = random.randint(1, 6)  # Cambia el número del dado continuamente

    # Dibujar fondo
    screen.fill('white')
    screen.blit(background_image, (0, 0))

    # Dibujar el cuadrado del dado
    dado_rect = pygame.draw.rect(screen, (178, 203, 33), (480 + 125, (48 * 2) + 50, 100, 100))  # Verde

    # Dibujar el número actual del dado
    
    texto_dado = dadoText.render(str(num), True, 'black')
    texto_rect = texto_dado.get_rect(center=(480 + 125 + 50, (48 * 2) + 50 + 50))
    screen.blit(texto_dado, texto_rect)

    # Actualizar pantalla
    pygame.display.update()
    clock.tick(20)  # Controla la velocidad de cambio del dado
