import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Game settings
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
CELL_NUMBER = WINDOW_WIDTH // CELL_SIZE

class Snake:
    def __init__(self):
        self.body = [pygame.Vector2(5, 10), pygame.Vector2(4, 10), pygame.Vector2(3, 10)]
        self.direction = pygame.Vector2(1, 0)
        self.new_block = False
        
    def draw_snake(self, screen):
        for block in self.body:
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
    
    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True
    
    def check_collision(self):
        # Check if snake hits walls
        if not 0 <= self.body[0].x < CELL_NUMBER or not 0 <= self.body[0].y < CELL_NUMBER:
            return True
        
        # Check if snake hits itself
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        
        return False

class AntiSnake:
    def __init__(self):
        # Start at opposite corner from player snake
        self.body = [pygame.Vector2(CELL_NUMBER-5, CELL_NUMBER-10), 
                     pygame.Vector2(CELL_NUMBER-4, CELL_NUMBER-10), 
                     pygame.Vector2(CELL_NUMBER-3, CELL_NUMBER-10)]
        self.direction = pygame.Vector2(-1, 0)
        self.new_block = False
        self.move_timer = 0
        self.move_delay = 200  # Move slower than player initially
        
    def draw_anti_snake(self, screen):
        for i, block in enumerate(self.body):
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            # Head is purple, body is orange
            color = PURPLE if i == 0 else ORANGE
            pygame.draw.rect(screen, color, rect)
    
    def move_anti_snake(self, target_pos):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True
    
    def ai_pathfinding(self, target_pos):
        """Simple AI to chase the player snake"""
        head = self.body[0]
        
        # Calculate distances for each possible direction
        possible_moves = [
            pygame.Vector2(1, 0),   # Right
            pygame.Vector2(-1, 0),  # Left
            pygame.Vector2(0, 1),   # Down
            pygame.Vector2(0, -1)   # Up
        ]
        
        best_direction = self.direction
        best_distance = float('inf')
        
        for move in possible_moves:
            new_pos = head + move
            
            # Skip if move would hit walls
            if not (0 <= new_pos.x < CELL_NUMBER and 0 <= new_pos.y < CELL_NUMBER):
                continue
            
            # Skip if move would hit own body
            if new_pos in self.body:
                continue
            
            # Skip if moving backwards
            if move == -self.direction:
                continue
            
            # Calculate distance to target
            distance = abs(new_pos.x - target_pos.x) + abs(new_pos.y - target_pos.y)
            
            if distance < best_distance:
                best_distance = distance
                best_direction = move
        
        self.direction = best_direction
    
    def check_wall_collision(self):
        """Check if anti-snake hits walls"""
        if not 0 <= self.body[0].x < CELL_NUMBER or not 0 <= self.body[0].y < CELL_NUMBER:
            return True
        return False
    
    def check_self_collision(self):
        """Check if anti-snake hits itself"""
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False

