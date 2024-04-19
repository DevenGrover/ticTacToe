import pygame
pygame.init()
s=pygame.display.set_mode((600,600))
pygame.display.set_caption("tic-tac-toe")
DEFAULT_IMAGE_SIZE=(180,180)
cross = pygame.image.load('cross.jpg')
cross = pygame.transform.scale(cross, DEFAULT_IMAGE_SIZE)
circle= pygame.image.load("circle.png")
circle = pygame.transform.scale(circle, DEFAULT_IMAGE_SIZE)
color=(0,0,0)
coord_x=200
coord_y=0
coord_a=0
coord_b=200
running = True
s.fill(color)
pygame.draw.rect(s,(255,255,255), pygame.Rect(coord_x,coord_y,20,600))
pygame.draw.rect(s,(255,255,255), pygame.Rect(coord_x+200,coord_y,20,600))
pygame.draw.rect(s,(255,255,255), pygame.Rect(coord_a,coord_b,600,20))
pygame.draw.rect(s,(255,255,255), pygame.Rect(coord_a,coord_b+200,600,20))
current_player="x"
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_player=="x":
                s.blit(cross,(int(event.pos[0]/200)*200+20,int(event.pos[1]/200)*200+20))
                current_player="o"
            else:
                s.blit(circle,(int(event.pos[0]/200)*200+20,int(event.pos[1]/200)*200+20))
                current_player="x"
            
        if event.type == pygame.QUIT:
            running=False
    # s.blit(cross,(210,10))
    # s.blit(circle,(210,210))
    pygame.display.flip()