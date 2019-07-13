
from talon.voice import Context, Key, press, Str, Rep
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype

exts = (".py", ".orgx")

context = Context("python", func=is_filetype(exts))

py_map = {
        'snip  escapist': 'esc',
    'snip  commander': 'cmd-esc',
}

context.keymap(py_map)












 
