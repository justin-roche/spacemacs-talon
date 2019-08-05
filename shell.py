import time

from talon.voice import Context, Key
from user.utils import is_filetype

exts = ("*shell*", ".orgx")

context = Context("shell", func=is_filetype(exts))

shell_map = {
    "shell start": [Key('cmd-esc space b S')],
    "which":
    "which ",
    "pseudo":
    "sudo ",
    "echo":
    "echo ",
    "path":
    "$PATH",
    "shell quit":
    [Key('esc space m x esc'), lambda x: time.sleep(.5),
     Key('G a')],
    "shell repeat": [Key('up')],
    "shell root": [Key('esc p !')],
    "em install": ['npm install', Key('enter')],
    "em all": ['npm run all:prod', Key('enter')],
    "em save": ['npm install --save '],
    "em test": ['npm test', Key('enter')],
    "em start": [
        Key('esc'), 'G0', 'i',
        Key('ctrl-c'),
        Key('ctrl-\\'), 'npm start',
        Key('enter')
    ],
    "gulp start": [
        Key('esc'), 'G0', 'i',
        Key('ctrl-c'),
        Key('ctrl-\\'), 'gulp watch',
        Key('enter')
    ],

    # "em hero": ['npm run heroku',Key('enter')],
    "hero push": [
        Key('esc'), 'G0', 'i',
        Key('ctrl-c ctrl-\\'), 'git push heroku master',
        Key('enter')
    ],
    "hero log": [
        Key('esc'), 'G0', 'i',
        Key('ctrl-c ctrl-\\'), 'heroku logs --tail',
        Key('enter')
    ],
    "version": ['--version'],
    "python location":
    "python -m site --user-base",
    "python version": ['python --version'],

    # "pippin run": ['pipenv run python '],
    # "pippin install": ['pipenv install '],
    # "pippin user": ['pipenv install --user'],
    "virtual": ['virtualenv '],
    "virtual new": ['virtualenv venv'],
    "virtual start": ['source venv/bin/activate'],
    "pip install": ['pip install '],
    "pip user": ['pip install --user '],
    "jekyll": ['jekyll serve'],

    # "environment new": ['mkvirtualenv project_folder'],
    "talon log": ['tail -f ~/.talon/talon.log'],
    # "environment make": ['mkproject '],
    # "environment work": ['workon '],
    # "environment list": ['lsvirtualenv '],
}
context.keymap(shell_map)

# ctx.keymap({
# "toggle on": [ lambda _: ctx.load()],
# "toggle off": [ lambda _: ctx.unload()],
# "snap done": [mg.stop, lambda _: ctx.unload()],
# })
