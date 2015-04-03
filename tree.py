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

    elif toktyp == tokenize.NUMBER:
        print "Habemus NUMBER " + tokval
        return int(tokval)
    elif toktyp == tokenize.ENDMARKER:
        print "Habemus ENDMARKER "
        return 0
    else:
        print "Habemus splat"

t = '+1 2 +1 3 + +2'

tokenizer = tokenize.generate_tokens(iter([t]).next)

print reduce(tokenizer)

tokenizer.close()
print 'Bye-bye World'
