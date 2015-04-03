import tokenize 

operators = ['+', '-', '*', '/']

def operate(op, val1, val2):
    if (op == '+'):
        return val1 + val2
    elif (op == '-'):
        return val1 - val2
    elif (op == '*'):
        return val1 * val2
    elif (op == '/'):
        return val1 / val2
    else:
       assert False, 'Lost all hope'


def reduce(tokenizer):

    toktyp,tokval, _,_,_ = tokenizer.next()

    if toktyp == tokenize.OP and any(s in tokval for s in operators):

        #
        # Enforce the fact that every node has at least 2 children
        #
        accum = reduce(tokenizer)  
        accum = operate(tokval, accum, reduce(tokenizer))
 
        #
        # Manager the case for > 2
        #
        while True:
            try:
                accum = operate(tokval, accum, reduce(tokenizer))
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
#t = '+1'
#t = '+1 2'

tokenizer = tokenize.generate_tokens(iter([t]).next)

print reduce(tokenizer)

tokenizer.close()
print 'Bye-bye World'
