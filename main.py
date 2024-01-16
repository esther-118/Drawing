import pygame, sys

window_x = 1000
window_y = 1000
button_x = 100
button_y = 40
black = (0, 0, 0)
white = (255, 255, 255)
gray = (100, 100, 100)
red = (255, 0, 0)
blue = (0, 0, 255)

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 36)
font_button = pygame.font.SysFont("Arial", 27)
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

class buttons():
    def __init__(self, x, y, color, hover_color, text, text_color):
        self.x = x
        self.y = y
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
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
        
        text = font_button.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=(button_x/2 + self.x, button_y/2 + self.y))
        
        pygame.draw.rect(screen, color, rect, 3)
        screen.blit(text, text_rect)

def main():
    drawing = False
    mouse_position = (0, 0)
    last_pos = None
    condition = True

    draw = False
    draw_color = black
    draw_size = 1

    screen.fill(white)
    window()
    draw_button = buttons(window_x/10, window_y - 2 * window_y/10, black, gray, "DRAW", black)
    erase_button = buttons(window_x/10 * 2 + 5, window_y - 2 * window_y/10, black, gray, "ERASE", black)
    black_button = buttons(window_x/10, window_y - 1 * window_y/10, black, gray, "BLACK", black)
    red_button = buttons(window_x/10 * 2 + 5, window_y - 1 * window_y/10, black, gray, "RED", red)
    blue_button = buttons(window_x/10 * 3 + 10, window_y - 1 * window_y/10, black, gray, "BLUE", blue)
    draw_button.draw_button()
    erase_button.draw_button()
    black_button.draw_button()
    red_button.draw_button()
    blue_button.draw_button()
    while(condition):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == pygame.MOUSEMOTION:
                if (draw and drawing):
                    mouse_position = pygame.mouse.get_pos()
                    if last_pos is not None:
                        pygame.draw.line(screen, draw_color, last_pos, mouse_position, draw_size)
                    last_pos = mouse_position
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_position = (0, 0)
                drawing = False
                last_pos = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (draw_button.rect.collidepoint(event.pos)):
                    draw_size = 3
                    if draw == True:
                        draw = False
                    else:
                        draw = True
                elif (erase_button.rect.collidepoint(event.pos)):
                    draw_color = white
                    draw_size = 5
                if (black_button.rect.collidepoint(event.pos)):
                    draw_color = black
                elif (red_button.rect.collidepoint(event.pos)):
                    draw_color = red
                elif (blue_button.rect.collidepoint(event.pos)):
                    draw_color = blue
                drawing = True
        pygame.display.update()

if __name__ == "__main__":
    main()