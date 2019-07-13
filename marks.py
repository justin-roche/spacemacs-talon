from talon.voice import Context, Key, press, Str, Rep

vim_marks = {
    # 'show marks' : Key('esc'), 
    'fold': Key('esc z c'), 
    'unfold': Key('cmd-esc space z . o'),
    'show folds': Key('cmd-esc space z .'),
    'unfold all': Key('cmd-esc space z . r q'),
    'fold all': Key('cmd-esc space z . m q'),
}  




