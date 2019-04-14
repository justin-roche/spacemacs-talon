from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer, numerals
import functools
import time
from user.emacs.vim_utils import jump_to_line,execute_action,set_mode

def start_press(m,mode,t):
    def rf(a):
      global pressing
      pressing = True
      press(mode)  
      for i in range(0,100):
          if pressing  == True:
            time.sleep((t or 0.1))
            press(m)

    return rf

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
    # "delete occurrences": [Key("esc"),':%s///g',Key('left left left') ],
}

