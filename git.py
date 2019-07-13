from talon.voice import Context, Key, press, Str, Rep 
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype
from user.emacs.server import send
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number 
import functools
import time 

exts = ("magit:", "COMMIT_EDITMSG")

context = Context("git", func=is_filetype(exts))

git_map = {
    "get finalize ": [Key('alt-m g f')],

    "sin": [Key('ctrl-l')],
    "down" : Key('cmd-esc ctrl-n'),
    "up" : Key('cmd-esc ctrl-p'),
    "up" + numerals: lambda x: key_repeat(x, 1,["ctrl-p"]),
    "down" + numerals: lambda x: key_repeat(x,1, ["ctrl-n"]),

    "center": [Key('ctrl-l')],
    "test": [Key('space')],
    "save": [Key('ctrl-c ctrl-c')],
    "cancel": [Key('ctrl-c ctrl-k')],

}

context.keymap(git_map)












 
