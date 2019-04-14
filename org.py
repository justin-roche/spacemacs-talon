from talon.voice import Context, Key, press, Str, Rep

from user.utils import parse_words_as_integer,    parse_words_as_integer
import functools
import time


org_map = {
    "organ": [Key('esc space o l')],
    "org toggle": [Key('esc shift-tab')],
    "org up": [Key('alt-up')],
    "org down": [Key('alt-down')],
    "head": [Key('esc , h i a')],
    "subhead": [Key('esc , h i alt-right A')],

    "promote": [Key('alt-left')],
    "promoter": [Key('shift-alt-left')],
    "demote": [Key('alt-right')],
    "demoter": [Key('shift-alt-right')],
    
    "org to do": [Key('esc shift-right')],
    "org tag": [Key('esc ctrl-c ctrl-q')],
    "org view": [Key('esc ctrl-c / t')],
    "org schedule": [Key('esc ctrl-c ctrl-s')],
    "org agenda": [Key('esc space m a c')],
    "org archive": [Key('esc , A')],

    "org row": [Key('esc alt-shift-down')],
    "org column": [Key('esc alt-shift-right')],
 
}
