import pygame

# inizializzazione di pygame
pygame.init()

# impostazione della finestra di gioco
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision example")

# definizione dei colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# classe dell'oggetto "player"
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# classe dell'oggetto "enemy"
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((70, 70))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

# gruppo di sprite
all_sprites = pygame.sprite.Group()

# creazione degli oggetti "player" ed "enemy"
player = Player(100, 100)
enemy = Enemy(200, 200)

# aggiunta degli oggetti al gruppo di sprite
all_sprites.add(player, enemy)

# impostazione del clock di pygame
clock = pygame.time.Clock()

# loop di gioco
while True:
    # gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # movimento del player con le frecce direzionali
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -5
    elif keys[pygame.K_RIGHT]:
        dx = 5
    if keys[pygame.K_UP]:
        dy = -5
    elif keys[pygame.K_DOWN]:
        dy = 5
    player.update(dx, dy)

    # movimento automatico dell'enemy
    enemy.update(2, 0)

    # collision detection tra i due oggetti
    if pygame.sprite.collide_rect(player, enemy):
        # il player finisce sotto l'enemy
        player.rect.bottom = enemy.rect.top

    # rendering degli oggetti
    window.fill(WHITE)
    all_sprites.draw(window)

    # aggiornamento della finestra di gioco
    pygame.display.update()

    # limitazione dei frame al secondo a 60
    clock.tick(60)

# uscita dal programma
pygame.quit()
exit()