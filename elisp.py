from talon.voice import Context, Key
from user.emacs.utils import elisp
from user.utils import is_filetype

exts = (".el", ".orgx")

context = Context("elisp", func=is_filetype(exts))

lisp_map = {
    "sex above": [Key('cmd-esc space k (')],
    "sex below": [Key('cmd-esc space k )')],
    "sex delete": [Key('cmd-esc space k d x esc i')],
    "sex rap": [Key('esc space k w esc')],
    "sex rap": [Key('esc space k w esc')],
    "sex comment": [Key('esc ctrl-alt-space alt-;')],
    "sex isolate": [Key('esc ctrl-alt-space alt-; alt-;')],
    "slurp": [Key('esc space k s')],
    "jump": [Key('cmd-esc space m g g')],
    "barf": [Key('esc space k b')],
    # evaluation
    "evaluate buffer": [Key('esc , e b')],
    "eve region": [Key('cmd-esc , e r')],
    "evelyn": [Key('cmd-esc , e l')],
    "eve": [Key('cmd-esc , e b')],
    "saver": [Key('cmd-esc f s cmd-esc , e b')],
    # "debug break": lambda x: elisp("(edebug-x-modify-breakpoint-wrapper t)"),
    # "debug break": lambda x: elisp("(edebug-set-breakpoint t)"),
    "show breakpoints":
    lambda x: elisp("(edebug-x-show-breakpoints)"),
    "debug break": [
        lambda x: elisp("(spacemacs/edebug-instrument-defun-on)"),
        lambda x: elisp("(edebug-set-breakpoint t)"),
    ],
    "optional":
    " &optional ",
    "debug finish":
    lambda x: elisp("(debugger-quit)"),
}

context.keymap(lisp_map)
