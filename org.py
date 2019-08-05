from talon import app
from talon.engine import engine
from talon.voice import Context, Key, Str
from user.emacs.utils import elisp, key_repeat
from user.std import parse_words
from user.utils import is_filetype_regexp, numerals

exts = ["\d{8}", ".org", "20190730"]

context = Context("org", func=is_filetype_regexp(exts))

enabled = True

org_map = {
    # view
    # "org expand": [Key('esc shift-tab')],
    "toggle <dgndictation>": [
        lambda x: elisp("(evil-search-forward)"),
        lambda x: Str(parse_words(x)[0])(None),
        Key("enter"),
        Key("tab"),
    ],
    "hide all":
    lambda x: elisp("(org-global-cycle)"),
    # "6": lambda x: elisp("(outline-show-all)"),
    "org widen": [Key('cmd-esc , N')],
    "org narrow": [Key('cmd-esc , n')],
    "org center":
    lambda x: elisp("(jr/org-center-toggle)"),
    "org focus":
    lambda x: elisp("(org-theme-toggle)"),

    # headings
    "cut head":
    lambda x: elisp("(org-cut-subtree)"),
    "clear head":
    lambda x: elisp("(org-clear-subtree)"),
    "head": [Key('esc , h i a')],
    "subhead": [Key('esc , h i alt-right A')],

    # movement
    "head down": [Key('alt-down')],
    "head up": [Key('alt-up')],
    "promote": [Key('alt-left')],
    "promoter": [Key('shift-alt-left')],
    "demote": [Key('alt-right')],
    "easel": [Key('cmd-esc space j l')],
    "demoter": [Key('shift-alt-right')],

    # tags
    "org bold": [Key(', x b')],
    "org italic": [Key(', x i')],

    # tags
    "org priority":
    lambda x: elisp("(org-priority)"),
    "org to do": [Key('esc shift-right')],
    "org tag": [Key('esc ctrl-c ctrl-q')],
    "org view": [Key('esc ctrl-c / t')],
    "org schedule": [Key('esc ctrl-c ctrl-s')],
    "org agenda": [Key('esc space m a c')],

    # external
    "org archive": [Key('esc , A')],
    "org ark": [Key('cmd-esc Y p , A')],
    "org row": [Key('esc alt-shift-down')],
    "org column": [Key('esc alt-shift-right')],
    # ispell
    "new journal":
    lambda x: elisp("(jr/org-brain-journal-add)"),
    "grammar check":
    lambda x: elisp("(langtool-check-buffer)"),
    "grammar finish":
    lambda x: elisp("(langtool-check-done)"),
    "grammar correct":
    lambda x: elisp("(langtool-correct-buffer)"),
    "spell check":
    lambda x: elisp("(ispell-buffer)"),
    #flycheck
    # "spell check": [Key('cmd-esc space t S')],
    # "spell buffer": [Key('cmd-esc space S b')],
    # "spell next": [Key('cmd-esc space S n')],
    # "spell corect": [Key('cmd-esc space S c')],

    # clock
    "org pom":
    Key("cmd-esc space m p"),
    "org clock out":
    Key("cmd-esc space m O"),
    "org clock report":
    lambda x: elisp("(org-clock-report)"),
    "org clock in":
    Key("cmd-esc space m I"),
    "org new journal":
    lambda x: elisp("(org-journal-new-entry nil)"),
}

toggle_map = {
    "edit mode": lambda x: activate(),
    "pros mode": lambda x: deactivate(),
}

dictation_map = {
    "new head": [Key('esc , h i a')],
    "new subhead": [Key('esc , h i alt-right A')],
    "center": [Key('cmd-esc z z')],
    "down" + numerals: lambda x: key_repeat(x, 1, "j"),
    "up" + numerals: lambda x: key_repeat(x, 1, "k"),
    'quotes': ["''", Key('left')],
    'call': ['()', Key('left')],
    'brackets': ['[]', Key('left')],
    'doubles': Key('\" \" left'),
}


def deactivate():
    # dictation (prose mode) is not implemented through speech_toggle, but through changing context maps here and in std.
    context.unload()
    engine.mimic("talon deactivate emacs map".split())
    engine.mimic("talon deactivate standard map".split())
    dictation_map.update(toggle_map)
    context.keymap(dictation_map)
    context.load()
    app.notify("pros mode")


def activate():

    context.unload()
    engine.mimic("talon activate emacs map".split())
    engine.mimic("talon activate standard map".split())
    org_map.update(toggle_map)
    context.keymap(org_map)
    context.load()
    app.notify("edit mode")


# noise.register('noise', on_noise)

# context.keymap(org_map.update(toggle_map))
activate()
