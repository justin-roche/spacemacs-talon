from talon.voice import Context, Key, press, Str, Rep

project_map = {
    "project directory": [Key('esc space p d')],
    "list projects": [Key('esc space p p')], 
    "project file": [Key('esc space p f') ],
    "project": [Key('esc space p l')],

    "get status": [Key('cmd-esc space g s')],
    "get push": [Key('cmd-esc space g P')],
    "get initialize": [Key('cmd-esc space g i')],
    # "repo  finalize": [Key('ctrl-c ctrl-c')],
}  
