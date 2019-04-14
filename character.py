from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer,text_to_number, numerals, optional_numerals 

import functools
import time
#from user.vim.utils import jump_to_line,execute_action,set_mode
def goto_character(r,m):
                    jump_number = text_to_number(m._words[1:] )-1
                    # press('esc')
                    Key(r)(None)
                    Key('esc')(None)
                    Str(str('n') * jump_number)(None)

def del_action(m):
    line_number = parse_words_as_integer(m._words[1:] )
    for a in range(0,line_number):
        press('backspace')

def con_action(m):
    line_number = text_to_number(m._words[1:] ) 
    press('esc')
    press('i')
    for a in range(0,line_number):
        press('delete')

def key_action(k):
    key = k
    press('esc')
    def fn(m):
      n = text_to_number(m._words[1:] )
      press(str(n))
      press(key)
    return fn

character_map = {
    'repy caps': Key('esc ~'),
    'del' + numerals: del_action,
    'connor' + numerals: con_action ,
    'repy caps': Key('esc ~'),

    'gecko': Key('esc / \' \ | " enter a'),
    'gecko' + optional_numerals:  functools.partial(goto_character, 'esc / \' \ | " enter a' ),
    'geek': Key('esc / = enter a'),
    'geek' + optional_numerals:  functools.partial(goto_character, 'esc / = enter a' ),
    'gamma': Key('esc / \ , enter a'),
    'gamma' + optional_numerals:  functools.partial(goto_character, 'esc / \ , enter a'),
    'garage': Key('esc / \ [ \ | \ ] enter a'),
    # 'gab': Key('esc / \ [ \ | \ ] enter a'),
    'gap': Key('esc / ( \ | ) enter a'),
    'gap' + optional_numerals:  functools.partial(goto_character, 'esc / ( \ | ) enter a'),
    'goalie': Key('esc / : enter a'),
    'goalie' + optional_numerals:  functools.partial(goto_character, 'esc / : enter a'),

}
