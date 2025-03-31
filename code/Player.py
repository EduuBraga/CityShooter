import pygame
import os
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Configurações de animação
        self.animations = {
            'idle': [],
            'walk': []
        }
        self.current_animation = 'idle'
        self.animation_frame = 0
        self.animation_speed = 0.15
        self.animation_counter = 0  # Adicionei esta linha
        self.facing_right = True
        self.is_moving = False

        # Redimensiona a imagem inicial
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.rect = self.surf.get_rect(center=position)

        # Carrega as animações
        self.load_animations()

        # Configura a imagem inicial
        if len(self.animations['idle']) > 0:
            self.surf = self.animations['idle'][0]

    def load_animations(self):
        """Carrega as sprites de animação"""
        base_path = "./assets/player_animations/"

        try:
            # Usa a imagem base como primeiro frame de idle
            self.animations['idle'].append(pygame.transform.scale(self.surf, (200, 200)))

            # Carrega frames adicionais de idle
            i = 1
            while True:
                frame_path = f"{base_path}{self.name}_idle_{i}.png"
                if not os.path.exists(frame_path):
                    break
                img = pygame.image.load(frame_path).convert_alpha()
                self.animations['idle'].append(pygame.transform.scale(img, (200, 200)))
                i += 1

            # Carrega frames de walk
            i = 1
            while True:
                frame_path = f"{base_path}{self.name}_walk_{i}.png"
                if not os.path.exists(frame_path):
                    break
                img = pygame.image.load(frame_path).convert_alpha()
                self.animations['walk'].append(pygame.transform.scale(img, (200, 200)))
                i += 1

        except Exception as e:
            print(f"Erro ao carregar animações: {e}")
            # Fallback: usa a imagem base para walk se não encontrar arquivos
            if len(self.animations['walk']) == 0:
                self.animations['walk'].append(pygame.transform.scale(self.surf, (200, 200)))

    def animate(self):
        """Atualiza a animação atual"""
        self.animation_counter += self.animation_speed

        if self.animation_counter >= 1:
            self.animation_counter = 0
            frames = self.animations[self.current_animation]
            self.animation_frame = (self.animation_frame + 1) % len(frames)

            self.surf = frames[self.animation_frame]
            if not self.facing_right:
                self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        was_moving = self.is_moving
        self.is_moving = False

        # Movimento para direita
        if pressed_key[pygame.K_RIGHT] and self.rect.right < 1280:
            self.rect.centerx += ENTITY_SPEED[self.name]
            if not self.facing_right:
                self.facing_right = True
                self.animation_counter = 1  # Força atualização
            self.is_moving = True

        # Movimento para esquerda
        if pressed_key[pygame.K_LEFT] and self.rect.left != 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
            if self.facing_right:
                self.facing_right = False
                self.animation_counter = 1  # Força atualização
            self.is_moving = True

        # Muda animação se necessário
        if self.is_moving != was_moving:
            self.current_animation = 'walk' if self.is_moving else 'idle'
            self.animation_frame = 0
            self.animation_counter = 0

        # Atualiza animação
        self.animate()