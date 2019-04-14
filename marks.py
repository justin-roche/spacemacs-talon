from talon.voice import Context, Key, press, Str, Rep

vim_marks = {
    'show marks' : [Key('esc'), ':DoShowMarks',Key('enter') ],
    'list marks' : [Key('esc'), ':marks',Key('enter') ],
    'fold': [Key('esc'), 'za',Key('enter')],
    'unfold': Key('esc cmd-alt-]'),
    'fold all': Key('cmd-k cmd-0'),
    'basil': Key('esc ` `'),
}  




