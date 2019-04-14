from talon.voice import Context, Key, press, Str, Rep

area_map = {
    "copy quotes": [Key('esc y i "')],
    "copy paren": [Key('esc y i (')],
    "copy quote": [Key("esc y i '")],
    "copy tick": [Key("esc y i `")],
    "copy space": [Key('esc B v E y')],

    #changes by surround

    "change paren": [Key('esc c i (')],
    "change tick": [Key("esc c i `")],
    "change space": [Key('esc B v E c')],
    "change angle": [Key('esc c i <')],
    'change brackets': Key('esc " _ c i ['),
    'change paren': Key('esc " _ c i ('),
    "change angle": [Key('esc c i <')],

    "change quote": [Key("esc c i '")],
    "change quotes": [Key('esc c i "')],
    'mutatis': Key("esc l \" _ c i '"),
    'mute': Key("esc l \" _ c i '"),
    'mutotis': Key('esc \" c i "'),
    'change quote': Key('esc \" c i "'),
    
    "paste quotes": [Key('esc " _ c i " esc p')],
    "paste paren": [Key('esc " _ c i ( esc p')],
    "paste tick": [Key('esc " _ c i ` esc p')],
    "paste bracket": [Key('esc " _ c i [ esc p')],
    "paste brace": [Key('esc " _ c i { esc p')],
    "paste line": [Key('esc " _ d d esc p')],

    # surrounds
    'surround quote': "gS'", 
    'wrap quote': "gS'", 
    'surround double': 'gS"',
    'wrap double': 'gS"',
    'surround bracket': 'gS[', 
    'wrap bracket': 'gS[', 
    'surround paren': "gS(",
    'wrap paren': "gS(",

    'delta': Key('esc d t'),
    'delta back': Key('esc d T'),
}
 
