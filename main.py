import pygame
print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(680,480))
print('Setup end')
print('Loop start')
while True:
    #Check for all events
    for event in pygame.event.get():
        print('Quitting...')
        if event.type == pygame.QUIT:
            quit()#end pygame
