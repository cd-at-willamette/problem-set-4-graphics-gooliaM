########################################
# Name: Julia Martin
# Collaborators:NO CHAT GPT ALL THESE BRAINCELLS
# Estimated time spent (hrs):2
########################################

from pgl import GWindow, GRect

BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    
    #calculate what width and height need to be
    WIDTH = BRICK_WIDTH * BRICKS_IN_BASE
    HEIGHT = BRICK_HEIGHT * BRICKS_IN_BASE/1.3
    
    #rectangle-making function
    rect = lambda x,y,w,h : GRect(x,y,w,h)

    #graphics window
    gw = GWindow(WIDTH, HEIGHT)
    
    #0,0 is top left, so this sets it equal to bottom right minus height of one brick
    y = HEIGHT - BRICK_HEIGHT

    #a function to round up, i couldnt figure out another way to do it :(
    round_up = lambda x : int((x/2)+(x%2))

    #outer loop is for height, inner is for setting the bricks down according to width
    for i in range(round_up(BRICKS_IN_BASE)):
        x = 0
        x = x + BRICK_WIDTH*i
        for a in range(BRICKS_IN_BASE):
            brick = rect(x,y,BRICK_WIDTH,BRICK_HEIGHT)
            gw.add(brick)
            x = x + BRICK_WIDTH
            print(x)
            #creates the right side of the pyramid
            if x == WIDTH - BRICK_WIDTH*i:
                break
        y = y - BRICK_HEIGHT





if __name__ == '__main__':
    draw_pyramid()
