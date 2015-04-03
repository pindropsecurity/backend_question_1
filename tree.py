import tokenize 

def reduce(tokenizer):
    toktyp,tokval, _,_,_ = tokenizer.next()

    if toktyp == tokenize.OP and '+' in tokval:
       return reduce(tokenizer)

    elif toktyp == tokenize.NUMBER:
       print "Habemus NUMBER " + tokval
       return int(tokval)
    elif toktyp == tokenize.ENDMARKER:
       print "Habemus ENDMARKER "
       return
    else:
       print "Habemus splat"

t = '+1 2 3'

tokenizer = tokenize.generate_tokens(iter([t]).next)

print reduce(tokenizer)

tokenizer.close()
print 'Bye-bye World'
