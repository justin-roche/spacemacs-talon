from talon.voice import Context, Key, press, Str, Rep
from talon.engine import engine
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype
from talon.audio import noise
from user.emacs.utils import jump, key_repeat, select_lines, range_select,interpolate_number,send_parsed_number 

exts = (".org", ".orgx")

context = Context("org", func=is_filetype(exts))

enabled = True

org_map = {
    
    "org toggle": [Key('esc shift-tab')],
    "org up": [Key('alt-up')],
    "org down": [Key('alt-down')],
    "head": [Key('esc , h i a')],
    "subhead": [Key('esc , h i alt-right A')],

    "promote": [Key('alt-left')],
    "promoter": [Key('shift-alt-left')],
    "demote": [Key('alt-right')],
    "demoter": [Key('shift-alt-right')],
    "org to do": [Key('esc shift-right')],
    "org tag": [Key('esc ctrl-c ctrl-q')],
    "org view": [Key('esc ctrl-c / t')],
    "org schedule": [Key('esc ctrl-c ctrl-s')],
    "org agenda": [Key('esc space m a c')],
    "org archive": [Key('esc , A')],
    "org ark": [Key('cmd-esc Y p , A')],

    "org row": [Key('esc alt-shift-down')],
    "org column": [Key('esc alt-shift-right')],
 }


def on_noise(noise):
    global enabled

    context.unload()
    if noise == 'pop':
              # engine.mimic("dragon toggle".split())
        if enabled == True:
              # engine.mimic("talon deactivate emacs map".split())
            deactivate()
        else:
            activate()
              # engine.mimic("talon activate emacs map".split())
    context.load()

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


