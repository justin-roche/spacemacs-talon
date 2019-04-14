from talon.voice import Context, Key, press, Str, Rep 
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals
import functools
import time 
# from user.emacs.utils import multiline_select, execute_action,set_mode


def jump(m,k = None):
                    
                    jump_number = text_to_number(m._words[1:] )
                    if jump_number == 0:
                                        jump_number = 1
                    press("cmd-esc")
                    Str(str(jump_number) + k)(None)
                    
def key_repeat(m,i = 1,k = []):
                    
                    repeat_number = text_to_number(m._words[i:] )
                    if repeat_number == 0:
                                        repeat_number = 1
                    press("cmd-esc")
                    for i in range(0, repeat_number):
                                       for k in k: 
                                                           Key(k)(None)
def put_action(m):
                    
                    jump_number = text_to_number(m._words[1:] )
                    if jump_number == 0:
                                        jump_number = 1
                    press("cmd-esc")
                    Str('yy')(None)
                    Str(str(jump_number - 1) + 'j')(None)
                    Str('p')(None)

def select_lines(m,k = None):
        line_number = text_to_number(m._words[1:])
        press("cmd-esc")
        press("V")
        Str(str(line_number) + k)(None)

def range_select(m):
        i = -1
        if m._words[2] == "to":
                            i = 2
        if m._words[3] == "to":
                            i = 3
        line_number_1 = parse_words_as_integer(m._words[1:i] )
        line_number_2 = parse_words_as_integer(m._words[i:] )
        Str(str(line_number_1))(None)
        
line_map  = {
                    "down" + numerals: lambda x: jump(x, "j"),
                    "up" + numerals: lambda x: jump(x, "k"),

                    'lock' + optional_numerals + "to" + optional_numerals: range_select,
                    'line end': Key('esc $'),
                    'line start': Key('esc 0'),

    #region selection
                    'select line': Key('esc V'),
                    'select end':[Key('esc'), 'v$','h'],
                    'select start':[Key('esc'), 'v^' ],
                    'copy line': Key('esc Y'),

#   line delete
                    'cut line': Key('esc X'),
                    'color': Key('esc X'),
                    'delete line': Key('esc d d'),
                    'clear line': Key('esc ^ _ d $ a'),
                    'paste over line':  Key('esc V p' ),
                    'pastel':  Key('esc V p' ),

                    "deli" + numerals: lambda x: jump(x, "dd"),
                    "deli" : lambda x: jump(x, "dd"),
                    # line joins

                    'join':  Key('esc k J' ),
                    'joined':  Key('esc J' ),

                    "move up" + numerals: lambda x: key_repeat(x, 2,["space", "x", "K"]),
                    "move up"  : lambda x: key_repeat(x, 2,["space", "x", "K"]),
                    "move down" + numerals: lambda x: key_repeat(x, 2,["space", "x", "J"]),
                    "move down"  : lambda x: key_repeat(x, 2,["space", "x", "J"]),

                    # delete to the end
                    'dark': Key('esc D'),
                    'delete to end': Key('esc l D a'),
                    'delete to start': Key('esc l d 0'),
                    

                    #  line creation
                    'insert line': Key('esc o'),
                    'island': Key('esc o'),
                    'insert line above': Key('esc O'),
                    'inlet': Key('esc O'),

                    'line break': [Key('esc i'), "\n"],
                    'duplicate line': Key('esc v Y p'),
                    'dope': Key('cmd-esc Y P'),

                    'dope up': Key('esc v Y O esc p'),
                    "put" + numerals: lambda x: put_action(x) ,

                    'insert space ': [Key('esc i'), " "],


                    "liner" + numerals: lambda x: select_lines(x, "k"),
                    "lines" + numerals: lambda x: select_lines(x, "j"),
                    'comment': [Key('esc space ;')],
                    'comment lines': [Key('space ;')],

                    'tag colon': [ Key('esc $ a'),Key(':')],
                    'tag comma': [ Key('esc $ a'),Key(',')],
                    'tag semi': [ Key('esc $ a'),Key(';')],

#interline navigation

                    "northwest": Key("esc k $"),
                    "southwest": Key("esc j $"),
                   "northeast": Key("esc k 0"),
                    "southeast": Key("esc j 0"),
}
