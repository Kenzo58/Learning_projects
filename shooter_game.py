import pygame
from os.path import join
from random import randint
from random import uniform

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect= self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2)) 
        self.direction=pygame.Vector2()
        self.speed=400

        #laser
        self.canshoot=True
        self.shoot_time=0
        self.cooldown=400

    def timer(self):
        if not self.canshoot:
            current_time=pygame.time.get_ticks()
            if current_time-self.shoot_time>=self.cooldown:
                self.canshoot=True

    def update(self,delta_time):
        keys=pygame.key.get_pressed()
        self.direction.x=int(keys[pygame.K_d])-int(keys[pygame.K_a])
        self.direction.y=int(keys[pygame.K_s])-int(keys[pygame.K_w])
        self.direction=self.direction.normalize() if self.direction else self.direction
        self.rect.center+=self.speed*delta_time*self.direction
        self.timer()
        if keys[pygame.K_SPACE] and self.canshoot:
            Laser(laser_image,self.rect.midtop,(all_sprites,laser_sprites))
            self.canshoot=False
            self.shoot_time=pygame.time.get_ticks()

class Stars(pygame.sprite.Sprite):
    def __init__(self,groups,surf):
        super().__init__(groups)
        self.image=surf
        self.rect = self.image.get_rect(center=(randint(0,WIDTH),randint(0,HEIGHT)))
    def visible(self):
        for self.position in self.star_positions:
            screen.blit(self.image, self.position)

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf,pos,groups ):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_rect(midbottom=pos)

    def update(self,delta_time):
        self.rect.centery-=delta_time*400
        if self.rect.bottom<0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self,surf,pos, groups):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_rect(center=pos)

        self.time_passed=pygame.time.get_ticks()
        self.cooldown=3000
        self.direction=pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed=randint(400,500)
    def update(self,delta_time):
        self.rect.centery+=delta_time*self.speed*self.direction.y
        self.rect.centerx+=delta_time*self.speed*self.direction.x
        if pygame.time.get_ticks()-self.time_passed>=self.cooldown:
            self.kill()
        

pygame.init()

HEIGHT = 600
WIDTH = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Space Shooter")

meteor_image=pygame.image.load(join('images', 'meteor.png')).convert_alpha()
laser_image = pygame.image.load(join('images', 'laser.png')).convert_alpha()
star_surf=pygame.image.load(join('images','star.png')).convert_alpha()

all_sprites=pygame.sprite.Group()
meteor_sprites=pygame.sprite.Group()
laser_sprites=pygame.sprite.Group()
for i in range(30):
    Stars(all_sprites,star_surf)
player=Player(all_sprites)

clock = pygame.time.Clock()

meteor_event=pygame.event.custom_type()
pygame.time.set_timer(meteor_event,500)

running=True
num=0
game_over_font = pygame.font.SysFont("Arial", 48)
font = pygame.font.SysFont("Arial", 24)
game_over=False

while running:

    delta_time = clock.tick(60) / 1000 

    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_ESCAPE]:
            running = False
        if event.type == meteor_event:
           x,y=randint(0,WIDTH),randint(-100,-50)
           Meteor(meteor_image,(x,y),(all_sprites,meteor_sprites))

    for sprit in laser_sprites:
        check=pygame.sprite.spritecollide(sprit,meteor_sprites,True)
        if check:
            sprit.kill()
            num+=1

    check2=pygame.sprite.spritecollide(player,meteor_sprites,False)
    if check2:
        game_over=True
    if game_over:
        game_over_text = game_over_font.render("Game Over NOOB", True, (255, 0, 0))
        score_text = font.render(f"Score: {num}", True, (255, 255, 255))
        screen.fill("black")
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50)) 
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10)) 
        pygame.display.update()
        continue
        

    all_sprites.update(delta_time)
    screen.fill("black")
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {num}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
