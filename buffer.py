from talon.voice import Context, Key, press, Str, Rep
from user.emacs.utils import lisp_eval,elisp
from user.emacs.server import send,disconnect,connect
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words

def helm_select(x):
    n = text_to_number(x._words[1:] )
    press("ctrl-c")
    Str(str(n))(None)

buffer_map = {
    "file lint": [ Key('esc space m l')],
    "save": [ Key('esc space f s z z')],
    "savage": lambda x: elisp("(save-and-switch)"),
    "list buffers": [ Key('esc space l b')],
    # "buffs": lambda x: send("buffs"),
    "buffs": [ Key('esc space l b')],
    # "tap": [ Key('esc space l b')],
    "hat" + numerals: lambda x: helm_select(x) ,
    "list buffs": [ Key('esc space l b')],
    "scratch": [Key('esc space b s')],
    "close buffer": [ Key('esc'),':bd',Key('enter')],
    "close other buffers": [ Key('esc space b m')],
    "clobber": [ Key('esc space b o')],
    "lab": [ Key('esc space b p')],
    "last buffer": [ Key('esc space b p')],
    "nab": [ Key('esc space b n')],
    "next buffer": [ Key('esc space b n')],

    #windows
    # "next window": [ Key('esc [-w')],
    # "nafta": [ Key('cmd-`')],
    "new win": [ Key('esc space w n')],
    "winner": [ Key('esc space w n')],
    "widow": [ Key('esc space w o')],
    
    "war": [ Key('esc space w l')],
    "well": [ Key('esc space w h')],
    
    "close window": [ Key('esc space w d')],
    # "close win": [ Key('esc space w d')],
    "whaler": [ Key('esc space w d')],

    "new horizontal": [ Key('ctrl-x 3')],
    "new vertical": [ Key('ctrl-x 2')],

    #windows by number
    "win 1": [Key('esc space 1')],
    "win 2": [Key('esc space 2')],
    "win 3": [Key('esc space 3')], 
    "win 4": [Key('esc space 4')],

    #frames
    "next frame": [ Key('esc space f f')],
    "NAFTA": [ Key('esc space f f')],
    "new frame": [ Key('esc space f n')],
    "delete frame": [ Key('esc space f d')],

}

