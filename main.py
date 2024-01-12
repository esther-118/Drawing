import pygame, sys

window_x = 1000
window_y = 1000
button_x = 100
button_y = 40
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 36)
font_button = pygame.font.SysFont("Arial", 25)
screen = pygame.display.set_mode([window_x, window_y])

clicked = True

def window():
    #boundary
    pygame.draw.line(screen, black, (window_x/10, window_y/10), (window_x - window_x/10, window_y/10), 3)
    pygame.draw.line(screen, black, (window_x/10, window_y - 3 * window_y/10), (window_x - window_x/10, window_y - 3 * window_y/10), 3)
    pygame.draw.line(screen, black, (window_x/10, window_y/10), (window_x/10, window_y - 3 * window_y/10), 3)
    pygame.draw.line(screen, black, (window_x - window_x/10, window_y/10), (window_x - window_x/10, window_y - 3 * window_y/10), 3)

    text = font.render('CANVAS', True, black)
    text_rect = text.get_rect(center=(window_x/2, window_y/20))
    screen.blit(text, text_rect)

    draw = buttons(window_x/10, window_y - 2 * window_y/10, black, gray, "DRAW")
    draw.draw_button()

class buttons():
    def __init__(self, x, y, color, hover_color, text):
        self.x = x
        self.y = y
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, button_x, button_y)

    def draw_button(self):
        global clicked
        pos = pygame.mouse.get_pos()
        rect = self.rect
        hover = rect.collidepoint(pos)
        
        if hover and pygame.mouse.get_pressed()[0] == 1:
            clicked = not clicked
        
        color = self.color
        color_text = self.color
        
        if hover:
            color = self.hover_color
            color_text = self.hover_color
        
        text = font_button.render(self.text, True, color_text)
        text_rect = text.get_rect(center=(button_x/2 + self.x, button_y/2 + self.y))
        
        pygame.draw.rect(screen, color, rect, 3)
        screen.blit(text, text_rect)


def draw():
    window()

def main():
    condition = True
    while(condition):
        screen.fill(white)
        draw()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)

        pygame.display.update()

if __name__ == "__main__":
    main()