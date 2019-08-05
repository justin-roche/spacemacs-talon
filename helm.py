from talon.voice import Context, Key, Str, press
from user.utils import is_filetype, numerals, text_to_number

exts = ("*Minibuf", ".orgx")

context = Context("helm", func=is_filetype(exts))


def helm_select(x):
    n = text_to_number(x._words[1:])
    press("ctrl-c")
    Str(str(n))(None)


def on_noise(noise):
    if noise == 'pop':
        press("enter")


# noise.register('noise', on_noise)

helm_map = {
    "down" + numerals: lambda x: helm_select(x),
    "hat" + numerals: lambda x: helm_select(x),
    "copy": Key("ctrl-c ctrl-k"),
}

context.keymap(helm_map)
