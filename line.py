from talon.voice import Context, Key, press, Str, Rep 
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype
from user.emacs.server import send
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number 
import functools
import time 

def tag(x):
    Key('enter')(None)
    key_repeat(x, 1,[" xJ"])

def duplicate(x):
    interpolate_number(x,"V{n}jY`>pO",1) 


line_map  = {

                    "down" + numerals: lambda x: key_repeat(x,1, "j"),
                    "up" + numerals: lambda x: key_repeat(x, 1,"k"),
                    "down" : Key('cmd-esc j'),
                    "up" : Key('cmd-esc k'),

                    # 'lock' + optional_numerals + "to" + optional_numerals: range_select,
                    'line end': Key('esc $'),
                    'line start': Key('esc 0'),
    #region selection

                    'select line': Key('esc V'),
                    'select end':[Key('esc'), 'v$','h'],
                    'select start':[Key('esc'), 'v^' ],
                    'copy line': Key('esc Y'),

#   line delete
                    'cut line': Key('esc X'),
                    # 'color': Key('esc X'),
                    'delete line': Key('esc d d'),
                    'clear line': Key('esc ^ _ d $ a'),
                    'paste over line':  Key('esc V p' ),
                    # 'pastel':  Key('esc V p' ),

                    "deli" + numerals: lambda x: jump(x, "dd"),
                    "deli" : lambda x: jump(x, "dd"),

                    # line joins
                    'join':  Key('esc k J' ),
                    'joined':  Key('esc J' ),

                    "move up" + numerals : lambda x: key_repeat(x, 2,[" xK"]),


    "move down" + numerals : lambda x: key_repeat(x, 2,[" xJ"]),

                    # delete to the end
                    'dark': Key('esc D'),
                    'delete to end': Key('esc l D a'),
                    'delete to start': Key('esc l d 0'),
                    # 'keyboard': lambda x: send('this isa test'),

                    #  line creation
                    'insert line': Key('esc o'),
                    'break': Key('i enter enter esc k i'),
    
                    'island': Key('esc o'),
                    # 'insert line above': Key('esc O'),
                    'inlet': Key('esc O'),

                    'line break': [Key('esc i'), "\n"],
                    'duplicate line': Key('esc v Y p'),
                    'dope': Key('cmd-esc Y P'),
                    # 'doper': Key('cmd-esc V y P o'),
                    # "doper" + numerals: duplicate,
    
                    'dope up': Key('cmd-esc v Y O esc p'),
                    # "put down" + numerals: lambda x: interpolate_number(x,"x{n}jp",2) ,
                    # "put up" + numerals: lambda x: interpolate_number(x,"x{n}kp",2) ,
                    # "goalie" + numerals: lambda x: interpolate_number(x,"{n}G",1) ,

                    # 'insert space ': [Key('esc i'), " "],

    "get down" + numerals: lambda x: key_repeat(x,2, ["ctrl-n"]),
                    "liner" + numerals: lambda x: interpolate_number(x, "V{n}k",1),
                    "lines" + numerals: lambda x: interpolate_number(x, "V{n}j",1),

                    'comment': [Key('esc space ;')],
                    'comment lines': [Key('space :')],

                    'tag colon': [ Key('esc $ a'),Key(':')],
                    'tag comma': [ Key('esc $ a'),Key(',')],
                    'tag' + numerals:  lambda x: tag(x),

#interline navigation

                    "northwest": Key("esc k $"),
                    "southwest": Key("esc j $"),
    "northeast": Key("esc k 0"),
                    "southeast": Key("esc j 0"),
}
