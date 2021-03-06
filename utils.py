import threading
import time

from talon import ctrl
from talon.voice import Str, press
from user.emacs.server import send
from user.utils import parse_words_as_integer, text_to_number

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split(
)

alphabet = " (" + " | ".join(alpha_alt) + ") +"
scroll_speed = 10
cancel_scroll = False


def del_action(m):
    line_number = parse_words_as_integer(m._words[1:])
    for a in range(0, line_number):
        press('backspace')


def interpolate_number(m, s, i=1):
    n = text_to_number(m._words[i:])
    # if n == 0:
    # n = 1
    press('cmd-esc')
    Str(str(s.format(n=n)))(None)


def jump(m, k=None):
    jump_number = text_to_number(m._words[1:])
    if jump_number == 0:
        jump_number = 1
    press("cmd-esc")

    Str(str(jump_number))(None)
    Str(k)(None)


def key_repeat(m, i=1, k=[]):
    repeat_number = text_to_number(m._words[i:])
    if repeat_number == 0:
        repeat_number = 1
    press("cmd-esc")
    repeat_k(repeat_number, k)

def repeat_k(n, k):
    for i in range(0, n):
        for key in k:
            if key == 'down' or key == 'up' or key == 'enter' or key == "ctrl-alt-j" or key == "ctrl-alt-k" or key == "ctrl-p" or key == "ctrl-n":
                press(key)
            else:
                Str(str(key))(None)  # Key(key)




def parse_command(m, k, i=1):
    # n = text_to_number(m._words[i:] )
    n = 2


parse_command(1, "{n*j}")


def select_lines(m, k=None):
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
    line_number_1 = parse_words_as_integer(m._words[1:i])
    line_number_2 = parse_words_as_integer(m._words[i:])
    Str(str(line_number_1))(None)


def start_press(m, mode, t):
    def rf(a):
        global pressing
        pressing = True
        press(mode)
        for i in range(0, 100):
            if pressing == True:
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


def elisp(c):
    press('cmd-esc')
    press('alt-:')
    Str(c)(None)
    press('enter')


def send_parsed_number(m, c, i=1):
    n = text_to_number(m._words[i:])
    n = str(n)

    send(str(c) + "/" + n)
