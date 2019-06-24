from talon.voice import Context, Key, press, Str, Rep
from user.emacs.utils import start_press, mouse_scroll_up,stop_scroll,mouse_scroll_down
from user.emacs.server import send,disconnect,connect

document_map = {
    'fun': Key( 'cmd-esc ctrl-b'),
    'fan': Key( 'cmd-esc ctrl-f'),
    'half up': Key( 'cmd-esc ctrl-u'),
    'half': Key( 'cmd-esc ctrl-d'),
    'last': Key( 'cmd-esc ctrl-o'),
    'next': Key( 'cmd-esc ctrl-o'),

    'go end': [Key('cmd-esc'), 'G0'],
    'go top': [Key('cmd-esc'), 'gg'],
    'go begin': [Key('cmd-esc'), 'gg'],
    
    "sin": [Key('cmd-esc z z') ],
    "center": [Key('cmd-esc z z') ],

    'scroll': mouse_scroll_down,
    'scroll up': mouse_scroll_up ,
    'stop': stop_scroll,
    
    # "abe": [Key('esc space s j') ],
    # "acer": [Key('space j j') ],
    "ace": [Key('cmd-esc space j j') ],

    "start next": start_press('n','esc',0.3),
    # "search": lambda x: send("search"),

    "search": Key('cmd-esc /'),
    "back": Key('cmd-esc ?'),

    "jump": [Key('esc , g g')],
    "mode jump": [Key('esc space m j')],
    # "show jumps": [ Key('esc ctrl-c ctrl-j')],
    # "halt": stop_right,
    
    "pretty": [Key('cmd-esc space m =')],
    "replace": [Key('esc g g space y r')],
}

