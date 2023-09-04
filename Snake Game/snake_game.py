import pygame,random,time
import sys
from pygame.math import Vector2
class SNAKE:
    def __init__(self):
        self.body=[Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction=Vector2(1,0)
        self.new_block=False

        self.head_up = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('C:/Users/aksha/OneDrive/Desktop/CODER/Devops_Lab/Snake_Game/Graphics/body_bl.png').convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()
        for index,block in enumerate(self.body):
                x_pos=block.x * cell_size
                y_pos=block.y * cell_size
                block_rect=pygame.Rect(int(x_pos),int(y_pos),cell_size,cell_size)
                
                if index==0:
                    screen.blit(self.head,block_rect)
                elif index==len(self.body)-1:
                    screen.blit(self.tail,block_rect)
                else:
                    previous_block= self.body[index+1]-block
                    next_block=self.body[index-1]-block
                    if previous_block.x==next_block.x:
                        screen.blit(self.body_vertical,block_rect)
                    elif previous_block.y==next_block.y:
                        screen.blit(self.body_horizontal,block_rect)
                    else:
                        if previous_block.x==-1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==-1:
                            screen.blit(self.body_tl,block_rect)
                        elif previous_block.x==-1 and next_block.y==1 or previous_block.y==1 and next_block.x==-1:
                            screen.blit(self.body_bl,block_rect)
                        elif previous_block.x==1 and next_block.y==-1 or previous_block.y==-1 and next_block.x==1:
                            screen.blit(self.body_tr,block_rect)
                        elif previous_block.x==1 and next_block.y==1 or previous_block.y==1 and next_block.x==1:
                            screen.blit(self.body_br,block_rect)        
    

    def update_head_graphics(self):
        head_relation=self.body[1]-self.body[0]
        if head_relation==Vector2(1,0):self.head=self.head_left
        elif head_relation==Vector2(-1,0):self.head=self.head_right
        elif head_relation==Vector2(0,1):self.head=self.head_up
        elif head_relation==Vector2(0,-1):self.head=self.head_down
            
    def update_tail_graphics(self):
         tail_relation=self.body[-2]-self.body[-1]
         if tail_relation==Vector2(1,0):self.tail=self.tail_left
         elif tail_relation==Vector2(-1,0):self.tail=self.tail_right
         elif tail_relation==Vector2(0,1):self.tail=self.tail_up
         elif tail_relation==Vector2(0,-1):self.tail=self.tail_down

    def move_snake(self):
        if self.new_block==True:
            body_copy=self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]
            self.new_block=False
        else:
            body_copy=self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body=body_copy[:]

    def add_block(self):
        self.new_block=True

class FRUIT:
    def _init_(self):
    #create an x,y pos
    #draw a square
        self.randomize()
    
    def draw_fruit(self):
        fruit_Rect=pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_Rect)
        #pygame.draw.rect(screen,(126,166,144),fruit_Rect)

    def randomize(self):
        self.x=random.randint(0,cell_number-1)
        self.y=random.randint(0,cell_number-1)
        self.pos=Vector2(self.x,self.y)

class MAIN:
   def __init__(self):
       self.snake=SNAKE()
       self.fruit=FRUIT()
     
  
   def update(self):
       self.snake.move_snake()
       self.check_collision()
       self.check_fails()

   def draw_elements(self):
    self.draw_grass()
    self.fruit.draw_fruit()
    self.snake.draw_snake()
    self.draw_score()

   def check_collision(self):
       if self.fruit.pos == self.snake.body[0]:
           self.fruit.randomize()
           self.snake.add_block()
           

       for block in self.snake.body[1:]:
           if block == self.fruit.pos:
               self.fruit.randomize()   

   def check_fails(self):
       if not 0 <= self.snake.body[0].x <cell_number or not 0 <= self.snake.body[0].y <cell_number:
           self.game_over()

       for block in self.snake.body[1:]:
           if block==self.snake.body[0]:
               self.game_over()

   def game_over(self):
       print("\nSCORE: "+str(len(self.snake.body)-3))
       pygame.quit()
       sys.exit()

   def draw_grass(self):
       grass_color=(167,209,61)
       for row in range(cell_number):
           if row%2==0:
               for col in range(cell_number):
                   if col%2==0:
                       grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                       pygame.draw.rect(screen,grass_color,grass_rect)
           else:
                for col in range(cell_number):
                   if col%2!=0:
                       grass_rect=pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                       pygame.draw.rect(screen,grass_color,grass_rect)
   def draw_score(self):
       score_text=str(len(self.snake.body)-3)
       score_surface=game_font.render(score_text,True,(56,74,12))
       score_x=int(cell_size*cell_number-60)
       score_y=int(cell_size*cell_number-40)
       score_rect=score_surface.get_rect(center=(score_x,score_y))
       apple_rect=apple.get_rect(midright=(score_rect.left,score_rect.centery))
       screen.blit(score_surface,score_rect)
       screen.blit(apple,apple_rect)
       def Wanna_Play():
    Ans=input("\nDo you Want to Play Snake game (y/n): ")
    if Ans.lower()== 'y':
        intro="\nHello, {} ! 😊\n(: I hope you will enjoy this Game 😁 :)"  
        print(intro.format(name))
    elif Ans.lower()=='n':
        print("(: THANK YOU :)")
        sys.exit()
    else:
        print("\nInvalid Input!!!\nPlease enter only 'y' or 'n':>>\n")
        time.sleep(2)
        Wanna_Play()
def Rules():
    print('''
\n\t\tGameplay:
          
The game takes place on a rectangular grid.          
The player controls a snake that starts as a single block or segment.
The snake moves continuously in a particular direction (up, down, left, or right).
The snake's head can change direction using the arrow keys on the keyboard (up arrow, down arrow, left arrow, right arrow).
The snake's body follows the head's movement.
The snake cannot reverse its direction to move directly into its own body, as this would result in collision and game over.
The snake can only turn at right angles, not diagonally.
The snake grows longer when it consumes food.
          
\t\tFood:

Food items appear randomly on the grid.
The snake's objective is to consume these food items to grow longer.
When the snake's head occupies the same cell as a food item, the snake grows by adding one block to its tail.
After consuming food, a new food item spawns at a random location on the grid.
          
\t\tCollision:

Game over occurs when the snake's head collides with any of the following:
    1)The walls of the grid.
    2)The snake's own body.

\t\tScoring:

The player earns points for every food item consumed.
The score usually corresponds to the length of the snake, as longer snakes are more difficult to control and present more opportunities for collision.
          
\t\tControls:

The player can control the snake's direction using the arrow keys on the keyboard:
          
Up arrow: Move the snake's head upwards.
Down arrow: Move the snake's head downwards.
Left arrow: Move the snake's head to the left.
Right arrow: Move the snake's head to the right.
          
The snake's direction cannot be reversed instantly, preventing the snake from colliding with its own body.

\t\tWinning:
          
The Snake game doesn't typically have a winning condition; the goal is to achieve the highest score possible before colliding with a wall or the snake's body.
''')
