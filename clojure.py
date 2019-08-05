from talon.voice import Context, Key
from user.utils import is_filetype

exts = (".clj")

context = Context("clojure", func=is_filetype(exts))

clojure_map = {
    "ripple connect": [Key('cmd-esc space m s i')],
    "format": [Key('cmd-esc space m =')],
    "( bevel | evaluate buffer )": [Key('esc , e b')],
    # expressions
    "sexy": [Key('cmd-esc space k k right i')],
    "sex": [Key('cmd-esc space k j right i')],
    "raise": [Key('cmd-esc space k r i')],
    "splice": [Key('cmd-esc space k E i')],
    "barf back": [Key('esc space k B i')],
    "barf": [Key('esc space k b i')],
    "slurp": [Key('esc space k s i')],
    "slurp back": [Key('esc space k S i')],
    "sex above": [Key('cmd-esc space k (')],
    "sex below": [Key('cmd-esc space k )')],
    "sex delete": [Key('cmd-esc space k d x esc i')],
    "sex rap": [Key('esc space k w esc')],
    "sex comment": [Key('esc ctrl-alt-space alt-;')],
    "sex isolate": [Key('esc ctrl-alt-space alt-; alt-;')],
    # "eve": [Key('cmd-esc , e b')],
    "jump": [Key('cmd-esc space m g g')],
    "eve region": [Key('cmd-esc , e r')],
    "evelyn": [Key('cmd-esc , e l')],
    "saver": [Key('cmd-esc f s cmd-esc , e b')],
}

context.keymap(clojure_map)
