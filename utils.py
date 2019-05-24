from talon.voice import Context, Key, press, Str, Rep 
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals
import functools
import time 
import threading
from talon import ctrl


alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()

alphabet = " (" + " | ".join(alpha_alt) + ") +"
scroll_speed = 10
cancel_scroll = False

def del_action(m):
    line_number = parse_words_as_integer(m._words[1:] )
    for a in range(0,line_number):
        press('backspace')
        
def interpolate_number(m,s,i = 1):
                    
                    n = text_to_number(m._words[i:] )
                    if n == 0:
                                        n = 1
                    press('cmd-esc')
                    Str(str(s.format(n = n)) )(None)

def jump(m,k = None):
                    jump_number = text_to_number(m._words[1:] )
                    if jump_number == 0:
                                        jump_number = 1
                    press("cmd-esc")

                    Str(str(jump_number))(None)
                    Str(k)(None)
                    

def key_repeat(m,i = 1,k = []):
                    repeat_number = text_to_number(m._words[i:] )
                    if repeat_number == 0:
                                        repeat_number = 1
                    press("cmd-esc") 
                    for i in range(0, repeat_number):
                        for key in k:
                            if key == 'down' or key == 'up' or key == 'enter' or key  == "ctrl-alt-j" or key  == "ctrl-alt-k"  :
                                press(key)
                                # (Nonel
                            else:
                                Str(str(key))(None) # Key(key)
                                                           

# def put_action(m):
                    # jump_number = text_to_number(m._words[1:] )
                    # if jump_number == 0:
                    #                     jump_number = 1
                    # press("cmd-esc")
                    # Str('yy')(None)
                    # Str(str(jump_number - 1) + 'j')(None)
                    # # Str('p')(None)

def select_lines(m,k = None):
        line_number = text_to_number(m._words[1:])
        press("cmd-esc")
        press("V")
        Str(str(line_number) + k)(None)

def range_select(m):
        i = -1
        if m._words[2] == "to":
                            i = 2
        if m._words[3] == "to":
                            i = 3
        line_number_1 = parse_words_as_integer(m._words[1:i] )
        line_number_2 = parse_words_as_integer(m._words[i:] )
        Str(str(line_number_1))(None)

def start_press(m,mode,t):
    def rf(a):
      global pressing
      pressing = True
      press(mode)  
      for i in range(0,100):
          if pressing  == True:
            time.sleep((t or 0.1))
            press(m)

    return rf


def threaded_scroll(dir):
    global cancel_scroll
    global scroll_speed
    while True:
         ctrl.mouse_scroll(dir * scroll_speed)
         time.sleep(.1)
         if cancel_scroll == True:
             cancel_scroll = False
             break
            
def mouse_scroll_down(a):
            thread = threading.Thread(target=threaded_scroll, args=([-1]))
            thread.start()

def mouse_scroll_up(a):
            thread = threading.Thread(target=threaded_scroll, args=([1]))
            thread.start()

def stop_scroll(a):
    global cancel_scroll
    cancel_scroll = True

def lisp_eval(c):
    # Key('cmd-esc alt-:')
    Str(c)
    # Key('enter')
def elisp(c):
    press('cmd-esc')
    press('alt-:')
    Str(c)(None)
    press('enter')
