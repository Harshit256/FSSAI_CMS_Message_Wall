#!/bin/sh/python3

import urllib.request
import pygame
import io
import time

pygame.init()
pygame.mouse.set_visible(False)
infoObject = pygame.display.Info()
screen=pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.NOFRAME)

pygame.font.init()
#myfont = pygame.font.SysFont('Comic Sans MS', 115)
myfont = pygame.font.Font('/home/pi/Desktop/Message_Wall/Raleway-Black.ttf', 75)

'''def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def display_message(msg):
    TextSurf, TextRect = text_objects(msg, msgFont)
    TextRect.center = ((display_width/2), (display_height/2))
    screen.blit(TextSurf, TextRect)
    
    pygame.display.update()'''

def display_text(text):
        screen.fill((0,0,0))
        textsurface = myfont.render(text, True, (255, 234, 138))
        #for i in text:
         #       print("enter here")
          #      textsurface = myfont.render(i[:-1], True, (255, 234, 138))
        #text_rect = textsurface.get_rect(center=(infoObject.current_w/2, infoObject.current_h/3))
        text_rect = textsurface.get_rect()
        screen.blit(textsurface,text_rect)
        pygame.display.update()


try:
    while True:
        try:
            url = urllib.request.urlopen("http://antzy.net/fssai/read_message.php")
            stream = io.TextIOWrapper(url, encoding='utf-8')
            message = stream.read()
            
            print(message)
            display_text(message)
            
            for i in range(0,60):
                time.sleep(1)
        except:
            display_text(stream.read())            
            for i in range(0,5):
                time.sleep(1)

except KeyboardInterrupt:
    print("exiting...")
    pygame.quit()
