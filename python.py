from talon.voice import Context, Key
from user.utils import is_filetype
import time
exts = (".py")

context = Context("python", func=is_filetype(exts))

py_map = {
    'snip  escapist': 'esc',
    'auto flake': Key("cmd-esc space m r i"),
    'references': [Key('cmd-esc , g u'),
                   lambda x: time.sleep(0.3),
                   Key("space j l")],
    'jump': Key('cmd-esc , g g'),
    'live mode': Key('cmd-esc space m l'),
    'bevel': Key('cmd-esc space m c c'),
    # 'bevel': Key('xxx'),
    'format': Key('cmd-esc space m = ='),
    'snip  commander': 'cmd-esc',
}

context.keymap(py_map)
