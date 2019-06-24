from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer,text_to_number, numerals, optional_numerals 
import functools

def goto_character(r,m):
                    jump_number = text_to_number(m._words[1:] )-1
                    # press('esc')
                    Key(r)(None)
                    Key('esc')(None)
                    Str(str('n') * jump_number)(None)

character_map = {
    'repy caps': Key('esc ~'),
    'repy caps': Key('esc ~'),

# surrounds

    'gamma': Key('esc / \ , enter a'),
    'gamma' + optional_numerals:  functools.partial(goto_character, 'esc / \ , enter a' ),
    'gecko': Key('esc / \' \ | " enter a'),
    'gecko' + optional_numerals:  functools.partial(goto_character, 'esc / \' \ | " enter a' ),
    'gap': Key('esc / ( \ | ) enter a'),
    'gap' + optional_numerals:  functools.partial(goto_character, 'esc / ( \ | ) enter a' ),
    'garage': Key('esc / \ [ \ | \ ] enter a'),

# symbols
    'geek': Key('esc / = enter a'),
    'goalie': Key('esc / : enter a'),
    # 'geek' + optional_numerals:  functools.partial(goto_character, 'esc / = enter a' ),
    # 'gamma' + optional_numerals:  functools.partial(goto_character, 'esc / \ , enter a'),
    # 'gab': Key('esc / \ [ \ | \ ] enter a'),
    # 'gap' + optional_numerals:  functools.partial(goto_character, 'esc / ( \ | ) enter a'),
    # 'goalie' + optional_numerals:  functools.partial(goto_character, 'esc / : enter a'),

}
