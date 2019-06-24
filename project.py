from talon.voice import Context, Key, press, Str, Rep


project_map = {
    "project directory": [Key('esc space p d')],
    "list projects": [Key('esc space p p')], 
    "project file": [Key('esc space p f') ],
    "pro shell": [Key('esc space p s') ],
    "find file": [Key('esc space p f') ],
    "project": [Key('esc space p l')],
    
    "go module": [Key('esc space m m')],
    "go package": [Key('esc space m p')],

    "get init": [Key('cmd-esc space g i')],
    "get initialize": [Key('cmd-esc space g i')],
    "get status": [Key('cmd-esc space g s')],
    "get fast": [Key('cmd-esc space g f y c')],
    "get push": [Key('cmd-esc space g P')],
    # "repo  finalize": [Key('ctrl-c ctrl-c')],

    "quad": [Key('cmd-esc space c b')],
    "quad stop": [Key('cmd-esc space c S')],

    "build frame": [Key('cmd-esc space c B')],
    "get frame": [Key('cmd-esc space c G')],
    "code frame": [Key('cmd-esc space c C')],
    "mode check": Key('cmd-esc space m f'),

    "other file": [Key('cmd-esc space m t')],
    "template file": [Key('cmd-esc space m t')],
    "style file": [Key('cmd-esc space m s')],
}  
