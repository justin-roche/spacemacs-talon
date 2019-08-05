from talon.voice import Key, Str
from user.custom_utils import (mouse_scroll_down, mouse_scroll_up, start_press,
                               stop_scroll)
from user.emacs.utils import elisp
from user.std import parse_words

document_map = {
    'fun':
    Key('cmd-esc ctrl-b'),
    'fan':
    Key('cmd-esc ctrl-f'),
    'half up':
    Key('cmd-esc ctrl-u'),
    'half':
    Key('cmd-esc ctrl-d'),
    'go top': [Key('cmd-esc'), 'gg'],
    'gab': [Key('cmd-esc'), 'gg'],
    'go end': [Key('cmd-esc'), 'G0'],
    'move end': [Key('cmd-esc'), "mzxG0p'z"],
    "sin": [Key('cmd-esc z z')],
    "center": [Key('cmd-esc z z')],
    'scroll':
    mouse_scroll_down,
    'scroll up':
    mouse_scroll_up,
    'stop':
    stop_scroll,
    "acer":
    lambda x: elisp("(avy-goto-word-crt-line)"),
    "ace": [Key('cmd-esc space j j')],
    "go <dgndictation>": [
        lambda x: elisp("(evil-search-forward)"),
        lambda x: Str(parse_words(x)[0])(None),
    ],
    "search":
    Key('cmd-esc /'),
    "search back":
    Key('cmd-esc ?'),
    'basil':
    Key('esc ` `'),
    "jump": [Key('esc , g g')],
    "mode jump": [Key('esc space m j')],
    "pretty": [Key('cmd-esc space m =')],
    "replace": [Key('esc g g space y r')],
}

# "show jumps": [ Key('esc ctrl-c ctrl-j')],
# "abe": [Key('esc space s j') ],
# "acer": [Key('space j j') ],
# "search": lambda x: send("search"),
# "search": lambda x: elisp("(voice-search)"),
# "halt": stop_right,
