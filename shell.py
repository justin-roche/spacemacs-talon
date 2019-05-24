from talon.voice import Context, Key, press, Str, Rep

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
