from talon.voice import Context, Key, press, Str, Rep
from user.emacs.utils import lisp_eval,elisp
from user.emacs.server import send,disconnect,connect
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number,elisp
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words


buffer_map = {
    "file lint": [ Key('esc space m l')],
    "save": [ Key('esc space f s z z')],
    "savage": lambda x: elisp("(save-and-switch)"),
    # "buffs": lambda x: send("buffs"),
    # "tap": [ Key('esc space l b')],
    "scratch": [Key('esc space b s')],
    "close buffer": [ Key('esc'),':bd',Key('enter')],
    "close other buffers": [ Key('esc space b m')],
    "clobber": [ Key('esc space b o')],

    #buffers
    "lab": [ Key('esc space b p')],
    "list buffers": [ Key('esc space l b')],
    "buffs": [ Key('esc space l b')],
    "last buffer": [ Key('esc space b p')],
    "list buffs": [ Key('esc space l b')],
    "nab": [ Key('esc space b n')],
    "next buffer": [ Key('esc space b n')],

    # tabs
    "tabber": lambda x: elisp("(centaur-tabs-forward-group)"),
    "tabby": lambda x: elisp("(centaur-tabs-backward-group)"),
    "lat": lambda x: elisp("(centaur-tabs-backward)"),
    "nat": lambda x: elisp("(centaur-tabs-forward)"),
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

