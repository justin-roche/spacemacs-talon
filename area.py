from talon.voice import Key

area_map = {
    "cut match": [Key('esc v % x')],
    "go match": [Key('cmd-esc %')],
    "go match": [Key('cmd-esc %')],
    "copy quotes": [Key('esc y i "')],
    "copy paren": [Key('esc y i (')],
    "copy quote": [Key("esc y i '")],
    "copy tick": [Key("esc y i `")],
    "copy space": [Key('esc B v E y')],
    "copy match": [Key('esc v % y')],

    #select by surround
    "select paren": [Key('esc v i (')],
    "select tick": [Key('esc v i `')],
    "select quotes": [Key('esc v i "')],
    "select double": [Key('esc v i "')],
    "select quote": [Key('esc v i \'')],
    "select single": [Key('esc v i \'')],
    "select bracket": [Key('esc v i [')],
    "select angle": [Key('esc v i >')],
    # select to
    'fat': Key('cmd-esc v t'),
    'vat': Key('cmd-esc v t'),
    "vase": [Key('cmd-esc v space j j')],

    # "select space": [Key('esc v i  ')],

    #changes by surround
    "change tick": [Key("esc c i `")],
    "change space": [Key('esc B v E c')],
    "change angle": [Key('esc c i <')],
    'change brackets': Key('esc " _ c i ['),
    'chap': Key('esc " _ c i ('),
    # 'change paren': Key('esc " _ c i ('),
    "change angle": [Key('esc c i <')],
    "change single": [Key("esc c i '")],
    "change double": [Key('esc c i "')],
    'change quote': Key('esc \" c i "'),
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
    'sand': Key("cmd-esc space v"),
    'shrink': Key("cmd-esc alt-V"),
    'surround': Key("cmd-esc s"),
    'select matcher': Key('cmd-esc v % h o l'),
    'select match': Key('cmd-esc v %'),
    'dope match': Key('cmd-esc v % y P'),

    'copy match': Key('cmd-esc v % y'),
    'select back': Key('cmd-esc v T'),
}
