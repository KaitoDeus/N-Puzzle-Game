import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("N-Puzzle Game")

# Màu sắc
BG_COLOR = (30, 30, 30)

def main():
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Vẽ
        screen.fill(BG_COLOR)
        
        # Cập nhật màn hình
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
