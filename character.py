# from talon import app
from talon.voice import Key, Str
from user.utils import optional_numerals, text_to_number


def goto_character(m, r, i=1):
    jump_number = text_to_number(m._words[i:]) - 1
    # app.notify(str(jump_number))
    Key('esc')(None)
    Key(r)(None)
    Key("enter")(None)
    Str('n' * jump_number)(None)
    Key("a")(None)


base = {
    # spaces as required by talon, backslash for vim search, backslash with no space for python escaping
    "gecko": "' \ | \ \"",
    "gamma": ",",
    "gap": "( \ | )",
    "gary": "\ [ \ | \ ]",
    "goalie": ":",
}

character_map = {
    'repy caps': Key('esc ~'),
    'repy caps': Key('esc ~'),
}

for n in base:
    character_map.update({n: Key('esc / ' + base[n] + " enter a")})
    character_map.update({n + "back": Key('esc ? ' + base[n] + " enter a")})
    character_map.update({
        n + optional_numerals:
        # avoid loop capture; retain value of n at point in iteration (with default value of n)
        lambda x, n=n: goto_character(x, 'esc / ' + base[n])
    })
    character_map.update({
        n + "back" + optional_numerals:
        lambda x, n=n: goto_character(x, 'esc ? ' + base[n], 1)
    })
