from talon.voice import Key
from user.emacs.utils import elisp

project_map = {
    "project": [Key('esc space p l')],
    "list projects": [Key('esc space p p')],
    "pro shell": lambda x: elisp("(jr/project-shell)"),
    # search in project
    "grep": [Key('esc alt-m s a h'),
             Key("backspace " * 15)],
    "project directory": [Key('esc space p d')],
    "project file": [Key('esc space p f')],
    "find file": [Key('esc space p f')],
    "go module": [Key('esc space m m')],
    "go package": [Key('esc space m p')],
    # magit
    "get init": [Key('cmd-esc space g i')],
    "get initialize": [Key('cmd-esc space g i')],
    "get status": [Key('cmd-esc space g s')],
    "get fast": [Key('cmd-esc space g f y c')],
    "get push": [Key('cmd-esc space g P')],
    # build frame management
    "quad": [Key('cmd-esc space c b')],
    "quad stop": [Key('cmd-esc space c S')],
    "build frame": [Key('cmd-esc space c B')],
    "get frame": [Key('cmd-esc space c G')],
    "code frame": [Key('cmd-esc space c C')],
    "mode check": Key('cmd-esc space m f'),
    # angular project file switching
    "other file": [Key('cmd-esc space m t')],
    "template file": [Key('cmd-esc space m t')],
    "style file": [Key('cmd-esc space m s')],
}
