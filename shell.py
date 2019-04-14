from talon.voice import Context, Key, press, Str, Rep

shell_map = {
    "em install": ['npm install',Key('enter')],
    "em start": [ Key('esc'), 'G0','i',Key('ctrl-c' ), Key('ctrl-\\' ), 'npm start',Key('enter' )],
    "em test": [ Key('esc'), 'G0','i',Key('ctrl-c' ), Key('ctrl-\\' ), 'npm start',Key('enter' )],
    "gulp start": [ Key('esc'), 'G0','i',Key('ctrl-c' ), Key('ctrl-\\' ), 'gulp watch',Key('enter' )],
    "hero": [ Key('esc'), 'G0','i',Key('ctrl-c ctrl-\\' ), 'git push heroku master',Key('enter' )],
    "em save": ['npm install --save '],
    "em test": ['npm test',Key('enter')],  
    "shell quit": [Key('esc space m x esc G a')], 
    "raptor": [Key('esc space m x esc G a enter')], 

    "shell root": [Key('esc p !')], 
}  
