from talon.voice import Context, Key
from user.emacs.utils import elisp
from user.std import parse_words
from user.utils import is_filetype_regexp

exts = ["org-brain"]

context = Context("brain", func=is_filetype_regexp(exts))

enabled = True

brain_map = {
    # view
    # "org expand": [Key('esc shift-tab')],
    "child":
    lambda x: elisp("(call-interactively 'org-brain-goto-child)"),
    # "parent": lambda x: elisp("(call-interactivley 'org-brain-goto-parent)"),
    "rename":
    lambda x: elisp("(call-interactively 'org-brain-rename-file)"),
    "parent":
    lambda x: elisp("(call-interactively 'org-brain-visualize-parent)"),
    "add parent":
    lambda x: elisp("(call-interactively 'org-brain-add-parent)"),
    "add child":
    lambda x: elisp("(call-interactively 'org-brain-add-child)"),
    "add friend":
    lambda x: elisp("(call-interactively 'org-brain-add-friendship)"),
    "add resource":
    lambda x: elisp("(call-interactively 'org-brain-paste-resource)"),
    "new journal":
    lambda x: elisp("(jr/org-brain-journal-add)"),
    "remove friend":
    lambda x: elisp("(call-interactively 'org-brain-remove-friendship)"),
    "remove child":
    lambda x: elisp("(call-interactively 'org-brain-remove-child)"),
    "remove parent":
    lambda x: elisp("(org-brain-remove-parent)"),
    # "ace":
    # lambda x: elisp("(jr/avy-brain-jump)"),
    "go <dgndictation>": [
        Key("g g"),
        lambda x: elisp("(re-search-forward \"" + parse_words(x)[0] + "\")"),
        Key("h enter"),
        lambda x: elisp("(org-brain-goto-current)"),
        # lambda x: time.sleep(.5),
        lambda x: elisp("(call-interactively 'evil-window-down)")
    ],
    "visualize": [lambda x: elisp("(org-brain-visualize)")],
    "go to": [lambda x: elisp("(org-brain-goto)")],
    "search": [lambda x: elisp("(helm-org-rifle-brain)")],
    "show": [lambda x: elisp("(org-brain-goto-current)"),
             Key("j a")],
    # "go to":
    # lambda x: elisp("(org-brain-goto)"),
    "pin":
    lambda x: elisp("(call-interactively 'org-brain-pin)"),
    "org widen": [Key('cmd-esc , N')],
    "back":
    lambda x: elisp("(org-brain-visualize-back)"),
}

context.keymap(brain_map)
