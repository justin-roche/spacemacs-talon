from talon.voice import Key
from user.emacs.utils import (mouse_scroll_down, mouse_scroll_up, start_press,
                              stop_scroll)

document_map = {
    'fun': Key('cmd-esc ctrl-b'),
    'fan': Key('cmd-esc ctrl-f'),
    'half up': Key('cmd-esc ctrl-u'),
    'half': Key('cmd-esc ctrl-d'),
    'go end': [Key('cmd-esc'), 'G0'],
    'go top': [Key('cmd-esc'), 'gg'],
    'go begin': [Key('cmd-esc'), 'gg'],
    # 'last': Key( 'cmd-esc ctrl-o'),
    # 'next': Key( 'cmd-esc ctrl-o'),
    "sin": [Key('cmd-esc z z')],
    "center": [Key('cmd-esc z z')],
    'scroll': mouse_scroll_down,
    'scroll up': mouse_scroll_up,
    'stop': stop_scroll,

    # "ace": [Key('cmd-esc space j j') ],
    "search": Key('cmd-esc /'),
    "search back": Key('cmd-esc ?'),
    'basil': Key('esc ` `'),
    "jump": [Key('esc , g g')],
    "mode jump": [Key('esc space m j')],
    "pretty": [Key('cmd-esc space m =')],
    "replace": [Key('esc g g space y r')],
}

# "start next": start_press('n','esc',0.3),
# "show jumps": [ Key('esc ctrl-c ctrl-j')],
# "abe": [Key('esc space s j') ],
# "acer": [Key('space j j') ],
# "search": lambda x: send("search"),
# "search": lambda x: elisp("(voice-search)"),
# "halt": stop_right,
