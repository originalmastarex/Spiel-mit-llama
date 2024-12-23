# alt + z
import pygame
import sys
# Variabeln

llama_url = "https://212.132.112.15:11434/api/chat"

llama_model = "llama3.1:8b-instruct-q5.K_M"

prompt = "p"

prompt__sp = "sp"

prompt_bew = "bew"

prompt1 = "1"

prompt2 = "2"

prompt3 = "3"

prompt4 = "4"

antwort = "a"

data = {
    "model": llama_model,
    "messages": [
        {
            "role": "system",
            "content": prompt,
        }
    ],
    "stream": False,
}


# Meine Sachen

global ort
ort = "title_screen"
global gespräch


def char_1():
    g


def gespräch():
    print(1)


def laufen():
    if ort == "title_screen":
        if mouse and mouse:
            ort = "bedroom_1"
    if ort == "bedroom_1":
        if mouse and mouse:
            ort = "hallway_1"


def GoderL():
    if gespräch == 0:
        laufen()
    if gespräch == 1:
        gespräch()


while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


def main():
    d


main()
