from talon.voice import Key
from user.custom_utils import interpolate
from user.emacs.utils import elisp, interpolate_number, jump, key_repeat
from user.utils import numerals

line_map = {

    # navigation
    "up" + numerals: [
        lambda x: key_repeat(x, 1, "k"),
        lambda x: elisp("(back-to-indentation)"),
        # Key("i")
    ],
    "down" + numerals: [
        lambda x: key_repeat(x, 1, "j"),
        lambda x: elisp("(back-to-indentation)"),
        # Key("i")
    ],
    # "up" + numerals: lambda x: key_repeat(x, 1,"k"),
    "down":
    Key('cmd-esc j'),
    "up":
    Key('cmd-esc k'),
    'lend' + numerals:
    lambda x: interpolate("cmd-esc $ {h*n} a", x),
    'lend':
    Key('esc $ a'),
    'lens' + numerals: [
        lambda x: elisp("(back-to-indentation)"),
        lambda x: interpolate("{l*n} a", x),
    ],
    'lens': [
        lambda x: elisp("(back-to-indentation)"),
        Key("i"),
    ],

    #interline navigation
    "northwest":
    Key("esc k $"),
    "southwest":
    Key("esc j $"),
    "northeast":
    Key("esc k 0"),
    "southeast":
    Key("esc j 0"),

    #region selection
    'select line':
    Key('esc V'),
    'select end': [Key('esc'), 'v$', 'h'],
    'select start': [Key('esc'), 'v^'],
    'copy line':
    Key('esc Y'),

    #   line delete
    'cut line':
    Key('esc X'),
    'delete line':
    Key('esc d d'),
    'clear line':
    Key('esc ^ _ d $ a'),
    'paste over line':
    Key('esc V p'),
    "deli" + numerals:
    lambda x: jump(x, "dd"),
    "deli":
    lambda x: jump(x, "dd"),

    # line joins
    'join':
    Key('esc k J'),
    'joined':
    Key('esc J'),
    "move up" + numerals:
    lambda x: key_repeat(x, 2, [" xK"]),
    "move down" + numerals:
    lambda x: key_repeat(x, 2, [" xJ"]),

    # delete to the end
    'delete to end':
    Key('esc l D a'),
    'delete to start':
    Key('esc l d 0'),

    #  line creation
    'insert line':
    Key('esc o'),
    'break':
    Key('i enter enter esc k i'),
    'island':
    Key('esc o'),
    'inlet':
    Key('esc O'),
    'line break': [Key('esc i'), "\n"],
    'duplicate line':
    Key('esc v Y p'),
    'dope':
    Key('cmd-esc Y P'),
    'dope up':
    Key('cmd-esc v Y O esc p'),

    # "get down" + numerals: lambda x: key_repeat(x,2, ["ctrl-n"]),
    "jumper" + numerals:
    lambda x: interpolate("{n} G", x, 1),
    "liner" + numerals:
    lambda x: interpolate_number(x, "V{n}k", 1),
    "lines" + numerals:
    lambda x: interpolate_number(x, "V{n}j", 1),

    # tags
    'commie': [Key("cmd-esc V g c i")],
    "commie" + numerals:
    lambda x: interpolate("cmd-esc V {n} j g c i", x, 1),
    # 'commies': [Key('g c i')],
    'tag colon': [Key('esc $ a'), Key(':')],
    'tag comma': [Key('esc $ a'), Key(',')],
}
# 'lock' + optional_numerals + "to" + optional_numerals: range_select,
# "put down" + numerals: lambda x: interpolate_number(x,"x{n}jp",2) ,
# "put up" + numerals: lambda x: interpolate_number(x,"x{n}kp",2) ,
# "goalie" + numerals: lambda x: interpolate_number(x,"{n}G",1) ,
# 'insert space ': [Key('esc i'), " "],
# 'tag' + numerals:  lambda x: tag(x),
# 'doper': Key('cmd-esc V y P o'),
# "doper" + numerals: duplicate,

# 'insert line above': Key('esc O'),
# 'pastel':  Key('esc V p' ),
# 'color': Key('esc X'),
# 'line start': Key('esc 0'),
