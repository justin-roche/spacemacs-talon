
from talon.voice import Context, Key, press, Str, Rep
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number 

from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals

exts = ("*Minibuf-1*", ".orgx")

context = Context("helm", func=is_filetype(exts))

def helm_select(x):
    n = text_to_number(x._words[1:] )
    press("ctrl-c")
    Str(str(n))(None)

helm_map = {
    "down" + numerals: lambda x: helm_select(x),
    "hat" + numerals: lambda x: helm_select(x) ,
}

context.keymap(helm_map)












 
