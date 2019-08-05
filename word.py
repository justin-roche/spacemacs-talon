from talon.voice import Key
from user.emacs.utils import interpolate_number
from user.utils import numerals

word_map = {
    'cut small': Key('esc l b v w x'),
    '(backward | back word)': Key('cmd-esc b'),
    'word': Key('cmd-esc w'),
    'chase': Key('cmd-esc c i w'),
    # "small": lambda x: jump(x, "w"),
    "delete small": [Key('cmd-esc'), "daw"],
    "copy small" + numerals: lambda x: interpolate_number(x, "by{n}w", 2),
    "copy small": lambda x: interpolate_number(x, "by{n}w", 2),
    #
    # "copy big" + numerals: lambda x: interpolate_number(x, "y{n}W", 2),

    # "big" + numerals: lambda x: jump(x, "W"),
    # "big": lambda x: jump(x, "W"),
    # "delete big": [Key('cmd-esc'), "daW"],
    # "copy big": lambda x: interpolate_number(x, "y{n}W", 2),
    # 'change big': Key('esc l B c W'),
    # 'paste big': Key('esc l B c E esc p x'),
    # 'select big': Key('esc l B v E'),
    # 'put big': Key('esc B y W esc ` ` p'),
    # 'select small': Key('esc l b v e'),
    # 'paste small': Key('esc l b c e esc p x'),
    # 'put small': Key('esc b y w esc ` ` p'),
    'repy': Key('x i'),
    'change case': Key('esc b ~ e a '),
    # 'transpose words': [Key('esc'),'dawwP'],
}

# "small" + numerals: lambda x: jump(x, "w"),
# "big back" + numerals: lambda x: jump(x, "B"),
# "big back": lambda x: jump(x, "B"),

# "delete small" + numerals: lambda x: jump(x, "daw"),
# "delete big" : lambda x: jump(x, "daW"),
