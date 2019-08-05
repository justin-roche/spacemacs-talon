from talon.voice import Key
from user.emacs.utils import elisp

deletions_map = {
    # delete until
    "delta": lambda x: elisp("(call-interactively 'jr/delete-to)"),
    "delta back":
    lambda x: elisp("(call-interactively 'jr/delete-to-backward)"),
    # delete until shortcuts
    'dealer space': Key('esc d t space i'),
    'delta end': Key('esc D a'),
    'delta space': Key('esc d t space i'),
    'darko': Key('esc d t , a'),
    'darpa': Key('esc d t ) i'),
    # delete inside
    "delete match": [Key('esc v % d')],
    "delete tick": [Key("esc d i `")],
    "delete space": [Key('esc B v E d')],
    "delete angle": [Key('esc d i <')],
    'delete brackets': Key('esc " _ d i ['),
    'delete paren': Key('esc " _ d i ('),
    "delete angle": [Key('esc d i <')],
    "delete single": [Key("esc d i '")],
    "delete double": [Key('esc d i "')],
    'mute': Key("esc l \" _ d i ' i"),
}
