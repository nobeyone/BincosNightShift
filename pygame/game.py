import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Original game resolution
SCREEN_WIDTH = 640 
SCREEN_HEIGHT = 480 
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Flag to keep track of fullscreen mode
is_fullscreen = True

# Function to update display mode and scaling factors
def update_display_mode():
    global screen, display_width, display_height, scale_x, scale_y, scale
    global new_width, new_height, x_pos, y_pos, clock, game_surface
    if is_fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    display_width, display_height = screen.get_size()
    # Recalculate scaling factors
    scale_x = display_width / SCREEN_WIDTH
    scale_y = display_height / SCREEN_HEIGHT
    scale = min(scale_x, scale_y)
    new_width = int(SCREEN_WIDTH * scale)
    new_height = int(SCREEN_HEIGHT * scale)
    x_pos = (display_width - new_width) // 2
    y_pos = (display_height - new_height) // 2

# Utility function to adjust mouse position according to scaling
def get_adjusted_mouse_pos(pos):
    adjusted_pos = (pos[0] - x_pos, pos[1] - y_pos)
    adjusted_pos = (adjusted_pos[0] / scale, adjusted_pos[1] / scale)
    return adjusted_pos

# Base Scene Class
class Scene:
    def __init__(self, manager):
        self.manager = manager

    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def render(self, surface):
        pass

# Scene Manager Class
class SceneManager:
    def __init__(self, initial_scene):
        self.current_scene = initial_scene

    def go_to(self, scene):
        self.current_scene = scene

    def handle_events(self, events):
        self.current_scene.handle_events(events)

    def update(self, dt):
        self.current_scene.update(dt)

    def render(self, surface):
        self.current_scene.render(surface)

# Button Class
class Button:
    def __init__(self, image_path, hover_image_path, position):
        self.image_path = r"images/" + image_path
        self.hover_image_path = r"images/" + hover_image_path
        # Load the images
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.hover_image = pygame.image.load(self.hover_image_path).convert_alpha()
        self.current_image = self.image
        self.rect = self.image.get_rect(topleft=position)
        # Create a mask from the image
        self.mask = pygame.mask.from_surface(self.image)
        # Get the last modification times
        self.last_mod_time = os.path.getmtime(self.image_path)
        self.last_mod_time_hover = os.path.getmtime(self.hover_image_path)
        # Timer for checking updates
        self.time_since_last_check = 0  # in seconds

    def is_hovered(self, pos):
        x, y = pos
        x_rel = x - self.rect.x
        y_rel = y - self.rect.y
        if 0 <= x_rel < self.rect.width and 0 <= y_rel < self.rect.height:
            # Check if the mask at that point is not transparent
            return self.mask.get_at((int(x_rel), int(y_rel)))
        return False

    def is_clicked(self, pos):
        return self.is_hovered(pos)

    def check_for_updates(self, dt):
        self.time_since_last_check += dt
        CHECK_INTERVAL = 1.0  # seconds
        if self.time_since_last_check >= CHECK_INTERVAL:
            self.time_since_last_check = 0
            # Check if the images have been modified
            new_mod_time = os.path.getmtime(self.image_path)
            if new_mod_time != self.last_mod_time:
                # Reload the image
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.mask = pygame.mask.from_surface(self.image)
                self.last_mod_time = new_mod_time
            new_mod_time_hover = os.path.getmtime(self.hover_image_path)
            if new_mod_time_hover != self.last_mod_time_hover:
                # Reload the hover image
                self.hover_image = pygame.image.load(self.hover_image_path).convert_alpha()
                self.last_mod_time_hover = new_mod_time_hover

    def update(self, mouse_pos, dt):
        # First, check for updates
        self.check_for_updates(dt)
        if self.is_hovered(mouse_pos):
            self.current_image = self.hover_image
        else:
            self.current_image = self.image

    def draw(self, surface):
        surface.blit(self.current_image, self.rect)

# Menu Scene with a Start Button
class MenuScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        # Initialize the start button
        self.start_button = Button('start_button.png', 'start_button_hover.png',
                                   position=(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2 - 50))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Adjust mouse position according to scaling
                adjusted_pos = get_adjusted_mouse_pos(event.pos)
                if self.start_button.is_clicked(adjusted_pos):
                    self.manager.go_to(GameScene(self.manager))

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        # Adjust mouse position according to scaling
        adjusted_pos = get_adjusted_mouse_pos(mouse_pos)
        self.start_button.update(adjusted_pos, dt)

    def render(self, surface):
        surface.fill(BLACK)
        self.start_button.draw(surface)

# Game Scene with a Back Button
class GameScene(Scene):
    def __init__(self, manager):
        super().__init__(manager)
        # Initialize the back button
        self.back_button = Button('microphone.png', 'back_button_hover.png',
                                  position=(0, 0))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Adjust mouse position according to scaling
                adjusted_pos = get_adjusted_mouse_pos(event.pos)
                if self.back_button.is_clicked(adjusted_pos):
                    self.manager.go_to(MenuScene(self.manager))

    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        # Adjust mouse position according to scaling
        adjusted_pos = get_adjusted_mouse_pos(mouse_pos)
        self.back_button.update(adjusted_pos, dt)

    def render(self, surface):
        surface.fill(BLACK)
        self.back_button.draw(surface)

# Main Function
def main():
    global is_fullscreen, clock, game_surface
    clock = pygame.time.Clock()
    update_display_mode()
    pygame.display.set_caption("Pygame Scene Manager Example with Buttons")
    # Create a game surface with the original resolution
    game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    manager = SceneManager(MenuScene(None))
    manager.current_scene.manager = manager  # Assign manager after creation
    running = True

    while running:
        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    is_fullscreen = not is_fullscreen
                    update_display_mode()
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Or any other action to quit the game

        # Now pass the events to the current scene
        manager.handle_events(events)
        manager.update(dt)
        # Render everything to the game_surface
        manager.render(game_surface)
        # Scale the game_surface to the new dimensions
        scaled_surface = pygame.transform.smoothscale(game_surface, (new_width, new_height))
        # Fill the screen with black to clear any previous frames
        screen.fill(BLACK)
        # Blit the scaled_surface onto the screen at the calculated position
        screen.blit(scaled_surface, (x_pos, y_pos))
        pygame.display.flip()

if __name__ == "__main__":
    main()
