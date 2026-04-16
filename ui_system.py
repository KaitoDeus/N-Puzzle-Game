import pygame
import pygame.gfxdraw

# Colors (Clean & Professional Palette)
BG_COLOR = (15, 17, 26)       # Deep Night
PRIMARY_ACCENT = (59, 130, 246) # Blue
SECONDARY_ACCENT = (139, 92, 246) # Purple
SUCCESS_ACCENT = (34, 197, 94)  # Green
DANGER_ACCENT = (239, 68, 68)   # Red
BORDER_COLOR = (45, 55, 72)     # Grayish Blue
GLASS_COLOR = (30, 41, 59, 180) # Muted dark glass
TEXT_COLOR = (248, 250, 252)    # Off White
SUBTEXT_COLOR = (148, 163, 184) # Muted Gray

# Font Utility
def get_font(size, bold=False):
    font_priority = ['montserrat', 'segoe ui', 'tahoma', 'arial', 'sans-serif']
    return pygame.font.SysFont(font_priority, size, bold=bold)

class UIUtils:
    @staticmethod
    def draw_rounded_rect(surface, rect, color, radius=10, border=0, border_color=None):
        rect = pygame.Rect(rect)
        color = pygame.Color(*color)
        
        # Draw background
        if border == 0 or color.a > 0:
            shape_surf = pygame.Surface(rect.size, pygame.SRCALPHA)
            pygame.draw.rect(shape_surf, color, (0, 0, *rect.size), border_radius=radius)
            surface.blit(shape_surf, rect.topleft)
            
        # Draw border
        if border > 0 and border_color:
            pygame.draw.rect(surface, border_color, rect, width=border, border_radius=radius)

    @staticmethod
    def draw_soft_border(surface, rect, color, radius=10, border_width=2, glow=False):
        rect = pygame.Rect(rect)
        if glow:
            # Very subtle glow
            for i in range(3, 0, -1):
                alpha = 40 // i
                glow_color = (*color[:3], alpha)
                glow_rect = rect.inflate(i * 2, i * 2)
                UIUtils.draw_rounded_rect(surface, glow_rect, (0,0,0,0), radius=radius+i, border=1, border_color=glow_color)
        
        # Solid Border
        UIUtils.draw_rounded_rect(surface, rect, (0,0,0,0), radius=radius, border=border_width, border_color=color)

class UIComponent:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.visible = True

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, surface):
        pass

class Panel(UIComponent):
    def __init__(self, rect, radius=15, border_color=(255, 255, 255, 40)):
        super().__init__(rect)
        self.radius = radius
        self.border_color = border_color

    def draw(self, surface):
        if not self.visible: return
        # Glass effect
        UIUtils.draw_rounded_rect(surface, self.rect, GLASS_COLOR, radius=self.radius, border=1, border_color=self.border_color)

class Button(UIComponent):
    def __init__(self, rect, text, color=PRIMARY_ACCENT, font_size=20, callback=None):
        super().__init__(rect)
        self.text = text
        self.color = color
        self.callback = callback
        self.hovered = False
        self.font = get_font(font_size, bold=True)
        self.text_surf = self.font.render(text, True, TEXT_COLOR)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered and self.callback:
                self.callback()

    def draw(self, surface):
        if not self.visible: return
        
        # Draw background when hovered
        bg_alpha = 60 if self.hovered else 30
        UIUtils.draw_rounded_rect(surface, self.rect, (*self.color[:3], bg_alpha), radius=10)
        
        # Border
        UIUtils.draw_soft_border(surface, self.rect, self.color, radius=10, border_width=2, glow=self.hovered)
        
        text_rect = self.text_surf.get_rect(center=self.rect.center)
        surface.blit(self.text_surf, text_rect)

class Label(UIComponent):
    def __init__(self, pos, text, font_size=20, color=TEXT_COLOR, bold=False, center=False):
        self.font = get_font(font_size, bold=bold)
        self.text = text
        self.color = color
        self.center = center
        self.update_surf()
        super().__init__(self.text_surf.get_rect(topleft=pos))
        if center:
            self.rect.center = pos

    def update_surf(self):
        self.text_surf = self.font.render(self.text, True, self.color)

    def set_text(self, text):
        self.text = text
        self.update_surf()

    def draw(self, surface):
        if not self.visible: return
        surface.blit(self.text_surf, self.rect)

class Tile(UIComponent):
    def __init__(self, rect, number, color=PRIMARY_ACCENT):
        super().__init__(rect)
        self.number = number
        self.color = color
        self.font = get_font(40, bold=True)
        self.text_surf = self.font.render(str(number) if number != 0 else "", True, TEXT_COLOR)
        
    def draw(self, surface):
        if not self.visible: return
        if self.number == 0:
            # Empty tile
            UIUtils.draw_rounded_rect(surface, self.rect, (10, 10, 15), radius=10)
            return

        # Tile background
        UIUtils.draw_rounded_rect(surface, self.rect, (30, 41, 59), radius=10)
        
        # Border (Soft)
        UIUtils.draw_soft_border(surface, self.rect, self.color, radius=10, border_width=2)
        
        text_rect = self.text_surf.get_rect(center=self.rect.center)
        surface.blit(self.text_surf, text_rect)
