from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer, numerals, optional_numerals,text_to_number
# alphabet
import functools
import time
context = Context('Emacs', bundle='org.gnu.Emacs' )

def del_action(m):
    line_number = parse_words_as_integer(m._words[1:] )
    for a in range(0,line_number):
        press('backspace')
        
def interpolate_number(m,s,i = 1):
                    
                    n = text_to_number(m._words[i:] )
                    if n == 0:
                                        n = 1
                    press('esc')
                    # press('v')
                    Str(str(s.format(n = n)) )(None)
                    
def test():
    Str(context.connection)(None)

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near odd pit quest red sun trap urge vest whale box yes zip'.split()

alphabet = " (" + " | ".join(alpha_alt) + ") +"

def interpolate_letter(w,l):
                    # press('esc')
                    # Str(alphabet)(None)
                    Str('letter')(None)
                    # Str(numerals)(None)
                    # l = m._words[i:] 
                    # if n == 0:
                                        # n = 1
                    # press('v')
                    # Str(str(s.format(n = n)) )(None)
vim_map = {
    "ink": Key("esc i"),
    "normie": Key("esc"),
    
    "vizy": Key("esc v"),
    # "castle": Key("esc v"),
    "castle": lambda x: interpolate_letter(x),
    # "test": lambda x: test(),
    "vizy" + numerals: lambda x: interpolate_number(x, "v{n}w"),
    "vizy" + alphabet: lambda x: interpolate_letter(x, "v{n}w"),
    "vizy big" + numerals: lambda x: interpolate_number(x, "v{n}W",2),

    # "" : lambda x: interpolate_letter(x),
    #  'left' + optional_numerals: jump_left,
    # 'right' + optional_numerals: jump_right,
    
    'deal' + numerals: del_action,
    'cut' : [Key('x')],
    
    'paste' : [Key('esc p')],
    'paster' : [Key('esc o p')],
    'paste below' : [Key('esc o p')],
    
    "undies": Key("esc u") ,
    "redo":[Key('esc'),Key('ctrl-r')],
    "undo": [Key('esc'),'u'],
    "doozy": [Key('esc space a u')],
}
