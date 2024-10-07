############################################################
# Name: Julia Martin
# Name(s) of anyone worked with:
# Est time spent (hr): 2
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

#i made it into a lambda without (much) AI help!
rect = lambda x,y,w,h : GRect(x,y,w,h)
oval = lambda x,y,w,h : GOval(x,y,w,h)
line = lambda x1,y1,x2,y2 : GLine(x1,y1,x2,y2)
label = lambda str,x,y : GLabel(str,x,y)

def draw_image():
    gw = GWindow(WIDTH, HEIGHT)
    
    rect_neck = rect(285,200,50,100)
    rect_neck.set_filled(True)
    rect_neck.set_fill_color("#707070")
    gw.add(rect_neck)
    
    oval_head = oval(160,110,300,170)
    oval_head.set_filled(True)
    oval_head.set_fill_color("#BABABA")
    gw.add(oval_head)

    rect_body = rect(200,300,220,150)
    rect_body.set_filled(True)
    rect_body.set_fill_color("#BABABA")
    gw.add(rect_body)

    rect_left_arm = rect(120,340,80,35)
    rect_left_arm.set_filled(True)
    rect_left_arm.set_fill_color("#707070")
    gw.add(rect_left_arm)

    rect_right_arm = rect(420,340,80,35)
    rect_right_arm.set_filled(True)
    rect_right_arm.set_fill_color("#707070")
    gw.add(rect_right_arm)
    
    rect_left_leg = rect(230,450,50,100)
    rect_left_leg.set_filled(True)
    rect_left_leg.set_fill_color("#707070")
    gw.add(rect_left_leg)
    
    rect_right_leg = rect(340,450,50,100)
    rect_right_leg.set_filled(True)
    rect_right_leg.set_fill_color("#707070")
    gw.add(rect_right_leg)
    
    rect_mouth = rect(265,220,90,25)
    rect_mouth.set_filled(True)
    rect_mouth.set_fill_color("#ffffff")
    gw.add(rect_mouth)
    
    line_tooth1 = line(295,220,295,245)
    gw.add(line_tooth1)
    
    line_tooth2 = line(325,220,325,245)
    gw.add(line_tooth2)
    
    oval_left_eye = oval(210,145,45,45)
    oval_left_eye.set_filled(True)
    oval_left_eye.set_fill_color("#ffffff")
    gw.add(oval_left_eye)

    oval_right_eye = oval(360,145,45,45)
    oval_right_eye.set_filled(True)
    oval_right_eye.set_fill_color("#ffffff")
    gw.add(oval_right_eye)

    text = label("TaKe Me To YoUr LeAdEr", 215, 90)
    gw.add(text)

if __name__ == '__main__':
    draw_image()
