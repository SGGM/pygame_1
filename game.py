import pygame



# Makes game window and caption
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game!")


# Place for constants
WHITE = (255, 255, 255)


pygame.draw.circle(WIN, WHITE, (250, 250), 50)

pygame.display.update()



def main():
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    pygame.quit()


if __name__ == "__main__":
    main()