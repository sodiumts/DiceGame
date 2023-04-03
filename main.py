import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

rect_size = (200, 200)
rect_pos = [screen.get_width()/10, screen.get_height()/6]
running = True
font = pygame.font.Font("freesansbold.ttf", 30)
text = font.render("Dice Games Are Stupid", True, "#827b7a")
textBox = text.get_rect()
textBox.move(screen.get_width()/1.5, screen.get_height()/5)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    screen.fill(pygame.Color("#dae8fc"), pygame.Rect(rect_pos, rect_size))
    screen.fill(pygame.Color("#d5e8d4"), pygame.Rect(rect_pos, rect_size).move(200, 0))
    screen.fill(pygame.Color("#ffe6cc"), pygame.Rect(rect_pos, rect_size).move(400, 0))
    screen.fill(pygame.Color("#ffe6cc"), pygame.Rect(rect_pos, rect_size).move(0, 200))
    screen.fill(pygame.Color("#f8cecc"), pygame.Rect(rect_pos, rect_size).move(200, 200))
    screen.fill(pygame.Color("#e1d5e7"), pygame.Rect(rect_pos, rect_size).move(400, 200))

    screen.blit(text, textBox)

    pygame.display.flip()

    clock.tick(60)
pygame.quit()

