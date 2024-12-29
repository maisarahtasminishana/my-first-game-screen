import pygame 
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My First Game Screen")
image=pygame.transform.scale(pygame.image.load("penguin.jpeg").convert(),(250,250))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(image,(150,150))
    pygame.display.flip()