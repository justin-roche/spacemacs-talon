from user.emacs.utils import elisp

compound_jumps_map = {
    # current
    "chaser":
    lambda x: elisp('(custom-avy-generic-crt "dw")'),
    # "vaser":
    # lambda x: elisp('(custom-avy-generic-crt "e" "v" :state 1)'),
    "dicer":
    lambda x: elisp('(custom-avy-generic-crt "ex" "v")'),
    # document
    # "chase":
    # lambda x: elisp('(custom-avy-generic "dw")'),
    "chase big":
    lambda x: elisp('(custom-avy-generic "dW")'),
    #
    "chase match":
    lambda x: elisp('(custom-avy-generic-match "x" nil nil nil)'),
    "chase matcher":
    lambda x: elisp('(custom-avy-generic-match "d" nil nil t)'),
    #
    # "vase":
    # lambda x: elisp('(custom-avy-generic-2-visual "v" "e")'),
    "dice":
    lambda x: elisp('(custom-avy-generic-2 "v" "ed")'),
    "dice end":
    lambda x: elisp('(custom-avy-generic "D")'),
    #
    # append
    "mace":
    lambda x: elisp('(custom-avy-visual-return "ex" "p")'),
    "place":
    lambda x: elisp('(custom-avy-generic "ea")'),
    # copy
    "case line":
    lambda x: elisp('(custom-avy-generic-line-return "yy")'),
    "case":
    lambda x: elisp('(custom-avy-generic-return "yw")'),
    "case match":
    lambda x: elisp('(custom-avy-generic-match-return "y" nil nil nil)'),
    "case matcher":
    lambda x: elisp('(custom-avy-generic-match-return "y" nil nil t)'),
    "case big":
    lambda x: elisp('(custom-avy-generic-return "yW")'),
    #
    # grab from elsewhere and paste here
    "mace match":
    lambda x: elisp('(custom-avy-generic-match-return "x" "p" nil nil)'),
    "grace match":
    lambda x: elisp('(custom-avy-generic-match-return "y" "p" nil nil)'),
    "grace matcher":
    lambda x: elisp('(custom-avy-generic-match-return "y" "p" nil t)'),
    "grace pair":
    lambda x: elisp('(custom-avy-generic-return "yi(" "p" )'),
    "grace big":
    lambda x: elisp('(custom-avy-generic-return "yW" "p")'),
    "grace line":
    lambda x: elisp('(custom-avy-generic-line-return "Y" "p")'),
    "zap line":
    lambda x: elisp('(custom-avy-generic-line-return "dd")'),
    "clay line":
    lambda x: elisp('(custom-avy-generic-line-return "dd")'),
    "zap lines":
    lambda x: elisp('(custom-avy-generic-lines-2-return "V" "d")'),
    # move line
    "mace lines":
    lambda x: elisp('(custom-avy-generic-lines-3 "V" "x" "p")'),
    "mace line":
    lambda x: elisp('(custom-avy-generic-lines "X" "p")'),
}
