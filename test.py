# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
    #add a solid background as r,g,b:


    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
    dims = [800, 400]
    screen = pygame.display.set_mode((dims[0], dims[1]))
     
    # define a variable to control the main loop
    running = True
    #add a solid background as r,g,b:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, 20, dims[1]))
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, dims[0], 20))
    pygame.draw.rect(screen, (255, 255, 255), (0, dims[1] - 20, dims[0], 20))

    pygame.display.update()

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()