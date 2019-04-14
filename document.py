from talon.voice import Context, Key, press, Str, Rep
from user.emacs.utils import start_press

document_map = {
    'fun': Key( 'cmd-esc ctrl-b'),
    'fan': Key( 'cmd-esc ctrl-f'),

    'go end': [Key('cmd-esc'), 'G0'],
    'go top': [Key('cmd-esc'), 'gg'],
    'go begin': [Key('cmd-esc'), 'gg'],
    
    "center": [Key('cmd-esc z z') ],

    "abe": [Key('esc space s j') ],
    "acer": [Key('space j j') ],
    "ace": [Key('cmd-esc space j j') ],
    "vase": [Key('esc v space j j') ],

    "start next": start_press('n','esc',0.3),
    "search this": ['*'],

    "jump": [Key('esc , g g')],
    "show jumps": [ Key('esc ctrl-c ctrl-j')],
    # "halt": stop_right,
    
    "pretty": [Key('cmd-esc space m =')],
    "replace": [Key('esc space y r')],
}

