from talon.voice import Key
from user.emacs.utils import elisp

buffer_map = {
    "file lint": [Key('esc space m l')],
    "save": [Key('esc space f s z z')],
    "savage": lambda x: elisp("(save-and-switch)"),
    "scratch": [Key('esc space b s')],

    # window navigation
    "war": [Key('esc space w l')],
    "well": [Key('esc space w h')],

    # closing buffers
    "close buffer": [Key('esc'), ':bd', Key('enter')],
    "close other buffers": [Key('esc space b m')],
    "clobber": [Key('esc space b o')],

    # buffer navigation
    "lab": [Key('esc space b p')],
    "list recent": lambda x: elisp("(helm-recentf)"),
    "show messages": lambda x:  elisp("(view-echo-area-messages)"),
    
    "buff": [Key('esc space l b')],
    "nab": [Key('esc space b n')],
    "next buffer": [Key('esc space b n')],

    # tabs navigation
    "tabber": lambda x: elisp("(centaur-tabs-forward-group)"),
    "tabby": lambda x: elisp("(centaur-tabs-backward-group)"),
    "lat": lambda x: elisp("(centaur-tabs-backward)"),
    "nat": lambda x: elisp("(centaur-tabs-forward)"),

    # closing
    "close window": [Key('esc space w d')],
    "widow": [Key('esc space w o')],

    # new windows
    "new win": [Key('esc space w n')],
    "winner": [Key('esc space w n')],
    "whaler": [Key('esc space w d')],
    "new horizontal": [Key('ctrl-x 3')],
    "new vertical": [Key('ctrl-x 2')],

    #windows by number
    "win 1": [Key('esc space 1')],
    "win 2": [Key('esc space 2')],
    "win 3": [Key('esc space 3')],
    "win 4": [Key('esc space 4')],

    #frames
    "next frame": [Key('esc space f f')],
    "NAFTA": [Key('esc space f f')],
    "new frame": [Key('esc space f n')],
    "delete frame": [Key('esc space f d')],
}
