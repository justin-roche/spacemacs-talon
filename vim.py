from talon.voice import Context, Key, press, Str, Rep
from user.utils import numerals, optional_numerals
from user.emacs.utils import interpolate_number, del_action 

context = Context('Emacs', bundle='org.gnu.Emacs' )

def test():
    Str(context.connection)(None)

vim_map = {
    # "vizy" + alphabet: lambda x: interpolate_letter(x, "v{n}w"),
    "ink": Key("esc i"),
    "inks": Key("esc i space"),
    "normie": Key("esc"),
    "vizy": Key("esc v"),
    # "castle": lambda    interpolaetttt_ellttre(x),
    # "vizy word" + numerals: lambda x: interpolate_number(x, "v{n}w"),
    # "vizy big" + numerals: lambda x: interpolate_number(x, "v{n}W",2),
 



    "left" + numerals: lambda x: interpolate_number(x, "{n}ha",1),
    "right" + numerals: lambda x: interpolate_number(x, "{n}la",1),

    'registers' : [Key('cmd-esc space r e')],
    "register" + numerals: lambda x: interpolate_number(x, '"{n}p',1),

    'deal' + numerals: del_action,
    'cut' : [Key('x')],
    'copy' : [Key('cmd-esc y cmd-esc')],
    
    'paste' : [Key('esc p')],
    'paster' : [Key('esc o p')],
    'paste below' : [Key('cmd-esc o cmd-esc p')],
    'paste above' : [Key('cmd-esc O cmd-esc p')],
    
    "undies": Key("esc u") ,
    "redo":[Key('esc'),Key('ctrl-r')],
    "undo": [Key('esc'),'u'],
    
    "trim" + numerals: lambda x: interpolate_number(x, "v{n}hr "),
    "doozy": [Key('esc space a u')],
    
    # "copy group": [Key('esc space y y')],
    # "search group": [Key('esc space y G')],
    # "select group": [Key('esc space y g')],
    # "cut group": [Key('esc space y x')],
}
