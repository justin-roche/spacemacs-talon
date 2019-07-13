from talon.voice import Context, Key, press, Str, Rep
from talon.voice import Context, Key, press, Str, Rep

from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number 

exts = ("*NeoTree*", ".orgx")

context = Context("tree", func=is_filetype(exts))

def open_file(x):
    key_repeat(x,1, "j"),
    # n = text_to_number(x._words[1:] )
    press("enter")
    # Str(str(n))(None)

tree_map = {
   # "neo": [Key('esc space f t')],

    "open" + numerals: lambda x: open_file(x),
   "book": [Key('cmd-esc space t B')],
   "center": [Key('ctrl-l')],
   "sin": [Key('ctrl-l')],
   "copy": [Key('space t c')],
   "refresh": [Key('cmd-esc space t r')],
   "target": [Key('cmd-esc space t T')],
   "tree move": [Key('cmd-esc space t m')],
   "shell": [Key('cmd-esc space t s')],
   "generate": [Key('cmd-esc space t g')],
   "tree up": [Key('cmd-esc space t [')],

   "dirt": [Key('cmd-esc space a d')],
   "dirt up": [Key('cmd-esc / \ . \ . enter enter')],
}  
context.keymap(tree_map)
