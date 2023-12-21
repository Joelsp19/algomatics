import pygame
import sys
import random
import math

# Cover a 2^n x 2^n chessboard that is missing one square using L-shaped pieces (sides of length 2 and 1)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100 , 100)
DARK_GREY = (50,50,50)
BROWN = (139, 69, 19)
RED = (255,0,0)
ALTCOLORS = [WHITE,GREY]

def main():

    # set up pygame and its screen
    pygame.init()
    screen_size = (1200, 800)
    screen = pygame.display.set_mode(screen_size)

    # add window caption
    pygame.display.set_caption('Cover Chessboard')

    # set up font and text; size=25, bold=True, italic=False
    font = pygame.font.SysFont('Arial', 25, True, False)
    font2 = pygame.font.SysFont('Arial', 20, True, False)
    
    # create a clock to track time
    clock = pygame.time.Clock()


    #initial state
    n = 2
    i = random.randrange(0, 2**n) 
    j = random.randrange(0, 2**n) 
    missing_square = (i,j)
    missing_square_rect = None

    reset = False #used to check if reset key pressed
    
    #draws a transparent polygon
    def draw_polygon_alpha(surface, color, points):
        lx, ly = zip(*points)
        min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
        target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points])
        surface.blit(shape_surf, target_rect)
    #draws a transparent rectangle
    def draw_rect_alpha(surface, color, rect):
        shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
        surface.blit(shape_surf, rect)
    #resets the pieces
    def reset_pieces():
        num_pieces = (((2**n)**2)-1)//3 
        initial_position = (100,y_center-square_side_length)
        for i in range(num_pieces):
            while(points_list[i][0][0] >= points_list[i][1][0]):
                rotate_piece(i,1)

            x_rel = initial_position[0] - pieces[i][0].left
            y_rel = initial_position[1] - pieces[i][0].top

            pieces[i][0].move_ip((x_rel,y_rel))
            pieces[i][1].move_ip((x_rel,y_rel))
            points_list[i] = [(x+x_rel,y+y_rel) for x,y in points_list[i]]
    #rotates a piece in a given direction
    def rotate_piece(selected_piece: int, dir: int):
        x_piece_center = points_list[selected_piece][3][0]
        y_piece_center = points_list[selected_piece][3][1]
        
        dir = -1 if dir < 0 else 1

        #uses some trig to rotate by 90degrees
        #find the theta compared to the horizontal add 135 deg
        #take sin and cos of the radius*sqrt2(magnitude of change for a point) to get components
        new_points = []
        for point in points_list[selected_piece]:
            x=point[0]
            y=point[1]
            if x == x_piece_center and y == y_piece_center:
                new_points.append((x,y))
                continue
            r = math.sqrt((x-x_piece_center)**2+(y-y_piece_center)**2)   
            θ = (math.pi/2 if y>y_piece_center else -math.pi/2) if x==x_piece_center else math.atan(-(y-y_piece_center)/(x-x_piece_center))
            θ = math.pi + θ if (x-x_piece_center)<=0 else 2*math.pi + θ
            fract = 3*math.pi/4 * dir
            dx = int(round(math.cos(θ+fract)*(math.sqrt(2)*r),1))
            dy = -int(round(math.sin(θ+fract)*(math.sqrt(2)*r),1)) 
            point = (x+dx,y+dy)
            new_points.append(point)
 
        points_list[selected_piece] = new_points
        
        #this takes care of rotating the rectangles representing the pieces
        #messy but works

        w = pieces[selected_piece][0].width 
        h = pieces[selected_piece][0].height

        x_small_rect = pieces[selected_piece][1].left
        y_small_rect = pieces[selected_piece][1].top

        x_big_rect = pieces[selected_piece][0].left
        y_big_rect = pieces[selected_piece][0].top 

        op = max(w,h) if dir == 1 else min(w,h)

        if op == h:
            pieces[selected_piece][0].height /= 2 if dir==1 else 0.5
            pieces[selected_piece][0].width *= 2 if dir==1 else 0.5
            comp = x_big_rect < x_small_rect if dir ==1 else y_big_rect >= y_small_rect
            if comp:
                pieces[selected_piece][0].top += square_side_length * dir
                pieces[selected_piece][1].left -= square_side_length * dir
            else:
                pieces[selected_piece][0].left -= square_side_length * dir
                pieces[selected_piece][1].left += square_side_length * dir
        else:
            pieces[selected_piece][0].width /= 2 if dir ==1 else 0.5
            pieces[selected_piece][0].height *= 2 if dir == 1 else 0.5
            comp = y_big_rect < y_small_rect if dir ==1 else x_big_rect < x_small_rect
            if comp:
                pieces[selected_piece][1].top -= square_side_length * dir
            else:
                pieces[selected_piece][0].left += square_side_length * dir
                pieces[selected_piece][0].top -= square_side_length * dir
                pieces[selected_piece][1].top += square_side_length * dir
    #checks if the board is a state of completion
    def check_win():
        #we win if
        #1. none of the Ls overlap
        #2. all of the squares are covered
        #3. the black square isn't covered
        distinct = True
        for i,points in enumerate(points_list):
            check = (pieces[i][0].collidelist([p[0] for ind,p in enumerate(pieces) if ind!=i]) == -1) \
                and (pieces[i][1].collidelist([p[1] for ind,p in enumerate(pieces) if ind!=i]) == -1) \
                and (pieces[i][1].collidelist([p[0] for ind,p in enumerate(pieces) if ind!=i]) == -1) \
                and (pieces[i][0].collidelist([p[1] for ind,p in enumerate(pieces) if ind!=i]) == -1)
            distinct &= check
            if not distinct:
                return False
        tot_list = [p[0] for p in pieces] + [p[1] for p in pieces]
        pot_win = (pieces[0][0].unionall(tot_list))
        distinct &= pot_win.left == board.left \
            and pot_win.top == board.top \
            and pot_win.width == board.width \
            and pot_win.height == board.height
        if not distinct:
            return False
        distinct &= missing_square_rect.collidelist(tot_list)
        return distinct


    #board
    padding = 20
    x_center = screen_size[0]/2
    y_center = screen_size[1]/2

    board_side_length = min(screen_size[1],screen_size[0])/2 #the entire board side length
    square_side_length = board_side_length/(2**n) #the length of an individual square
    
    background_length = board_side_length+padding # the length of the border around the board

    #rectangle objects representing the board and the border
    board = pygame.Rect(x_center-board_side_length/2, y_center-board_side_length/2, board_side_length, board_side_length)
    background = pygame.Rect(x_center-background_length/2, y_center-background_length/2, background_length, background_length)

    highlight = False #used to indicate when the green snap-grd highlight should be shown 

    #pieces
    num_pieces = (((2**n)**2)-1)//3 
    initial_position = (100,y_center-square_side_length)

    active_piece = None #used to keep track of piece that is being moved
    selected_piece = None #used to keep track of piece that has been selected
    pieces = []
    points_list = []
    #sets up the initial state of the pieces
    for i in range(num_pieces):
        piece_location = (initial_position[0],initial_position[1])
        pt1 = piece_location
        pt2 = (piece_location[0] + square_side_length*2,piece_location[1])
        pt3 = (piece_location[0] + square_side_length*2,piece_location[1] + square_side_length)
        pt4 = (piece_location[0] + square_side_length,piece_location[1]+ square_side_length)
        pt5 = (piece_location[0] + square_side_length,piece_location[1]+ square_side_length*2)
        pt6 = (piece_location[0],piece_location[1]+ square_side_length*2)
        points = (pt1,pt2,pt3,pt4,pt5,pt6) #the list of points for the L piece

        #two rectangles that will be used when checking if the mouse pressed on the piece
        rect1 = pygame.Rect(pt1[0],pt1[1],square_side_length,square_side_length*2)
        rect2 = pygame.Rect(pt1[0]+square_side_length,pt1[1],square_side_length,square_side_length)
        pieces.append((rect1,rect2))
        points_list.append(points)
        

    while True:
        if reset:
            i = random.randrange(0, 2**n) 
            j = random.randrange(0, 2**n) 
            missing_square = (i,j)
            reset_pieces()
            selected_piece = None
            active_piece = None
            reset = False

        # fills screen with a background color
        screen.fill(BLACK)

        # handle mouse and keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: #restart the game
                    reset = True
                elif event.key == pygame.K_UP: #rotate a selected piece clockwise
                    if selected_piece!=None:
                        rotate_piece(selected_piece,-1) 
                elif event.key == pygame.K_DOWN: #rotate a selected piece counter clockwise
                    if selected_piece!=None: 
                        rotate_piece(selected_piece,1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:        
                    #check if we are pressing on one of our pieces
                    for num,piece in enumerate(pieces):
                        if piece[0].collidepoint(event.pos) or piece[1].collidepoint(event.pos):
                            active_piece = num
                    #unselect a piece if selected, or else the selected piece is now the current active piece
                    if selected_piece != None:
                        selected_piece = None
                    else:
                        selected_piece = active_piece
                            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if active_piece != None:
                        x_piece_center = points_list[active_piece][3][0]
                        y_piece_center = points_list[active_piece][3][1]
                        snap_board = board.inflate(-square_side_length,-square_side_length)
                        #if the piece is inside the "snap board" then snap the piece, if valid
                        if snap_board.collidepoint((x_piece_center,y_piece_center)):
                            #get the position relative to the snap board
                            x_board_coor = x_piece_center - snap_board.left 
                            y_board_coor = y_piece_center - snap_board.top
                            #get the intended location of the center
                            x_coor = x_center - (board_side_length)/2 + (x_board_coor//square_side_length+1)*square_side_length
                            y_coor = y_center - (board_side_length)/2 + (y_board_coor//square_side_length+1)*square_side_length
                            #find the difference between the current position and the intended position
                            x_rel = x_coor - x_piece_center
                            y_rel = y_coor - y_piece_center
                            #represents the potential location to move the piece
                            pot_rect_1 = pieces[active_piece][0].move((x_rel,y_rel))
                            pot_rect_2 = pieces[active_piece][1].move((x_rel,y_rel))

                            #checks if the move is valid: in our case if it overlaps with the missing square it's invalid 
                            if not pot_rect_1.colliderect(missing_square_rect) and not pot_rect_2.colliderect(missing_square_rect):
                                pieces[active_piece][0].move_ip((x_rel,y_rel))
                                pieces[active_piece][1].move_ip((x_rel,y_rel))
                                points_list[active_piece] = [(x+x_rel,y+y_rel) for x,y in points_list[active_piece]]

                    active_piece = None
                    highlight = False

            if event.type == pygame.MOUSEMOTION:
                #similar logic as in MOUSEBUTTONUP
                if active_piece != None:
                    selected_piece = None
                    x_piece_center = points_list[active_piece][3][0]
                    y_piece_center = points_list[active_piece][3][1]
                    snap_board = board.inflate(-square_side_length,-square_side_length)
                    if snap_board.collidepoint((x_piece_center,y_piece_center)):
                        x_board_coor = x_piece_center - snap_board.left 
                        y_board_coor = y_piece_center - snap_board.top
                        
                        x_coor = x_center - (board_side_length)/2 + (x_board_coor//square_side_length+1)*square_side_length
                        y_coor = y_center - (board_side_length)/2 + (y_board_coor//square_side_length+1)*square_side_length

                        x_rel = x_coor - x_piece_center
                        y_rel = y_coor - y_piece_center

                        pot_rect_1 = pieces[active_piece][0].move((x_rel,y_rel))
                        pot_rect_2 = pieces[active_piece][1].move((x_rel,y_rel))

                        #now if valid, we show the highlight - the potential location to snap to
                        if not pot_rect_1.colliderect(missing_square_rect) and not pot_rect_2.colliderect(missing_square_rect):
                            highlight = True
                        else: 
                            highlight = False
                    else:
                        highlight = False

                    #move the piece to the relative location from the mouse (not the snap grid)
                    pieces[active_piece][0].move_ip((event.rel))
                    pieces[active_piece][1].move_ip((event.rel))
                    #change the points to see the results when drawing
                    points_list[active_piece] = [(x+event.rel[0],y+event.rel[1]) for x,y in points_list[active_piece]]
         
    

        #title
        title = "Cover Chessboard"
        text = font.render(title, True, WHITE)
        text_width, text_height = font.size(title)

        #draw background
        pygame.draw.rect(screen, BROWN,background)

        #draw board
        for i in range(2**n):  
            for j in range(2**n):
                if i != missing_square[0] or j != missing_square[1]:
                    pygame.draw.rect(screen, ALTCOLORS[(i+j)%2], [x_center-board_side_length/2 + square_side_length*i, y_center-board_side_length/2 + square_side_length*j, square_side_length, square_side_length])
                else:
                    missing_square_rect = pygame.draw.rect(screen, BLACK, [x_center-board_side_length/2 + square_side_length*i, y_center-board_side_length/2 + square_side_length*j, square_side_length, square_side_length])

        #draw pieces:
        for i,points in enumerate(points_list):
            #check if there is any overlap with any piece
            check = (pieces[i][0].collidelist([p[0] for ind,p in enumerate(pieces) if ind!=i]) == -1) \
                and (pieces[i][1].collidelist([p[1] for ind,p in enumerate(pieces) if ind!=i]) == -1) \
                and (pieces[i][1].collidelist([p[0] for ind,p in enumerate(pieces) if ind!=i]) == -1) \
                and (pieces[i][0].collidelist([p[1] for ind,p in enumerate(pieces) if ind!=i]) == -1)

            if selected_piece==i:
                draw_polygon_alpha(screen, (225,225,50,170),points) #yellow when selected
            elif check:
                draw_polygon_alpha(screen, (139, 69, 19,170),points) #brown when no overlap
            else:
                draw_polygon_alpha(screen, (255,0,0,170),points) #red when there is overlap

            
        #highlight
        if active_piece!=None and highlight:
            #if we are moving a piece and highlight is set to true - in mouse events, 
            #then show where the piece would snap to
            draw_rect_alpha(screen,(0,225,0,50),pot_rect_1)
            draw_rect_alpha(screen,(0,225,0,50),pot_rect_2)

        #display text on screen
        screen.blit(text, [x_center-text_width/2, 100])

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
        controls = "r-restart : UP-rotate CW : DOWN-rotate CCW"
        con = font2.render(controls,True,WHITE)
        text_width, text_height = font2.size(controls)
        screen.blit(con, [x_center-text_width/2, screen_size[1]-legend_height-bot_offset+leg_tit_height+text_offset*2]) 

        #check if we have a winning state and determine whether to show win message
        if check_win() == 1:
            win_msg = "Completed. Good Job!"
            win = font2.render(win_msg,True,WHITE)
            text_width, text_height = font2.size(win_msg)
            screen.blit(win, [x_center-text_width/2, 100+text_offset+text_height]) 

        # refresh everyting on screen
        pygame.display.flip()
        
        # limit the update to 60 frames per second
        clock.tick(60)
 
if __name__ == "__main__":
    main()
