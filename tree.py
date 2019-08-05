from talon.voice import Context, Key, press
from user.emacs.utils import elisp, key_repeat
from user.utils import is_filetype, numerals

exts = ("*NeoTree*", "*Treemacs")

context = Context("tree", func=is_filetype(exts))

tree_map = {
    "open": [Key('ctrl-l ')],
    "tree path":
    lambda x: elisp("(treemacs-copy-path-at-point)"),
    "workspace":
    lambda x: elisp("(treemacs-edit-workspaces)"),
    "tree shell":
    lambda x: elisp("(treemacs-shell)"),
    # "tree project":
    # lambda x: elisp("(treemacs-projectile)"),
    # "center": [Key('ctrl-l')],
    "last pro":
    lambda x: elisp("(treemacs-previous-project)"),
    "next pro":
    lambda x: elisp("(treemacs-next-project)"),
    "sin": [Key('ctrl-l')],
    "parent": [
        lambda x: elisp("(treemacs-goto-parent-node)"),
        lambda x: elisp("(evil-scroll-line-to-center nil)")
    ],
    "last": [
        lambda x: elisp("(treemacs-previous-neighbour)"),
        lambda x: elisp("(evil-scroll-line-to-center nil)")
    ],
    "next": [
        lambda x: elisp("(treemacs-next-neighbour)"),
        lambda x: elisp("(evil-scroll-line-to-center nil)")
    ],
    "collapse":
    lambda x: elisp("(treemacs-collapse-project)"),
    "tree up":
    lambda x: elisp("(treemacs-collapse-parent-node 1)"),

    # open
    "split":
    lambda x: elisp("(treemacs-visit-node-horizontal-split)"),
    "peak":
    lambda x: elisp("(treemacs-peek)"),
    "open" + numerals:
    [lambda x: key_repeat(x, 1, "j"), lambda x: press("enter")],
    "opener" + numerals:
    [lambda x: key_repeat(x, 1, "k"), lambda x: press("enter")],
    "tree copy":
    lambda x: elisp("(treemacs-copy-file)"),
    "rename":
    lambda x: elisp("(treemacs-rename)"),
    "create directory":
    lambda x: elisp("(treemacs-create-dir)"),
    "create":
    lambda x: elisp("(treemacs-create-file)"),
    "tree delete":
    lambda x: elisp("(treemacs-delete)"),
    # "delete node": lambda x:  elisp("(treemacs-delete)"),
    "shell":
    lambda x: elisp("(treemacs-shell)"),
    "refresh":
    lambda x: elisp("(treemacs-refresh)"),
    "new book":
    lambda x: elisp("(treemacs-add-bookmark)"),
    "book":
    lambda x: elisp("(treemacs-bookmark)"),
    "help":
    lambda x: elisp("(treemacs-helpful-hydra)"),

    # special commands
    "target": [Key('cmd-esc space t T')],
    "tree move": [Key('cmd-esc space t m')],
    # "shell": [Key('cmd-esc space t s')],
    "generate": [Key('cmd-esc space t g')],
    "open profile":
    lambda x: elisp('(find-file "/Users/justin/.zprofile")')
}
context.keymap(tree_map)
# "tree up": [Key('cmd-esc space t [')],
# "book": [Key('cmd-esc space t B')],
# "copy": [Key('space t c')],
# "refresh": [Key('cmd-esc space t r')],
# dired
# "dirt": [Key('cmd-esc space a d')],
# "dirt up": [Key('cmd-esc / \ . \ . enter enter')],
