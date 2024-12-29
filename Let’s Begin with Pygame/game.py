import pygame 
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Adding Image")
image=pygame.transform.scale(pygame.image.load("cat.jpeg").convert(),(250,250))
image2=pygame.transform.scale(pygame.image.load("dog.jpeg").convert(),(250,250))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(image,(0,0))
    screen.blit(image2,(250,250))
    pygame.display.flip()
