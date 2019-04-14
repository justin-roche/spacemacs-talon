from talon.voice import Context, Key, press, Str, Rep
import functools
from talon import applescript

def open_server(m):
   applescript.run(r'''
    tell application "System Events"
        do shell script "python -S ~/dbg/py3_dbgp -d localhost:9000 ~/taest.py"
        display notification "Hello world."
    end tell
    ''') 

debugger_map =  {
   # 'debug start':[helm_action("realgud:trepan3k")] ,
   # 'debug eval': Key('e'),
   # 'debug restart': Key('R'),
   # 'debug quit': Key('q'),
   # 'debug up': Key('u'),
   # 'debug down': Key('d'),
   # 'debug step': Key('s'),
   # 'debug finish': Key('f'),
   # 'debug next': Key('n'),
   # 'debug break': Key('b'),
   # 'debug continue': Key("c"),
}
