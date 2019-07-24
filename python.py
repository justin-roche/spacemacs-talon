from talon.voice import Context, Key
from user.utils import is_filetype

exts = (".py", ".orgx")

context = Context("python", func=is_filetype(exts))

py_map = {
    'snip  escapist': 'esc',
    'auto flake': Key("cmd-esc space m r i"),
    'format': Key('cmd-esc space m = ='),
    'snip  commander': 'cmd-esc',

}

context.keymap(py_map)
