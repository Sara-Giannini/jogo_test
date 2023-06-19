import pygame
from pygame.locals import *

pygame.init()

largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Criação de Personagem")

class Jogo:
    def __init__(self):
        self.running = True

    def run (self):
        while self.running:
            self.eventos()
            self.atualizar()
            self.renderizar()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
    
    def atualizar(self):
        pass

    def renderizar(self):
        tela.fill((0, 0, 0))
        pygame.display.update()

    def tela_inicial(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            
            tela.fill((255, 255, 255))
            #aqui é pra desenhar o botão "criação de personagem"
            pygame.draw.rect(tela, (0, 0, 255), (300, 250, 200, 50))
            pygame.display.update()

    def tela_criacao_personagem(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

            tela.fill((255, 255, 255))
            #desenhar a interface de criação de personagem
            #adicionar lógica pra escolher caracteristicas (sprites) 

if __name__== "__main__":
    jogo = Jogo()
    jogo.run()