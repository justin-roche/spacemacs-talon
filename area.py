from talon.voice import Context, Key, press, Str, Rep

area_map = {
    "delete match": [Key('esc v % d')],
    "cut match": [Key('esc v % x')],
    "go match": [Key('cmd-esc %')],
    
    "copy quotes": [Key('esc y i "')],
    "copy paren": [Key('esc y i (')],
    "copy quote": [Key("esc y i '")],
    "copy tick": [Key("esc y i `")],
    "copy space": [Key('esc B v E y')],
    "copy match": [Key('esc v % y')],
    
    "carry quotes": [Key('esc y a "')],
    "carry double": [Key('esc y a "')],
    "carry paren": [Key('esc y a (')],
    "carry quote": [Key("esc y a '")],
    "carry single": [Key("esc y a '")],
    "carry tick": [Key("esc y a `")],
    # "carry space": [Key('esc B v E y')],
    # "copy match": [Key('esc v % y')],
    
    #select by surround
    "select paren": [Key('esc v i (')],
    "select tick": [Key('esc v i `')],
    "select quotes": [Key('esc v i "')],
    "select double": [Key('esc v i "')],
    "select quote": [Key('esc v i \'')],
    "select single": [Key('esc v i \'')],
    "select bracket": [Key('esc v i [')],
    "select angle": [Key('esc v i >')],

    # "select space": [Key('esc v i  ')],
    
    #changes by surround
    "change tick": [Key("esc c i `")],
    "change space": [Key('esc B v E c')],
    "change angle": [Key('esc c i <')],
    'change brackets': Key('esc " _ c i ['),
    'change paren': Key('esc " _ c i ('),
    "change angle": [Key('esc c i <')],
    "change single": [Key("esc c i '")],
    "change double": [Key('esc c i "')],
    'change quote': Key('esc \" c i "'),

    "delete tick": [Key("esc d i `")],
    "delete space": [Key('esc B v E d')],
    "delete angle": [Key('esc d i <')],
    'delete brackets': Key('esc " _ d i ['),
    'delete paren': Key('esc " _ d i ('),
    "delete angle": [Key('esc d i <')],
    "delete single": [Key("esc d i '")],
    "delete double": [Key('esc d i "')],
    'mute': Key("esc l \" _ d i ' i"),
    # 'merry': Key("esc l \" _ d a ' i"),
    # 'delete match': Key('esc \" c i "'),
    
    "paste quotes": [Key('esc " _ c i " esc p')],
    "paste quote": [Key("esc \" _ c i ' esc p")],
    "paste paren": [Key('esc " _ c i ( esc p')],
    "paste tick": [Key('esc " _ c i ` esc p')],
    "paste bracket": [Key('esc " _ c i [ esc p')],
    "paste brace": [Key('esc " _ c i { esc p')],
    "paste line": [Key('esc " _ d d esc p')],

    # surrounds
    'change surround': Key("cmd-esc space y S"),
    'surround tag': Key("cmd-esc alt-m S"),
    'surround': Key("cmd-esc s"),

    # 'surround quote': "gS'", 
    # 'wrap quote': "gS'", 
    # 'surround double': 'gS"',
    # 'wrap double': 'gS"',
    # 'surround bracket': 'gS[', 
    # 'wrap bracket': 'gS[', 
    # 'surround paren': "gS(",
    # 'wrap paren': "gS(",
    
    'select match': Key('cmd-esc v %'),
    'copy match': Key('cmd-esc v % y'),
    
    # 'sell to': Key('cmd-esc v t'),
    'fat': Key('cmd-esc v t'),
    'vat': Key('cmd-esc v t'),
    'face': Key('cmd-esc v space j j'),
    "vase": [Key('cmd-esc v space j j') ],

    # 'celta': Key('cmd-esc v t'),
    'select back': Key('cmd-esc v T'),

    'delta end': Key('esc D'),
    'delta': Key('esc d t'),
    # 'delta start': Key('esc d t 0'),
    'delta back': Key('esc d T'),

    'select content': Key('cmd-esc space m c'),


}
 
