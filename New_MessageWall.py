#!/usr/bin/python

import urllib
import pygame
import io
import time

pygame.init()
pygame.mouse.set_visible(False)
infoObject = pygame.display.Info()
screen=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.NOFRAME)
#screen=pygame.display.set_mode((1920,1080),pygame.RESIZABLE)

#SIZE = WIDTH, HEIGHT = (1024, 720)
#FPS = 30
#screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
#screen=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.NOFRAME)
#clock = pygame.time.Clock()

def blit_text(surface, text, pos, font, color=pygame.Color(255, 234, 138)):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 1, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


#text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
 #      "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
#       "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
#       "text will disappear underneath the surface"
#font = pygame.font.SysFont('Arial', 64)

pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 115)
myfont = pygame.font.Font('/home/pi/Desktop/Message_Wall/Raleway-Black.ttf', 65)

try:
    while True:
        try:
            url = urllib.urlopen("http://antzy.net/fssai/read_message.php")
            #stream = io.TextIOWrapper(url, encoding='utf-8')
            message = url.read()
            
            print(message)
            screen.fill(pygame.Color('black'))
            blit_text(screen, message, (410, 110), myfont)
            pygame.display.update()
            
            for i in range(0,60):
                time.sleep(1)
        except:
            screen.fill(pygame.Color('black'))
            blit_text(screen, '  Because \n  every Indian \n  deserves \n  Safe & Nutritious \n  Food', (380, 110), myfont)
            pygame.display.update()
            for i in range(0,5):
                time.sleep(1)

except KeyboardInterrupt:
    print("exiting...")
    pygame.quit()
