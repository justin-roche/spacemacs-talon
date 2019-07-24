from talon.voice import Context, Key, press, Str, Rep
from talon.engine import engine
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype
from talon.audio import noise
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number,elisp 

exts = (".org", ".orgx")

context = Context("org", func=is_filetype(exts))

enabled = True

org_map = {
    # view
    "org expand": [Key('esc shift-tab')],
    "org widen": [Key('cmd-esc , N')],
    "org narrow": [Key('cmd-esc , n')],
    "org focus": [Key('cmd-esc space w c')],

    # headings
    "org cut": lambda x: elisp("(org-cut-subtree)"),
    "org clear": lambda x: elisp("(org-clear-subtree)"),
    "head": [Key('esc , h i a')],
    "subhead": [Key('esc , h i alt-right A')],

    # movement
    "org down": [Key('alt-down')],
    "org up": [Key('alt-up')],
    "promote": [Key('alt-left')],
    "promoter": [Key('shift-alt-left')],
    "demote": [Key('alt-right')],
    "demoter": [Key('shift-alt-right')],

    # tags
    "org bold": [Key(', x b')],
    "org italic": [Key(', x i')],

    # tags
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
 }


toggle_map = {
        "edit mode": lambda x: activate(),
        "pros mode": lambda x: deactivate(),
    }

dictation_map = {
    "new head": [Key('esc , h i a')],
    "new subhead": [Key('esc , h i alt-right A')],
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


def activate():
    context.unload()
    engine.mimic("talon activate emacs map".split())
    engine.mimic("talon activate standard map".split())
    org_map.update(toggle_map)
    context.keymap(org_map)
    context.load()

# noise.register('noise', on_noise)

# context.keymap(org_map.update(toggle_map))
activate()


