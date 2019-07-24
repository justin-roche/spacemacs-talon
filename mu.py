import sys

from talon.engine import engine
from talon.voice import Context, Key
from user.emacs.utils import elisp, key_repeat
from user.utils import is_filetype, numerals

exts = ("*mu4e", "Re: ", ".orgx")

context = Context("mu4e", func=is_filetype(exts))

mu4e_map = {
    "reply": [Key('R')],
    "new message": lambda x: elisp("(mu4e-compose-new)"),
}  

toggle_map = {
        "edit mode": lambda x: activate(),
        "pros mode": lambda x: deactivate(),
}

dictation_map = {
    "center": [Key('cmd-esc z z') ],
    "down" + numerals: lambda x: key_repeat(x,1, "j"),
    "up" + numerals: lambda x: key_repeat(x, 1,"k"),
}

def deactivate():
    context.unload()
    engine.mimic("talon deactivate emacs map".split())
    engine.mimic("talon deactivate standard map".split())
    dictation_map.update(toggle_map)
    context.keymap(dictation_map)
    context.load()

    sys.stdout.write('\a')
    sys.stdout.flush()


def activate():
    context.unload()
    engine.mimic("talon activate emacs map".split())
    engine.mimic("talon activate standard map".split())
    mu4e_map.update(toggle_map)
    context.keymap(mu4e_map)
    context.load()

    sys.stdout.write('\a')
    sys.stdout.flush()

activate()
