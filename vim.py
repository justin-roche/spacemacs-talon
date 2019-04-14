from talon.voice import Context, Key, press, Str, Rep
from user.utils import numerals, optional_numerals
from user.emacs.utils import interpolate_number, del_action 

context = Context('Emacs', bundle='org.gnu.Emacs' )

def test():
    Str(context.connection)(None)

vim_map = {
    # "vizy" + alphabet: lambda x: interpolate_letter(x, "v{n}w"),
    "ink": Key("esc i"),
    "normie": Key("esc"),
    "vizy": Key("esc v"),
    "castle": lambda x: interpolate_letter(x),
    "vizy" + numerals: lambda x: interpolate_number(x, "v{n}w"),
    "vizy big" + numerals: lambda x: interpolate_number(x, "v{n}W",2),
    'deal' + numerals: del_action,
    'cut' : [Key('x')],
    'paste' : [Key('esc p')],
    'paster' : [Key('esc o p')],
    'paste below' : [Key('esc o p')],
    "undies": Key("esc u") ,
    "redo":[Key('esc'),Key('ctrl-r')],
    "undo": [Key('esc'),'u'],
    "doozy": [Key('esc space a u')],
}
