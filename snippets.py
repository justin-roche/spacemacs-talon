from talon.voice import Context, Key, press, Str, Rep
from user.utils import parse_words_as_integer
import functools
import time

snippet_map = {
    'snip temparray': Key('esc i a r r'),
    'snip temp': 'temp',
    'snip tempstring': Key('esc i s t r'),
    'snip temp2': 'temp2',
    'snip temp3': 'temp3',
    'snip temp4': 'temp4',
    'snip typestring': 'String',
    'snip typeint': 'Int',
    'snip  escapist': 'esc',
    'snip  min': 'min',
    'snip Lenny': Str(' len' ),
    'call': ['()', Key('left')],
    'double quotes': ['""', Key('left')],
    'quotes': ["''", Key('left')],
    'braces': ['{}', Key('left')], 
    'brackets': ['[]', Key('left')], 
    'expand':[Key('esc space i s down enter')]
}  
