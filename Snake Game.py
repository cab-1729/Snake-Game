import pygame
import itertools
import random
import sys
#Constants
colors={
    'white':(255,255,255),
    'alice blue':(240,248,255),
    'grey':(169,169,169),
    'black':(0,0,0),
    'medium orchid':(186,85,211),
    'deep pink':(255,20,147),
    'dark orchid':(153,50,204),
    'deep blue':(0,0,255),
    'cyan':(0,255,255),
    'dark cyan':(0,139,139),
    'chareuse':(127,255,0),
    'forest green':(34,139,34),
    'light green':(144,238,144),
    'yellow':(255,255,0),
    'khaki':(240,230,140),
    'gold':(255,215,0),
    'orange':(255,165,0),
    'light salmon':(255,160,122),
    'tomato':(255,99,71),
    'red':(255,0,0),
    'dark red':(139,0,0),
    'fire brick':(178,34,34),
}
boxes_in_row=25
fps=15
gap=1
box_side=20
width= (boxes_in_row * box_side) + ((boxes_in_row - 1) * gap)
height=width
#Environment
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake game')
clock=pygame.time.Clock()
all_sprites=pygame.sprite.Group()
#Sprites
class Box(pygame.sprite.Sprite):
    def __init__(self,arg1,arg2):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((box_side,box_side))
        self.color='white'
        self.image.fill(colors[self.color])
        self.rect=self.image.get_rect()
        self.row=arg1
        self.column=arg2
        x=(self.column-1)*(gap+box_side)
        y=(self.row-1)*(gap+box_side)
        self.rect.x,self.rect.y=x,y
    def change_color(self,color):
        self.color=color
        self.image.fill(colors[self.color])
#Create sprite
map=[]
#making map
for r in range(1, boxes_in_row + 1):
    t=[]
    for c in range(1, boxes_in_row + 1):
        te=Box(r,c)
        all_sprites.add(te)
        t.append(te)
    map.append(t)
choice_of_colors=list(colors.keys())
choice_of_colors.remove('black')
choice_of_colors.remove('white')
#snake functions
def move_up():
    if snake[0][0]>1:
        l=snake[0].copy()
        t=[]
        for n in range(len(snake)):
            if n==0:
                snake[0][0]=snake[0][0]-1
            else:
                t=[]
                t=snake[n].copy()
                snake[n][0]=l[0];snake[n][1]=l[1]
                l[0]=t.copy()[0];l[1]=t.copy()[1]
def move_down():
    if snake[0][0]<boxes_in_row:
        l = snake[0].copy()
        t = []
        for n in range(len(snake)):
            if n == 0:
                snake[0][0] = snake[0][0] + 1
            else:
                t = []
                t = snake[n].copy()
                snake[n][0] = l[0];
                snake[n][1] = l[1]
                l[0] = t.copy()[0];
                l[1] = t.copy()[1]
def move_left():
    if snake[0][1]>1:
        l = snake[0].copy()
        t = []
        for n in range(len(snake)):
            if n == 0:
                snake[0][1] = snake[0][1]-1
            else:
                t = []
                t = snake[n].copy()
                snake[n][0] = l[0];
                snake[n][1] = l[1]
                l[0] = t.copy()[0];
                l[1] = t.copy()[1]
def move_right():
    if snake[0][1]<boxes_in_row:
        l = snake[0].copy()
        t = []
        for n in range(len(snake)):
            if n == 0:
                snake[0][1] = snake[0][1] + 1
            else:
                t = []
                t = snake[n].copy()
                snake[n][0] = l[0];
                snake[n][1] = l[1]
                l[0] = t.copy()[0];
                l[1] = t.copy()[1]
def overlap():
    x=None
    y=None
    segments=[]
    for n in range(len(snake)):
        co=(snake[n][0],snake[n][1])
        if segments.count(co)==0:
            segments.append(co)
        else:
            return True
    return False
def eaten():
    global food,snake
    if len(snake)>1:
        last_1=snake[-1]
        last_2=snake[-2]
        snake.append([(2*last_1[0])-last_2[0],(2*last_1[1])-last_2[1],food.copy()[2]])
    else:
        snake.append([snake[0][0],snake[0][1]+1,food.copy()[2]])
    food = [random.randint(1, boxes_in_row), random.randint(1, boxes_in_row), random.choice(choice_of_colors)]
def display_text(text,font,size,color,x,y):
    font_name=pygame.font.match_font(font,bold=15)
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,color)
    text_rect=text_surface.get_rect()
    text_rect.topright=(x,y)
    screen.blit(text_surface,text_rect)
#Picture creation
class Picture(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('D:\\Satan\\Text\\Programs\\Python\\Games\\Snake game\\Lost page.png').convert()
        self.rect=self.image.get_rect()
        self.rect.x,self.rect.y=(0,0)
#Game Loop
while True:
    pos = (random.randint(1, boxes_in_row), random.randint(1, boxes_in_row))
    snake = [[pos[0], pos[1], random.choice(choice_of_colors)]]
    food = [random.randint(1, boxes_in_row), random.randint(1, boxes_in_row), random.choice(choice_of_colors)]
    running = True
    while running:
        #Time
        clock.tick(fps)
        #Input
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_UP] and not(keystate[pygame.K_DOWN] or keystate[pygame.K_RIGHT] or keystate[pygame.K_RIGHT]):
            move_up()
        elif keystate[pygame.K_DOWN] and not(keystate[pygame.K_UP] or keystate[pygame.K_RIGHT] or keystate[pygame.K_RIGHT]):
            move_down()
        if keystate[pygame.K_LEFT] and not(keystate[pygame.K_RIGHT] or keystate[pygame.K_UP] or keystate[pygame.K_DOWN]):
            move_left()
        elif keystate[pygame.K_RIGHT] and not(keystate[pygame.K_LEFT] or keystate[pygame.K_UP] or keystate[pygame.K_DOWN]):
            move_right()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#close window
                sys.exit(0)
        #Events
        if snake[0][1]==food[1] and snake[0][0]==food[0]:#Eats food
            eaten()
        if overlap():#runs into itself
            running=False
        #Update
        for i in map:
            for j in i:
                j.change_color('white')
        map[food[0]-1][food[1]-1].change_color(food[2])
        for row,column,col in snake:
            try:
                map[row-1][column-1].change_color(col)
            except:
                print(row,column)
        all_sprites.update()
        #Render
        screen.fill(colors['black'])
        all_sprites.draw(screen)
        #Flip
        pygame.display.flip()
    #You lost loop
    message=Picture()
    messages = pygame.sprite.Group()
    messages.add(message)
    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            keystate=pygame.key.get_pressed()
        if keystate[pygame.K_RETURN]:
            del messages,message
            break
        messages.draw(screen)
        display_text('You reached a length of '+str(len(snake)),"Game Cables",16,(173,255,47),400,500)
        pygame.display.flip()

