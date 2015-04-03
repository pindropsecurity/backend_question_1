import tokenize 

class tree:
    def __init__(self, tokenizer):
        toktyp,tokval, _,_,_ = tokenizer.next()
        print toktyp
        print tokval
        if toktyp == tokenize.OP and '+' in tokval:
            print "Habemus +"
            tree(tokenizer)
        elif toktyp == tokenize.OP and '-' in tokval:
            print "Habemus -"
        elif toktyp == tokenize.OP and '*' in tokval:
            print "Habemus *"
        elif toktyp == tokenize.OP and '/' in tokval:
            print "Habemus /"
        else:
            print "Habemus splat"

t = '+1 2 - 3 2'

tokenizer = tokenize.generate_tokens(iter([t]).next)
toktyp,tokval, _,_,_ = tokenizer.next()

if toktyp == tokenize.OP or '[' in tokval:
   tree(tokenizer)
else:
   print 'bad tree'

tokenizer.close()
print 'Bye-bye World'
