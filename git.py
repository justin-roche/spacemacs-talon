from talon.voice import Context, Key 

from user.utils import is_filetype, numerals
from user.emacs.utils import key_repeat ,elisp

exts = ("magit:", "COMMIT_EDITMSG")

context = Context("git", func=is_filetype(exts))

git_map = {
    "get init": lambda x:  elisp("(magit-init)"),
    "get finalize ": [Key('alt-m g f')],

    "sin": [Key('ctrl-l')],
    "down" : Key('cmd-esc ctrl-n'),
    "up" : Key('cmd-esc ctrl-p'),
    "up" + numerals: lambda x: key_repeat(x, 1,["ctrl-p"]),
    "down" + numerals: lambda x: key_repeat(x,1, ["ctrl-n"]),

    "center": [Key('ctrl-l')],
    "test": [Key('space')],
    "save": [Key('ctrl-c ctrl-c')],
    "cancel": [Key('ctrl-c ctrl-k')],

}

context.keymap(git_map)












 
