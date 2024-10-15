########################################
# Name: Julia Martin
# Collaborators: Jimmy & Gabby
# Estimate time spent (hrs): 3
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score


def clicky_box():
    def rand_rect(x,y,w,h):
        r = GRect(x,y,w,h)
        r.set_filled(True)
        r.set_color('#FF0000')
        return r
    
    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    sqr_w = 50
    sqr_h = 50
    
    x = random.randint(50,GW_WIDTH-50)
    y = random.randint(50,GW_HEIGHT-50)
    
    r = rand_rect(x-sqr_w/2, y-sqr_h/2, sqr_w, sqr_h)
    gw.add(r)
    
    score = 0
    
    text = GLabel(str(score) + " points scored", 215, 90)
    gw.add(text)
    
    def on_mouse_down(event):
        nonlocal x, y, r, score, text
        
        click_x = event.get_x()
        click_y = event.get_y()
        
        print(event.get_x(), event.get_y())
        if (click_x >= x) and (click_x <= x+sqr_w) and (click_y >= y) and (click_y <= y+sqr_h):
            gw.remove(r)
            x = random.randint(50,GW_WIDTH-50)
            y = random.randint(50,GW_HEIGHT-50)
            r = rand_rect(x,y,sqr_w,sqr_h)
            gw.add(r)
            score = score + 1
            gw.remove(text)
            text = GLabel(str(score) + " points scored", 215, 90)
            gw.add(text)
        else:
            score = 0
            text = GLabel(str(score) + " points scored", 215, 90)
            gw.remove(text)
            gw.add(text)
        
    

    
    gw.add_event_listener("click",on_mouse_down)

















if __name__ == '__main__':
    clicky_box()










if __name__ == '__main__':
    clicky_box()
