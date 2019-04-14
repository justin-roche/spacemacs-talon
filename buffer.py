from talon.voice import Context, Key, press, Str, Rep

buffer_map = {

    "list buffers": [ Key('esc space l b')],
    "buffs": [ Key('esc space l b')],
    "list buffs": [ Key('esc space l b')],
    "save": [ Key('esc space f s')],
    "scratch": [Key('esc space b s')],
    
    "close buffer": [ Key('esc'),':bd',Key('enter')],
    "close other buffers": [ Key('esc space b m')],

    "lab": [ Key('esc space b p')],
    "last buffer": [ Key('esc space b p')],
    "nab": [ Key('esc space b n')],
    "next buffer": [ Key('esc space b n')],

    #windows
    # "next window": [ Key('esc [-w')],
    "new win": [ Key('esc space w n')],
    "winner": [ Key('esc space w n')],
    "widow": [ Key('esc space w o')],
    "war": [ Key('esc space w l')],
    "wall": [ Key('esc space w h')],
    "close window": [ Key('esc space w d')],
    "close win": [ Key('esc space w d')],

    "new horizontal": [ Key('ctrl-x 3')],
    "new vertical": [ Key('ctrl-x 2')],

    #windows by number
    "win 1": [Key('esc space 1')],
    "win 2": [Key('esc space 2')],
    "win 3": [Key('esc space 3')], 
    "win 4": [Key('esc space 4')],

    #frames
    "next frame": [ Key('esc space f f')],
    "new frame": [ Key('esc space f n')],
    "delete frame": [ Key('esc space f d')],

}

