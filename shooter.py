import pygame


pygame.init()



SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("D-Kill")

# Set Frame rate
clock = pygame.time.Clock()
FPS = 60

#game variables

GRAVITY = 0.75


# Player action variables
moving_left = False
moving_right = False

#colors
BG = (144,201,120)

def draw_bg():
    screen.fill(BG)


class Soldier(pygame.sprite.Sprite):
    
    def __init__(self,char_type, x,y,scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        temp_list =[]
        
        for i in range(5):
            img = pygame.image.load(f'img/{self.char_type}/Idle/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        temp_list =[]   
        for i in range(6):
            img = pygame.image.load(f'img/{self.char_type}/Run/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width()*scale),int(img.get_height()*scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    
    
    def move(self, moving_left, moving_right):
        # movement variables
        dx = 0 
        dy = 0
        
        #movement variable if moving left or right
        if player.alive:
            if moving_left:
                dx = -self.speed
                self.flip = True
                self.direction = -1   
            if moving_right:
                dx = self.speed
                self.flip = False
                self.direction = 1
        #jump
        if self.jump == True:
            self.vel_y = -11
            self.jump = False
            
         # adding gravity
        self.vel_y += GRAVITY
        dy += self.vel_y   
            
            
        # update player position
        self.rect.x += dx
        self.rect.y += dy
    
    def update_animation(self):
        # updating animation
        
        ANIMATION_COOLDOWN = 100
        
        #update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # when animation go out of index
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        
    def update_action(self,new_action):
        # check  whether the animation is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings 
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks() 
         
    
    
    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),  self.rect)
    
        
        
        
        

player = Soldier('player',200,200,3,5)
enemy = Soldier('enemy',400,200,3,5)







run = True
while run:
    
    clock.tick(FPS)
    
    draw_bg()
    player.update_animation()
    
    player.draw()
    enemy.draw()
    
    #player action updating
    if moving_left or moving_right:
        player.update_action(1)#1 = run mathi ko for loop
    else:
        player.update_action(0)#0 = idle
    
    
    player.move(moving_left,moving_right)
    
    
    
    
    
    
    
    
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # when keyboard is hit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w and player.alive:
                player.jump = True
        
        # when keyboard button is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_ESCAPE:
                run = False
                
        
        
        
        
        
        
    pygame.display.update()
            
            
pygame.quit()
