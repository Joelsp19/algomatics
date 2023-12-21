import pygame
import sys

# define colors in the RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
DISC_COLOR = WHITE


def main(n: int, initial_state: list, moves: list):
    GRADIENT = [(DISC_COLOR[0]/i,DISC_COLOR[1]/i,DISC_COLOR[2]/i) for i in range(1,n+1)]

    # set up pygame and its screen
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)

    # add window caption
    pygame.display.set_caption('Tower of Hanoi')

    # set up font and text; size=25, bold=True, italic=False
    title = "Tower of Hanoi"
    font = pygame.font.SysFont('Arial', 25, True, False)
    font2 = pygame.font.SysFont('Arial', 20, True, False)

    # create a clock to track time
    clock = pygame.time.Clock()

    done = False
    reset = False
    delay = False
    delay_time = 500
    max_delay_time = 1000
    min_delay_time = 100

    while True:
        for move in moves:    
            # handle mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset = True
                    elif event.key == pygame.K_d:
                        delay = not delay
                    elif event.key == pygame.K_s:
                        delay_time += 100
                        delay_time = min(delay_time,max_delay_time)
                    elif event.key == pygame.K_f:
                        delay_time -= 100
                        delay_time = max(delay_time,min_delay_time)
            if reset:
                done = False
                initial_state = set_tower(src)
                pygame.display.flip()
                break
            # fills screen with a background color
            screen.fill(BLACK)

            #pegs
            x_center = screen_size[0]/2

            peg_distance = screen_size[0]/6 
            x_peg1 = x_center - peg_distance
            x_peg2 = x_center
            x_peg3 = x_center + peg_distance
            x_pegs = [x_peg1,x_peg2,x_peg3]
            y_peg_low = screen_size[1]/3
            y_peg_high = screen_size[1]*2/3
            peg_thickness = 10
            pygame.draw.line(screen, RED, [x_peg1, y_peg_low], [x_peg1, y_peg_high], peg_thickness)
            pygame.draw.line(screen, RED, [x_peg2, y_peg_low], [x_peg2, y_peg_high], peg_thickness)
            pygame.draw.line(screen, RED, [x_peg3, y_peg_low], [x_peg3, y_peg_high], peg_thickness)

            #disks

            top_offset = 30
            width_offset = 20
            y_offset = -1
            tot_height = y_peg_high-y_peg_low - (top_offset)
            disk_height = tot_height/n
            max_width = peg_distance - width_offset
            min_width = 30
            shrink_factor = (max_width - min_width)/n 
            y_disk_high = y_peg_high-disk_height+peg_thickness/5

            for i,peg in enumerate(initial_state):  
                for j,disk in enumerate(peg):
                    pygame.draw.rect(screen, GRADIENT[disk-1], [x_pegs[i] - (max_width-shrink_factor*(n-disk-1))/2, y_disk_high - ((j) * (disk_height+y_offset)), max_width-((n-disk-1)*shrink_factor), disk_height])

            # display text on screen
            text = font.render(title, True, WHITE)
            text_width, text_height = font.size(title)
            screen.blit(text, [x_center-text_width/2, 100])

            description = f"Disk {move[0]} moves from {move[1]} to {move[2]}"
            desc = font2.render(description, True, WHITE)
            text_width, text_height = font2.size(description)
            if not done: 
                screen.blit(desc, [x_center-text_width/2, y_peg_low-100]) 

            #legend
            legend_width = 400
            legend_height = 100
            bot_offset = 20
            text_offset = 10
            pygame.draw.rect(screen, WHITE, [x_center-legend_width/2, screen_size[1]-legend_height-bot_offset, legend_width, legend_height],3)
            legend_title = "Controls"
            leg_tit = font2.render(legend_title,True,WHITE)
            text_width, leg_tit_height = font2.size(legend_title)
            screen.blit(leg_tit, [x_center-text_width/2, screen_size[1]-legend_height-bot_offset+text_offset]) 
            controls = "r-reset : d-delay : s-slow : f-fast"
            con = font2.render(controls,True,WHITE)
            text_width, text_height = font2.size(controls)
            screen.blit(con, [x_center-text_width/2, screen_size[1]-legend_height-bot_offset+leg_tit_height+text_offset*2]) 

            # refresh everyting on screen
            if initial_state[move[1]] != [] and not done:
                initial_state[move[2]].append(initial_state[move[1]].pop())
            pygame.display.flip()
            if delay:
                pygame.time.delay(delay_time)

            # limit the update to 60 frames per second
            clock.tick(60)
        if reset:
            reset = False
        else:
            done = True


def tower_of_hanoi(disk, source, dest, aux, pegs, moves):  
    '''
    used recursion
    base case: if disk is smallest, then immedietely move to destination
    call tower_of_hanoi with disk = n-1, source = source, destination = aux, aux = destination
    move the disk to destination
    call tower_of_hanoi with disk = n-1, source = aux, destination = destination, aux = source
    '''
    if (disk == 1):
        moves.append((disk,source,dest))
    else:
        tower_of_hanoi(disk-1,source,aux,dest,pegs,moves)
        moves.append((disk,source,dest))
        tower_of_hanoi(disk-1,aux,dest,source,pegs,moves)
    

def set_tower(src):
    tower = [i for i in range(n,0,-1)]
    initial_state = [[],[],[]]
    initial_state[src] = tower
    return initial_state

if __name__ == "__main__":
    
    n = 8
    src = 0
    dest = 1
    aux = 2
    tower = [i for i in range(n,0,-1)]
    tower2 = [i for i in range(n,0,-1)]

    initial_state = [[],[],[]]
    initial_state[src] = tower2
    moves = []
    tower_of_hanoi(n,src,dest,aux,initial_state,moves)
    main(n,initial_state,moves)

  