class Food:
    def __init__(self):
        self.randomize()
    
    def draw_food(self, screen):
        food_rect = pygame.Rect(int(self.pos.x * CELL_SIZE), int(self.pos.y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)
    
    def randomize(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = pygame.Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.anti_snake = AntiSnake()
        self.score = 0
        self.game_over = False
        self.game_over_reason = ""
        
    def update(self):
        if not self.game_over:
            self.snake.move_snake()
            
            # Move anti-snake with AI pathfinding
            self.anti_snake.ai_pathfinding(self.snake.body[0])
            self.anti_snake.move_anti_snake(self.snake.body[0])
            
            self.check_collision()
            self.check_fail()
            self.check_anti_snake_collision()
    
    def draw_elements(self, screen):
        screen.fill(BLACK)
        self.food.draw_food(screen)
        self.snake.draw_snake(screen)
        self.anti_snake.draw_anti_snake(screen)
    
    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()
            self.score += 1
            
        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize()
    
    def check_fail(self):
        if self.snake.check_collision():
            self.game_over = True
            self.game_over_reason = "Hit wall or yourself!"
    
    def check_anti_snake_collision(self):
        """Check if anti-snake catches the player or hits obstacles"""
        # Check if anti-snake catches player
        if self.anti_snake.body[0] == self.snake.body[0]:
            self.game_over = True
            self.game_over_reason = "Caught by Anti-Snake!"
            return
        
        # Check if anti-snake hits player's body
        for block in self.snake.body:
            if self.anti_snake.body[0] == block:
                self.game_over = True
                self.game_over_reason = "Anti-Snake hit you!"
                return
        
        # Anti-snake collision with walls - respawn it
        if self.anti_snake.check_wall_collision():
            self.respawn_anti_snake()
        
        # Anti-snake collision with itself - respawn it
        if self.anti_snake.check_self_collision():
            self.respawn_anti_snake()
    
    def respawn_anti_snake(self):
        """Respawn anti-snake at a safe location"""
        # Find a corner far from player
        player_head = self.snake.body[0]
        corners = [
            pygame.Vector2(2, 2),
            pygame.Vector2(CELL_NUMBER-3, 2),
            pygame.Vector2(2, CELL_NUMBER-3),
            pygame.Vector2(CELL_NUMBER-3, CELL_NUMBER-3)
        ]
        
        best_corner = corners[0]
        max_distance = 0
        
        for corner in corners:
            distance = abs(corner.x - player_head.x) + abs(corner.y - player_head.y)
            if distance > max_distance:
                max_distance = distance
                best_corner = corner
        
        # Reset anti-snake at the farthest corner
        self.anti_snake.body = [
            best_corner,
            best_corner + pygame.Vector2(1, 0),
            best_corner + pygame.Vector2(2, 0)
        ]
        self.anti_snake.direction = pygame.Vector2(-1, 0)
    
    def display_game_over(self, screen, font):
        """Display game over screen"""
        # Game Over text
        game_over_text = font.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 60))
        
        # Reason text
        reason_text = font.render(self.game_over_reason, True, WHITE)
        reason_rect = reason_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 10))
        
        # Score text
        score_text = font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 30))
        
        # Restart text
        restart_text = font.render("Press R to restart or Q to quit", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 80))
        
        screen.blit(game_over_text, game_over_rect)
        screen.blit(reason_text, reason_rect)
        screen.blit(score_text, score_rect)
        screen.blit(restart_text, restart_rect)
    
    def restart_game(self):
        """Restart the game"""
        self.snake = Snake()
        self.food = Food()
        self.anti_snake = AntiSnake()
        self.score = 0
        self.game_over = False
        self.game_over_reason = ""
    
    def draw_score(self, screen, font):
        score_text = f"Score: {self.score}"
        score_surface = font.render(score_text, True, WHITE)
        score_rect = score_surface.get_rect(center=(WINDOW_WIDTH//2, 30))
        screen.blit(score_surface, score_rect)

def main():
    # Set up display
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    # Create game instance
    game = Game()
    
    # Custom event for snake movement
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == SCREEN_UPDATE and not game.game_over:
                game.update()
            
            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key == pygame.K_r:
                        game.restart_game()
                    elif event.key == pygame.K_q:
                        running = False
                else:
                    if event.key == pygame.K_UP:
                        if game.snake.direction.y != 1:
                            game.snake.direction = pygame.Vector2(0, -1)
                    if event.key == pygame.K_DOWN:
                        if game.snake.direction.y != -1:
                            game.snake.direction = pygame.Vector2(0, 1)
                    if event.key == pygame.K_RIGHT:
                        if game.snake.direction.x != -1:
                            game.snake.direction = pygame.Vector2(1, 0)
                    if event.key == pygame.K_LEFT:
                        if game.snake.direction.x != 1:
                            game.snake.direction = pygame.Vector2(-1, 0)
        
        game.draw_elements(screen)
        
        if game.game_over:
            game.display_game_over(screen, font)
        else:
            game.draw_score(screen, font)
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()