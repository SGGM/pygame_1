import pygame



# Makes game window and caption
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Game!")


# Place for constants
WHITE = (255, 255, 255)


pygame.draw.circle(WIN, WHITE, (250, 250), 50)




def draw_window():
    pygame.display.update()


def main():
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_window()
            
    pygame.quit()


if __name__ == "__main__":
    main()