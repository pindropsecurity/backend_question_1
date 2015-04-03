import tokenize 

class tree:
    def __init__(self, tokenizer):
        toktyp,tokval, _,_,_ = tokenizer.next()
        if toktyp == tokenize.OP and '+' in tokval:
            print "Habemus +"
            tree(tokenizer)
        elif toktyp == tokenize.OP and '-' in tokval:
            print "Habemus -"
            tree(tokenizer)
        elif toktyp == tokenize.OP and '*' in tokval:
            print "Habemus *"
            tree(tokenizer)
        elif toktyp == tokenize.OP and '/' in tokval:
            print "Habemus /"
            tree(tokenizer)
        elif toktyp == tokenize.NUMBER:
            print "Habemus NUMBER " + tokval
            return tokval;
        else:
            print "Habemus splat"

t = '+1 2 - 3 2'

tokenizer = tokenize.generate_tokens(iter([t]).next)

tree(tokenizer)

tokenizer.close()
print 'Bye-bye World'
