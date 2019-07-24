from talon.voice import Key

snippet_map = {
    'call': ['()', Key('left')],
    'double quotes': ['""', Key('left')],
    'quotes': ["''", Key('left')],
    'braces': ['{}', Key('left')], 
    'brackets': ['[]', Key('left')], 
    
    'expand':[Key('ctrl-l')],
    'snip create':[Key('cmd-esc space y c')],
    'snip visit':[Key('cmd-esc space y v')],
    'snip insert':[Key('cmd-esc space y i')],
    'snip reload':[Key('cmd-esc space y R')]
    # 'snip reload':[Key('cmd-esc space y r')]
}  
