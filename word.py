from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer, numerals, optional_numerals,text_to_number 
import functools
import time
from user.emacs.vim_utils import jump_to_line,execute_action,set_mode

                    
                    
# def delete_small(m):

                    # jump_number = text_to_number(m._words[1:] )
                    # press('esc')
                    # Str(str(jump_number) + 'dw')(None)
                    
def jump(m,k = None,a = None):
                    
                    jump_number = text_to_number(m._words[1:] )
                    if jump_number == 0:
                                        jump_number = 1
                    press('cmd-esc')
                    Str(str(jump_number) + k)(None)
                    # if a != None:
                                        # Str(str(a))(None)
def interpolate_number(m,s,i = 1):
                    
                    n = text_to_number(m._words[i:] )
                    if n == 0:
                                        n = 1
                    press('cmd-esc')
                    Str(str(s.format(n = n)) )(None)

word_map = {
                    "big" + numerals: lambda x: jump(x, "W"),
                    "big" : lambda x: jump(x, "W"),
                    "small" + numerals: lambda x: jump(x, "w"),
                    "small" : lambda x: jump(x, "w"),
                    "big back" + numerals: lambda x: jump(x, "B"),
                    "big back" : lambda x: jump(x, "B"),
                    
                    "delete small" + numerals: lambda x: jump(x, "dw"),
                    "delete small" : lambda x: jump(x, "dw"),
                    "dog" + numerals: lambda x: jump(x, "dw"),
                    "dog" : lambda x: jump(x, "dw"),

                    "copy small" + numerals: lambda x: interpolate_number(x, "y{n}w",2),
                    "copy small" : lambda x: interpolate_number(x, "y{n}w",2),
                    "copy big" + numerals: lambda x: interpolate_number(x, "y{n}W",2),
                    "copy big" : lambda x: interpolate_number(x, "y{n}W",2),
                    
                    'change big': Key('esc l B c W'),
                    'change small': Key('esc l b c w'),
                    
                    'put small': Key('esc b y w esc ` ` p'),
                    'put big': Key('esc B y W esc ` ` p'),

                    'repy': Key('x i'),
                    'change case': Key('esc b ~ e a '),
                    'transpose words': [Key('esc'),'dawwP'],
}

