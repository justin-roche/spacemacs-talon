from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer

tree_map = {
   "neo": [Key('esc space f t')],
   "tree": [Key('esc space f t')],
   "book": [Key('cmd-esc space T b')],
   "tree shell": [Key('ctrl-s')],
   "tree up": [Key('ctrl-K')],
   "neo root": [Key('esc space p t')],
   "neo copy": [Key('esc space p c')],
   "nerd": [Key('K')],
   # "nerd": [Key('K')],
   # "neo": [Key('esc space 0 space j j') ],
}  
