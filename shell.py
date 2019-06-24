from talon.voice import Context, Key, press, Str, Rep
from user.utils import get_integer, parse_words_as_integer, numerals,text_to_number,optional_numerals,parse_words,is_filetype

exts = ("*shell*", ".orgx")

context = Context("shell", func=is_filetype(exts))

shell_map = {
    "shell start": [Key('cmd-esc space b S')],
    "shell quit": [Key('esc space m x esc G a')], 
    "shell root": [Key('esc p !')], 

    "em install": ['npm install',Key('enter')],
    "em all": ['npm run all:prod',Key('enter')],
    "em save": ['npm install --save '],
    "em test": ['npm test',Key('enter')],  
    # "em hero": ['npm run heroku',Key('enter')],
    "em start": [ Key('esc'), 'G0','i',Key('ctrl-c' ), Key('ctrl-\\' ), 'npm start',Key('enter' )],
    
    "hero push": [ Key('esc'), 'G0','i',Key('ctrl-c ctrl-\\' ), 'git push heroku master',Key('enter' )],
    "hero log": [ Key('esc'), 'G0','i',Key('ctrl-c ctrl-\\' ), 'heroku logs --tail',Key('enter' )],

    # "raptor": [Key('esc space m x esc G a enter')], 

    "gulp start": [ Key('esc'), 'G0','i',Key('ctrl-c' ), Key('ctrl-\\' ), 'gulp watch',Key('enter' )],
}  
context.keymap(shell_map)







# ctx.keymap({
    # "toggle on": [ lambda _: ctx.load()],
    # "toggle off": [ lambda _: ctx.unload()],
    # "snap done": [mg.stop, lambda _: ctx.unload()],
# })  






 
