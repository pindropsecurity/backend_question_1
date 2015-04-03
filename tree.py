import tokenize 

def reduce(tokenizer):

    toktyp,tokval, _,_,_ = tokenizer.next()

    if toktyp == tokenize.OP and '+' in tokval:
        accum = 0
        while True:
            try:
                accum += reduce(tokenizer)
            except StopIteration:
                return accum
            except EOFError:
                return accum

    elif toktyp == tokenize.NUMBER:
        print "Habemus NUMBER " + tokval
        return int(tokval)
    elif toktyp == tokenize.ENDMARKER:
        print "Habemus ENDMARKER "
        raise EOFError
    else:
        print "Habemus splat"
        raise SyntaxError

t = '+1 2 +1 3 2'

tokenizer = tokenize.generate_tokens(iter([t]).next)

print reduce(tokenizer)

tokenizer.close()
print 'Bye-bye World'
